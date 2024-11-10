#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import rospy
import os
import sys
import time
from vision_msgs.msg import Webotsmsg
from movement_utils.srv import *
from movement_utils.msg import *
from geometry_msgs.msg import PoseStamped  # Import para o estado de queda

edrom_dir = '/home/' + os.getlogin() + '/edromufu/src/'

sys.path.append(edrom_dir + 'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters

class GoalkeeperBrain:
    def __init__(self):
        rospy.init_node('goalkeeper_brain')

        self.parameters = BehaviourParameters()

        # Espera pelos serviços
        rospy.wait_for_service('u2d2_comm/feedbackHead')
        self.motorsFeedback = rospy.ServiceProxy('u2d2_comm/feedbackHead', head_feedback)
        self.pageCall = rospy.ServiceProxy('movement_central/request_page', page)

        # Inscrições nos tópicos
        rospy.Subscriber(self.parameters.vision2BhvTopic, Webotsmsg, self.updateBallParameters)
        rospy.Subscriber(self.parameters.headPositionsTopic, head_motors_data, self.updateHorRotation)
        rospy.Subscriber(self.parameters.fallStateTopic, PoseStamped, self.updateFallState)  # Novo Subscriber para estado de queda

        # Variáveis internas
        self.found = False
        self.x = 0
        self.y = 0
        self.timesFoundFalse = 0
        self.fallState = self.parameters.up  # Estado inicial como "em pé"

    def updateBallParameters(self, msg):
        """
        Callback para atualizar os parâmetros da bola a partir dos dados de visão
        """
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
            self.ballClose = self.y > self.parameters.yCenterBottomLimit
            self.timesFoundFalse = 0

    def updateHorRotation(self, msg):
        """
        Callback para atualizar a rotação horizontal da cabeça
        """
        self.HorRotation, self.VerRotation = msg.pos_vector

    def updateFallState(self, msg):
        """
        Callback para atualizar o estado de queda
        """
        # Define o estado de queda de acordo com a mensagem recebida
        self.fallState = msg.pose.position.x  # Representação do estado da queda

    def run(self):
        while not rospy.is_shutdown():
            # Verifica se o robô está em pé antes de realizar ações de defesa
            if self.fallState == self.parameters.up:
                if self.found:
                    self.pageCall('natasha_squat')

                elif self.found and self.ballClose:
                    # Decide a direção da defesa com base na rotação horizontal
                    if self.HorRotation < self.parameters.lookingLeftRad / 2:
                        self.pageCall('natasha_left_defense')
                        self.fall()
                    elif self.HorRotation > self.parameters.lookingRightRad / 2:
                        self.pageCall('natasha_right_defense')
                        self.fall()
            else:
                # Se o robô estiver em queda, chama a página de queda
                self.fall()

    def fall(self):
        """
        Chama a página de 'fallen_natasha' quando detecta uma queda
        """
        self.pageCall('fallen_natasha')

if __name__ == '__main__':
    goalkeeper_brain = GoalkeeperBrain()
    goalkeeper_brain.run()
    rospy.spin()
