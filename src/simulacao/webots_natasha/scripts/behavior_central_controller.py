#!/usr/bin/env python3
#coding=utf-8

import movement_controller
import vision_controller
import supervisor

import rospy
from controller import Supervisor
from geometry_msgs.msg import Vector3

class Controller(object):
    ###########################FUNÇÕES DO CÓDIGO###########################

    #Construtor, define as váriaveis do Objeto Controller necessárias para o funcionamento do código
    def __init__(self):
        #Inicialização da "Constantes" da biblioteca do Webots
        #self.natasha = Robot()
        self.natasha = Supervisor()
        self.timeStep = int(self.natasha.getBasicTimeStep())

        #Inicilização dos outros controladores
        self.movement = movement_controller.ControllerMovement(self.natasha)
        self.vision = vision_controller.ControllerVision(self.natasha)
        self.supervisor = supervisor.SupervisorNatasha(self.natasha)

        #Inicialização das mensagens e tópicos do ROS
        self.accel_msg = Vector3()

        self.pubAccel = rospy.Publisher('/webots_natasha/behaviour_controller', Vector3, queue_size = 100)
        
    #Start, define o comandos a serem enviados, além do loop do código
    def start(self):
        self.natasha.step(self.timeStep)

        #Definição e ativação do Acelerômetro
        self.accel_sensor = self.natasha.getDevice('Accelerometer')
        self.accel_sensor.enable(self.timeStep)

        while self.natasha.step(self.timeStep) != -1 and not rospy.is_shutdown():
            self.sensorAccelerometer()
            self.movement.loop()
            self.vision.loop()
            #Chama o loop de verificação da entrada no teclado e garante que a posição dos motores esteja nula, caso seja para a posição inicial
            if(self.supervisor.loop() == 'repositionedToStart'):
                self.movement.dataArray = [0]*20
    
    ###########################FUNÇÕES DO WEBOTS###########################
    
    #Função que captura e envia os dados do acelerômetro
    def sensorAccelerometer(self):
        [self.accel_msg.x, self.accel_msg.y, self.accel_msg.z] = self.accel_sensor.getValues()
        self.pubAccel.publish(self.accel_msg)

            
if __name__ == '__main__':
    rospy.init_node('Webots_controller_node', anonymous=False)
    controller = Controller()
    controller.start()
    rospy.spin()