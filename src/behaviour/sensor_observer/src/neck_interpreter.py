#!/usr/bin/env python3
#coding=utf-8

import rospy, os, sys
from movement_utils.msg import head_motors_data  #Mensagem associada ao tópico utilizado para receber info dos motores da cabeça

edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters

class NeckInterpreter():

    def __init__(self):
        """
        Construtor:
        - Define as variaveis do ROS
        - Define e inicializa variaveis do código
        """

        self.parameters = BehaviourParameters()

        #Variaveis do ROS
        rospy.Subscriber(self.parameters.headPositionsTopic, head_motors_data, self.callback_positions)

        #Variaveis de código
        self.horHeadPosition = None
        self.verAngleAccomplished = False

    #Funcao chamada pelo agrupador ROS quando necessitar saber 
    #a interpretacao dos motores da cabeça para alguma requisicao
    def getValues(self):
        """
        -> Output:
            - horHeadPosition: Informa a posição horizontal atual da cabeça
            - verAngleAccomplished: Informa se a cabeca esta suficientemente rotacionada verticalmente para um bom chute
        """

        return self.horHeadPosition, self.verAngleAccomplished
    
    #Callback do tópico de infos dos motores da cabeça do ROS
    def callback_positions(self, msg):
        """
        -> Funcao:
        Repassar os valores dos motores da cabeça da robô para as variáveis de código 
        acessando os valores recebidos no tópico e verificar dinamicamente se o motor
        vertical atingiu o estabelecido como "bom chute"
        -> Input:
            - msg: Variavel associada a mensagem recebida no topico do ROS, contem as
            informacoes dos motores horizontal e vertical da cabeça   
        """

        horMotorValue = msg.pos_vector[0]
        verMotorValue = msg.pos_vector[1]

        if (horMotorValue < self.parameters.lookingLeftRad) and (horMotorValue > self.parameters.lookingRightRad):
            self.horHeadPosition = self.center
        elif horMotorValue > self.parameters.lookingLeftRad:
            self.horHeadPosition = self.left
        else:
            self.horHeadPosition = self.right

        if verMotorValue < minVerRad2Kick:
            self.verAngleAccomplished = True


