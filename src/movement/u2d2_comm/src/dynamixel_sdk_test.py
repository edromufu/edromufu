#!/usr/bin/env python3

import time
import rospy
from dynamixel_sdk import *

from movement_utils.msg import *
from movement_utils.srv import *

BAUDRATE = 1000000


if rospy.get_param('u2d2_false/robot_name') == 'aurea':
    print('Aurea')
    MIN_MAX_DICT = {0: [1450,4095],1: [0,2650],2: [2040,3600],3: [500,2100],4: [700,2300],
                    5: [1800,3400],6: [1930,2425],7: [1589,2275],8: [1600,2444],9: [1700,2500],
                    10: [1690,2922],11: [1100,2922],12: [750,2226],13: [750,2226],14: [900,2300],
                    15: [865,2330],16: [1760,2290],17: [1665,2300],18: [0,1023],19: [0,1023]}
else:
    print('Natasha')
    MIN_MAX_DICT = {0: [1261,4028],1: [0,3900],2: [233,2047],3: [0,2047],4: [2061,3350],
                    5: [900,2100],6: [0,4095],7: [0,4095],8: [0,4095],9: [0,4095],
                    10: [1050,3048],11: [1097,3083],12: [1024,2082],13: [1974,3071],14: [0,4095],
                    15: [0,4095],16: [1760,2290],17: [1760,2290],18: [0,1023],19: [0,1023]}

class u2d2Control():

    def __init__(self):
        self.motorLimitsDict = MIN_MAX_DICT

        rospy.init_node('u2d2')
        
        rospy.Subscriber('u2d2_comm/data2body', body_motors_data, self.data2body)

        rospy.Subscriber('u2d2_comm/data2head', head_motors_data, self.data2head)

        rospy.Service('u2d2_comm/enableTorque', enable_torque, self.enableTorque)
        self.enableTorqueRes = enable_torqueResponse()

        rospy.Service('u2d2_comm/feedbackBody', body_feedback, self.feedbackBodyMotors)
        self.bodyFeedbackRes = body_feedbackResponse()

        rospy.Service('u2d2_comm/feedbackHead', head_feedback, self.feedbackHeadMotors)
        self.headFeedbackRes = head_feedbackResponse()    

        self.currentPosition = [2047]*18

    def checkPositionInLimit(self, value, motor_id):

        if motor_id in self.motorLimitsDict.keys():
            if self.motorLimitsDict[motor_id][0] > value:

                valueTmp = value
                value = self.motorLimitsDict[motor_id][0]
                print(f'Foi comandado {valueTmp} para o motor {motor_id}, isso extrapola o limite {value}, comandando {value}')

            elif self.motorLimitsDict[motor_id][1] < value:

                valueTmp = value
                value = self.motorLimitsDict[motor_id][1]
                print(f'Foi comandado {valueTmp} para o motor {motor_id}, isso extrapola o limite {value}, comandando {value}')
        
        return value

    def enableTorque(self, req):

        self.enableTorqueRes.success = True
        
        return self.enableTorqueRes

    def feedbackBodyMotors(self, req):

        for motor_id in range(18):
            self.bodyFeedbackRes.pos_vector[motor_id] = self.pos2rad(self.currentPosition[motor_id], 2.0)

        return self.bodyFeedbackRes

    def feedbackHeadMotors(self, req):

        self.headFeedbackRes.pos_vector = [0]*2

        return self.headFeedbackRes

    def data2body(self, msg):
        for motor_id in range(18):
            motor_position = msg.pos_vector[motor_id]          
            
            value = self.rad2pos(motor_position, 2.0)            
            value = self.checkPositionInLimit(value, motor_id)

            self.currentPosition[motor_id] = value

    def data2head(self, msg):
        pass
    
    def rad2pos(self, pos_in_rad, motor_protocol):
        
        if motor_protocol == 1.0:
            motor_position = int(195.379*pos_in_rad + 512)
            motor_position = min(motor_position, 1023)
            motor_position = max(motor_position, 0)

        elif motor_protocol == 2.0:
            motor_position = int(651.739*pos_in_rad + 2047.5)
            motor_position = min(motor_position, 4095)
            motor_position = max(motor_position, 0)
        
        return motor_position

    def pos2rad(self, motor_position, motor_protocol):

        if motor_protocol == 1.0:
            pos_in_rad = (motor_position-512)/195.379
        
        elif motor_protocol == 2.0:
            pos_in_rad = (motor_position-2047.5)/651.739

        return pos_in_rad

    def run(self):
        rospy.spin()

if __name__ == '__main__':

    u2d2 = u2d2Control()
    u2d2.run()