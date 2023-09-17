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

UP_Y_POSITION = 0
BOTTOM_Y_POSITION = -0.95
LEFT_X_POSITION = 1.15
RIGHT_X_POSITION = -1.15
X_STEPS = 30
Y_STEPS = 10
TIME = 2e8 #1e9 = seg

class CoreHead:
    def __init__(self):

        rospy.init_node('head_central')

        self.parameters = BehaviourParameters()

        rospy.wait_for_service('u2d2_comm/feedbackHead')
        self.motorsFeedback = rospy.ServiceProxy('u2d2_comm/feedbackHead', head_feedback)
        self.pub2motors = rospy.Publisher('u2d2_comm/data2head', head_motors_data, queue_size=10)
        self.pub2motorsMsg = head_motors_data()
        
        rospy.Subscriber(self.parameters.vision2BhvTopic, Webotsmsg, self.updateBallParameters)

        self.found = False
        self.x = 0
        self.y = 0
        self.hasReceivedVision = False
        self.timesFoundFalse = 0

        self.defineSearchPattern()
    
    def defineSearchPattern(self):
        x_top_cw = np.linspace(LEFT_X_POSITION, RIGHT_X_POSITION, X_STEPS)
        y_right_cw = np.linspace(UP_Y_POSITION, BOTTOM_Y_POSITION, Y_STEPS)
        x_bot_cw = np.linspace(RIGHT_X_POSITION, LEFT_X_POSITION, X_STEPS)
        y_left_cw = np.linspace(BOTTOM_Y_POSITION, UP_Y_POSITION, Y_STEPS)
        
        top_cw      = np.c_[x_top_cw, UP_Y_POSITION*np.ones(len(x_top_cw))]
        right_cw    = np.c_[RIGHT_X_POSITION*np.ones(len(y_right_cw)), y_right_cw]
        bottom_cw   = np.c_[x_bot_cw, BOTTOM_Y_POSITION*np.ones(len(x_bot_cw))]
        left_cw     = np.c_[LEFT_X_POSITION*np.ones(len(y_left_cw)), y_left_cw]

        self.cwHeadPositions = np.concatenate((top_cw, right_cw, bottom_cw, left_cw))

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
            self.timesFoundFalse = 0
            self.hasReceivedVision = True
            
    def callPx(self, x):
        if x > self.parameters.cameraWidth/2: #Direita
            return -0.05
        else: #Esquerda
            return 0.05

    def callPy(self, y):
        if y > self.parameters.cameraHeight/2: #Baixo
            return -0.05
        else: #Cima
            return 0.05
    
    def run(self):
        lastTime = rospy.Time.now().nsecs
        justLoseTheBall = True

        while not rospy.is_shutdown():
            if self.found:
                if self.hasReceivedVision:
                    
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
                    
                    self.hasReceivedVision = False
                
                justLoseTheBall = True

            else:
                if justLoseTheBall:
                    if self.x > self.parameters.xCenterRightLimit:
                        rotation = 1
                    else:
                        rotation = -1

                    [currentHorRotation, currentVerRotation] = self.motorsFeedback(True).pos_vector
                    if abs(currentVerRotation-UP_Y_POSITION) < abs(currentVerRotation-BOTTOM_Y_POSITION):
                        startVer = UP_Y_POSITION
                    else:
                        startVer = BOTTOM_Y_POSITION
                    
                    dists = np.sqrt((self.cwHeadPositions[:, 0] - currentHorRotation)**2 + (self.cwHeadPositions[:, 1] - currentVerRotation)**2)
                    i = np.argmin(dists)

                    justLoseTheBall = False

                if abs(rospy.Time.now().nsecs - lastTime) >= TIME:
                    self.pub2motorsMsg.pos_vector = self.cwHeadPositions[i]
                    self.pub2motors.publish(self.pub2motorsMsg)
                    i += rotation
                    i = i%len(self.cwHeadPositions)

                    lastTime = rospy.Time.now().nsecs


if __name__ == '__main__':
    movement_head = CoreHead()
    movement_head.run()
    rospy.spin()