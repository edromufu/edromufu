#!/usr/bin/env python3
#coding=utf-8

import rclpy
from rclpy.node import Node
from controller import Supervisor

# Assumindo que modularized_bhv_msgs foi migrado para ROS2
from modularized_bhv_msgs.msg import CurrentStateMsg
from modularized_bhv_msgs.srv import MoveRequest, MoveRequestResponse # Importar a resposta também

# QoS para publishers e subscribers
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy

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
        self.get_logger().info("HeadMover node initialized.") # Log para confirmar inicialização
        
        self.search_index = 0
        self.last_run = 0
        self.current_state = None
        # O 'origin' era do ROS1 connection_header. No ROS2, se você precisa de origens,
        # elas devem ser parte da sua mensagem de requisição.
        # Por enquanto, vamos manter req_dict com chaves fixas ou adaptar se 'origin' for um campo do MoveRequest.
        self.req_dict = {'body_alignment': None, 'search_ball': None, 'body_search': None} 
        self.general_supervisor = supervisor

        # ROS2 Subscriber
        # QoS para subscribers (depth é o mais comum, mas pode usar QoSProfile completo)
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.RELIABLE, # Geralmente RELIABLE para estados
            history=HistoryPolicy.KEEP_LAST,
            depth=10
        )
        self.state_subscriber = self.create_subscription(
            CurrentStateMsg,
            '/transitions_and_states/state_machine',
            self.flag_update,
            qos_profile # Use o perfil QoS
        )

        # ROS2 Service
        self.head_service = self.create_service(
            MoveRequest, # Tipo do serviço
            '/bhv2mov_communicator/head_requisitions',
            self.move_sim_head
        )

        self.init_head()

    def search_routine(self):
        current_move = SEARCH_MOVEMENT[self.search_index % len(SEARCH_MOVEMENT)]
        self.search_index += 1
        return current_move

    # Renomear para snake_case para consistência Python
    def call_clock(self): 
        """
        Chamar o método para atualização interna da posição da cabeça.
        """
        self.motor_update()
        if (self.general_supervisor.getTime() - self.last_run) > 0.35:
            # O current_state pode ser None no início. Trate isso.
            movement = self.req_dict.get(self.current_state, None) # Usar .get() para evitar KeyError
            # Se movement ainda for None, pule a chamada para move_head_clock
            if movement is not None:
                self.move_head_clock(movement)

    # Renomear para snake_case para consistência Python
    def flag_update(self, message):
        self.current_state = message.current_state
        self.get_logger().debug(f"Current state updated to: {self.current_state}") # Debug log

    # Renomear para snake_case para consistência Python
    def move_head_clock(self, movement):
        """
        Alterar o campo de rotação dos nodes da cabeça para simular o movimento do pescoço.
        """
        if movement == SEARCH: 
            movement = self.search_routine()
        else:
            self.search_index = 0

        # Mover lógica de 'increment' para dentro dos blocos IF para evitar erro se movement for CENTER
        increment = 0 
        if movement in [RIGHT, DOWN]:
            increment = 1
        elif movement in [LEFT, UP]:
            increment = -1

        if movement in [RIGHT, LEFT]:  # Movimentação horizontal
            increment *= HOR_INCREMENT
            # Checar se sim_hor_head_motor existe antes de usar
            if self.sim_hor_head_motor:
                rotation = self.sim_hor_head_motor.getSFRotation()[:3] + [round(self.hor_head_pos + increment, 2)]
                self.sim_hor_head_motor.setSFRotation(rotation)
            else:
                self.get_logger().warn("Horizontal motor not found, skipping movement.")
        elif movement in [UP, DOWN]:  # Movimentação vertical
            increment *= VER_INCREMENT
            # Checar se sim_ver_head_motor existe antes de usar
            if self.sim_ver_head_motor:
                rotation = self.sim_ver_head_motor.getSFRotation()[:3] + [round(self.ver_head_pos + increment, 2)]
                self.sim_ver_head_motor.setSFRotation(rotation)
            else:
                self.get_logger().warn("Vertical motor not found, skipping movement.")
        elif movement == CENTER:  # Posição central
            if self.sim_hor_head_motor:
                hor_rotation = self.sim_hor_head_motor.getSFRotation()[:3] + [0]
                self.sim_hor_head_motor.setSFRotation(hor_rotation)
            else:
                self.get_logger().warn("Horizontal motor not found for centering.")
            
            if self.sim_ver_head_motor and self.current_state != 'body_alignment':
                ver_rotation = self.sim_ver_head_motor.getSFRotation()[:3] + [0.45]
                self.sim_ver_head_motor.setSFRotation(ver_rotation)
            elif not self.sim_ver_head_motor:
                self.get_logger().warn("Vertical motor not found for centering.")

        self.last_run = self.general_supervisor.getTime()

    # Renomear para snake_case para consistência Python
    def motor_update(self):
        """Atualizar a posição dos motores da cabeça."""
        if self.sim_hor_head_motor:
            self.hor_head_pos = self.sim_hor_head_motor.getSFRotation()[3]
        if self.sim_ver_head_motor:
            self.ver_head_pos = self.sim_ver_head_motor.getSFRotation()[3]
        
    # Renomear para snake_case para consistência Python
    def init_head(self):
        """Inicializar todas as variáveis necessárias para movimentação dos motores da cabeça."""
        sim_horizontal_head_motor_node = self.general_supervisor.getFromDef('HorizontalMotor')
        sim_vertical_head_motor_node = self.general_supervisor.getFromDef('VerticalMotor')

        if sim_horizontal_head_motor_node is None:
            self.get_logger().error("Node 'HorizontalMotor' não encontrado para Head Mover.")
            return # Ou levante uma exceção, dependendo do quão crítico é
        if sim_vertical_head_motor_node is None:
            self.get_logger().error("Node 'VerticalMotor' não encontrado para Head Mover.")
            return

        self.sim_hor_head_motor = sim_horizontal_head_motor_node.getField('rotation')
        self.sim_ver_head_motor = sim_vertical_head_motor_node.getField('rotation')

        self.hor_head_pos = self.sim_hor_head_motor.getSFRotation()[3]
        self.ver_head_pos = self.sim_ver_head_motor.getSFRotation()[3]

    # Renomear para snake_case para consistência Python
    def move_sim_head(self, request, response):
        """
        Salvar as últimas requisições de cada código como variável deste código.
        """
        # No ROS2, o 'origin' não vem do connection_header. Se você precisa de uma origem
        # da requisição, ela deve ser um campo da sua mensagem MoveRequest.
        # Por exemplo, se MoveRequest tiver um campo 'string caller_id'.
        # Por enquanto, vou remover a lógica de 'origin' se não for um campo direto.
        
        # Assume que request.move_request é a string de requisição (e.g., 'head_to_right')
        # e que a lógica de "origin" foi movida para um campo em 'MoveRequest' se necessária.
        # Se 'origin' não é um campo da sua mensagem de serviço, a lógica do req_dict deve ser revisada.
        
        # Temporariamente, vamos assumir que self.req_dict usa chaves fixas
        # ou que 'origin' é uma parte da sua lógica de estado, não da requisição direta.
        
        # Se você precisa que o serviço salve uma requisição baseada na 'origem' da chamada,
        # você deve adicionar um campo 'string origin' à sua mensagem de serviço 'MoveRequest'.
        
        # Por agora, vamos apenas processar a requisição de movimento diretamente.
        self.req_dict['body_alignment'] = request.move_request # Exemplo: apenas um local de armazenamento
        self.get_logger().info(f"Received head request: {request.move_request}")

        response.success = True # Assumir sucesso por padrão, ou baseado na lógica
        return response