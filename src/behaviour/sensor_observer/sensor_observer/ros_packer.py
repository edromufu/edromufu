#!/usr/bin/env python3
#coding=utf-8

import rclpy
from rclpy.node import Node
import sys, os
import fall_interpreter, ball_interpreter, neck_interpreter

# Importação para os tópicos ROS
from modularized_bhv_msgs.msg import StateMachineMsg  # Mensagem associada ao tópico utilizado para receber info dos estados do robô

edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters
NUM_CONNECTIONS = 2

class RosPacker(Node):

    def __init__(self):
        """
        Construtor:
        - Inicializa os objeto dos interpretadores
        """
        super().__init__('ros_packer')

        self.parameters = BehaviourParameters()

        # Inicialização dos interpretadores em variáveis deste objeto
        self.iBall = ball_interpreter.BallInterpreter() 
        self.iFall = fall_interpreter.FallInterpreter() 
        self.iNeck = neck_interpreter.NeckInterpreter() 

        # Inicialização das variáveis do ROS
        self.pub2StateMachine = self.create_publisher(StateMachineMsg, self.parameters.stateMachineTopic, 1)  # Envia as mensagens para o StateMachineMsg
        self.stateMachineVars = StateMachineMsg()

        # Variáveis de interpretação para facilitação do fluxo
        [self.pBallPosition, self.pBallClose, self.pBallFound] = self.iBall.getValues()
        self.pFallState = self.iFall.getValues()
        [self.pHorMotorOutOfCenter, self.pHeadKickCheck] = self.iNeck.getValues() 

        self.smVarsLastValue = [self.pBallPosition, self.pBallClose, self.pBallFound,
                                self.pFallState,
                                self.pHorMotorOutOfCenter, self.pHeadKickCheck]
        
        while self.pub2StateMachine.get_subscription_count() != NUM_CONNECTIONS:
            pass

        self.publish2StateMachine()
    
    # Loop capturando as novas interpretações para o código
    def run(self):
        while rclpy.ok():
            self.runValuesUpdate()
            self.stateMachineFlagger([self.pBallPosition, self.pBallClose, self.pBallFound,
                                      self.pFallState,
                                      self.pHorMotorOutOfCenter, self.pHeadKickCheck])
            rclpy.spin_once(self, timeout_sec=0.1)

    def runValuesUpdate(self):
        [self.pBallPosition, self.pBallClose, self.pBallFound] = self.iBall.getValues()
        self.pFallState = self.iFall.getValues()
        [self.pHorMotorOutOfCenter, self.pHeadKickCheck] = self.iNeck.getValues()         

    def stateMachineFlagger(self, smVarsCurrentValue):
        if smVarsCurrentValue != self.smVarsLastValue:  # Se os valores forem diferentes do anterior, roda o runPrints
            self.smVarsLastValue = smVarsCurrentValue
            self.runPrints()
            self.publish2StateMachine()

    def publish2StateMachine(self):
        self.stateMachineVars.ball_position = self.pBallPosition
        self.stateMachineVars.ball_close = self.pBallClose
        self.stateMachineVars.ball_found = self.pBallFound
        self.stateMachineVars.fall_state = self.pFallState
        self.stateMachineVars.hor_motor_out_of_center = self.pHorMotorOutOfCenter
        self.stateMachineVars.head_kick_check = self.pHeadKickCheck

        self.pub2StateMachine.publish(self.stateMachineVars)
    
    def runPrints(self):
        print("----------------------------")
        print("Posição da bola: ", self.pBallPosition)
        print("Encontrada: ", self.pBallFound, "   | Bola próxima: ", self.pBallClose)
        print("Posição do robô (queda): ", self.pFallState)
        print("Posição horizontal da cabeça: ", self.pHorMotorOutOfCenter)
        print("Cabeça confirma o chute: ", self.pHeadKickCheck)
        print("----------------------------")

def main(args=None):
    rclpy.init(args=args)
    
    ros_packer = RosPacker()  # Inicia o agrupador
    ros_packer.run()  # Inicia o loop do agrupador

    rclpy.shutdown()

if __name__ == '__main__':
    main()
