#!/usr/bin/env python3
#coding=utf-8

import rospy
from movement_msgs.msg import ApprovedMovementMsg
from vision_msgs.msg import Webotsmsg

#Parametros de configuracao da camera e seus quadrantes
[cameraWidth, cameraHeight] = [416, 416]

[xCenterLeftLimit, xCenterRightLimit] = [cameraWidth/2, cameraWidth/2]
[close_width, close_height] = [40, 40] #Parametro de definicao da proximidade da bola
timesSecurity = 7 #Numero de vezes para verificacoes de seguranca no codigo

LEFT = 'left_arm'
RIGHT = 'right_arm'
STAND = 'first_pose'

vision2BhvTopic = '/webots_natasha/vision_inference'

class BallInterpreter():

    def __init__(self):

        rospy.Subscriber(vision2BhvTopic, Webotsmsg, self.callback_vision)
        self.ballRelativePosition = None
        self.ballClose = False
        self.ballFound = False
        self.countDistance = 0
        self.countFound = 0

        self.movement_request_topic = rospy.Publisher('/movement/approved_movement', ApprovedMovementMsg, queue_size=10)
        self.request = ApprovedMovementMsg()
        self.rate = rospy.Rate(10)

    def start(self):  
        while not rospy.is_shutdown():   
            if 'Left' in self.ballRelativePosition:
                self.request.approved_movement = LEFT
                self.movement_request_topic.publish(self.request)
                self.rate.sleep() 
            elif 'Right' in self.ballRelativePosition:
                self.request.approved_movement = RIGHT
                self.movement_request_topic.publish(self.request)
                self.rate.sleep() 
            elif 'Nothing' in self.ballRelativePosition:
                self.request.approved_movement = STAND
                self.movement_request_topic.publish(self.request) 
                self.rate.sleep()

    #Callback do tópico de infos da bola do ROS
    def callback_vision(self, general):    

        #Captura das informacoes da bola de dentro da mensagem completa
        msg = general.ball

        #Contador para informar que a bola foi perdida apos um numero de vezes sem encontra-la
        self.countFound += 1
        if(self.countFound > timesSecurity):
            self.ballFound = False
            self.ballClose = False

        if(msg.found):
            #Reseta o contador de informar que a bola foi perdida, pois encontrou :)
            self.ballFound = True
            self.countFound = 0

            #Módulo de verificacao da proximidade da bola, serve para resetar
            #a interpretacao apenas apos um numero definido de medidas desfavoraveis
            if(msg.roi_width*msg.roi_height < close_width*close_height):
                self.ballClose = False
            else:
                self.ballClose = True

            #Módulo de verificacao da posicao relativa da bola
            #Interpretacao horizontal
            if(msg.x <= xCenterLeftLimit):
                analysisX = 'Left'
            elif(msg.x >= xCenterRightLimit):
                analysisX = 'Right' 

            self.ballRelativePosition = analysisX
        else:
            self.ballRelativePosition = 'Nothing'
        
if __name__ == '__main__':
    rospy.init_node('Defense_node', anonymous=False)

    routine = DefenseRoutine()
    rospy.spin()
