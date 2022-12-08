#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import rospy
from rospy import logerr

# --------------------------------- Variáveis da Visão --------------------------------- #

xTop_centralized    = 240                           #Estas quatro primeiras variáveis são
xBottom_centralized = 160                          #limites x e y para decidir se a bola
yTop_centralized    = 290                            #está centralizada ou não.
yBottom_centralized = 120       

xTop_to_centralize    = 220                         #Estas quatro variáveis irão informar
xBottom_to_centralize = 180                         #os valores para centralizar a cabeça
yTop_to_centralize    = 270                         #com a bola.
yBottom_to_centralize = 140

ball_width  = 120                                   #Variáveis para nos informar a altura
ball_height = 120                                   #e largura do raio da bola. Define se
                                                    #a bola está perto ou longe.

importantMeasures = 6                                #Variáveis da media móvel da visão
timesMeasured = (importantMeasures/2) + 1            #falam o tamanho do vetor de ultimas medidas
                                                     #e quantas vezes deve ser medido para 
                                                     #considerar valida a situação

# ------------------------------- Variáveis do Sensor ---------------------------------- #

gravitySecurity = 4                                 #Define gravity da queda do robô
z_sensor_front  = -5                                #Define se o robô caiu de frente
z_sensor_back   = 5                                 #Define se o robô caiu de costas
x_sensor_left   = -5                                #Define se o robô caiu sobre o lado esquerdo
x_sensor_right  = 5                                 #Define se o robô caiu sobre o lado direito
importantMeasuresSensor = 10
timesMeasuredSensor = (importantMeasuresSensor/2) + 1 

# -------------------------------- Variáveis do Pescoço ------------------------------- #

xTop_limit_position     = 3062 - (3062-1028)/100    #Limite superior do motor horizontal    
xBottom_limit_position  = 1028 + (3062-1028)/100    #Limite inferior do motor horizontal

'''De acordo com o opencm.h do robô, o cálculo dos limites para o limite superior é dado
por lim_sup - (lim_sup + lim_inf/100) e lim_inf + (lim_sup + lim_inf/100) para o limite de 
segurança inferior'''

x_to_turn_Right = 1938                              #Valores para alinhar corpo e cabeça
x_to_turn_Left  = 2158

class Think(object):
    def __init__(self):
        self.listMedsHor = []
        self.listMedsVer = []
        self.listActionsHead = []

        self.listMedsYSensor = []

    def vision(self, x_ball, y_ball, roi_width, roi_height,ball):
        self.ball = ball
        self.ball_centered = False
        self.ball_close = False
        horAction = 3
        verAction = 3


        if(len(self.listMedsHor) > importantMeasures): 
            self.listMedsHor.remove(self.listMedsHor[0])

        if(len(self.listMedsVer) > importantMeasures): 
            self.listMedsVer.remove(self.listMedsVer[0])

        if(len(self.listActionsHead) > 80*importantMeasures): 
            self.listActionsHead.remove(self.listActionsHead[0])

        #Construção da media movel vertical e horizontal
        if self.ball:
            if x_ball > xTop_to_centralize:
                self.listMedsHor = self.listMedsHor + ["Right"]

            elif x_ball < xBottom_to_centralize:
                self.listMedsHor = self.listMedsHor + ["Left"]
            
            elif x_ball >= xBottom_centralized and x_ball <= xTop_centralized:
                self.listMedsHor = self.listMedsHor + ["Center"]

            if y_ball > yTop_to_centralize:
                self.listMedsVer = self.listMedsVer + ["Down"]

            elif y_ball < yBottom_to_centralize:
                self.listMedsVer = self.listMedsVer + ["Up"]
            
            elif y_ball >= yBottom_centralized and y_ball <= yTop_centralized:
                self.listMedsVer = self.listMedsVer + ["Center"]
        else:
            self.listMedsHor = self.listMedsHor + ["Out"]
            self.listMedsVer = self.listMedsVer + ["Out"]

        #Calcula da media movel horizontal
        
        if(self.listMedsHor.count("Out") > timesMeasured+1):
            horAction = 3
        if(self.listMedsHor.count("Left") > timesMeasured):
            horAction = -1
        if(self.listMedsHor.count("Right") > timesMeasured):
            horAction = 1
        if(self.listMedsHor.count("Center") > timesMeasured/2):
            horAction = 0

        #Calculo da media movel vertical
        
        if(self.listMedsVer.count("Out") > timesMeasured+1):
            verAction = 3
        if(self.listMedsVer.count("Up") > timesMeasured):
            verAction = -2
        if(self.listMedsVer.count("Down") > timesMeasured):
            verAction = 2
        if(self.listMedsVer.count("Center") > timesMeasured/2):
            verAction = 0
        
        #Tomada de decisão para motorhead com base no medido da media móvel
        if(self.listActionsHead.count(3) > 80*timesMeasured and len(self.listActionsHead) > 90*timesMeasured): #Fora do campo de visão à muito tempo
            self.motorhead = 4
            self.listActionsHead.clear()

        elif(verAction == 3 and horAction == 3): #Completamente fora
            self.motorhead = 3

        elif(verAction == 0 and horAction == 0):#Centralizou
            self.motorhead = 0
            self.ball_centered = True

        elif(horAction == 0): #Centralizou horizontalmente
            self.motorhead = verAction

        elif(verAction == 0): #Centralizou verticalmente
            self.motorhead = horAction

        else: #Prioriza centralização horizontal em caso de não estar centralizado em ambos
            self.motorhead = horAction
        
        if roi_width*roi_height >= ball_height*ball_width:
            self.ball_close = True

        self.listActionsHead = self.listActionsHead + [self.motorhead]

        return (self.ball_centered, self.ball_close, self.motorhead)

    def game_controller(self, game_controller):
        self.game_controller = game_controller
        return self.game_controller

    def sensor_think(self, x_sensor, y_sensor, z_sensor):
        if(len(self.listMedsYSensor) > importantMeasuresSensor): 
            self.listMedsYSensor.remove(self.listMedsYSensor[0])
            
        if y_sensor < gravitySecurity:
            self.listMedsYSensor = self.listMedsYSensor + ["Falled"]
        else:
            self.listMedsYSensor = self.listMedsYSensor + ["Stand"]
        
        if(self.listMedsYSensor.count("Falled") > timesMeasuredSensor):
            return True
        else:
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

    def movement(self, neck_horizontal_position, neck_vertical_position):
        
        if (neck_horizontal_position <= xBottom_limit_position) or (neck_horizontal_position >= xTop_limit_position):
            limit_reached = True

        else:
            limit_reached = False 

        if neck_horizontal_position >= x_to_turn_Left:
            body_alignment = 'turn_left'

        elif neck_horizontal_position <= x_to_turn_Right:
            body_alignment = 'turn_right'

        else:
            body_alignment = 'body_centralized'

        return(body_alignment, limit_reached)
    
    def period_counter(self, wState, old_wState, counter, walk_flag, motor_limit_reached):
        
        if not(wState == old_wState) and (walk_flag == True or motor_limit_reached == True):

            counter += 1
        
        return counter