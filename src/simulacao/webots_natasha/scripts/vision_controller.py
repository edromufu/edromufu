#!/usr/bin/env python3
#coding=utf-8

import rospy
from controller import Robot
from sensor_msgs.msg import Image as visionSimImage

class ControllerVision(object):
    ###########################FUNÇÕES DO CÓDIGO###########################

    #Construtor, recebe o objeto da robô gerado no controlador central e define as variáveis necessárias para o funcionamento do código
    def __init__(self, robot):
        #Inicialização das mensagens e tópicos do ROS
        self.image_msg = visionSimImage()

        self.pubImage = rospy.Publisher('/webots_natasha/vision_controller', visionSimImage, queue_size= 33)

        #Definição dos valores estáticos necessários para decodificação da mensagem da Imagem pelo código da visão
        self.image_msg.encoding = 'bgra8'
        [self.image_msg.height, self.image_msg.width] = [416,416]
        self.image_msg.step = 1664

        #Inicialização da "Constantes" da biblioteca do Webots
        self.natasha = robot

        #Definição e ativação da camera
        self.camera_sensor = self.natasha.getDevice('Camera')
        self.camera_sensor.enable(33)
    
    #Define o loop do código
    def loop(self):
            self.sensorImage()
    
    ###########################FUNÇÕES DO WEBOTS###########################
    #Função que captura e envia a imagem da camera
    def sensorImage(self):
        self.image_msg.data = self.camera_sensor.getImage()
        self.pubImage.publish(self.image_msg)  
