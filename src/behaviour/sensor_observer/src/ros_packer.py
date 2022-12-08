#!/usr/bin/env python3
#coding=utf-8

import rospy
import time
#import fall_interpreter, neck_interpreter 
import ball_interpreter

#Importacao para os topicos ROS
from modularized_bhv_msgs.msg import stateMachineMsg #Mensagem associada ao topico utilizado para receber info dos estados da robo

N_SUBSCRIBERS = 2

class RosPacker():

    def __init__(self):
        """
        Construtor:
        - Inicializa os objeto dos interpretadores
        """

        #Inicialização dos interpretadores em variaveis deste objeto
        self.iBall = ball_interpreter.BallInterpreter() #Ve se a robo achou e onde esta a bola
        #self.iFall = fall_interpreter.FallInterpreter() #Ve se a robo esta em pe e qual e a posicao da queda
        #self.iNeck = neck_interpreter.NeckInterpreter() #Captura as informacoes dos motores e define os intervalos extremos do pescoco

        #Inicialização das variáveis do ROS
        self.pub2StateMachine = rospy.Publisher('/sensor_observer/state_machine_vars', stateMachineMsg, queue_size=1) #Envia as mensagens para o stateMachineMsg
        self.stateMachineVars = stateMachineMsg()

        #Variáveis de interpretação para facilitação do fluxo
        self.pBallPosition = self.iBall.getValues()[0] #Captura a posicao da bola em x e y
        self.pBallClose = self.iBall.getValues()[1] #Captura se a bola ta perto
        self.pBallFound = self.iBall.getValues()[2] #Ve se a bola foi achada
        #self.pFallState = self.iFall.getValues() #Captura a posicao da queda
        #self.pHeadKickCheck = self.iNeck.getValues()[1] #Ve se a cabeca ta no local certo para a robo mudar o estado para chute
        #self.pPossibleHeadMovs = self.iNeck.getValues()[0] #Ve qual sao as possibilidades de movimento devido aos intervalos extremos do pescoco
        #self.pHorMotorOutOfCenter = self.iNeck.getValues()[2] #Ve se o motor horizontal esta fora do centro
        #self.pHorMotorPosition = self.iNeck.getValues()[3] #Pega o valor do motor horizontal

        self.smVarsLastValue = [self.pBallPosition,self.pBallFound,self.pBallClose]
                               # self.pFallState,self.pHeadKickCheck,self.pPossibleHeadMovs, self.pHorMotorOutOfCenter] #?

        while self.pub2StateMachine.get_num_connections() != N_SUBSCRIBERS:
            time.sleep(1)
            
        self.publish2StateMachine()
    
    #Loopa capturando as novas interpretações para o código
    def run(self):

        while not rospy.is_shutdown():
            self.runValuesUpdate()
            self.runMethodsCalls()

    def runValuesUpdate(self):
        self.pBallPosition = self.iBall.getValues()[0]
        self.pBallClose = self.iBall.getValues()[1]
        self.pBallFound = self.iBall.getValues()[2]
        #self.pFallState = self.iFall.getValues()
        #self.pHeadKickCheck = self.iNeck.getValues()[1]
        #self.pPossibleHeadMovs = self.iNeck.getValues()[0]
        #self.pHorMotorOutOfCenter = self.iNeck.getValues()[2]
        #self.pHorMotorPosition = self.iNeck.getValues()[3]

    def runMethodsCalls(self):
        self.stateMachineFlagger([self.pBallPosition,self.pBallFound,self.pBallClose])
                                #self.pFallState,self.pHeadKickCheck,self.pPossibleHeadMovs, self.pHorMotorOutOfCenter])

    def stateMachineFlagger(self,smVarsCurrentValue):
        if not smVarsCurrentValue == self.smVarsLastValue: #Se os valores forem diferentes do anterior, roda o runPrints
            self.smVarsLastValue = smVarsCurrentValue
            self.runPrints()
            self.publish2StateMachine()

    def publish2StateMachine(self):
        #self.stateMachineVars.fallState = self.pFallState
        self.stateMachineVars.ballFound = self.pBallFound
        self.stateMachineVars.ballClose = self.pBallClose
        self.stateMachineVars.ballRelativePosition = self.pBallPosition
        #self.stateMachineVars.verAngleAccomplished = self.pHeadKickCheck
        #self.stateMachineVars.headPossibleMovements = self.pPossibleHeadMovs
        #self.stateMachineVars.horMotorOutOfCenter = self.pHorMotorOutOfCenter
        #self.stateMachineVars.horMotorPosition = self.pHorMotorPosition

        self.pub2StateMachine.publish(self.stateMachineVars)
    
    def runPrints(self):
        print("----------------------------")
        print("Posicao da bola: ", self.pBallPosition)
        print("Encontrada: ", self.pBallFound, "   | Bola proxima: ", self.pBallClose)
        #print("Posicao de robo (queda): ", self.pFallState)
        #print("Movimentos disponíveis: ", self.pPossibleHeadMovs)
        #print("Cabeca confirma o chute: ", self.pHeadKickCheck)
        #print("Motor horizontal fora do centro: ", self.pHorMotorOutOfCenter)
        print("----------------------------")

if __name__ == '__main__':
    rospy.init_node('ROS_packer_node', anonymous=False)

    packer = RosPacker() #Inicia o agrupador
    packer.run()  #Inicia o loop do agrupador

    rospy.spin()