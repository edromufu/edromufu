#!/usr/bin/env python3
#coding=utf-8

import rclpy
from rclpy.node import Node
import os, sys
from vision_msgs.msg import Webotsmsg

edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters

class BallInterpreter(Node):

    def __init__(self):
        """
        Construtor:
        - Define as variáveis do ROS
        - Define e inicializa variáveis do código
        """
        super().__init__('ball_interpreter')
        
        self.parameters = BehaviourParameters()

        # Variáveis do ROS
        self.create_subscription(Webotsmsg, self.parameters.vision2BhvTopic, self.callback_vision, 10)

        # Variáveis de código
        self.ballRelativePosition = 'none'
        self.ballClose = False
        self.ballFound = False
        self.countDistance = 0
        self.countFound = 0

    # Função chamada quando necessário saber as interpretações da bola para alguma requisição
    def getValues(self):
        """
        -> Output:
            - ballRelativePosition: Última posição relativa da bola interpretada
            - ballClose: Interpretação da proximidade da bola
            - ballFound: Se False, bola perdida há muito tempo
        """
        return self.ballRelativePosition, self.ballClose, self.ballFound   

    # Callback do tópico de informações da bola
    def callback_vision(self, general):    
        """
        -> Função:
        Avaliar a bola através de:
            - Recebe os dados da bola da visão no campo ball do argumento general
            - Interpreta o x e y retornando a posição relativa da bola
            - Interpreta o width e height retornando a proximidade da bola
            - Realiza resets das variáveis booleanas baseado em contador
            * Os dados só são interpretados, ou seja, a posição relativa só é atualizada
            * se a bola estiver sendo encontrada (para ter uma espécie de 'visto por último')  
        -> Input:
            - general: Variável associada à mensagem recebida no tópico, contém as
            informações de todos os objetos, e separada somente para a bola nesse caso.   
        """

        # Captura das informações da bola de dentro da mensagem completa
        msg = general.ball

        # Contador para informar que a bola foi perdida após um número de vezes sem encontrá-la
        self.countFound += 1
        if self.countFound > self.parameters.timerCountLimit:
            self.ballFound = False
            self.ballClose = False
            self.ballRelativePosition = 'none'

        if msg.found:
            # Reseta o contador de informar que a bola foi perdida, pois encontrou :)
            self.ballFound = True
            self.countFound = 0

            # Módulo de verificação da proximidade da bola, serve para resetar
            # a interpretação apenas após um número definido de medidas desfavoráveis
            if msg.roi_width * msg.roi_height < self.parameters.closeSize:
                self.countDistance += 1
                if self.countDistance > self.parameters.timerCountLimit:
                    self.ballClose = False
            else:
                self.countDistance = 0
                self.ballClose = True

            # Módulo de verificação da posição relativa da bola
            # Interpretação horizontal
            if msg.x < self.parameters.xCenterLeftLimit:
                analysisX = self.parameters.left
            elif msg.x > self.parameters.xCenterRightLimit:
                analysisX = self.parameters.right
            else:
                analysisX = self.parameters.center
            
            # Interpretação vertical
            if msg.y > self.parameters.yCenterBottomLimit:  # Deve ser maior por conta da referência ([0,0] no canto superior esquerdo)
                analysisY = self.parameters.bottom
            elif msg.y < self.parameters.yCenterTopLimit:
                analysisY = self.parameters.top
            else:
                analysisY = self.parameters.center

            # Junção das interpretações em cada eixo
            if analysisX == self.parameters.center and analysisY == self.parameters.center:
                analysis = self.parameters.center
            else:
                analysis = f'{analysisX} {analysisY}'

            self.ballRelativePosition = analysis

def main(args=None):
    rclpy.init(args=args)
    
    ball_interpreter = BallInterpreter()
    
    try:
        rclpy.spin(ball_interpreter)
    except KeyboardInterrupt:
        pass
    finally:
        ball_interpreter.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
