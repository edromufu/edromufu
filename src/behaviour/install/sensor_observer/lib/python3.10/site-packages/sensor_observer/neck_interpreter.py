#!/usr/bin/env python3
#coding=utf-8

import rclpy
from rclpy.node import Node
import os, sys
from movement_utils.msg import HeadMotorsData  # Mensagem associada ao tópico utilizado para receber info dos motores da cabeça

edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters

class NeckInterpreter(Node):

    def __init__(self):
        """
        Construtor:
        - Define as variáveis do ROS
        - Define e inicializa variáveis do código
        """
        super().__init__('neck_interpreter')

        self.parameters = BehaviourParameters()

        # Variáveis do ROS
        self.create_subscription(HeadMotorsData, self.parameters.headPositionsTopic, self.callback_positions, 10)

        # Variáveis de código
        self.horHeadPosition = 'none'
        self.verAngleAccomplished = False

    # Função chamada quando necessário saber a interpretação dos motores da cabeça para alguma requisição
    def getValues(self):
        """
        -> Output:
            - horHeadPosition: Informa a posição horizontal atual da cabeça
            - verAngleAccomplished: Informa se a cabeça está suficientemente rotacionada verticalmente para um bom chute
        """
        return self.horHeadPosition, self.verAngleAccomplished
    
    # Callback do tópico de informações dos motores da cabeça
    def callback_positions(self, msg):
        """
        -> Função:
        Repassar os valores dos motores da cabeça do robô para as variáveis de código 
        acessando os valores recebidos no tópico e verificar dinamicamente se o motor
        vertical atingiu o estabelecido como "bom chute"
        -> Input:
            - msg: Variável associada à mensagem recebida no tópico, contém as
            informações dos motores horizontal e vertical da cabeça   
        """

        horMotorValue = msg.pos_vector[0]
        verMotorValue = msg.pos_vector[1]

        if self.parameters.lookingRightRad < horMotorValue < self.parameters.lookingLeftRad:
            self.horHeadPosition = self.parameters.center
        elif horMotorValue > self.parameters.lookingLeftRad:
            self.horHeadPosition = self.parameters.left
        else:
            self.horHeadPosition = self.parameters.right

        if verMotorValue < self.parameters.minVerRad2Kick:
            self.verAngleAccomplished = True
        else:
            self.verAngleAccomplished = False

def main(args=None):
    rclpy.init(args=args)
    
    neck_interpreter = NeckInterpreter()
    
    try:
        rclpy.spin(neck_interpreter)
    except KeyboardInterrupt:
        pass
    finally:
        neck_interpreter.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
