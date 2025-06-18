#!/usr/bin/env python3
#coding=utf-8

import rospy
from controller import Supervisor
from controller import Robot

from modularized_bhv_msgs.msg import simMovMsg #Mensagem associada ao tópico utilizado para enviar info dos motores
from geometry_msgs.msg import Vector3 #Mensagem associada ao tópico utilizado para enviar info do acelerometro
from sensor_msgs.msg import Image as visionSimImage #Mensagem associada ao tópico utilizado para enviar as imagens da câmera

class RobotSensors():

    def __init__(self, supervisor):
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

        self.sim_hor_head_motor = sim_horizontal_head_motor_node.getField('rotation')
        self.sim_ver_head_motor = sim_vertical_head_motor_node.getField('rotation')

        self.hor_head_pos = self.sim_hor_head_motor.getSFRotation()[3]
        self.ver_head_pos = self.sim_ver_head_motor.getSFRotation()[3]

        self.head_pos_publisher = rospy.Publisher('/webots/motors', simMovMsg, queue_size=100)
        self.head_pos_msg = simMovMsg()

    #Função chamada pelo construtor para habilitação de todos recursos do acelerômetro
    def init_accel(self):
        """
        -> Funcao:
        Inicializar todas as variáveis necessárias para disponibilização das informações do acelerômetro, atraves de:
            - Capturar os device de acelerometro na robô e ativá-lo;
            - Configurar a variável do ROS responsável pela publicação das informações e sua mensagem.
        """
        self.accel_sensor = self.general_supervisor.getDevice('Accelerometer')

        self.accel_sensor.enable(32)

        self.accel_publisher = rospy.Publisher('/webots_natasha/behaviour_controller', Vector3, queue_size=100)
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

        self.camera_sensor.enable(32)

        self.pubImage = rospy.Publisher('/webots_natasha/vision_controller', visionSimImage, queue_size= 33)

        self.image_msg = visionSimImage()
        self.image_msg.encoding = 'bgra8'
        [self.image_msg.height, self.image_msg.width] = [416,416]
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
        [self.accel_msg.x, self.accel_msg.y, self.accel_msg.z] = self.accel_sensor.getValues()

        self.accel_publisher.publish(self.accel_msg)

    #Função chamada no loop para publicar continuamente a imagem da câmera
    def camUpdate(self):
        """
        -> Funcao:
        Publicar via ROS a imagem da câmera, atraves de:
            - Capturar a imagem no momento atual como a "data" da mensagem;
            - Publicar esta mensagem.
        """
        self.image_msg.data = self.camera_sensor.getImage()
        self.pubImage.publish(self.image_msg)
    
    #Função chamada no loop para publicar continuamente a posição atual dos motores da cabeça
    def motorUpdate(self):
        """
        -> Funcao:
        Publicar via ROS a posição dos motores da cabeça, atraves de:
            - Capturar a posição no momento através do campo da rotação dos motores;
            - Criar um vetor que armazena a posição como mensagem;
            - Publicar esta mensagem.
        """
        self.hor_head_pos = self.sim_hor_head_motor.getSFRotation()[3]
        self.ver_head_pos = self.sim_ver_head_motor.getSFRotation()[3]

        self.head_pos_msg.positions = [self.hor_head_pos,self.ver_head_pos]

        self.head_pos_publisher.publish(self.head_pos_msg)