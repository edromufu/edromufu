#!/usr/bin/env python3
#coding=utf-8

from controller import Supervisor, Keyboard
import rospy

#Vetores de posição e rotação do robô no início e durante o FP
standStillRobotTranslationStart = [-0.80, 0.02, 0.44]
standStillRobotRotationStart    = [0.0279, -0.972, -0.234, 0.0149]

standStillRobotTranslationFP  = [0.157431, 0.411797, -0.735326]
standStillRobotRotationFP     = [0.0368072, 0.985366, -0.166432, 2.69003]

#Valores associados Às teclas pressionadas
FPkey = 80 #p
STARTkey = 83 #s

class SupervisorNatasha(object):
    ###########################FUNÇÕES DO CÓDIGO###########################

    #Construtor, recebe o objeto da robô gerado no controlador central e define as variáveis necessárias para o funcionamento do código
    def __init__(self, supervisor_object):
        #Inicialização do supervisor e do teclado
        self.supervisor = supervisor_object
        self.input = Keyboard()
        self.input.enable(int(self.supervisor.getBasicTimeStep()))

        #Inicialização do node da Natasha e captura dos seus campos de translação e rotação
        self.natasha_node = self.supervisor.getSelf()
        self.natasha_translation_field = self.natasha_node.getField('translation')
        self.natasha_rotation_field = self.natasha_node.getField('rotation')

    ##Define o loop, de receber o input do teclado, do código
    def loop(self):
        key = self.input.getKey()
        if(key != -1):
            return(self.resetPosition(key))

    ###########################FUNÇÕES DO WEBOTS###########################

    #Função que realiza o reposicionamento da robô através dos vetores típicos de cada situação e anulação temporária da física
    def resetPosition(self, action):
        self.supervisor.simulationResetPhysics()
        if(action == FPkey):
            self.natasha_translation_field.setSFVec3f(standStillRobotTranslationFP)
            self.supervisor.simulationResetPhysics()
            self.natasha_rotation_field.setSFRotation(standStillRobotRotationFP)
            self.supervisor.simulationResetPhysics()
            return 'repositionedToFP'
        elif(action == STARTkey):
            self.natasha_translation_field.setSFVec3f(standStillRobotTranslationStart)
            self.supervisor.simulationResetPhysics()
            self.natasha_rotation_field.setSFRotation(standStillRobotRotationStart)
            self.supervisor.simulationResetPhysics()  
            #Return utilizado no código do supervisor central 
            return 'repositionedToStart'
