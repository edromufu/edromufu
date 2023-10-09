#!/usr/bin/env python3
#coding=utf-8

import rospy, os, sys
from movement_utils.srv import *
from movement_utils.msg import *
from modularized_bhv_msgs.msg import currentStateMsg

edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters

class stand_still_routine():

    def __init__(self):

        self.parameters = BehaviourParameters()
        
        self.move_request = rospy.ServiceProxy('/movement_central/request_page', page)
        rospy.Subscriber('/transitions_and_states/state_machine', currentStateMsg, self.flagUpdate)
        rospy.wait_for_service('/movement_central/request_page')

        self.flag = False 
        rospy.Timer(rospy.Duration(self.parameters.timerFirstPose), self.runStandStill)

    def runStandStill(self, event):
        if self.flag:
            print('Routine Stand Still')
            self.move_request('aurea_first_pose')
    
    def flagUpdate(self, msg):
        message = msg.currentState

        if message == 'stand_still':
            self.flag = True
        else:
            self.flag = False


if __name__ == '__main__':
    rospy.init_node('stand_still_node', anonymous=False)

    routine = stand_still_routine()
    rospy.spin()