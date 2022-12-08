#!/usr/bin/env python3
#coding=utf-8

import rospy
import time
from transitions import Machine
from modularized_bhv_msgs.msg import currentStateMsg

#Parametros associados a posicao relativa da bola
LEFT = 'Left' #Strings de resposta do interpretador da bola
RIGHT = 'Right' #para cada posicao
CENTER = 'Center'
BOTTOM = 'Bottom'

UP = 'Up' #String associada a estar de pe na resposta do interpretador de queda

#Parametros associados a movimentacao da cabeca
RIGHT_HEAD_MOVEMENT = 'R' #Strings de reposta do interpretador
LEFT_HEAD_MOVEMENT = 'L' #para possiveis movimentos da cabeca

class StateMachine():

    def __init__(self):
        """
        Construtor:
        - Define a lista de possiveis estados
        - Define a lista de transicoes para cada um dos possiveis estados
        - Concatena os vetores de transicoes para listar todas as transicoes da robo
        - Inicializa a maquina de estados, utilizando as caracteristicas ja criadas
        """

        states = ['stand_still','defense', 'impossible']

        go_to_defense_transitions = [
            { 'trigger': 'go_to_defense', 'source': 'stand_still', 'dest': 'defense',
             'conditions': 'defense_condition'}
        ]

        go_to_stand_still_transitions = [
            { 'trigger': 'go_to_stand_still', 'source': 'defense', 'dest': 'stand_still',
             'unless': 'defense_condition'}
        ]

        go_to_impossible_transitions = [
            {'trigger': 'go_to_stand_still', 'source': '*', 'dest': 'impossible',
             'conditions': 'impossible_condition'},
            {'trigger': 'go_to_defense', 'source': '*', 'dest': 'impossible',
             'conditions': 'impossible_condition'}
        ]

        all_transitions = (go_to_defense_transitions + go_to_stand_still_transitions + go_to_impossible_transitions) 

        self.robot_state_machine = Machine(self, states=states, transitions=all_transitions, initial='stand_still')

        self.state_publisher = rospy.Publisher('/transitions_and_states/state_machine', currentStateMsg, queue_size=1)
        self.state_msg = currentStateMsg()
    
    #Funcao para chamada de atualizacao de cada uma das variaveis
    #que controlarao as transicoes de estados da maquina
    def request_state_machine_update(self, ballFound, ballClose):
        """
        -> Funcao:
        Chamar a atualizacao das variaveis de transicao, atraves de:
            - Recebe as variaveis de interesse da state_machine_receiver
            - Realiza a chamada individual de cada uma das funcoes de atualizacao das variaveis 
        -> Input:
            - fallState: Resultado da interpretacao de queda da robo
            - ballFound: Declara se a bola foi encontrada pela camera
            - ballClose: Informa se a bola passou de um limite de proximidade
            - ballRelativePosition: Informa a posicao relativa da bola na interpretacao da camera
            - verAngleAccomplished: Informa se a posicao vertical do motor passou de um limite definido
            - headPossibleMovements: Lista os movimentos possiveis dos motores da cabeca
            - horMotorOutOfCenter: Indica se o motor horizontal ultrapassou os limites do centro
        """
        self.defense_condition_update(ballFound, ballClose)

        #!
        print(f'-------------------\nEstado {str(self.state)}')
        self.update_state()
        self.state_msg.currentState = str(self.state)
        self.state_publisher.publish(self.state_msg)
    
    #Funcao para transicao de estado da biblioteca
    def update_state(self):
        """
        -> Funcao:
        Atualiza do estado da maquina em si, atraves de:
            - Chamada de funcoes criadas pela biblioteca durante a
            inicializacao da maquina de estados em um logica de if's
            funcional
        """

        if self.go_to_stand_still():
            print('Transição para o stand_still\n-------------------\n')
            return True

        elif self.go_to_defense():
            print('Transição para o defense\n-------------------\n')
            return True
        
        else:
            return False
    
    ########################################FUNÇÕES UPDATE CONDITION########################################
    def defense_condition_update(self, ball_found, ball_close):
        if ball_close and ball_found:
            self.defense_condition = True
        else:
            self.defense_condition = False

    ########################################FUNÇÕES RETURN CONDITION########################################
    def defense_condition(self): return self.defense_condition
    def impossible_condition(self): return False