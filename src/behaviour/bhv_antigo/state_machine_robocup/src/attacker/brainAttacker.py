#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import attacker
import thinkAttacker
import time
import rospy
import yamlTransition 
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import *
from vision_msgs.msg import Webotsmsg as WebotsVisionMsg, Ball
from behaviour_msgs.msg import StateMachineActionsMsg
from behaviour_msgs.srv import *
from movement_msgs.srv import *
from movement_msgs.msg import *

"""
Definições estabelecidas na criação desse código do behavior:

    - Toda método callback SOMENTE irá pegar as msgs do Ros e repassa-lás para a variaveis da própria Brain (criadas no construtor(__init__));
    - Ainda nos métodos callback, lá será onde iremos também chamar os métodos da Think, que são métodos que trabalham, calculam e devolve outras variaveis 
    para novamente ser passadas para a Brain;
    - Métodos callback NUNCA deverão ter um retorno, devido ao fato de eles somente repassarem as valores para as variaveis criadas no construtor da Brain;
    - A Think não deve receber diretamente a msg do ROS, a msg do ROS primeiramente atualiza as variaveis da Brain e posteriormente essas são repassadas 
    para os métodos da think;
    - O métodos destinados a realmente passar comandos para o movimento são os métodos run;
    - As variaveis SEMPRE serão passadas para a maquina de estados dentro do método update_state_machine.
"""

