#!/usr/bin/env python3
#coding=utf-8

import numpy as np

import rospy, os, sys,time
from vision_msgs.msg import Webotsmsg
from movement_utils.srv import *
from movement_utils.msg import *

edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters


class goalkeeper_brain:
    def __init__(self):

        rospy.init_node('goalkeeper_brain')

        self.parameters = BehaviourParameters()

        rospy.wait_for_service('u2d2_comm/feedbackHead')
        self.motorsFeedback = rospy.ServiceProxy('u2d2_comm/feedbackHead', head_feedback)
        self.pageCall = rospy.ServiceProxy('movement_central/request_page', page)
        
        rospy.Subscriber(self.parameters.vision2BhvTopic, Webotsmsg, self.updateBallParameters)
        rospy.Subscriber(self.parameters.headPositionsTopic, head_motors_data, self.updateHorRotation)


        self.found = False
        self.x = 0
        self.y = 0
 
        self.timesFoundFalse = 0
    
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
            self.ballClose = True if self.y>self.parameters.yCenterBottomLimit else False
            self.timesFoundFalse = 0
            self.hasReceivedVision = True
    
    def updateHorRotation(self, msg):
        self.HorRotation,VerRotation = msg.pos_vector
    
    def run():
        while not rospy.is_shutdown():

            if self.found:
                self.pageCall('natasha_squat')

            elif self.found and self.ballClose:
                # >0 Direita e <0 esquerda
                
                if self.HorRotation < self.parameters.lookingLeftRad/2:              
                    self.pageCall('natasha_left_defense')
                    self.fall()
                elif self.HorRotation > self.parameters.lookingRighttRad/2:
                    self.pageCall('natasha_right_defense')
                    self.fall()
                else:
                    pass
    
    def fall():
        while not rospy.is_shutdown():
            self.pageCall('fallen_natasha')
                
if __name__ == '__main__':
    goalkeeper_brain = goalkeeper_brain()
    goalkeeper_brain.run()
    rospy.spin()