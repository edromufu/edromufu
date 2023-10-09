#!/usr/bin/env python3
#coding=utf-8

import rospy
from movement_utils.srv import *
from movement_utils.msg import *
from modularized_bhv_msgs.msg import currentStateMsg


class WalkingRoutine():

    def __init__(self):
        
        self.move_request = rospy.ServiceProxy('/movement_central/request_walk', walk_forward)
        rospy.Subscriber('/transitions_and_states/state_machine', currentStateMsg, self.flagUpdate)

        self.flag = False
        self.last_decision = None

        rospy.wait_for_service('/movement_central/request_walk')
        while not rospy.is_shutdown():
            self.createRequest()

            if self.last_decision != self.support_foot:
                self.last_decision = self.support_foot
                self.move_request(self.support_foot,self.step_number)
    
    def flagUpdate(self, msg):
        message = msg.currentState

        if message == 'walking':
            self.flag = True
        else:
            self.flag = False

        
    def createRequest(self):
        
        if self.flag:
            self.support_foot = 1
            self.step_number = 2
        else:
            self.support_foot = None


if __name__ == '__main__':
    rospy.init_node('walking_node', anonymous=False)

    routine = WalkingRoutine()
    rospy.spin()