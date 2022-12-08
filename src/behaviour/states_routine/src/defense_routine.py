#!/usr/bin/env python3
#coding=utf-8

import rospy
import time
from modularized_bhv_msgs.msg import currentStateMsg, stateMachineMsg
from movement_msgs.msg import ApprovedMovementMsg

LEFT = 'left_fall'
RIGHT = 'right_fall'

class DefenseRoutine():

    def __init__(self):

        rospy.Subscriber('/transitions_and_states/state_machine', currentStateMsg, self.flagUpdate)
        rospy.Subscriber('/sensor_observer/state_machine_vars', stateMachineMsg, self.varsUpdate)

        self.flag = False
        
        self.movement_request_topic = rospy.Publisher('/movement/approved_movement', ApprovedMovementMsg, queue_size=10)
        self.request = ApprovedMovementMsg()
        

        while not rospy.is_shutdown():   

            if self.flag:
                self.flag = False
                if 'Left' in self.current_ball_position:
                    self.request.approved_movement = LEFT
                elif 'Right' in self.current_ball_position:
                    self.request.approved_movement = RIGHT
                
                self.movement_request_topic.publish(self.request) 

    def flagUpdate(self, msg):
        if msg.currentState == 'defense':
            self.flag = True
        else:
            self.flag = False

    def varsUpdate(self, msg):
        self.current_ball_position = msg.ballRelativePosition
        
if __name__ == '__main__':
    rospy.init_node('Defense_node', anonymous=False)

    routine = DefenseRoutine()
    rospy.spin()
