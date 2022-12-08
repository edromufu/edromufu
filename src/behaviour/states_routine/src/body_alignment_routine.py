#!/usr/bin/env python3
#coding=utf-8

import rospy
from modularized_bhv_msgs.msg import currentStateMsg, stateMachineMsg
from modularized_bhv_msgs.srv import moveRequest

#Setando a grafia correta das requisições para a cabeça
CENTER = 'head_to_center'

#Setando a grafia correta das requisições para movimento de caminhada
CLOCKWISE = 'rotate_clockwise'
COUNTER_CLOCKWISE = 'rotate_counter_clockwise'

#Setando o step para cada tipo de movimento
ROTATION_STEP = 0.1309

HEADER = { 'origin' : 'body_alignment', 'n_rotations':0}

class BodyAlignmentRoutine():

    def __init__(self):
        
        self.move_request = rospy.ServiceProxy('/bhv2mov_communicator/head_requisitions', moveRequest, headers=HEADER)
        self.threeD_request = rospy.ServiceProxy('/bhv2mov_communicator/3D_move_requisitions', moveRequest,headers=HEADER)
        rospy.Subscriber('/transitions_and_states/state_machine', currentStateMsg, self.flagUpdate)
        rospy.Subscriber('/sensor_observer/state_machine_vars', stateMachineMsg, self.varsUpdate)

        self.last_decision1 = None
        self.last_decision2 = None

        self.flag = False
        self.current_hor_motor_position = 0

        rospy.wait_for_service('/bhv2mov_communicator/head_requisitions')
        rospy.wait_for_service('/bhv2mov_communicator/3D_move_requisitions')

        while not rospy.is_shutdown():
            self.createRequest()

            if self.last_decision1 != self.request1: 

                self.last_decision1 = self.request1
                self.move_request(self.request1)
            if self.last_decision2 != self.request2:
                
                self.last_decision2 = self.request2
                self.threeD_request(self.request2)

    def flagUpdate(self, msg):
        if msg.currentState == 'body_alignment':
            self.flag = True
        else:
            self.flag = False

    def varsUpdate(self, msg):
        self.current_hor_motor_position = msg.horMotorPosition
        
    def createRequest(self):
        if self.flag:
            HEADER['n_rotations'] = str(round(abs(self.current_hor_motor_position/ROTATION_STEP))) 
            if self.current_hor_motor_position <= 0:
                self.request1 = CENTER
                self.request2 = COUNTER_CLOCKWISE
            elif self.current_hor_motor_position > 0:
                self.request1 = CENTER
                self.request2 = CLOCKWISE
        else:
            self.request1 = None
            self.request2 = None

if __name__ == '__main__':
    rospy.init_node('Body_alignment_node', anonymous=False)

    routine = BodyAlignmentRoutine()
    rospy.spin()