#!/usr/bin/env python3
#coding=utf-8

import numpy as np
import rclpy, os, sys, time
from vision_msgs.msg import Webotsmsg
from movement_utils.srv import *
from movement_utils.msg import *
from modularized_bhv_msgs.msg import GameControllerMsg  # Mensagem do GameController

edrom_dir = '/home/' + os.getlogin() + '/edromufu/src/'

sys.path.append(edrom_dir + 'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters

class goalkeeper_brain:
    def __init__(self):
        rclpy.init(args=sys.argv)
        self.node = rclpy.create_node('goalkeeper_brain')

        self.parameters = BehaviourParameters()

        self.motorsFeedback = self.node.create_client(HeadFeedback, 'u2d2_comm/feedbackHead')
        self.pageCall = self.node.create_client(Page, 'movement_central/request_page')

        while not self.motorsFeedback.wait_for_service(timeout_sec=1.0):
            self.node.get_logger().info('Service not available, waiting again...')
        while not self.pageCall.wait_for_service(timeout_sec=1.0):
            self.node.get_logger().info('Service not available, waiting again...')

        # Subscribes para as mensagens de visão e dos motores
        self.node.create_subscription(Webotsmsg, self.parameters.vision2BhvTopic, self.updateBallParameters, 10)
        self.node.create_subscription(HeadMotorsData, self.parameters.headPositionsTopic, self.updateHorRotation, 10)

        # Subscriber para o GameController
        self.node.create_subscription(GameControllerMsg, 'Game_Controller', self.game_controller_callback, 10)

        # Variáveis de estado
        self.found = False
        self.x = 0
        self.y = 0
        self.timesFoundFalse = 0
        self.game_controller_state = None  #Variável para controlar o estado do gamecontroller
    
    def game_controller_callback(self, msg):
 
        self.game_controller_state = msg.game_state
        self.node.get_logger().info(f'Estado do GameController: {self.game_controller_state}')

    def updateBallParameters(self, msg):
        ballInfos = msg.ball

        if not ballInfos.found:
            self.timesFoundFalse += 1
            if self.timesFoundFalse == 3:
                self.found = False
                self.timesFoundFalse = 0
        else:
            self.found = True
            self.x = ballInfos.x
            self.y = ballInfos.y
            self.ballClose = True if self.y > self.parameters.yCenterBottomLimit else False
            self.timesFoundFalse = 0
            self.hasReceivedVision = True
    
    def updateHorRotation(self, msg):
        self.HorRotation, VerRotation = msg.pos_vector
    
    def run(self):
        while rclpy.ok():

            if self.game_controller_state == 3:  # Playing
                if self.found:
                    self.pageCall('natasha_squat')

                elif self.found and self.ballClose:
                    # >0 Direita e <0 esquerda
                    if self.HorRotation < self.parameters.lookingLeftRad / 2:
                        self.pageCall('natasha_left_defense')
                        self.fall()
                    elif self.HorRotation > self.parameters.lookingRightRad / 2:
                        self.pageCall('natasha_right_defense')
                        self.fall()
                    else:
                        pass


                        #CONTROLADORES PARA INTERAÇÃO DO GAMECONTROLLER (ADICIONAR PAGES AQUI)
            elif self.game_controller_state == 1:  # Ready
                self.node.get_logger().info('GameController: Ready - Preparando para começar')

            elif self.game_controller_state == 2:  # Set
                self.node.get_logger().info('GameController: Set - Posicionando-se')
                
            elif self.game_controller_state == 4:  # Finished
                self.node.get_logger().info('GameController: Finished - Parando ações')

    def fall(self):
        while rclpy.ok():
            self.pageCall('fallen_natasha')
                

if __name__ == '__main__':
    goalkeeper = goalkeeper_brain()
    goalkeeper.run()
    rclpy.spin(goalkeeper.node)
