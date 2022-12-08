#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import rospy
from rospy import logerr

# --------------------------------- Variáveis da Visão --------------------------------- #

xTop_centralized    =  250                           #Estas quatro primeiras variáveis são
xBottom_centralized =  155                           #limites x e y para decidir se a bola
                                                     #está centralizada ou não.

ball_width  = 75                                   #Variáveis para nos informar a altura
ball_height = 75                                   #e largura do raio da bola. Define se
                                                    #a bola está perto ou longe.

# ------------------------------- Variáveis do Sensor ---------------------------------- #

gravitySecurity = 4                                 #Define gravity da queda do robô
z_sensor_front  = -5                                #Define se o robô caiu de frente
z_sensor_back   = 5                                 #Define se o robô caiu de costas
x_sensor_left   = -5                                #Define se o robô caiu sobre o lado esquerdo
x_sensor_right  = 5                                 #Define se o robô caiu sobre o lado direito

# -------------------------------- Variáveis do Pescoço ------------------------------- #

xTop_limit_position     = 2400 - (2400-1700)/100    #Limite superior do motor horizontal    
xBottom_limit_position  = 1700 + (2400-1700)/100    #Limite inferior do motor horizontal

'''De acordo com o config.xml do robô, o cálculo dos limites para o limite superior é dado
por lim_sup - (lim_sup + lim_inf/100) e lim_inf + (lim_sup + lim_inf/100) para o limite de 
segurança inferior'''

x_to_turn_Right = 1938                              #Valores para alinhar corpo e cabeça
x_to_turn_Left  = 2158

class Think(object):

    def vision(self, x_ball, y_ball, roi_width, roi_height,ball):
        self.ball = ball
        self.ball_close = False
        self.ball_position = 3 #Não encontrado
       
        if self.ball == True:
       
            if x_ball >= xBottom_centralized and x_ball <= xTop_centralized:
                self.ball_position = 0 #Centralizado

            # A visao irá verificar o eixo vertical e depois o outro eixo ate centralizar em ambos
            else:
                if x_ball > xTop_centralized:
                    self.ball_position = 1 #À direita

                elif x_ball < xBottom_centralized:
                    self.ball_position = -1 #À esquerda
     
        if roi_width*roi_height >= ball_height*ball_width:
            self.ball_close = True

        return (self.ball_close, self.ball_position)

    def game_controller(self, game_controller):
        self.game_controller = game_controller
        return self.game_controller

    def sensor_think(self, x_sensor, y_sensor, z_sensor):
        if abs(y_sensor) < gravitySecurity:
            return True
        else :
            return False  

    def falled_position(self, x_sensor, y_sensor, z_sensor):
        if z_sensor < z_sensor_front:
            # caiu de costa
            return('front')

        elif z_sensor > z_sensor_back:
            # caiu de frente     
            return('back')  

        elif x_sensor < x_sensor_left:
            # caiu sobre o lado esquerdo     
            return('left_side')

        elif x_sensor < x_sensor_right:
            # caiu sobre o lado direito    
            return('right_side')

        else:
            logerr("FALL_SECURITY: Fall position not identified")

    def feedback_page(self, page):

        if page == "Last_Page":

            return "finished"

        else:

            return "not_finished"
    
    def period_counter(self, wState, old_wState, counter, walk_flag):
        
        if not(wState == old_wState) and walk_flag == True:

            counter += 1
        
        return counter