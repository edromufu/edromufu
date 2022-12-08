#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import sys
import os
from movement_msgs.srv import BehRequestSrv, BehRequestSrvResponse, CommandToOpenCMSrv
from movement_msgs.msg import ApprovedMovementMsg

from std_msgs.msg import Bool

user_name = os.environ.get("HOME")
sys.path.append(user_name + "/edrom/src/movement/mov_bridge/include")

import statsManipulator

class MovementCommunication():

    def __init__(self):
        self.manipulator = statsManipulator.StatsManipulator()     
        self.srv_comunication_beh = BehRequestSrvResponse()

        self.is_simulation = rospy.get_param('mov_bridge/simulation')

        rospy.Service('/movement/mov_bridge/commands2movement', BehRequestSrv, self.requestMovement)
        self.movement_approved_pub = rospy.Publisher('/movement/approved_movement', ApprovedMovementMsg, queue_size=100)
        self.movement_approved_msg = ApprovedMovementMsg()

        self.client_torque_disable = rospy.ServiceProxy('opencm/request_command', CommandToOpenCMSrv)
        self.stop_motions_pub = rospy.Publisher('/mov_bridge/is_motion_stopped', Bool, queue_size=100)
        self.stop_motions_msg = Bool()
        
    def requestMovement(self, requisition):
        movement_exists = self.checkExistence(requisition.required_movement)

        print("\nO movimento solicitado existe:",movement_exists)

        if movement_exists:
            service_response = self.changeStatus(requisition.required_movement,requisition.required_status)
            
            if requisition.required_status:
                if requisition.required_movement == 'emergency_shutdown':
                    if not self.is_simulation:
                        self.client_torque_disable('shutdown_now')
                        
                    else:
                        self.stop_motions_msg.data = True
                        self.stop_motions_pub.publish(self.stop_motions_msg)

                elif requisition.required_movement == 'stop_all_motions':
                    self.stop_motions_msg.data = True
                    self.stop_motions_pub.publish(self.stop_motions_msg)

                else:
                    if not self.is_simulation:
                        self.client_torque_disable('reborn')
                        
                    self.stop_motions_msg.data = False
                    self.stop_motions_pub.publish(self.stop_motions_msg)

                    self.sendMovement(requisition.required_movement)             
        
        self.srv_comunication_beh.response = True
        return self.srv_comunication_beh

    def checkExistence(self, movement):

        return self.manipulator.isMovementListed(movement)

    def changeStatus(self,movement,status):

        return self.manipulator.changeMovementStatus(movement,status)
    
    def sendMovement(self, movement):
        self.movement_approved_msg.approved_movement = movement
        self.movement_approved_pub.publish(self.movement_approved_msg)

        
if __name__ == "__main__":
    rospy.init_node('Movement_bridge_node', anonymous=False)

    movement = MovementCommunication()

    rospy.spin()