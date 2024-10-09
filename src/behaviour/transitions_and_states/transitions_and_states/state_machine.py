#!/usr/bin/env python3
#coding=utf-8

import rclpy
import os, sys
from transitions import Machine
from modularized_bhv_msgs.msg import CurrentStateMsg  # Estado atual da StateMachine
from modularized_bhv_msgs.msg import GameControllerMsg  # Mensagem do GameController

LEFT = 'Left'  # Strings de resposta do interpretador da bola
RIGHT = 'Right'  # para cada posição
CENTER = 'Center'
BOTTOM = 'Bottom'
UP = 'Up'

# Definindo os estados do GameController
GAME_STATE_INITIAL = 0
GAME_STATE_READY = 1
GAME_STATE_SET = 2
GAME_STATE_PLAYING = 3
GAME_STATE_FINISHED = 4

edrom_dir = '/home/' + os.getlogin() + '/edromufu/src/'

sys.path.append(edrom_dir + 'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters


class StateMachine():

    def __init__(self):
        """
        Construtor:
        - Define a lista de possiveis estados
        - Define a lista de transicoes para cada um dos possiveis estados
        - Concatena os vetores de transicoes para listar todas as transicoes da robo
        - Inicializa a maquina de estados, utilizando as caracteristicas ja criadas
        """

        states = ['walking', 'stand_still', 'getting_up', 'impossible']

        go_to_walking_transitions = [
            {'trigger': 'go_to_walking', 'source': 'walking', 'dest': 'walking',
             'conditions': 'walking_condition', 'unless': 'getting_up_condition'},
            {'trigger': 'go_to_walking', 'source': 'stand_still', 'dest': 'walking',
             'conditions': 'walking_condition', 'unless': 'getting_up_condition'}
        ]

        go_to_stand_still_transitions = [
            {'trigger': 'go_to_stand_still', 'source': 'stand_still', 'dest': 'stand_still',
             'unless': 'getting_up_condition'},
            {'trigger': 'go_to_stand_still', 'source': 'getting_up', 'dest': 'stand_still',
             'unless': 'getting_up_condition'}
        ]

        go_to_getting_up_transitions = [
            {'trigger': 'go_to_getting_up', 'source': '*', 'dest': 'getting_up',
             'conditions': 'getting_up_condition'}
        ]

        go_to_impossible_transitions = [
            {'trigger': 'go_to_walking', 'source': '*', 'dest': 'impossible',
             'conditions': 'impossible_condition'},
            {'trigger': 'go_to_getting_up', 'source': '*', 'dest': 'impossible',
             'conditions': 'impossible_condition'},
            {'trigger': 'got_to_stand_still', 'source': '*', 'dest': 'impossible',
             'conditions': 'impossible_condition'}
        ]

        all_transitions = (go_to_walking_transitions
                           + go_to_getting_up_transitions + go_to_stand_still_transitions
                           + go_to_impossible_transitions)

        self.robot_state_machine = Machine(self, states=states, transitions=all_transitions, initial='stand_still')

        # Publisher e mensagens da StateMachine
        self.state_publisher = self.node.create_publisher(CurrentStateMsg, '/transitions_and_states/state_machine', 1)
        self.state_msg = CurrentStateMsg()

        # Subscriber do GameController
        self.game_controller_sub = self.node.create_subscription(GameControllerMsg, 'Game_Controller', self.game_controller_callback, 10)
        self.game_controller_status = None 

    def game_controller_callback(self, msg):
        self.game_controller_status = msg.game_state
        self.update_state()

    def request_state_machine_update(self, ballPosition, ballClose, ballFound, fallState, horMotorOutOfCenter, headKickCheck):

        self.getting_up_condition_update(fallState)
        self.walking_condition_update(ballFound)

        print(f'-------------------\nEstado {str(self.state)}')
        self.update_state()

        self.state_msg.currentState = str(self.state)
        self.state_publisher.publish(self.state_msg)

    def update_state(self):
        #Atualiza o estado da máquina de estados com base no estado do GameController.
        if self.game_controller_status == GAME_STATE_PLAYING:  # Estado "Playing"
            if self.go_to_walking():
                print('Transição para o walking\n-------------------\n')
                return True
            elif self.go_to_getting_up():
                print('Transição para o getting_up\n-------------------\n')
                return True
            elif self.go_to_stand_still():
                print('Transição para o stand_still\n-------------------\n')
                return True
        elif self.game_controller_status == GAME_STATE_INITIAL:
            print("Estado Inicial do GameController, aguardando...\n-------------------\n")
        elif self.game_controller_status == GAME_STATE_READY:
            print("GameController está em READY, se prepare...\n-------------------\n")
        elif self.game_controller_status == GAME_STATE_SET:
            print("GameController está em SET, aguarde início do jogo...\n-------------------\n")
        elif self.game_controller_status == GAME_STATE_FINISHED:
            print("GameController está em FINISHED, jogo acabou.\n-------------------\n")
        else:
            print('Aguardando o GameController para transicionar...')
            return False

    ########################################FUNÇÕES UPDATE CONDITION########################################

    def getting_up_condition_update(self, fall_state):
        """
        Atualiza a variável de controle para o estado de getting_up.
        """
        if fall_state != UP:
            self.getting_up_condition = True
        else:
            self.getting_up_condition = False

    def walking_condition_update(self, ball_found):
        if ball_found:
            self.walking_condition = True
        else:
            self.walking_condition = False

    ########################################FUNÇÕES RETURN CONDITION########################################
    def walking_condition(self): return self.walking_condition
    def getting_up_condition(self): return self.getting_up_condition
    def impossible_condition(self): return False


def main(args=None):
    rclpy.init(args=args)
    state_machine = StateMachine()
    rclpy.spin(state_machine)
    state_machine.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
