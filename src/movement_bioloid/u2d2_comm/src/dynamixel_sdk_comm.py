#!/usr/bin/env python3

import os
import rospy
from dynamixel_sdk import *

from ros_msgs.msg import motors_data
from ros_msgs.srv import enable_torque, enable_torqueResponse

PROTOCOL_VERSION = 1.0  
BAUDRATE = 1000000
DEVICENAME = '/dev/ttyUSB0'

ADDR_TORQUE_ENABLE = 24
ADDR_LED_ENABLE = 25
ADDR_GOAL_POSITION = 30
ADDR_MOVING_SPEED = 32

class u2d2Control():

    def __init__(self):
        rospy.init_node('u2d2')
        
        rospy.Subscriber('u2d2_comm/data2motors', motors_data, self.data2motors)

        rospy.Service('u2d2_comm/enableTorque', enable_torque, self.enableTorque)
        self.enableTorqueRes = enable_torqueResponse()

        self.portHandler = PortHandler(DEVICENAME)
        self.packetHandler = PacketHandler(PROTOCOL_VERSION)
        self.startComm()

    def startComm(self):
        # Open port
        try:
            self.portHandler.openPort()
            print("Succeeded to open the port")
        except:
            print("Failed to open the port")
            print("Press any key to terminate...")
            getch()
            quit()

        # Set port baudrate
        try:
            self.portHandler.setBaudRate(BAUDRATE)
            print("Succeeded to change the baudrate")
        except:
            print("Failed to change the baudrate")
            print("Press any key to terminate...")
            getch()
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

    def data2motors(self, msg):

        for motor_id in range(20):
            self.packetHandler.write2ByteTxOnly(self.portHandler, motor_id, ADDR_GOAL_POSITION, msg.pos_vector[motor_id]+512)         

    def run(self):
        rospy.spin()

if __name__ == '__main__':

    u2d2 = u2d2Control()
    u2d2.run()