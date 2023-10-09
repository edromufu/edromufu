#!/usr/bin/env python3
#coding=utf-8

import rospy
from transitions import Machine
from modularized_bhv_msgs.msg import currentStateMsg

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

        states = [ 'walking','stand_still','kick','getting_up', 'impossible']

 


        go_to_walking_transitions = [
            
            { 'trigger': 'go_to_walking', 'source': 'stand_still', 'dest': 'walking',
             'conditions': 'walking_condition', 'unless': 'getting_up_condition'}
            ,
             { 'trigger': 'go_to_walking', 'source': 'stand_still', 'dest': 'walking',
             'conditions': 'walking_condition', 'unless': 'kick_condition'}
        ]
        
        go_to_stand_still_transitions = [
            { 'trigger': 'go_to_stand_still', 'source': 'getting_up', 'dest': 'stand_still',
             'unless': 'getting_up_condition'}
            ,
            { 'trigger': 'go_to_stand_still', 'source': 'kick', 'dest': 'stand_still',
             'unless': 'getting_up_condition'}
        ]

        go_to_kick_transitions = [
            { 'trigger': 'go_to_kick', 'source': 'walking', 'dest': 'kick',
             'conditions': 'kick_condition', 'unless': 'getting_up_condition'},
            { 'trigger': 'go_to_kick', 'source': 'stand_still', 'dest': 'kick',
             'conditions': 'kick_condition', 'unless': 'getting_up_condition'}
        ]

        go_to_getting_up_transitions = [
            { 'trigger': 'go_to_getting_up', 'source': '*', 'dest': 'getting_up',
             'conditions': 'getting_up_condition'}
        ]

        go_to_impossible_transitions = [
            {'trigger': 'go_to_search_ball', 'source': '*', 'dest': 'impossible',
             'conditions': 'impossible_condition'},
            {'trigger': 'go_to_body_search', 'source': '*', 'dest': 'impossible',
             'conditions': 'impossible_condition'},
            {'trigger': 'go_to_walking', 'source': '*', 'dest': 'impossible',
             'conditions': 'impossible_condition'},
            {'trigger': 'go_to_kick', 'source': '*', 'dest': 'impossible',
             'conditions': 'impossible_condition'},
            {'trigger': 'go_to_getting_up', 'source': '*', 'dest': 'impossible',
             'conditions': 'impossible_condition'},
            {'trigger': 'go_to_body_alignment', 'source': '*', 'dest': 'impossible',
             'conditions': 'impossible_condition'},
            {'trigger': 'go_to_stand_still', 'source': '*', 'dest': 'impossible',
             'conditions': 'impossible_condition'}
        ]

        all_transitions = (go_to_search_ball_transitions + go_to_body_alignment_transitions + go_to_walking_transitions 
        + go_to_kick_transitions + go_to_getting_up_transitions + go_to_stand_still_transitions + go_to_body_search_transitions
        + go_to_impossible_transitions)

        self.robot_state_machine = Machine(self, states=states, transitions=all_transitions, initial='stand_still')

        self.state_publisher = rospy.Publisher('/transitions_and_states/state_machine', currentStateMsg, queue_size=1)
        self.state_msg = currentStateMsg()
    
    #Funcao para chamada de atualizacao de cada uma das variaveis
    #que controlarao as transicoes de estados da maquina
    def request_state_machine_update(self, ballPosition, ballClose, ballFound, fallState, horMotorOutOfCenter, headKickCheck):
        
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
        
        if self.go_to_getting_up():
            print('Transição para o getting_up\n-------------------\n')
            return True
        
        elif self.go_to_kick():
            print('Transição para o kick\n-------------------\n')
            return True


        elif self.go_to_walking():
            print('Transição para o walking\n-------------------\n')
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
            self.walking_condition = False
        else:
            self.walking_condition = True
            self.getting_up_condition = False
    
    #Funcao para atualizar a variavel de codigo relacionada ao estado de kick
    def kick_condition_update(self, ball_relative_position, ver_angle_accomplished, ball_close):
        """
        -> Funcao:
        Avaliar a necessidade de transicao para o estado de kick e
        atualizar a variavel de controle responsavel, atraves de:
            - Verificar se a bola esta proxima o suficiente, centralizada para a robo
            e se a cabeca esta a um angulo minimo para garantia de um bom chute
            - Atualizar a variavel de condicao de acordo com verificacao
        """

        if ball_close and ball_relative_position == CENTER and ver_angle_accomplished:
            self.kick_condition = True
            self.walking_condition = False
        else:
            self.walking_condition = True
            self.kick_condition = False
    

    ########################################FUNÇÕES RETURN CONDITION########################################
    #Funcoes de retorno das variaveis de controle da forma necessitada pela state machine
    def walking_condition(self): return self.walking_condition   
    def getting_up_condition(self): return self.getting_up_condition  
    def kick_condition(self): return self.kick_condition 
    def impossible_condition(self): return False