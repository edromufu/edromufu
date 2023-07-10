#!/usr/bin/env python3

import os
import rospy
from dynamixel_sdk import *

from movement_utils.msg import *
from movement_utils.srv import *

PROTOCOL_VERSION = 1.0  
BAUDRATE = 1000000

DEVICENAME = rospy.get_param('u2d2/port')

ADDR_TORQUE_ENABLE = 24
ADDR_LED_ENABLE = 25

ADDR_GOAL_POSITION = 30
GOAL_POSITION_LENGTH = 2

ADDR_PRESENT_POSITION = 36

class u2d2Control():

    def __init__(self):
        rospy.init_node('u2d2')
        
        rospy.Subscriber('u2d2_comm/data2body', body_motors_data, self.data2body)

        rospy.Subscriber('u2d2_comm/data2head', head_motors_data, self.data2head)

        rospy.Service('u2d2_comm/enableTorque', enable_torque, self.enableTorque)
        self.enableTorqueRes = enable_torqueResponse()

        rospy.Service('u2d2_comm/feedbackBody', body_feedback, self.feedbackBodyMotors)
        self.bodyFeedbackRes = body_feedbackResponse()

        rospy.Service('u2d2_comm/feedbackHead', head_feedback, self.feedbackHeadMotors)
        self.headFeedbackRes = head_feedbackResponse()

        self.portHandler = PortHandler(DEVICENAME)
        self.packetHandler = PacketHandler(PROTOCOL_VERSION)

        self.bodyGroup = GroupSyncWrite(self.portHandler, self.packetHandler, ADDR_GOAL_POSITION, GOAL_POSITION_LENGTH)
        self.headGroup = GroupSyncWrite(self.portHandler, self.packetHandler, ADDR_GOAL_POSITION, GOAL_POSITION_LENGTH)

        self.startComm()

    def startComm(self):
        # Open port
        try:
            self.portHandler.openPort()
            print("Succeeded to open the port")
        except:
            print("Failed to open the port")
            quit()

        # Set port baudrate
        try:
            self.portHandler.setBaudRate(BAUDRATE)
            print("Succeeded to change the baudrate")
        except:
            print("Failed to change the baudrate")
            quit()
    
    def enableTorque(self, req):
        
        for _ in range(3):
            if req.motor_ids[0] == -1:
                motor_ids = range(20)
            else:
                motor_ids = req.motor_ids
            
            for motor_id in motor_ids:
                self.packetHandler.write1ByteTxOnly(self.portHandler, motor_id, ADDR_TORQUE_ENABLE, req.data)
                self.packetHandler.write1ByteTxOnly(self.portHandler, motor_id, ADDR_LED_ENABLE, req.data)

            self.enableTorqueRes.success = True
        
        return self.enableTorqueRes

    def feedbackBodyMotors(self, req):
        try:
            self.bodyFeedbackRes.pos_vector = [0]*18

            for motor_id in range(18):
                motor_position, comm, hard = self.packetHandler.read2ByteTxRx(self.portHandler, motor_id, ADDR_PRESENT_POSITION)

                if comm !=0 or hard != 0:
                    self.bodyFeedbackRes.pos_vector[motor_id] = -1
                else:
                    self.bodyFeedbackRes.pos_vector[motor_id] = self.pos2rad(motor_position)

            return self.bodyFeedbackRes
        except:
            return self.feedbackBodyMotors(req)
    
    def feedbackHeadMotors(self, req):
        try:
            self.headFeedbackRes.pos_vector = [0]*2

            for motor_id in range(2):
                motor_position, comm, hard = self.packetHandler.read2ByteTxRx(self.portHandler, motor_id+18, ADDR_PRESENT_POSITION)

                if comm !=0 or hard != 0:
                    self.headFeedbackRes.pos_vector[motor_id] = -1
                else:
                    self.headFeedbackRes.pos_vector[motor_id] = self.pos2rad(motor_position)

            return self.headFeedbackRes
        except:
            return self.feedbackHeadMotors(req)

    def data2body(self, msg):
        self.bodyGroup.clearParam()

        for motor_id in range(18):
            motor_position = msg.pos_vector[motor_id]

            value = self.rad2pos(motor_position)
            bytes_value = value.to_bytes(2, byteorder='little')

            self.bodyGroup.addParam(motor_id, bytes_value)

        self.bodyGroup.txPacket()

    def data2head(self, msg):
        self.headGroup.clearParam()

        for motor_id in range(2):
            motor_position = msg.pos_vector[motor_id]

            value = self.rad2pos(motor_position)
            bytes_value = value.to_bytes(2, byteorder='little')

            self.headGroup.addParam(motor_id+18, bytes_value)

        self.headGroup.txPacket()
    
    def rad2pos(self, pos_in_rad):
        
        motor_position = int(195.379*pos_in_rad + 512)
        motor_position = min(motor_position, 1023)
        motor_position = max(motor_position, 0)
        
        return motor_position

    def pos2rad(self, motor_position):
        pos_in_rad = (motor_position-512)/195.379

        return pos_in_rad

    def run(self):
        rospy.spin()

if __name__ == '__main__':

    u2d2 = u2d2Control()
    u2d2.run()