#!/usr/bin/env python3
#coding=utf-8

import rclpy
# from rclpy.node import Node # Não herda de Node, recebe o Node principal
from controller import Supervisor

# Assumindo que modularized_bhv_msgs foi migrado para ROS2 e que os tipos de mensagem estão disponíveis
from modularized_bhv_msgs.msg import SimMovMsg # Use o nome correto SimMovMsg
from geometry_msgs.msg import Vector3 # Já é ROS2
from sensor_msgs.msg import Image as visionSimImage # Já é ROS2

# QoS para publishers (bom para ajustar)
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy

class RobotSensors():

    # Recebe a instância do nó principal (BhvIndependentSim)
    def __init__(self, supervisor, node_instance): # Adicionar node_instance como argumento
        # super().__init__('robot_sensors_node') # Removido: Não herda de Node
        self.node = node_instance # Guardar a referência do nó principal
        self.node.get_logger().info("RobotSensors class initialized.") # Log da classe

        """
        Construtor:
        - Faz a chamada de funções para definir as variáveis field e ros dos sensores da simulação:
            -> Encoder da cabeça;
            -> Acelerômetro;
            -> Câmera.
        """
        self.general_supervisor = supervisor

        self.init_head()
        self.init_accel()
        self.init_cam()
    
    #Função de chamada recorrente no bhv_sim
    def callClock(self):
        """
        -> Funcao:
        Chamar os métodos de publicar as informações obtidas pelos sensores.
        """
        self.motorUpdate()
        self.accelUpdate()
        self.camUpdate()

    #Função chamada pelo construtor para habilitação de todos recursos dos encoders da cabeça
    def init_head(self):
        """
        -> Funcao:
        Inicializar todas as variáveis necessárias para obtenção de informação dos motores da cabeça, atraves de:
            - Capturar os nodes de Transform de cada motor;
            - Capturar seus campos de rotação;
            - Iniciar as variáveis que indica as posições dos motores da cabeça;
            - Inicializa as variáveis do ROS para publicação da posição dos motores.
        """
        sim_horizontal_head_motor_node = self.general_supervisor.getFromDef('HorizontalMotor')
        sim_vertical_head_motor_node = self.general_supervisor.getFromDef('VerticalMotor')

        if sim_horizontal_head_motor_node is None:
            self.node.get_logger().error("Node 'HorizontalMotor' não encontrado para Head Sensors.")
            return
        if sim_vertical_head_motor_node is None:
            self.node.get_logger().error("Node 'VerticalMotor' não encontrado para Head Sensors.")
            return

        self.sim_hor_head_motor = sim_horizontal_head_motor_node.getField('rotation')
        self.sim_ver_head_motor = sim_vertical_head_motor_node.getField('rotation')

        self.hor_head_pos = self.sim_hor_head_motor.getSFRotation()[3]
        self.ver_head_pos = self.sim_ver_head_motor.getSFRotation()[3]

        # Use o nó principal para criar o publisher
        # QoS para tópicos de sensor (pode usar QoSProfile ou apenas um número para depth)
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT, # ou RMW_QOS_POLICY_RELIABILITY_RELIABLE
            history=HistoryPolicy.KEEP_LAST,
            depth=10
        )
        self.head_pos_publisher = self.node.create_publisher(SimMovMsg, '/webots/motors', qos_profile)
        self.head_pos_msg = SimMovMsg()

    #Função chamada pelo construtor para habilitação de todos recursos do acelerômetro
    def init_accel(self):
        """
        -> Funcao:
        Inicializar todas as variáveis necessárias para disponibilização das informações do acelerômetro, atraves de:
            - Capturar os device de acelerometro na robô e ativá-lo;
            - Configurar a variável do ROS responsável pela publicação das informações e sua mensagem.
        """
        self.accel_sensor = self.general_supervisor.getDevice('Accelerometer')
        if self.accel_sensor is None:
            self.node.get_logger().error("Device 'Accelerometer' não encontrado.")
            return

        self.accel_sensor.enable(32)

        # QoS para tópicos de sensor
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            history=HistoryPolicy.KEEP_LAST,
            depth=100
        )
        self.accel_publisher = self.node.create_publisher(Vector3, '/webots_natasha/behaviour_controller', qos_profile)
        self.accel_msg = Vector3()
    
    #Função chamada pelo construtor para habilitação de todos recursos da câmera
    def init_cam(self):
        """
        -> Funcao:
        Inicializar todas as variáveis necessárias para envio da imagem da câmera, atraves de:
            - Capturar os device de camera na robô e ativá-lo;
            - Configurar a variável do ROS responsável pela publicação das imagens e sua mensagem;
            - Configurar campos padrão da mensagem.
        """
        self.camera_sensor = self.general_supervisor.getDevice('Camera')
        if self.camera_sensor is None:
            self.node.get_logger().error("Device 'Camera' não encontrado.")
            return

        self.camera_sensor.enable(32)

        # QoS para tópicos de imagem (pode precisar de depth maior ou KEEP_LAST)
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            history=HistoryPolicy.KEEP_LAST,
            depth=33 # Manter o original
        )
        self.pubImage = self.node.create_publisher(visionSimImage, '/webots_natasha/vision_controller', qos_profile)

        self.image_msg = visionSimImage()
        self.image_msg.encoding = 'bgra8'
        self.image_msg.height = 416
        self.image_msg.width = 416
        self.image_msg.step = 1664
    
    #Função chamada no loop para publicar continuamente a leitura do acelerômetro
    def accelUpdate(self):
        """
        -> Funcao:
        Publicar via ROS a leitura do acelerometro, atraves de:
            - Capturar os valores disponíveis no sensor o tempo todo;
            - Armazenar cada eixo em um campo da mensagem;
            - Publicar esta mensagem.
        """
        if self.accel_sensor and self.accel_publisher: # Adicionar verificações de existência
            [self.accel_msg.x, self.accel_msg.y, self.accel_msg.z] = self.accel_sensor.getValues()
            self.accel_publisher.publish(self.accel_msg)
        else:
            self.node.get_logger().warn("Acelerômetro ou publisher não inicializado, pulando update.")

    #Função chamada no loop para publicar continuamente a imagem da câmera
    def camUpdate(self):
        """
        -> Funcao:
        Publicar via ROS a imagem da câmera, atraves de:
            - Capturar a imagem no momento atual como a "data" da mensagem;
            - Publicar esta mensagem.
        """
        if self.camera_sensor and self.pubImage: # Adicionar verificações de existência
            self.image_msg.data = self.camera_sensor.getImage()
            self.pubImage.publish(self.image_msg)
        else:
            self.node.get_logger().warn("Câmera ou publisher não inicializado, pulando update.")
    
    #Função chamada no loop para publicar continuamente a posição atual dos motores da cabeça
    def motorUpdate(self):
        """
        -> Funcao:
        Publicar via ROS a posição dos motores da cabeça, atraves de:
            - Capturar a posição no momento através do campo da rotação dos motores;
            - Criar um vetor que armazena a posição como mensagem;
            - Publicar esta mensagem.
        """
        if self.sim_hor_head_motor and self.sim_ver_head_motor and self.head_pos_publisher: # Adicionar verificações
            self.hor_head_pos = self.sim_hor_head_motor.getSFRotation()[3]
            self.ver_head_pos = self.sim_ver_head_motor.getSFRotation()[3]

            self.head_pos_msg.positions = [float(self.hor_head_pos),float(self.ver_head_pos)] # Garantir float

            self.head_pos_publisher.publish(self.head_pos_msg)
        else:
            self.node.get_logger().warn("Motores da cabeça ou publisher não inicializados, pulando update.")    