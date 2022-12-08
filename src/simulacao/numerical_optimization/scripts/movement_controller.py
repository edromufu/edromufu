#!/usr/bin/env python3
#coding=utf-8

import rospy, math
from controller import Robot
from movement_msgs.msg import WebotsMsg
from movement_msgs.srv import LipCmdSrv

RAD2MOTOR = 651.74
MOTORREF = 2048

fpVector = [-0.1887255609035492, 0.1871912181377411, -0.04756497964262962, 0.04603062570095062, 1.5696443319320679, -1.571178674697876, 0.06597723066806793, -0.06290852278470993, -0.1963973343372345, 0.1825881451368332, 0.7871236801147461, 0.7978641986846924, -0.6597722768783569, 0.6751158237457275, 0.2056034654378891, -0.1948629766702652, 0.2025347501039505, -0.2102065235376358, 0.0, 0.0]

class ControllerMovement(object): 
    ###########################FUNÇÕES DO CÓDIGO###########################

    #Construtor, recebe o objeto da robô gerado no controlador central e define as variáveis necessárias para o funcionamento do código
    def __init__(self, robot):

        #Inicialização das mensagens e tópicos do ROS
        rospy.Subscriber('opencm/conversion', WebotsMsg, self.requestCmCallback)

        #Inicialização das variáveis de manipulação no código
        self.motorObjectArray = []
        self.dataArray = [0]*20
        self.velocityArray = [2]*20
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
        self.velocityFunction()

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

    #Função para retorno de todos os motores para a posição inicial
    def zeros(self):
        for index in range(20):
            self.motorObjectArray[index].setPosition(0)

    #Função para chamada manual da FirstPose
    def goToFP(self):
        for index in range(20):
            self.motorObjectArray[index].setPosition(fpVector[index])            
    
    ###########################FUNÇÕES DO ROS###########################
    #Função de callback do OpencmReq, pega o vetor de posições enviado e coloca em uma variável manipulável no código todo
    def requestCmCallback(self, msg):
        self.control = msg.control
        for index in range(20):
            self.dataArray[index] = msg.position[index]
    
    #Função trocar o estado do walk_flag de acordo com a necessidade
    def changeWalkFlag(self, option, velVec):
        
        rospy.wait_for_service('/humanoid_walking/walking_cmd')

        try:
            walkCmdService = rospy.ServiceProxy('/humanoid_walking/walking_cmd', LipCmdSrv)
            
            walkCmdService(False, False, option, False, True, velVec[0], velVec[1], velVec[2])

        except rospy.ServiceException as e:
            rospy.loginfo("Service call failed: %s"%e)

