#!/usr/bin/env python3
#coding=utf-8

import rospy, sys, os
import fall_interpreter, ball_interpreter, neck_interpreter

#Importacao para os topicos ROS
from modularized_bhv_msgs.msg import stateMachineMsg #Mensagem associada ao topico utilizado para receber info dos estados da robo

edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters

class RosPacker():

    def __init__(self):
        """
        Construtor:
        - Inicializa os objeto dos interpretadores
        """

        self.parameters = BehaviourParameters()

        #Inicialização dos interpretadores em variaveis deste objeto
        self.iBall = ball_interpreter.BallInterpreter() 
        self.iFall = fall_interpreter.FallInterpreter() 
        self.iNeck = neck_interpreter.NeckInterpreter() 

        #Inicialização das variáveis do ROS
        self.pub2StateMachine = rospy.Publisher(self.parameters.stateMachineTopic, stateMachineMsg, queue_size=1) #Envia as mensagens para o stateMachineMsg
        self.stateMachineVars = stateMachineMsg()

        #Variáveis de interpretação para facilitação do fluxo
        [self.pBallPosition, self.pBallClose, self.pBallFound] = self.iBall.getValues()
        self.pFallState = self.iFall.getValues()
        [self.pHorMotorOutOfCenter, self.pHeadKickCheck] = self.iNeck.getValues() 

        self.smVarsLastValue = [self.pBallPosition, self.pBallClose, self.pBallFound,
                                self.pFallState,
                                self.pHorMotorOutOfCenter, self.pHeadKickCheck]
            
        self.publish2StateMachine()
    
    #Loopa capturando as novas interpretações para o código
    def run(self):

        while not rospy.is_shutdown():
            self.runValuesUpdate()
            self.stateMachineFlagger([self.pBallPosition, self.pBallClose, self.pBallFound,
                                  self.pFallState,
                                  self.pHorMotorOutOfCenter, self.pHeadKickCheck])

    def runValuesUpdate(self):
        [self.pBallPosition, self.pBallClose, self.pBallFound] = self.iBall.getValues()
        self.pFallState = self.iFall.getValues()
        [self.pHorMotorOutOfCenter, self.pHeadKickCheck] = self.iNeck.getValues()         

    def stateMachineFlagger(self,smVarsCurrentValue):
        if not smVarsCurrentValue == self.smVarsLastValue: #Se os valores forem diferentes do anterior, roda o runPrints
            self.smVarsLastValue = smVarsCurrentValue
            self.runPrints()
            self.publish2StateMachine()

    def publish2StateMachine(self):
        self.stateMachineVars.ballPosition = self.pBallPosition
        self.stateMachineVars.ballClose = self.pBallClose
        self.stateMachineVars.ballFound = self.pBallFound
        self.stateMachineVars.fallState = self.pFallState
        self.stateMachineVars.horMotorOutOfCenter = self.pHorMotorOutOfCenter
        self.stateMachineVars.headKickCheck = self.pHeadKickCheck

        self.pub2StateMachine.publish(self.stateMachineVars)
    
    def runPrints(self):
        print("----------------------------")
        print("Posicao da bola: ", self.pBallPosition)
        print("Encontrada: ", self.pBallFound, "   | Bola proxima: ", self.pBallClose)
        print("Posicao de robo (queda): ", self.pFallState)
        print("Posição horizontal da cabeça: ", self.pHorMotorOutOfCenter)
        print("Cabeca confirma o chute: ", self.pHeadKickCheck)
        print("----------------------------")

if __name__ == '__main__':
    rospy.init_node('ROS_packer_node', anonymous=False)

    packer = RosPacker() #Inicia o agrupador
    packer.run()  #Inicia o loop do agrupador

    rospy.spin()