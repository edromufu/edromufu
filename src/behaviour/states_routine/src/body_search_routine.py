#!/usr/bin/env python3
#coding=utf-8

import rospy
from modularized_bhv_msgs.msg import currentStateMsg, stateMachineMsg
from modularized_bhv_msgs.srv import moveRequest

#Setando a grafia correta das requisições para movimento de caminhada
CLOCKWISE = 'rotate_clockwise'
COUNTER_CLOCKWISE = 'rotate_counter_clockwise'

HEADER = { 'origin' : 'body_search' }

class BodySearchRoutine():

    def __init__(self):
        
        self.move_request = rospy.ServiceProxy('/bhv2mov_communicator/3D_move_requisitions', moveRequest,headers=HEADER)
        self.head_request = rospy.ServiceProxy('/bhv2mov_communicator/head_requisitions', moveRequest,headers=HEADER)
        rospy.Subscriber('/transitions_and_states/state_machine', currentStateMsg, self.flagUpdate)
        rospy.Subscriber('/sensor_observer/state_machine_vars', stateMachineMsg, self.varsUpdate)

        self.flag = False
        self.current_ball_position = 'Left'
        self.last_decision = None
        self.last_decision2 = None

        rospy.wait_for_service('/bhv2mov_communicator/3D_move_requisitions')
        rospy.wait_for_service('/bhv2mov_communicator/head_requisitions')
        while not rospy.is_shutdown():
            self.createRequest()
            
            if self.last_decision != self.request:

                self.last_decision = self.request
                self.move_request(self.request)

            if self.last_decision2 != self.request2:

                self.last_decision2 = self.request2
                self.head_request(self.request2)
    
    def flagUpdate(self, msg):
        if msg.currentState == 'body_search':
            self.flag = True
        else:
            self.flag = False

    def varsUpdate(self, msg):
        self.current_ball_position = msg.ballRelativePosition
        
    def createRequest(self):

        if self.flag:
            self.request2 = 'head_search'
            if 'Left' in self.current_ball_position:
                self.request = COUNTER_CLOCKWISE
            elif 'Right' in self.current_ball_position:
                self.request = CLOCKWISE
        else:
            self.request = None
            self.request2 = None

if __name__ == '__main__':
    rospy.init_node('Body_search_node', anonymous=False)

    routine = BodySearchRoutine()
    rospy.spin()