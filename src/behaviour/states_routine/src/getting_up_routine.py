#!/usr/bin/env python3
#coding=utf-8

import rospy, os, sys
from movement_utils.srv import *
from movement_utils.msg import *
from modularized_bhv_msgs.msg import stateMachineMsg
from modularized_bhv_msgs.msg import currentStateMsg

edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters


class getting_up_routine():

    def __init__(self):
        self.parameters = BehaviourParameters()

        self.move_request = rospy.ServiceProxy('/movement_central/request_page', page)
        rospy.wait_for_service('/movement_central/request_page')

        rospy.Subscriber(self.parameters.stateMachineTopic, stateMachineMsg, self.fallStatusUpdate)
        rospy.Subscriber('/transitions_and_states/state_machine', currentStateMsg, self.flagUpdate)

        self.flag = False
        self.currentGetUpPage = None
        
        rospy.Timer(rospy.Duration(self.parameters.timerPage), self.runGetUp)

    def runGetUp(self, event):
        if self.flag:
            print('Routine Get Up') 
            self.move_request(self.currentGetUpPage)
    
    def flagUpdate(self, msg):
        message = msg.currentState

        if message == 'getting_up':
            self.flag = True
        else:
            self.flag = False

    def fallStatusUpdate(self,msg):
        
        if msg.fallState == self.parameters.left or msg.fallState == self.parameters.right or msg.fallState == self.parameters.back:
            self.currentGetUpPage = 'aurea_get_up_back'
        elif msg.fallState == self.parameters.front:
            self.currentGetUpPage = 'aurea_get_up_front'

if __name__ == '__main__':
    rospy.init_node('getting_up_node', anonymous=False)

    routine = getting_up_routine()
    rospy.spin()