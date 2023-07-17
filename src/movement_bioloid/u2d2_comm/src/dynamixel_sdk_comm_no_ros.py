#!/usr/bin/env python3

import os
import time
from dynamixel_sdk import *

PROTOCOL_VERSION = 1.0  
BAUDRATE = 1000000
DEVICENAME = '/dev/ttyUSB0'

ADDR_TORQUE_ENABLE = 24
ADDR_LED_ENABLE = 25
ADDR_GOAL_POSITION = 30
ADDR_PRESENT_POSITION = 36
ADDR_MOVING_SPEED = 32

class u2d2Control():

    def __init__(self):      

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
    
    def enableTorque(self, ids, enable):
        
        if ids[0] == -1:
            motor_ids = range(20)
        else:
            motor_ids = ids

        success_motors = []
        failure_motors = []

        for motor_id in motor_ids:
            self.packetHandler.write1ByteTxOnly(self.portHandler, motor_id, ADDR_TORQUE_ENABLE, enable)
            self.packetHandler.write1ByteTxOnly(self.portHandler, motor_id, ADDR_LED_ENABLE, enable)
            torque_status, _comm, _hard = self.packetHandler.read1ByteTxRx(self.portHandler, motor_id, ADDR_TORQUE_ENABLE)

            if torque_status != enable:
                failure_motors.append(motor_id)
            else:
                success_motors.append(motor_id)

        enableTorqueRes = f'Sucesso: {success_motors}   |   Falha: {failure_motors}'

        return enableTorqueRes

    def data2motors(self, pos_vector):

        for motor_id in range(20):
            self.packetHandler.write2ByteTxOnly(self.portHandler, motor_id, ADDR_GOAL_POSITION, pos_vector[motor_id])

    def feedback(self):
        feedback = 20 * [0]

        for motor_id in range(20):
            position, comm, hard = self.packetHandler.read2ByteTxRx(self.portHandler, motor_id, ADDR_PRESENT_POSITION)
            
            if comm !=0 or hard != 0:
                position = -1

            feedback[motor_id] = position

        return feedback


if __name__ == '__main__':

    u2d2 = u2d2Control()
    for i in range(20):
        print(u2d2.feedback())

        
        