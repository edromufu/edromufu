#!/usr/bin/env python3
#coding=utf-8

import rospy
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

        states = ['search_ball','body_alignment','body_search','walking','stand_still','kick','getting_up', 'impossible']
        
        go_to_search_ball_transitions = [
            { 'trigger': 'go_to_search_ball', 'source': 'body_alignment', 'dest': 'search_ball',
             'conditions': 'search_ball_condition', 'unless': 'getting_up_condition'}
            ,
            { 'trigger': 'go_to_search_ball', 'source': 'body_search', 'dest': 'search_ball',
             'conditions': 'search_ball_condition', 'unless': 'getting_up_condition'}
            ,
            { 'trigger': 'go_to_search_ball', 'source': 'stand_still', 'dest': 'search_ball',
             'conditions': 'search_ball_condition', 'unless': 'getting_up_condition'}
            ,
            { 'trigger': 'go_to_search_ball', 'source': 'getting_up', 'dest': 'search_ball',
             'conditions': 'search_ball_condition', 'unless': 'getting_up_condition'}
            ,
            { 'trigger': 'go_to_search_ball', 'source': 'walking', 'dest': 'search_ball',
             'conditions': 'search_ball_align_kick_condition', 'unless': 'getting_up_condition'}
        ]

        go_to_body_alignment_transitions = [
            { 'trigger': 'go_to_body_alignment', 'source': 'search_ball', 'dest': 'body_alignment',
             'conditions': 'body_alignment_condition', 'unless': 'getting_up_condition'}
        ]

        go_to_body_search_transitions = [
            { 'trigger': 'go_to_body_search', 'source': '*', 'dest': 'body_search',
             'conditions': 'body_search_condition', 'unless': 'getting_up_condition'}
        ]

        go_to_walking_transitions = [
            { 'trigger': 'go_to_walking', 'source': 'search_ball', 'dest': 'walking',
             'conditions': 'walking_condition', 'unless': 'getting_up_condition'}
            ,
            { 'trigger': 'go_to_walking', 'source': 'body_search', 'dest': 'walking',
             'conditions': 'walking_condition', 'unless': 'getting_up_condition'}
            ,
            { 'trigger': 'go_to_walking', 'source': 'body_alignment', 'dest': 'walking',
             'conditions': 'walking_condition', 'unless': 'getting_up_condition'}
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
            { 'trigger': 'go_to_kick', 'source': 'search_ball', 'dest': 'kick',
             'conditions': 'kick_condition', 'unless': 'getting_up_condition'},
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
    def request_state_machine_update(self, fallState, ballFound, ballClose, ballRelativePosition, verAngleAccomplished, headPossibleMovements, horMotorOutOfCenter):
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
        self.walking_condition_update(ballRelativePosition, horMotorOutOfCenter)
        self.getting_up_condition_update(fallState)
        self.kick_condition_update(ballRelativePosition, verAngleAccomplished, ballClose)
        self.body_alignment_condition_update(ballRelativePosition, headPossibleMovements, horMotorOutOfCenter)
        self.search_ball_condition_update(ballFound, ballRelativePosition)
        self.search_ball_align_kick_condition_update(ballRelativePosition)
        self.body_search_condition_update(ballFound)

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
        
        if self.go_to_getting_up():
            print('Transição para o getting_up\n-------------------\n')
            return True
        
        elif self.go_to_kick():
            print('Transição para o kick\n-------------------\n')
            return True

        elif self.go_to_search_ball():
            print('Transição para o search_ball\n-------------------\n')
            return True

        elif self.go_to_body_search():
            print('Transição para o body_search\n-------------------\n')
            return True

        elif self.go_to_walking():
            print('Transição para o walking\n-------------------\n')
            return True
        
        elif self.go_to_body_alignment():
            print('Transição para o body_alignment\n-------------------\n')
            return True
        
        elif self.go_to_stand_still():
            print('Transição para o stand_still\n-------------------\n')
            return True
        
        else:
            return False
    
    ########################################FUNÇÕES UPDATE CONDITION########################################
    #Funcao para atualizar a variavel de codigo relacionada ao estado de walking
    def walking_condition_update(self, ball_relative_position, hor_motor_out_of_center):
        """
        -> Funcao:
        Avaliar a necessidade de transicao para o estado de walking e
        atualizar a variavel de controle responsavel, atraves de:
            - Verificar se a bola esta centralizada com a camera e se a camera
            (motor horizontal da cabeca) esta centralizada com o corpo
            - Atualizacao da variavel de condicao segundo a interpretacao
        """

        if ball_relative_position == CENTER and not hor_motor_out_of_center:
            self.walking_condition = True
        else:
            self.walking_condition = False
    
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
        else:
            self.kick_condition = False
    
    #Funcao para atualizar a variavel de codigo relacionada ao estado de body_alignment
    def body_alignment_condition_update(self, ball_relative_position, head_possible_movements, hor_motor_out_of_center):
        """
        -> Funcao:
        Avaliar a necessidade de transicao para o estado de body_alignment e
        atualizar a variavel de controle responsavel, atraves de:
            - Verifica se ha a necessidade da cabeca de se movimentar
            em uma direcao nao disponivel (pelos limites do motor) para criar
            o caso na qual a bola esta fora do "range" da camera
            - Verifica se ha a necessidade de recentralizar a cabeca com o corpo
            apos centralizacao da bola, para criar o caso de alinhamento do corpo 
            em direcao a bola
            - Checar se qualquer um dos casos e verdadeiro para atualizacao
            da varivel de condicao
        """

        if ( (RIGHT_HEAD_MOVEMENT not in head_possible_movements and RIGHT in ball_relative_position) or 
            (LEFT_HEAD_MOVEMENT not in head_possible_movements and LEFT in ball_relative_position) ):
            out_of_range = True
        else:
            out_of_range = False

        if ball_relative_position == CENTER and hor_motor_out_of_center:
            align_to_ball = True
        else:
            align_to_ball = False
        
        if out_of_range or align_to_ball:
            self.body_alignment_condition = True
        else:
            self.body_alignment_condition = False

    #Funcao para atualizar a variavel de codigo relacionada ao estado de search_ball        
    def search_ball_condition_update(self, ball_found, ball_relative_position):
        """
        -> Funcao:
        Avaliar a necessidade de transicao para o estado de search_ball e
        atualizar a variavel de controle responsavel, atraves de:
            - Checar se a bola esta na camera e nao esta centralizada
            - Atualizar a variavel de condicao de acordo com verificacao
        """

        if ball_relative_position != CENTER and ball_found:
            self.search_ball_condition = True
        else:
            self.search_ball_condition = False

    #Funcao para atualizar a variavel de codigo relacionada ao estado de search_ball para alinhar para o chute
    def search_ball_align_kick_condition_update(self, ball_relative_position):
        """
        -> Funcao:
        Avaliar a necessidade de transicao para o estado de search_ball, alinhando para o chute,
        e atualizar a variavel de controle responsavel, atraves de:
            - Verifica se o estado atual era walking e se a bola se
            descentralizou em direcao a parte inferior da camera, indicando
            aproximacao da robo a bola
            - Atualizar a variavel de condicao de acordo com verificacao
        """

        if str(self.state) == 'walking' and ball_relative_position != CENTER:
            self.search_ball_align_kick_condition = True
        else:
            self.search_ball_align_kick_condition = False
    
    #Funcao para atualizar a variavel de codigo relacionada ao estado de body_search
    def body_search_condition_update(self, ball_found):
        """
        -> Funcao:
        Avaliar a necessidade de transicao para o estado de ball_found
        e atualizar a variavel de controle responsavel, atraves de:
            - Verifica se a bola nao esta localizada em qualquer lugar na camera,
            indicando necessidade de rotacao em torno de si mesmo para localiza-la
            - Atualizar a variavel de condicao de acordo com verificacao
        """

        if not ball_found:
            self.body_search_condition = True
        else:
            self.body_search_condition = False

    ########################################FUNÇÕES RETURN CONDITION########################################
    #Funcoes de retorno das variaveis de controle da forma necessitada pela state machine
    def walking_condition(self): return self.walking_condition   
    def getting_up_condition(self): return self.getting_up_condition  
    def kick_condition(self): return self.kick_condition  
    def body_alignment_condition(self): return self.body_alignment_condition
    def search_ball_condition(self): return self.search_ball_condition
    def search_ball_align_kick_condition(self): return self.search_ball_align_kick_condition  
    def body_search_condition(self): return self.body_search_condition
    def impossible_condition(self): return False