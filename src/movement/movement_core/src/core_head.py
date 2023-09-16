#!/usr/bin/env python3
#coding=utf-8

import numpy as np

import rospy, os, sys 
from vision_msgs.msg import Webotsmsg
from movement_utils.srv import *
from movement_utils.msg import *

edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters

class CoreHead:
    def __init__(self):

        rospy.init_node('head_central')

        self.parameters = BehaviourParameters()

        rospy.wait_for_service('u2d2_comm/feedbackHead')
        self.motorsFeedback = rospy.ServiceProxy('u2d2_comm/feedbackHead', head_feedback)
        self.pub2motors = rospy.Publisher('u2d2_comm/data2head', head_motors_data, queue_size=10)
        self.pub2motorsMsg = head_motors_data()
        
        rospy.Subscriber('/webots_natasha/vision_inference', Webotsmsg, self.callPID)

        self.found = False
        self.x = None
        self.y = None

    def callPID(self, msg):
        ballInfos = msg.ball

        self.found = ballInfos.found
        self.x = ballInfos.x
        self.y = ballInfos.y
    
    def callPx(self, x):
        error_x = (self.parameters.cameraWidth/2) - x
        return 0.0024*error_x

    def callPy(self, y):
        if y > self.parameters.cameraHeight/2: #Baixo
            return -0.05
        else: #Cima
            return 0.05
    
    def run(self):
        
        while not rospy.is_shutdown():
            if self.found:
                dx = 0
                dy = 0
                if self.x > self.parameters.xCenterRightLimit or self.x < self.parameters.xCenterLeftLimit:
                    [currentHorRotation, currentVerRotation] = self.motorsFeedback(True).pos_vector
                    dx = self.callPx(self.x)

                if self.y > self.parameters.yCenterBottomLimit or self.y < self.parameters.yCenterTopLimit:
                    [currentHorRotation, currentVerRotation] = self.motorsFeedback(True).pos_vector
                    dy = self.callPy(self.y)

                if dx or dy:
                    newHorPos = currentHorRotation + dx
                    newVerPos = currentVerRotation + dy

                    self.pub2motorsMsg.pos_vector = [newHorPos, newVerPos]
                    self.pub2motors.publish(self.pub2motorsMsg)
            else:
                pass

if __name__ == '__main__':
    movement_head = CoreHead()
    movement_head.run()
    rospy.spin()