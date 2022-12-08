#!/usr/bin/env python3
#coding=utf-8

import rospy
from controller import Robot
from movement_msgs.msg import WebotsMsg
from movement_msgs.srv import DynamixelCreatorSrv, DynamixelCreatorSrvResponse

RAD2MOTOR = 651.74
MOTORREF = 2048

class ControllerMovement(object): 
    ###########################FUNÇÕES DO CÓDIGO###########################

    #Construtor, recebe o objeto da robô gerado no controlador central e define as variáveis necessárias para o funcionamento do código
    def __init__(self, robot):

        #Inicialização das mensagens e tópicos do ROS
        self.SrvPositionMotor = DynamixelCreatorSrvResponse()

        rospy.Subscriber('opencm/conversion', WebotsMsg, self.requestCmCallback)
        rospy.Service('motor_comm/opencm/dynamixelServiceSrv', DynamixelCreatorSrv, self.poseCaptureService)

        #Inicialização das variáveis de manipulação no código
        self.motorObjectArray = []
        self.dataArray = [0]*20
        self.velocityArray = [2]*20
        self.pastDataArray = [0]*20
        self.control = ''

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
        
        self.motorRef =   [ 2048, 2048, 
                            2048, 2048,
                            2048, 2048,
                            2048, 2048,
                            2048, 2048,
                            2048, 2048,
                            2048, 2048,
                            2048, 2048, 
                            2048, 2048,
                            2048, 2048 ]
        
        #Inicialização da "Constantes" da biblioteca do Webots
        self.natasha = robot
        self.getMotors()

    #Define o loop do código
    def loop(self):
            self.velocityFunction()
            self.positionFunction()

    ###########################FUNÇÕES DO WEBOTS###########################
       
    #Função que percorre a lista de nomes dos motores criando uma lista de objetos de motores do Webots
    def getMotors(self):
        for name in self.motorNames:
            self.motorObjectArray = self.motorObjectArray + [self.natasha.getDevice(name)]

    #Função que percorre a lista de objetos de motores do Webots enviando velocidades para cada um deles com base no velocityArray
    def velocityFunction(self):
        for index in range(20):
            self.motorObjectArray[index].setVelocity(self.velocityArray[index])
    
    #Função que percorre a lista de objetos de motores do Webots enviando posições para cada um deles com base no dataArray definido pelo opencm/request
    def positionFunction(self):
        if self.control == 'conversion_mode': 
            for index in range(20):
                #if (self.pastDataArray[index] != self.dataArray[index]):
                self.motorObjectArray[index].setPosition(self.dataArray[index])
                
                #self.pastDataArray[index] = self.dataArray[index]

    #Função que retorna um vetor da posição atual de cada motor, percorrendo a lista de objetos de motores do Webots capturando a target position de cada um
    def getPose(self):
        posVec = [0]*20
        for index in range(20):
            posVec[index] = self.motorObjectArray[index].getTargetPosition()

        return posVec
    
    ###########################FUNÇÕES DO ROS###########################
    #Função de callback do OpencmReq, pega o vetor de posições enviado e coloca em uma variável manipulável no código todo
    def requestCmCallback(self, msg):
        self.control = msg.control
        for index in range(20):
            self.dataArray[index] = msg.position[index]

    #Função que retorna para o Service, em unidade de motor, a pose atual (posição dos motores) para criação de Pages
    def poseCaptureService(self, req):
        self.SrvPositionMotor.feedbackPosition = self.getPose()
        for index in range(20):
            self.SrvPositionMotor.feedbackPosition[index] = (self.SrvPositionMotor.feedbackPosition[index]*RAD2MOTOR) + self.motorRef[index]

        return self.SrvPositionMotor


