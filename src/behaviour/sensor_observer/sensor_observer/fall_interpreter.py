#!/usr/bin/env python3
#coding=utf-8

import rclpy
from rclpy.node import Node
import os, sys
from geometry_msgs.msg import Vector3

edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters

class FallInterpreter(Node):

    def __init__(self):
        """
        Construtor:
        - Define as variáveis do ROS
        - Define e inicializa variáveis do código
        """
        super().__init__('fall_interpreter')
        
        self.parameters = BehaviourParameters()

        # Variáveis do ROS
        self.create_subscription(Vector3, self.parameters.imuAccelTopic, self.callback_sensor, 10)

        # Variáveis de código
        self.fallState = self.parameters.up  # Estado da queda do robô, sendo up = em pé
        self.countFalled = 0  # Contador de quedas interpretadas para segurança
    
    # Função chamada quando necessário saber a interpretação da queda para alguma requisição
    def getValues(self):
        """
        -> Output:
            - fallState: Estado de queda avaliado pelo código, Up = de pé
        """
        return self.fallState
    
    # Callback do tópico de informações do acelerômetro
    def callback_sensor(self, msg):
        """
        -> Função:
        Avaliar se houve queda e para que lado através de:
            - Recebe os dados do acelerômetro do simulador no msg
            - Interpreta a medição y retornando se houve queda
            - Interpreta as medições x e z retornando a orientação da queda
            - Confia mais no estar de pé do que na queda, evitando falsos positivos 
        -> Input:
            - msg: Variável associada à mensagem recebida no tópico, contém as
            informações do acelerômetro    
        """

        # Contando quantas das últimas medições detectou-se queda
        if abs(msg.x) > self.parameters.xGravitySecurity or abs(msg.y) > self.parameters.xGravitySecurity:
            self.countFalled += 1
        else:
            self.fallState = self.parameters.up
            self.countFalled = 0

        # Situação na qual interpretou-se queda muitas vezes seguidas
        if self.countFalled > self.parameters.timerCountLimit:
            if msg.x < self.parameters.xSensorBack:
                # Caiu de costas
                self.fallState = self.parameters.back
            elif msg.x > self.parameters.xSensorFront:
                # Caiu de frente     
                self.fallState = self.parameters.front
            elif msg.y < self.parameters.ySensorRight:
                # Caiu sobre o lado direito    
                self.fallState = self.parameters.right
            elif msg.y > self.parameters.ySensorLeft:
                # Caiu sobre o lado esquerdo    
                self.fallState = self.parameters.left

def main(args=None):
    rclpy.init(args=args)
    
    fall_interpreter = FallInterpreter()
    
    try:
        rclpy.spin(fall_interpreter)
    except KeyboardInterrupt:
        pass
    finally:
        fall_interpreter.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
