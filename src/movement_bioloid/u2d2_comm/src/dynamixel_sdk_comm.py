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

ADDR_MOVING = 46

class u2d2Control():

    def __init__(self):
        rospy.init_node('u2d2')
        
        rospy.Subscriber('u2d2_comm/data2body', body_motors_data, self.data2body)

        #rospy.Subscriber('u2d2_comm/data2head', head_motors_data, self.data2head)

        rospy.Service('u2d2_comm/enableTorque', enable_torque, self.enableTorque)
        self.enableTorqueRes = enable_torqueResponse()

        rospy.Service('u2d2_comm/feedbackMotors', position_feedback, self.feedbackMotors)
        self.feedbackRes = position_feedbackResponse()

        self.portHandler = PortHandler(DEVICENAME)
        self.packetHandler = PacketHandler(PROTOCOL_VERSION)

        self.bodyGroup = GroupSyncWrite(self.portHandler, self.packetHandler, ADDR_GOAL_POSITION, GOAL_POSITION_LENGTH)
        self.headGroup = GroupSyncWrite(self.portHandler, self.packetHandler, ADDR_GOAL_POSITION, GOAL_POSITION_LENGTH)
        self.feedbackGroup = GroupSyncRead(self.portHandler, self.packetHandler, ADDR_GOAL_POSITION, GOAL_POSITION_LENGTH)
        for motor_id in range(20):
            _=self.feedbackGroup.addParam(motor_id)

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
        
        if req.motor_ids[0] == -1:
            motor_ids = range(20)
        else:
            motor_ids = req.motor_ids

        success_motors = []
        failure_motors = []

        for motor_id in motor_ids:
            self.packetHandler.write1ByteTxOnly(self.portHandler, motor_id, ADDR_TORQUE_ENABLE, req.data)
            self.packetHandler.write1ByteTxOnly(self.portHandler, motor_id, ADDR_LED_ENABLE, req.data)
            torque_status, _comm, _hard = self.packetHandler.read1ByteTxRx(self.portHandler, motor_id, ADDR_TORQUE_ENABLE)

            if torque_status != req.data:
                failure_motors.append(motor_id)
            else:
                success_motors.append(motor_id)

        self.enableTorqueRes.message = f'Sucesso: {success_motors}   |   Falha: {failure_motors}'
        if len(success_motors) == len(motor_ids):
            self.enableTorqueRes.success = True
        else:
            self.enableTorqueRes.success = False
        
        return self.enableTorqueRes

    def feedbackMotors(self, req):
        try:

            self.feedbackRes.pos_vector = [0]*20
            self.feedbackGroup.txRxPacket()
            for motor_id in range(20):
                print(self.feedbackGroup.isAvailable(motor_id,ADDR_GOAL_POSITION, GOAL_POSITION_LENGTH)) #! Debug?

                if self.feedbackGroup.isAvailable(motor_id,ADDR_GOAL_POSITION, GOAL_POSITION_LENGTH):
                    motor_pos= self.feedbackGroup.getData( motor_id,ADDR_GOAL_POSITION, GOAL_POSITION_LENGTH)

                    print(motor_pos)    #! Debug?           

                    self.feedbackRes.pos_vector[motor_id] = self.pos2rad(motor_pos)
                else:
                    self.feedbackRes.pos_vector[motor_id] = -1
                
            return self.feedbackRes
        except:
            return self.feedbackMotors(req)

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

            self.headGroup.addParam(motor_id, bytes_value)

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