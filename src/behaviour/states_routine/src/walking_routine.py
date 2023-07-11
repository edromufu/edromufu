#!/usr/bin/env python3
#coding=utf-8

import rospy
from modularized_bhv_msgs.msg import currentStateMsg
from modularized_bhv_msgs.srv import moveRequest

#Setando a grafia correta das requisições para movimento de caminhada
FORWARD = 'walk_forward'

HEADER = { 'origin' : 'walking' }

class WalkingRoutine():

    def __init__(self):
        
        self.move_request = rospy.ServiceProxy('/bhv2mov_communicator/3D_move_requisitions', moveRequest,headers=HEADER)
        rospy.Subscriber('/transitions_and_states/state_machine', currentStateMsg, self.flagUpdate)

        self.flag = False
        self.last_decision = None

        rospy.wait_for_service('/bhv2mov_communicator/3D_move_requisitions')
        while not rospy.is_shutdown():
            self.createRequest()

            if self.last_decision != self.request:
                self.last_decision = self.request
                self.move_request(self.request)
    
    def flagUpdate(self, msg):
        message = msg.currentState

        if message == 'walking':
            self.flag = True
        else:
            self.flag = False

        
    def createRequest(self):
        
        if self.flag:
            self.request = FORWARD
        else:
            self.request = None


if __name__ == '__main__':
    rospy.init_node('Walking_node', anonymous=False)

    routine = WalkingRoutine()
    rospy.spin()