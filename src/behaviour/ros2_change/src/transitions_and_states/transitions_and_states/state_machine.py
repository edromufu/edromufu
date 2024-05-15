#!/usr/bin/env python3
#coding=utf-8

#import rospy (1)
import rclpy #(1)
import os,sys
from transitions import Machine
#from modularized_bhv_msgs.msg import currentStateMsg (2)
from modularized_bhv_msgs.msg import CurrentStateMsg #(2)

LEFT = 'Left' #Strings de resposta do interpretador da bola
RIGHT = 'Right' #para cada posicao
CENTER = 'Center'
BOTTOM = 'Bottom'
UP = 'Up'
edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
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

        states = ['walking','stand_still','getting_up', 'impossible']
 
        go_to_walking_transitions = [
            { 'trigger': 'go_to_walking', 'source': 'walking', 'dest': 'walking',
             'conditions': 'walking_condition', 'unless': 'getting_up_condition'},
            { 'trigger': 'go_to_walking', 'source': 'stand_still', 'dest': 'walking',
             'conditions': 'walking_condition', 'unless': 'getting_up_condition'}
        ]
        
        go_to_stand_still_transitions = [
            { 'trigger': 'go_to_stand_still', 'source': 'stand_still', 'dest': 'stand_still',
             'unless': 'getting_up_condition'},
            { 'trigger': 'go_to_stand_still', 'source': 'getting_up', 'dest': 'stand_still',
             'unless': 'getting_up_condition'}
        ]

        go_to_getting_up_transitions = [
            { 'trigger': 'go_to_getting_up', 'source': '*', 'dest': 'getting_up',
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

        #self.state_publisher = rospy.Publisher('/transitions_and_states/state_machine', currentStateMsg, queue_size=1) (3)
        #self.state_msg = currentStateMsg()

        self.state_publisher = self.node.create_publisher(CurrentStateMsg, '/transitions_and_states/state_machine', 1) #(3)
        self.state_msg = CurrentStateMsg()


    #Funcao para chamada de atualizacao de cada uma das variaveis
    #que controlarao as transicoes de estados da maquina
    def request_state_machine_update(self, ballPosition, ballClose, ballFound, fallState, horMotorOutOfCenter, headKickCheck):
        
        self.getting_up_condition_update(fallState)
        self.walking_condition_update(ballFound)

        print(f'-------------------\nEstado {str(self.state)}')        
        self.update_state()

        #self.state_msg.currentState = str(self.state) (4)
        self.state_msg.CurrentState = str(self.state) #(4)
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
        if self.go_to_walking():
            print('Transição para o walking\n-------------------\n')
            return True
        
        elif self.go_to_getting_up():
            print('Transição para o getting_up\n-------------------\n')
            return True

        elif self.go_to_stand_still():
            print('Transição para o stand_still\n-------------------\n')
            return True
        
        else:
            return False
    
    ########################################FUNÇÕES UPDATE CONDITION########################################

    #Funcao para atualizar a variavel de codigo relacionada ao estado de getting_up
    def getting_up_condition_update(self, fall_state):
        """
        -> Funcao:
        Avaliar a necessidade de transicao para o estado de getting_up e
        atualizar a variavel de controle responsavel, atraves de:
            - Verificar se a resposta do interpretador de queda e qualquer
            diferente de "de pe"
            - Atualizar a variavel de condicao de acordo com verificacao
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
    #Funcoes de retorno das variaveis de controle da forma necessitada pela state machine
    def walking_condition(self): return False  
    def getting_up_condition(self): return self.getting_up_condition  
    def impossible_condition(self): return False