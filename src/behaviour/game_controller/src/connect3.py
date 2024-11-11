import socket
import time
import rospy

from construct import Container, ConstError
from std_msgs.msg import Bool
from game_controller.gamestate import GameState, ReturnData, GAME_CONTROLLER_RESPONSE_VERSION
from modularized_bhv_msgs.msg import GameControllerMsg

class GameStateReceiver:
    """ This class puts up a simple UDP Server which receives the
    *addr* parameter to listen to the packages from the game_controller.
    If it receives a package it will be interpreted with the construct data
    structure and the :func:`on_new_gamestate` will be called with the content.
    After this we send a package back to the GC """

    def __init__(self):
        rospy.init_node('game_controller')

        self.team = rospy.get_param('~team_number', 1)
        self.player_number = rospy.get_param('~robot_number', 2)
        rospy.loginfo('We are playing as player {} in team {}'.format(self.player_number, self.team))

        self.state_publisher = rospy.Publisher('gamestate', GameControllerMsg, queue_size=1)

        self.man_penalize = False
        self.game_controller_lost_time = 20
        self.game_controller_connected_publisher = rospy.Publisher('game_controller_connected', Bool, queue_size=1)

        # The address listening on and the port for sending back the robots meta data
        listen_host = rospy.get_param('~listen_host', '0.0.0.0')
        listen_port = rospy.get_param('~listen_port', 3838)
        self.answer_port = rospy.get_param('~answer_port', 3939)

        self.addr = (listen_host, listen_port)

        # The state and time we received last form the GC
        self.state = None
        self.time = time.time()

        # The socket and whether it is still running
        self.socket = None
        self.running = True

        self._open_socket()

    def _open_socket(self):
        """ Creates the socket """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.addr)
        self.socket.settimeout(2)
        self.socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def receive_forever(self):
        """ Waits in a loop that is terminated by setting self.running = False """
        while not rospy.is_shutdown():
            try:
                self.receive_once()
            except IOError as e:
                rospy.logwarn("Error while sending keepalive: " + str(e))

    def receive_once(self):
        """ Receives a package and interprets it.
            Calls :func:`on_new_gamestate`
            Sends an answer to the GC """
        try:
            data, peer = self.socket.recvfrom(GameState.sizeof())

            # Throws a ConstError if it doesn't work
            parsed_state = GameState.parse(data)

            # Assign the new package after it parsed successful to the state
            self.state = parsed_state
            self.time = time.time()

            # Publish that game controller received message
            msg = Bool()
            msg.data = True
            self.game_controller_connected_publisher.publish(msg)

            # Call the handler for the package
            self.on_new_gamestate(self.state)

            # Answer the GameController
            self.answer_to_gamecontroller(peer)

        except AssertionError as ae:
            rospy.logerr(ae)
        except socket.timeout:
            rospy.loginfo_throttle(5, "No GameController message received (socket timeout)")
        except ConstError:
            rospy.logwarn("Parse Error: Probably using an old protocol!")
        finally:
            if self.get_time_since_last_package() > self.game_controller_lost_time:
                self.time += 5  # Resend message every five seconds
                rospy.loginfo_throttle(5, "No GameController message received, allowing robot to move")
                msg = GameControllerMsg()
                msg.game_state = 3  # PLAYING
                self.state_publisher.publish(msg)
                msg2 = Bool()
                msg2.data = False
                self.game_controller_connected_publisher.publish(msg2)

    def answer_to_gamecontroller(self, peer):
        """ Sends a life sign to the game controller """
        return_message = 0 if self.man_penalize else 2

        data = Container(header=b"RGrt",
                         version=GAME_CONTROLLER_RESPONSE_VERSION,
                         team=self.team,
                         player=self.player_number,
                         message=return_message)
        try:
            destination = (peer[0], self.answer_port)
            rospy.logdebug('Sending answer to {} port {}'.format(destination[0], destination[1]))
            self.socket.sendto(ReturnData.build(data), destination)
        except Exception as e:
            rospy.logerr("Network Error: %s" % str(e))

    def on_new_gamestate(self, state):
        """ Is called with the new game state after receiving a package.
            The information is processed and published as a standard message to a ROS topic.
            :param state: Game State
        """

        is_own_team = lambda number: number == self.team
        own_team = self.select_team_by(is_own_team, state.teams)

        is_not_own_team = lambda number: number != self.team
        rival_team = self.select_team_by(is_not_own_team, state.teams)

        if not own_team or not rival_team:
            rospy.logerr('Team {} not playing, only {} and {}'.format(self.team, state.teams[0].team_number,
                                                                      state.teams[1].team_number))
            return

        try:
            me = own_team.players[self.player_number - 1]
        except IndexError:
            rospy.logerr('Robot {} not playing'.format(self.player_number))
            return

        msg = GameControllerMsg()
        msg.header.stamp = rospy.Time.now()
        msg.game_state = state.game_state.intvalue
        msg.secondary_state = state.secondary_state.intvalue
        msg.secondary_state_mode = state.secondary_state_info[1]
        msg.first_half = state.first_half
        msg.own_score = own_team.score
        msg.rival_score = rival_team.score
        msg.seconds_remaining = state.seconds_remaining
        msg.secondary_seconds_remaining = state.secondary_seconds_remaining
        msg.has_kick_off = state.kickoff_team == self.team
        msg.penalized = me.penalty != 0
        msg.seconds_till_unpenalized = me.secs_till_unpenalized
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
        self.state_publisher.publish(msg)

    def get_last_state(self):
        return self.state, self.time

    def get_time_since_last_package(self):
        return time.time() - self.time

    def stop(self):
        self.running = False

    def set_manual_penalty(self, flag):
        self.man_penalize = flag

    def select_team_by(self, predicate, teams):
        selected = [team for team in teams if predicate(team.team_number)]
        return next(iter(selected), None)

def main():
    receiver = GameStateReceiver()

    try:
        receiver.receive_forever()
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()
