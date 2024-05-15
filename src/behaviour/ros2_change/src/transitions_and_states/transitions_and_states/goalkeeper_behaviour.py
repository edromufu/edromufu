#!/usr/bin/env python3
#coding=utf-8

import numpy as np

#import rospy, os, sys,time (1)
import rclpy, os, sys,time #(1)
from vision_msgs.msg import Webotsmsg
from movement_utils.srv import *
from movement_utils.msg import *

edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters


class goalkeeper_brain:
    def __init__(self):

        #rospy.init_node('goalkeeper_brain') (2)
        rclpy.init(args=sys.argv)           #(2)
        self.node = rclpy.create_node('goalkeeper_brain')

        self.parameters = BehaviourParameters()

        #rospy.wait_for_service('u2d2_comm/feedbackHead')
        #self.motorsFeedback = rospy.ServiceProxy('u2d2_comm/feedbackHead', head_feedback) (3)
        #self.pageCall = rospy.ServiceProxy('movement_central/request_page', page) (4)

        self.motorsFeedback = self.node.create_client(HeadFeedback, 'u2d2_comm/feedbackHead') #(3)
        self.pageCall = self.node.create_client(Page, 'movement_central/request_page') #(4)

        while not self.motorsFeedback.wait_for_service(timeout_sec=1.0): #(3)
            self.node.get_logger().info('service not available, waiting again...')
        while not self.pageCall.wait_for_service(timeout_sec=1.0): #(4)
            self.node.get_logger().info('service not available, waiting again...')

        #rospy.Subscriber(self.parameters.vision2BhvTopic, Webotsmsg, self.updateBallParameters) (5)
        #rospy.Subscriber(self.parameters.headPositionsTopic, head_motors_data, self.updateHorRotation) (6)

        self.node.create_subscription(Webotsmsg, self.parameters.vision2BhvTopic, self.updateBallParameters, rclpy.qos.QoSProfile()) #(5)
        self.node.create_subscription(HeadMotorsData, self.parameters.headPositionsTopic, self.updateHorRotation, rclpy.qos.QoSProfile()) #(6)

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
        #while not rospy.is_shutdown(): (7)
        while not rclpy.ok(): #(7)

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
        #while not rospy.is_shutdown(): (8)
        while not rclpy.ok(): #(8)
            self.pageCall('fallen_natasha')
                
if __name__ == '__main__':
    #goalkeeper_brain = goalkeeper_brain() (9)
    goalkeeper = goalkeeper_brain() #(9)
    #goalkeeper_brain.run() (10)
    goalkeeper.run() #(10)
    #rospy.spin() (11)
    rclpy.spin(goalkeeper.node) #(11)