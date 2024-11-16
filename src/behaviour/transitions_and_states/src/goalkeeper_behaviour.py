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
        self.ballClose = False
        self.parameters = BehaviourParameters()

        rospy.wait_for_service('u2d2_comm/feedbackHead')
        self.motorsFeedback = rospy.ServiceProxy('u2d2_comm/feedbackHead', head_feedback)
        self.pageCall = rospy.ServiceProxy('movement_central/request_page', page)
        
        rospy.Subscriber(self.parameters.vision2BhvTopic, Webotsmsg, self.updateBallParameters)
        rospy.Subscriber(self.parameters.headPositionsTopic, head_motors_data, self.updateHorRotation)

        print("Goleira Iniciou")
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
                self.ballClose = False

        else:
            self.found = True
            self.x = ballInfos.x
            self.y = ballInfos.y
            self.ballClose = True if ballInfos.roi_width > 100 else False
            self.timesFoundFalse = 0
            self.hasReceivedVision = True
    
    def updateHorRotation(self, msg):
        self.HorRotation,VerRotation = msg.pos_vector


    def run(self):
        while not rospy.is_shutdown():

            try:
                
                if self.found: #Se quiser trocar para page infinita "IF not"
                    self.pageCall('aurea_front_walk4')   
                    print("Correndo pra bola")
                    rospy.sleep(6)
                       
                    if self.HorRotation < self.parameters.lookingLeftRad:              
                        self.pageCall('aurea_real_left_walk') #Para a page de andar de lado trocar para while
                        print("LEFT WALK")
                        rospy.sleep(6)

                    if self.HorRotation > self.parameters.lookingRightRad:
                        self.pageCall('aurea_right_walk') #MUDAR AQUI
                        print("RIGHT WALK")
                        rospy.sleep(6)
                    
                if self.found and self.ballClose:
                    self.pageCall('aurea_front_walk4')
                    print('socorro')
                    rospy.sleep(6)
                    self.pageCall('aurea_front_walk4') #MUDAR AQUI 
                    print('KICK')
                    rospy.sleep(6)
                    #self.fall()
                    self.found = False
                else:
                    self.pageCall('aurea_levantar_bracos')   
                    print("nao achou a bola")
                    rospy.sleep(6)
                
            except Exception as e:
              # print(f"{e}")   
              pass
                    
            
    '''
    def fall(self):
        while not rospy.is_shutdown():
            rospy.sleep(9)
            self.pageCall('fallen_aurea')
    '''            
if __name__ == '__main__':
    goalkeeper_brain = goalkeeper_brain()
    goalkeeper_brain.run()
