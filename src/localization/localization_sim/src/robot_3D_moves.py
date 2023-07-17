#!/usr/bin/env python3
#coding=utf-8

#Importanto as bibliotecas e módulos 
import rospy
import math as m
from controller import Supervisor

from modularized_bhv_msgs.msg import currentStateMsg
from modularized_bhv_msgs.srv import moveRequest, moveRequestResponse #Srv associado ao service utilizado para requisitar qualquer movimento dos motores

#Setando a grafia correta das requisições para movimento de caminhada
FORWARD = 'walk_forward'
CLOCKWISE = 'rotate_clockwise'
COUNTER_CLOCKWISE = 'rotate_counter_clockwise'
POSSIBLE_REQUESTS = [FORWARD,CLOCKWISE,COUNTER_CLOCKWISE]

#Setando o step para cada tipo de movimento
ROTATION_STEP = 0.1309
WALK_STEP = 0.05

class Robot3DMover():

    def __init__(self, supervisor):
        """
        Construtor:
        - Faz a chamada de funções para definir as variáveis field e ros dos motores da simulação.
        """

        rospy.Subscriber('/transitions_and_states/state_machine', currentStateMsg, self.flagUpdate)

        self.general_supervisor = supervisor
        self.n_rotations = 1
        self.last_run = 0
        self.currentState = None
        
        self.req_dict = {'body_alignment':None,'body_search':None,'walking':None}

        self.init_3D()
    
    #Função de chamada recorrente no bhv_sim
    def callClock(self):
        """
        -> Funcao:
            - Chamar o metodo para atualizacao interna da rotacao;
            - Executar a última requisição do estado atual solicitada. 
        """

        self.rotationUpdate()
        if (self.general_supervisor.getTime() - self.last_run) > 0.5:
            self.robot3DClock(self.req_dict[self.currentState] if self.currentState in self.req_dict.keys() else None)

    #Atualização da flag
    def flagUpdate(self,message):
        self.currentState = message.currentState

    #Função de atualização da rotação dos motores
    def robot3DClock(self, movement):
        """
        -> Funcao:
            Alterar os campos de rotação e translação do node principal para simular a caminhada.
        """

        #Definição do sentido de rotação
        if movement == CLOCKWISE:
            increment = -ROTATION_STEP
        elif movement == COUNTER_CLOCKWISE:
            increment = ROTATION_STEP

        for _ in range(self.n_rotations):  
            #Rotação horária ou anti-horária
            if movement == CLOCKWISE or movement == COUNTER_CLOCKWISE:
                new_rotation = self.sim_3D_rotation_field.getSFRotation()[:3]+[self.robot_rotation+increment]
                self.sim_3D_rotation_field.setSFRotation(new_rotation)
        
        #Andar em linha reta 
        if movement == FORWARD:
            x_increment = -WALK_STEP*m.sin(self.robot_rotation)
            z_increment = -WALK_STEP*m.cos(self.robot_rotation)

            new_translation = [self.sim_3D_translation_field.getSFVec3f()[0]+x_increment,self.sim_3D_translation_field.getSFVec3f()[1],self.sim_3D_translation_field.getSFVec3f()[2]+z_increment]
            self.sim_3D_translation_field.setSFVec3f(new_translation)
        
        self.last_run = self.general_supervisor.getTime()
    
    #Função chamada no loop para atualizar internamente a rotação atual da robo
    def rotationUpdate(self):
        """
        -> Funcao:
        Atualizar a rotação 3D da robô, atraves de:
            - Capturar a posição no momento através do campo da rotação do node principal.
        """
        self.robot_rotation = self.sim_3D_rotation_field.getSFRotation()[3]
    
    #Função chamada pelo construtor para habilitação da movimentação de caminhada
    def init_3D(self):
        """
        -> Funcao:
        Inicializar todas as variáveis necessárias para caminhada, atraves de:
            - Capturar o node de Transform principal;
            - Capturar seus campos de rotação e translação;
            - Iniciar as variáveis que indica a rotação da robô em relação ao eixo absoluto;
            - Inicializa as variáveis do ROS para publicação da posição dos motores.
        """
        sim_3D_robot_node = self.general_supervisor.getFromDef('Robot3D')

        self.sim_3D_rotation_field = sim_3D_robot_node.getField('rotation')
        self.sim_3D_translation_field = sim_3D_robot_node.getField('translation')

        self.robot_rotation = self.sim_3D_rotation_field.getSFRotation()[3]
        self.robot_translation = self.sim_3D_translation_field.getSFVec3f()

        rospy.Service('/bhv2mov_communicator/3D_move_requisitions', moveRequest, self.moveSimRobot)
        self.response = moveRequestResponse()
    
    #Função responsável pela movimentação 3D de acordo com as requisições
    def moveSimRobot(self, request):
        """
        -> Funcao:
        Salvar as ultimas requisições de cada codigo como variavel deste codigo, através de:
            - Alterar no dicionário o valor da requisição da chave que fez a requisição;
        """
        self.req_dict[request._connection_header['origin'] ]= request.moveRequest        
        if 'n_rotations' in request._connection_header.keys():
            self.n_rotations = int(request._connection_header['n_rotations'])
        else:
            self.n_rotations = 1
        self.response.success = True
        return self.response