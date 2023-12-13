#!/usr/bin/env python3
#coding=utf-8

import rospy
from movement_utils.srv import *
from movement_utils.msg import *
from modularized_bhv_msgs.msg import currentStateMsg


class KickRoutine():

    def __init__(self):
        
        self.move_request = rospy.ServiceProxy('/movement_central/request_page', page)
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

        if message == 'kick':
            self.flag = True
        else:
            self.flag = False

        
    def createRequest(self):
        
        if self.flag:
            self.request = f'aurea_kick'
        else:
            self.request = None


if __name__ == '__main__':
    rospy.init_node('Kick_node', anonymous=False)

    routine = KickRoutine()
    rospy.spin()