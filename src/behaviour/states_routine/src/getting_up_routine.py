#!/usr/bin/env python3
#coding=utf-8

import rospy,os,sys
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
        rospy.Subscriber(self.parameters.stateMachineTopic, stateMachineMsg, self.status_fall)
        rospy.Subscriber('/transitions_and_states/state_machine', currentStateMsg, self.flagUpdate)

        self.flag = False
        self.last_decision = None

        rospy.wait_for_service('/movement_central/request_page')
        while not rospy.is_shutdown():
            self.createRequest()

            if self.last_decision != self.request:
                self.last_decision = self.request
                self.move_request(self.request)
    
    def flagUpdate(self, msg):
        message = msg.currentState

        if message == 'getting_up':
            self.flag = True
        else:
            self.flag = False

    def status_fall(self,msg):
        self.fallCondition = msg.fallState

        if self.fallCondition == 'Left' or self.fallCondition == 'Right':
            self.fallCondition = 'Front'
        
    def createRequest(self):
        
        if self.flag:
            self.request = f'aurea_getting_up_{self.fallCondition}'
        else:
            self.request = None


if __name__ == '__main__':
    rospy.init_node('getting_up_node', anonymous=False)

    routine = getting_up_routine()
    rospy.spin()