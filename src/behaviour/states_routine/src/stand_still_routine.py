#!/usr/bin/env python3
#coding=utf-8

import rospy
from modularized_bhv_msgs.msg import currentStateMsg
from movement_msgs.msg import ApprovedMovementMsg

#Setando a grafia correta das requisições para movimento de caminhada
STAND = 'first_pose'

class WalkingRoutine():

    def __init__(self):
        
        self.movement_request_topic = rospy.Publisher('/movement/approved_movement', ApprovedMovementMsg, queue_size=10)
        self.request = ApprovedMovementMsg()

        self.request.approved_movement = STAND

        rospy.Subscriber('/transitions_and_states/state_machine', currentStateMsg, self.flagUpdate)

        self.flag = False

        while not rospy.is_shutdown():

            if self.flag:
                self.flag = False
                self.movement_request_topic.publish(self.request)
    
    def flagUpdate(self, msg):
        message = msg.currentState

        if message == 'stand_still':
            self.flag = True
        else:
            self.flag = False
            

if __name__ == '__main__':
    rospy.init_node('Walking_node', anonymous=False)

    routine = WalkingRoutine()
    rospy.spin()