#!/usr/bin/env python3
#coding=utf-8

import rospy
from controller import Robot
from movement_msgs.msg import WebotsRequestMsg

class Controller(object):
    ###########################FUNÇÕES DO CÓDIGO###########################

    #Construtor, define as váriaveis do Objeto Controller necessárias para o funcionamento do código
    def __init__(self):
        #Inicialização da "Constantes" da biblioteca do Webots
        self.natasha = Robot()
        self.timeStep = int(self.natasha.getBasicTimeStep())

        #Inicialização das variáveis de manipulação no código
        self.motorObjectArray = []
        self.motorSensorsObjectArray = []
        self.dataArray = [0]*20
        self.velocityArray = [0]*20

        #Vetores de identificação e referência dos motores
        self.motorNames = [ 'RARM_0 [shoulder]', 'LARM_0 [shoulder]', 
                            'RARM_1', 'LARM_1',
                            'LARM_2', 'RARM_2',
                            'RLEG_0', 'LLEG_0',
                            'RLEG_1 [hip]', 'LLEG_1 [hip]',
                            'RLEG_2', 'LLEG_2',
                            'RLEG_3', 'LLEG_3',
                            'RLEG_4', 'LLEG_4', 
                            'RFOOT',  'LFOOT',
                            'HEAD_0', 'HEAD_1' ]
        
        self.motorSensorsNames = [ 'RARM_0_sensor', 'LARM_0_sensor', 
                            'RARM_1_sensor', 'LARM_1_sensor',
                            'LARM_2_sensor', 'RARM_2_sensor',
                            'RLEG_0_sensor', 'LLEG_0_sensor',
                            'RLEG_1_sensor', 'LLEG_1_sensor',
                            'RLEG_2_sensor', 'LLEG_2_sensor',
                            'RLEG_3_sensor', 'LLEG_3_sensor',
                            'RLEG_4_sensor', 'LLEG_4_sensor', 
                            'RFOOT_sensor',  'LFOOT_sensor',
                            'HEAD_0_sensor', 'HEAD_1_sensor' ]

        #Inicilização dos outros controladores
        rospy.Subscriber('webots/request_move', WebotsRequestMsg, self.requestMove)
        self.sensor_motor_pub = rospy.Publisher('/webots/feedback', WebotsRequestMsg, queue_size=10)
        self.sensor_motor_pub_msg = WebotsRequestMsg()

        self.getMotors()
        self.last_req_time = self.natasha.getTime()
        
    #Start, define o comandos a serem enviados, além do loop do código
    def start(self):

        while self.natasha.step(self.timeStep) != -1 and not rospy.is_shutdown():
            self.feedbackWebots()

    #Função que percorre a lista de nomes dos motores criando uma lista de objetos de motores do Webots
    def getMotors(self):
        for name in self.motorNames:
            self.motorObjectArray = self.motorObjectArray + [self.natasha.getDevice(name)]
        for name in self.motorSensorsNames:
            self.motorSensorsObjectArray = self.motorSensorsObjectArray + [self.natasha.getDevice(name)]
        for motorSensor in self.motorSensorsObjectArray:
            motorSensor.enable(self.timeStep)

    #Função de callback do Webots/request_move, pega o vetor de posições enviado e coloca em uma variável manipulável no código todo
    def requestMove(self, msg):

        for index in range(20):
            self.dataArray[index] = msg.motors_position[index]
            self.velocityArray[index] = msg.motors_velocity[index]
        
        for index in range(20):
            self.motorObjectArray[index].setVelocity(self.velocityArray[index])
            self.motorObjectArray[index].setPosition(self.dataArray[index])

        self.last_req_time = self.natasha.getTime()

        while self.natasha.getTime() - self.last_req_time < 0.064:
            pass

    def feedbackWebots(self):
        for index, motorSensor in enumerate(self.motorSensorsObjectArray):
            self.sensor_motor_pub_msg.motors_position[index] = motorSensor.getValue()
        
        self.sensor_motor_pub.publish(self.sensor_motor_pub_msg)

if __name__ == '__main__':
    rospy.init_node('Webots_controller_node', anonymous=False)
    controller = Controller()
    controller.start()
    rospy.spin()