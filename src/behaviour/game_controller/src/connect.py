#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from __future__ import unicode_literals, print_function

import os
import socket
import time
import logging
import argparse
import sys
import rospy  # Substituição de rclpy para ROS 1
#Requires construct==2.5.3
from construct import Container, ConstError

edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'
sys.path.append(edrom_dir+'behaviour')
#sys.path.append(edrom_dir+'behaviour/modularized_bhv_msgs')

from game_controller.src.gamestate import GameState, ReturnData, GAME_CONTROLLER_RESPONSE_VERSION

sys.path.append(edrom_dir+'behaviour/modularized_bhv_msgs/msg')
from modularized_bhv_msgs.msg import gameControllerMsg
# Set up logging
logger = logging.getLogger('game_controller')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')

DEFAULT_LISTENING_HOST = '0.0.0.0'
GAME_CONTROLLER_LISTEN_PORT = 3838
GAME_CONTROLLER_ANSWER_PORT = 3939

parser = argparse.ArgumentParser()
parser.add_argument('--team', type=int, default=3, help="team ID, default is 1")
parser.add_argument('--player', type=int, default=1, help="player ID, default is 1")
parser.add_argument('--goalkeeper', action="store_true", help="if this flag is present, the player takes the role of the goalkeeper")


class GameStateReceiver(object):
    """ This class puts up a simple UDP Server which receives the
    *addr* parameter to listen to the packages from the game_controller.
    """

    def __init__(self, team, player, is_goalkeeper, addr=(DEFAULT_LISTENING_HOST, GAME_CONTROLLER_LISTEN_PORT), answer_port=GAME_CONTROLLER_ANSWER_PORT):
        # Information that is used when sending the answer to the game controller
        self.team = team
        self.player = player
        self.man_penalize = True
        self.is_goalkeeper = is_goalkeeper
        rospy.init_node('game_controller', anonymous=True)  # Inicia o nó no ROS 1

        self.publisher = rospy.Publisher("Game_Controller", gameControllerMsg, queue_size=1)
        
        # The address listening on and the port for sending back the robots meta data
        self.addr = addr
        self.answer_port = answer_port

        # The state and time we received last from the GC
        self.state = None
        self.time = None

        # The socket and whether it is still running
        self.socket = None
        self.running = True

        self._open_socket()

    def _open_socket(self):
        """ Creates the socket """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.addr)
        self.socket.settimeout(0.5)
        self.socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def receive_forever(self):
        """ Waits in a loop that is terminated by setting self.running = False """
        while not rospy.is_shutdown() and self.running:
            try:
                self.receive_once()
            except IOError as e:
                logger.debug("Error sending KeepAlive: " + str(e))

    def receive_once(self):
        """ Receives a package and interprets it. """
        try:
            data, peer = self.socket.recvfrom(GameState.sizeof())

            # Throws a ConstError if it doesn't work
            parsed_state = GameState.parse(data)

            # Assign the new package after it parsed successful to the state
            self.state = parsed_state
            self.time = time.time()

            # Call the handler for the package
            self.on_new_gamestate(self.state)

            # Answer the GameController
            self.answer_to_gamecontroller(peer)

        except AssertionError as ae:
            logger.error(ae)
        except socket.timeout:
            logger.warning("Socket timeout")
        except ConstError:
            logger.warning("Parse Error: Probably using an old protocol!")
        except Exception as e:
            logger.exception(e)

    def answer_to_gamecontroller(self, peer):
        """ Sends a life sign to the game controller """
        return_message = 0 if self.man_penalize else 2
        if self.is_goalkeeper:
            return_message = 1 ## anterior 3

        data = Container(
            header=b"RGrt",
            version=GAME_CONTROLLER_RESPONSE_VERSION,
            team=self.team,
            player=self.player,
            message=return_message)
        try:
            destination = (peer[0], GAME_CONTROLLER_ANSWER_PORT)
            self.socket.sendto(ReturnData.build(data), destination)
        except Exception as e:
            logger.error("Network Error: %s" % str(e))

    def on_new_gamestate(self, state):
        """ Is called with the new game state after receiving a package """
        if state.teams[1].team_number == self.team:
            own_team = state.teams[1]
            player = own_team.players[self.player - 1]
            rival_team = state.teams[0]
        elif state.teams[0].team_number == self.team:
            own_team = state.teams[0]
            player = own_team.players[self.player - 1]
            rival_team = state.teams[1]
        else:
            own_team = 0
            rival_team = 0
            player = 0
        #   msg = String()
        #  msg.data = "Olá paulo"
        
        msg = gameControllerMsg()
        msg.header.stamp = rospy.time.now()  # Altera para o tempo do ROS 1
        msg.game_state = state.game_state.intvalue
        msg.secondary_state = state.secondary_state.intvalue
        msg.secondary_state_mode = state.secondary_state_info[1]
        msg.first_half = state.first_half
        msg.own_score = own_team.score
        msg.rival_score = rival_team.score
        msg.seconds_remaining = state.seconds_remaining
        msg.secondary_seconds_remaining = state.secondary_seconds_remaining
        msg.has_kick_off = state.kickoff_team == self.team
        msg.penalized = player.penalty != 0
        msg.seconds_till_unpenalized = player.secs_till_unpenalized
        msg.secondary_state_team = state.secondary_state_info[0]
        msg.secondary_state_mode = state.secondary_state_info[1]
        msg.team_color = own_team.team_color.intvalue
        msg.drop_in_team = state.drop_in_team
        msg.drop_in_time = state.drop_in_time
        msg.penalty_shot = own_team.penalty_shot
        msg.single_shots = own_team.single_shots
        msg.coach_message = own_team.coach_message
        penalties = []
        red_cards = []
        for i in range(6):
            penalties.append(own_team.players[i].penalty != 0)
            red_cards.append(own_team.players[i].number_of_red_cards != 0)
        msg.team_mates_with_penalty = penalties
        msg.team_mates_with_red_card = red_cards
        
        self.publisher.publish(msg)

    def get_last_state(self):
        return self.state, self.time

    def get_time_since_last_package(self):
        return time.time() - self.time

    def stop(self):
        self.running = False

    def set_manual_penalty(self, flag):
        self.man_penalize = flag


def main():
    args = parser.parse_args(rospy.myargv()[1:])  # Usa rospy.myargv() para lidar com argumentos
    rec = GameStateReceiver(team=args.team, player=args.player, is_goalkeeper=args.goalkeeper)
    rec.receive_forever()


if __name__ == '__main__':
    main()
