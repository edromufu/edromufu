#!/usr/bin/env python3
#coding=utf-8

import rospy
import math as m
import numpy as np
from controller import Supervisor

from modularized_bhv_msgs.srv import moveRequest, moveRequestResponse #Srv associado ao service utilizado para requisitar qualquer movimento dos motores

#Setando a grafia correta das requisições de page
KICK = 'kick'
GET_UP_FRONT = 'front_up'
GET_UP_BACK = 'back_up'
POSSIBLE_REQUESTS = [KICK, GET_UP_FRONT, GET_UP_BACK]

class RobotPagesExec():

    def __init__(self, supervisor):
        """
        Construtor:
        - Faz a chamada de funções para definir as variáveis para checagem e reprodução das pages.
        """
        self.general_supervisor = supervisor

        rospy.Service('/bhv2mov_communicator/page_requisitions', moveRequest, self.pageSimRobot)
        self.response = moveRequestResponse()

        self.init_kick_check()

    #Função chamada no construtor para habilitar as checagens e realização da page de chute
    def init_kick_check(self):
        """
        -> Funcao:
        Tornar possível a realização da page de chute, atraves de:
            - Capturar os nodes do Webots necessários para as checagens do chute;
            - Capturar os nodes necessários para aplicação da força no chute.
        """

        self.ball_node = self.general_supervisor.getFromDef('Ball')

        self.ball_translation_field = self.ball_node.getField('translation')

        robot_3D_node = self.general_supervisor.getFromDef('Robot3D')
        self.robot_translation_field = robot_3D_node.getField('translation')

        self.robot_rotation_field = robot_3D_node.getField('rotation')
    
    #Função chamada ao solicitar um chute para verificar sua possibilidade
    def kick(self):
        """
        -> Funcao:
        Avaliar a possibilidade de um chute, atraves de:
            - Verificar se a bola está na frente da robo;
            - Verificar se a bola está próxima à robô;
            - Encontrar o vetor da força do chute.
        """

        robot_x_z = [self.robot_translation_field.getSFVec3f()[0]] + [self.robot_translation_field.getSFVec3f()[2]]
        ball_x_z = [self.ball_translation_field.getSFVec3f()[0]] + [self.ball_translation_field.getSFVec3f()[2]]
        robot_theta = self.robot_rotation_field.getSFRotation()[3]

        robot_to_ball_vec = [ball_x_z[0]-robot_x_z[0],ball_x_z[1]-robot_x_z[1]]
        forward_vec = [-0.005*m.sin(robot_theta), -0.005*m.cos(robot_theta)]

        robot_to_ball_auxiliar_vec = [robot_to_ball_vec[0]+forward_vec[0],robot_to_ball_vec[1]+forward_vec[1]]

        distance_robot_to_ball = m.sqrt((robot_to_ball_vec[0]**2)+(robot_to_ball_vec[1]**2))
        is_robot_facing_ball =  distance_robot_to_ball - m.sqrt((robot_to_ball_auxiliar_vec[0]**2)+(robot_to_ball_auxiliar_vec[1]**2))

        unit_robot_to_ball_vec = robot_to_ball_vec / np.linalg.norm(robot_to_ball_vec)
        unit_forward_vec = forward_vec / np.linalg.norm(forward_vec)
        dot_product = np.dot(unit_robot_to_ball_vec, unit_forward_vec)
        angle = np.arccos(dot_product)

        if is_robot_facing_ball < 0 and angle < 0.7 and distance_robot_to_ball < (1+angle/4)*0.16:
            self.general_supervisor.getFromDef('color').getField('baseColor').setSFColor([0,1,0])
            self.ball_node.addForce([unit_robot_to_ball_vec[0],0,unit_robot_to_ball_vec[1]],False)
            return(True)
        else:
            return(False)
    
    #Função responsável pela execução das pages de acordo com as requisições
    def pageSimRobot(self, request):
        """
        -> Funcao:
        Realizar a chamada das funções de execução das pages de acordo com a requisição, atraves de:
            - Comparar a requisição com os padrões definidos;
            - Chamar a função adequada da situação.
        """
        if request.moveRequest in POSSIBLE_REQUESTS:
            calm_down = True
            initial_time = self.general_supervisor.getTime()
        else:
            calm_down = False

        if request.moveRequest == KICK:
            self.response = self.kick()
        
        if calm_down:
            while self.general_supervisor.getTime()-initial_time < 1:
                pass

        return self.response
        
