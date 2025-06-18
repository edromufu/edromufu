#!/usr/bin/env python3
#coding=utf-8

import rclpy
from rclpy.node import Node
from controller import Supervisor

from modularized_bhv_msgs.msg import CurrentStateMsg
from modularized_bhv_msgs.srv import MoveRequest

# Limites relacionados aos motores da cabeça em radianos
HOR_INCREMENT = (1.7 + 1.7) / 10  # Valores de incremento obtidos através do step
VER_INCREMENT = 1.47 / 10  # dos motores do pescoço na neck_interpreter.py

# Setando a grafia correta das requisições para a cabeça
RIGHT = 'head_to_right'
LEFT = 'head_to_left'
UP = 'head_to_up'
DOWN = 'head_to_down'
CENTER = 'head_to_center'
SEARCH = 'head_search'
POSSIBLE_REQUESTS = [RIGHT, LEFT, UP, DOWN, CENTER, SEARCH]
SEARCH_MOVEMENT = [CENTER, UP, CENTER, DOWN, DOWN]

class HeadMover(Node):

    def __init__(self, supervisor):
        """
        Construtor:
        - Faz a chamada de funções para definir as variáveis field e ros dos motores da simulação.
        """
        super().__init__('head_mover_node')
        
        self.search_index = 0
        self.last_run = 0
        self.current_state = None
        self.req_dict = {'body_alignment': None, 'search_ball': None, 'body_search': None}
        self.general_supervisor = supervisor

        # ROS2 Subscriber
        self.state_subscriber = self.create_subscription(CurrentStateMsg,'/transitions_and_states/state_machine',
            self.flag_update,10)

        # ROS2 Service
        self.head_service = self.create_service(MoveRequest,'/bhv2mov_communicator/head_requisitions',
            self.move_sim_head)

        self.init_head()

    def search_routine(self):
        current_move = SEARCH_MOVEMENT[self.search_index % len(SEARCH_MOVEMENT)]
        self.search_index += 1
        return current_move

    def call_clock(self):
        """
        Chamar o método para atualização interna da posição da cabeça.
        """
        self.motor_update()
        if (self.general_supervisor.getTime() - self.last_run) > 0.35:
            movement = self.req_dict[self.current_state] if self.current_state in self.req_dict.keys() else None
            self.move_head_clock(movement)

    def flag_update(self, message):
        self.current_state = message.current_state

    def move_head_clock(self, movement):
        """
        Alterar o campo de rotação dos nodes da cabeça para simular o movimento do pescoço.
        """
        if movement == SEARCH: 
            movement = self.search_routine()
        else:
            self.search_index = 0

        if movement in [RIGHT, DOWN]:
            increment = 1
        elif movement in [LEFT, UP]:
            increment = -1
        else:
            increment = 0

        if movement in [RIGHT, LEFT]:  # Movimentação horizontal
            increment *= HOR_INCREMENT
            rotation = self.sim_hor_head_motor.getSFRotation()[:3] + [round(self.hor_head_pos + increment, 2)]
            self.sim_hor_head_motor.setSFRotation(rotation)
        elif movement in [UP, DOWN]:  # Movimentação vertical
            increment *= VER_INCREMENT
            rotation = self.sim_ver_head_motor.getSFRotation()[:3] + [round(self.ver_head_pos + increment, 2)]
            self.sim_ver_head_motor.setSFRotation(rotation)
        elif movement == CENTER:  # Posição central
            hor_rotation = self.sim_hor_head_motor.getSFRotation()[:3] + [0]
            ver_rotation = self.sim_ver_head_motor.getSFRotation()[:3] + [0.45]
            self.sim_hor_head_motor.setSFRotation(hor_rotation)
            if self.current_state != 'body_alignment':
                self.sim_ver_head_motor.setSFRotation(ver_rotation)

        self.last_run = self.general_supervisor.getTime()

    def motor_update(self):
        """Atualizar a posição dos motores da cabeça."""
        self.hor_head_pos = self.sim_hor_head_motor.getSFRotation()[3]
        self.ver_head_pos = self.sim_ver_head_motor.getSFRotation()[3]
        
    def init_head(self):
        """Inicializar todas as variáveis necessárias para movimentação dos motores da cabeça."""
        sim_horizontal_head_motor_node = self.general_supervisor.getFromDef('HorizontalMotor')
        sim_vertical_head_motor_node = self.general_supervisor.getFromDef('VerticalMotor')

        self.sim_hor_head_motor = sim_horizontal_head_motor_node.getField('rotation')
        self.sim_ver_head_motor = sim_vertical_head_motor_node.getField('rotation')

        self.hor_head_pos = self.sim_hor_head_motor.getSFRotation()[3]
        self.ver_head_pos = self.sim_ver_head_motor.getSFRotation()[3]

    def move_sim_head(self, request, response):
        """
        Salvar as últimas requisições de cada código como variável deste código.
        """
        # ROS2 não tem _connection_header como no ROS1, precisamos de alternativa
        # Você precisará implementar sua própria lógica para identificar a origem
        # Exemplo temporário - assumindo que a origem está no request
        origin = getattr(request, 'origin', 'unknown')
        
        if origin in self.req_dict:
            self.req_dict[origin] = request.move_request

        response.success = True
        return response