class Brain():

    def __init__(self):
        self.moving = False

        # Variaveis para serem mandadas para a cabeça
        self.headMsg = HeadMoveMsg()
        self.motorhead = 0
        self.neck_horizontal_position = -1
        self.neck_vertical_position = -1
        self.motor_limit_reached = False

        # Variaveis para a visão
        self.searching = False
        self.ball = False
        self.ball_centered = False
        self.ball_close = False
        self.x_ball = -1
        self.y_ball = -1
        self.roi_width = -1
        self.roi_height = -1

        # Variáveis dos sensores do movimento
        self.sensor = False
        self.falled = False 
        self.position_falled = ''
        self.x_sensor = 0.0
        self.y_sensor = 0.0
        self.z_sensor = 0.0

        # Variáveis das pages do movimento 
        self.page = ''
        self.current_page = ''
        self.before_page = None
        self.feedback_page = ''
        self.finished_page = 'finished'

        # Variáveis referentes a caminhada do movimento 
        self.test_mode = False
        self.wState = 0
        self.old_wState = 10
        self.walk_counter = 0
        self.period_counter = 0
        self.before_walk_counter = 0
        self.steps_number = 50
        self.walking = ''
        self.vx = 0.0
        self.vy = 0.0
        self.vz = 0.0
        self.body_alignment = ''
        self.before_body_alignment = ''
        self.move_head = False
        self.first_pose = False
        self.finish_kicking = False

        # Variáveis para o fluxo do behaviour
        self.before_state = ''
        self.actual_state = ''
        self.robot = attacker.Attacker()
        self.thoughts = thinkAttacker.Think()

        # Inicializador do node do behaviour
        rospy.init_node('Behaviour_Node', anonymous=True)

    # Metodo para a visão na robo física    
    def callback_vision(self, msg): # Acionado toda vez que uma mensagem da Visão chega

        self.searching = msg.searching
        self.ball = msg.ball.found
        self.x_ball = msg.ball.x # Coordenada horizontal da bola
        self.y_ball = msg.ball.y # Coordenada vertical da bola
        self.roi_width = msg.ball.roi_width
        self.roi_height = msg.ball.roi_height

        self.ball_centered, self.ball_close, self.motorhead = self.thoughts.vision(self.x_ball, self.y_ball, self.roi_width, self.roi_height, self.ball)
        
        self.update_state_machine()

    # Metodo para a visão na robo simulada
    def callback_vision_sim(self, msg): # Acionado toda vez que uma mensagem da Visão chega

        self.searching = msg.searching
        self.ball = msg.found
        self.x_ball = msg.x # Coordenada horizontal da bola
        self.y_ball = msg.y # Coordenada vertical da bola
        self.roi_width = msg.roi_width
        self.roi_height = msg.roi_height

        self.ball_centered, self.ball_close, self.motorhead = self.thoughts.vision(self.x_ball, self.y_ball, self.roi_width, self.roi_height, self.ball)
        
        self.update_state_machine()

    def callback_head(self, msg):

        self.neck_horizontal_position = msg.data[18]
        self.neck_vertical_position = msg.data[19]

        self.body_alignment, self.motor_limit_reached = self.thoughts.movement(self.neck_horizontal_position, self.neck_vertical_position)
        self.walking = msg.source

        self.update_state_machine()

    def walk_service(self, first_pose, move_head, walk_flag, test_mode):
        
        rospy.wait_for_service('/humanoid_walking/walking_cmd')

        try:

            service_walk = rospy.ServiceProxy('/humanoid_walking/walking_cmd', LipCmdSrv)

            service_walk(first_pose, move_head, walk_flag, False, test_mode, self.vx, self.vy, self.vz)

        except rospy.ServiceException as e:

            print("Service call failed: {e}")
    

    def callback_sensor(self, msg):
        #pegar valores pertinentes do sensor IMU 

        self.x_sensor = msg.x
        self.y_sensor = msg.y
        self.z_sensor = msg.z

        self.falled = self.thoughts.sensor_think(self.x_sensor, self.y_sensor, self.z_sensor)

        self.update_state_machine()
    
    def call_predefined_movement(self, predef_name):

        self.finished_page = 'not_finished'
        rospy.wait_for_service('/movement_predefined/request_txt')
        
        try:
            service_predef_mov = rospy.ServiceProxy('/movement_predefined/request_txt', PredefinedMovementSrv)

            resp = service_predef_mov(predef_name)
            self.finished_page = 'finished'
            self.update_state_machine()

        except rospy.ServiceException as e:
            print("Service call failed: {e}")

    # Método destinado a repassar as variveis para a máquina de estados
    def update_state_machine(self):

        # Visão
        self.robot.ball = self.ball
        self.robot.searching = self.searching
        self.robot.ball_centered = self.ball_centered
        self.robot.ball_close = self.ball_close

        # Movimento
        self.robot.moving = self.moving
        self.robot.falling = self.falled
        self.robot.finish_kicking = self.finish_kicking
        self.robot.motor_limit_reached = self.motor_limit_reached

    # Método responsavel por passar comandos ao movimento
    def run_movement(self):
        if self.robot.state != 'S_Search_ball':
            self.walk_service(first_pose=False, move_head = False, walk_flag = False, test_mode = self.test_mode)

        if self.robot.state == 'S_Getting_up':
            # Movimento desligar motores momentos antes de a robô realmente cair
            self.moving = False

            time.sleep(1) # Esperar um pouco para garantir que ela caiu
            self.position_falled = self.thoughts.falled_position(self.x_sensor, self.y_sensor, self.z_sensor) #verificar a posição que a robo caiu 
            print (self.position_falled) 

            if self.walking == 'not_walking' or self.finished_page == 'finished':               

                if self.position_falled == 'front':
                    self.call_predefined_movement('stand_up_front')
            
                elif self.position_falled == 'back':
                    self.call_predefined_movement('stand_up_back')
                
                elif self.position_falled == 'left_side':
                    self.call_predefined_movement('stand_up_left')
                
                elif self.position_falled == 'right_side':
                    self.call_predefined_movement('stand_up_right')

            elif self.finished_page == 'finished':
                self.falled = False
                self.moving = False
                self.update_state_machine()    

        elif (self.robot.state == 'S_Walking' and self.finished_page == 'finished'):
            
            count = 0
            
            if self.body_alignment == 'body_centralized':
                self.moving = True
                
                #Chamando page de andar reto varias vezes, pois anda pouco
                while count <= 4:
                    self.call_predefined_movement('go_ahead')
                    print('Andando reto')
                    count += 1
                
            elif self.body_alignment == 'turn_left':
                self.moving = True

                #Chamando page de virar para a esquerda
                self.call_predefined_movement('turn_left')
                print('Girando para esquerda')

            elif self.body_alignment == 'turn_right':
                self.moving = True

                #Chamando page de virar para a direita 
                self.call_predefined_movement('turn_right')
                print('Girando para direita')
            
            
            self.update_state_machine()

            self.robot.state = 'S_Search_ball'    

        elif (self.robot.state == 'S_Kick' and self.finished_page == 'finished'):
            count = 0
            while count <= 4:
                self.call_predefined_movement('go_ahead')
                count += 1
            self.call_predefined_movement('weak_kick')
            #self.finish_kicking = True
            self.update_state_machine()

        elif (self.robot.state == 'S_Stand_still' and self.finished_page == 'finished'):
            self.call_predefined_movement('first_pose')
            self.update_state_machine()

        elif (self.robot.state == 'S_Search_ball' and self.finished_page == 'finished'):

            self.headMsg.pos = self.motorhead
            self.pub_comm_head_params.publish(self.headMsg)

            if self.motorhead == 4: #Procurou demais
                self.call_predefined_movement('turn_left')

            elif self.motorhead == 3: #Casos legitimos
                self.walk_service(self.first_pose, move_head = True, walk_flag = False, test_mode = self.test_mode)
            
            else:
                self.walk_service(self.first_pose, move_head = True, walk_flag = False, test_mode = self.test_mode)

            self.update_state_machine()
            
        elif (self.robot.state == 'S_Body_alignment' and self.finished_page == 'finished'):    

            self.headMsg.pos = -self.motorhead
            self.pub_comm_head_params.publish(self.headMsg)
            self.walk_service(self.first_pose, move_head = True, walk_flag = False, test_mode = self.test_mode)

            time.sleep(5)
            self.walk_service(self.first_pose, move_head = False, walk_flag = False, test_mode = self.test_mode)
            
            if self.body_alignment == 'turn_left':
                self.moving = True
                print('Body_alignment virando a esquerda com cabeça à ', self.motorhead)
                self.call_predefined_movement('turn_left')

            elif self.body_alignment == 'turn_right':
                self.moving = True
                print('Body_alignment virando a direita com cabeça à ', self.motorhead)
                self.call_predefined_movement('turn_right')
            
            self.robot.state = 'S_Search_ball'

            self.update_state_machine()
    
    def start(self):

        rospy.Subscriber('/webots_natasha/vision_inference', WebotsVisionMsg, self.callback_vision) #Subscrição precisa ser feita apenas uma vez
        rospy.Subscriber('/webots_natasha/behaviour_controller', Vector3, self.callback_sensor)
        rospy.Subscriber('/opencm/request', OpencmRequestMsg, self.callback_head)
        #rospy.Subscriber('objects_sim', Ball, self.callback_vision_sim)
        #rospy.Subscriber('robot_actions', StateMachineActionsMsg, self.callback_test)

        self.pub_comm_head_params = rospy.Publisher('/motor_comm/head_params', HeadMoveMsg, queue_size = 100)
       
        self.robot.game_controller = True

        self.update_state_machine() # Método para atualizar a máquina de estados
        
        self.test_mode = True
        self.first_pose = False
        self.walk_service(self.first_pose, move_head = False, walk_flag = False, test_mode = self.test_mode)
        
        time.sleep(10)

        self.first_pose = True
        self.walk_service(self.first_pose, move_head = False, walk_flag = False, test_mode = self.test_mode)
        self.call_predefined_movement('first_pose')

        time.sleep(10)

        self.first_pose = False
        self.walk_service(self.first_pose, move_head = False, walk_flag = False, test_mode = self.test_mode)

        # Loop que mantém o Behaviour em execução
        while not rospy.is_shutdown():

            self.robot.clock()
            # time.sleep(0.1)
            
            self.actual_state = self.robot.state
            
            print ("Pagina: ", self.finished_page)
            print ("position: ", self.body_alignment)
            print("Periodos: ", self.period_counter)
            print ("Passos: ", self.walk_counter)
            print("Passos anteriores: ", self.before_walk_counter)
            print("Movimento da Cabeça: ", self.motorhead)
            
            self.run_movement()
            self.before_body_alignment = self.body_alignment
            self.before_state = self.robot.state

    
if __name__ == '__main__':
    cerebro = Brain() # Inicia o construtor da classe
    cerebro.start() # Roda o método start
    rospy.spin()
