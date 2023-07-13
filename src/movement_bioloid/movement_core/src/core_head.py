#!/usr/bin/env python3
#coding=utf-8

import numpy as np

import rospy
from vision_msgs.msg import Webotsmsg
from movement_utils.srv import *
from movement_utils.msg import *

WIDTH = 640
HEIGHT = 480

class CoreHead:
    def __init__(self):
        rospy.init_node('head_central')

        self.motorsFeedback = rospy.ServiceProxy('u2d2_comm/feedbackHead', head_feedback)
        self.pub2motors = rospy.Publisher('u2d2_comm/data2head', head_motors_data, queue_size=10)
        self.pub2motorsMsg = head_motors_data()
        rospy.wait_for_service('u2d2_comm/feedbackHead')

        rospy.Subscriber('/webots_natasha/vision_inference', Webotsmsg, self.callPID)

    def callPID(self, msg):
        ballInfos = msg.ball

        if ballInfos.found:
            dx = 0
            dy = 0
            if ballInfos.x > 344 or ballInfos.x < 296:
                dx = self.callPIDx(ballInfos.x)
            if ballInfos.y > 264 or ballInfos.y < 216:
                dy = self.callPIDy(ballInfos.y)

            [currentHorRotation, currentVerRotation] = self.motorsFeedback(True).pos_vector

            newHorPos = currentHorRotation + dx
            newVerPos = currentVerRotation + dy

            self.pub2motorsMsg.pos_vector = [newHorPos, newVerPos]
            self.pub2motors.publish(self.pub2motorsMsg)
    
    def callPIDx(self, x):
        if x > WIDTH/2: #Direita
            return -0.05
        else: #Esquerda
            return 0.05

    def callPIDy(self, y):
        if y > HEIGHT/2: #Baixo
            return -0.05
        else: #Cima
            return 0.05

if __name__ == '__main__':
    movement_head = CoreHead()
    rospy.spin()