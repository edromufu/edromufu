#!/usr/bin/env python3

import time
#import rospy (0)
import rclpy #(0)
from dynamixel_sdk import *

from movement_utils.msg import *
from movement_utils.srv import *

BAUDRATE = 1000000

'''
#DEVICENAME = rospy.get_param('u2d2/port') (1)
#DEVICENAME = node.declare_parameter('u2d2/port').value #(1) #joguei isso para dentro do init da classe (***)
'''

PROTOCOL_1_INFOS =  {'CW_LIMIT_ADDR': 6, 'CCW_LIMIT_ADDR': 8, 'TORQUE_ADDR': 24, 'LED_ADDR': 25 , 'PRES_POS_ADDR': 36, 'GOAL_POS_ADDR': 30, 'GOAL_POS_LEN': 2}
PROTOCOL_2_INFOS =  {'CW_LIMIT_ADDR': 48, 'CCW_LIMIT_ADDR': 52, 'TORQUE_ADDR': 64, 'LED_ADDR': 65 , 'PRES_POS_ADDR': 132, 'GOAL_POS_ADDR': 116, 'GOAL_POS_LEN': 4, 'VELOCITY_ADDR': 112, 'VELOCITY_LEN': 4, 'CURRENT_ADDR': 126}

PROTOCOL_2_MOTORS = list(range(18))
PROTOCOL_1_MOTORS = [18,19]

VELOCITY = 95 #max 195


#if rospy.get_param('u2d2/robot_name') == 'aurea': (2)
'''
if node.declare_parameter('u2d2/robot_name').value == 'aurea': #(2) #peguei isso e coloquei tudo no init da classe (***)
    print('Aurea')
    # MIN_MAX_DICT = {0: [570,4095],1: [0,3500],2: [2040,3600],3: [500,2100],4: [700,2300],
    #                 5: [1800,3400],6: [1930,2425],7: [1589,2275],8: [1600,2444],9: [1700,2500],
    #                 10: [1690,2922],11: [1100,2922],12: [750,2226],13: [750,2226],14: [900,2300],
    #                 15: [865,2330],16: [1760,2290],17: [1665,2300],18: [0,1023],19: [0,1023]}
    MIN_MAX_DICT = {0: [570,4095],1: [0,3500],2: [2040,3600],3: [500,2100],4: [700,2300],
                    5: [1800,3400],6: [1930,2425],7: [1589,2275],8: [1600,2444],9: [1700,2500],
                    10: [1690,3400],11: [650,2922],12: [750,2226],13: [750,2226],14: [900,2300],
                    15: [865,2330],16: [1760,2290],17: [1665,2300],18: [0,1023],19: [0,1023]}
else:
    print('Natasha')
    MIN_MAX_DICT = {0: [1261,4028],1: [0,3900],2: [233,2047],3: [0,2047],4: [2061,3350],
                    5: [900,2100],6: [0,4095],7: [0,4095],8: [0,4095],9: [0,4095],
                    10: [1050,3048],11: [1097,3083],12: [1024,2082],13: [1974,3071],14: [0,4095],
                    15: [0,4095],16: [1760,2290],17: [1760,2290],18: [0,1023],19: [0,1023]}
'''

class u2d2Control():

    def __init__(self):
        self.motorLimitsDict = MIN_MAX_DICT
        
        self.startComm()

        #rospy.init_node('u2d2') (3)

        rclpy.init(args=sys.argv) #(3)
        self.node = rclpy.create_node('u2d2') #(3)

        self.DEVICENAME = self.node.declare_parameter('u2d2/port').get_parameter_value().string_value #(***)

        if self.node.declare_parameter('u2d2/robot_name').get_parameter_value().string_value == 'aurea': #(2) #(***)
            print('Aurea')
            # MIN_MAX_DICT = {0: [570,4095],1: [0,3500],2: [2040,3600],3: [500,2100],4: [700,2300],
            #                 5: [1800,3400],6: [1930,2425],7: [1589,2275],8: [1600,2444],9: [1700,2500],
            #                 10: [1690,2922],11: [1100,2922],12: [750,2226],13: [750,2226],14: [900,2300],
            #                 15: [865,2330],16: [1760,2290],17: [1665,2300],18: [0,1023],19: [0,1023]}
            MIN_MAX_DICT = {0: [570,4095],1: [0,3500],2: [2040,3600],3: [500,2100],4: [700,2300],
                    5: [1800,3400],6: [1930,2425],7: [1589,2275],8: [1600,2444],9: [1700,2500],
                    10: [1690,3400],11: [650,2922],12: [750,2226],13: [750,2226],14: [900,2300],
                    15: [865,2330],16: [1760,2290],17: [1665,2300],18: [0,1023],19: [0,1023]}
        else:
            print('Natasha')
            MIN_MAX_DICT = {0: [1261,4028],1: [0,3900],2: [233,2047],3: [0,2047],4: [2061,3350],
                    5: [900,2100],6: [0,4095],7: [0,4095],8: [0,4095],9: [0,4095],
                    10: [1050,3048],11: [1097,3083],12: [1024,2082],13: [1974,3071],14: [0,4095],
                    15: [0,4095],16: [1760,2290],17: [1760,2290],18: [0,1023],19: [0,1023]}
        

        #rospy.Subscriber('u2d2_comm/data2body', body_motors_data, self.data2body) (4)
        self.node.create_subscription(BodyMotorsData, 'u2d2_comm/data2body', self.data2body, rclpy.qos.QoSProfile()) #(4)

        #rospy.Subscriber('u2d2_comm/data2head', head_motors_data, self.data2head) (5)
        self.node.create_subscription(HeadMotorsData, 'u2d2_comm/data2head', self.data2head, rclpy.qos.QoSProfile()) #(5)

        #rospy.Service('u2d2_comm/enableTorque', enable_torque, self.enableTorque) (6)
        self.node.create_service(EnableTorque, 'u2d2_comm/enableTorque', self.enableTorque) #(6)
        #self.enableTorqueRes = EnableTorqueResponse() *se tornou um argumento da função (10)

        #rospy.Service('u2d2_comm/feedbackBody', body_feedback, self.feedbackBodyMotors) (7)
        self.node.create_service(BodyFeedback, 'u2d2_comm/feedbackBody', self.feedbackBodyMotors) #(7)
        #self.bodyFeedbackRes = BodyFeedbackResponse() *se tornou um argumento da função (11)

        #rospy.Service('u2d2_comm/feedbackHead', head_feedback, self.feedbackHeadMotors) (8)
        self.node.create_service(HeadFeedback, 'u2d2_comm/feedbackHead', self.feedbackHeadMotors) #(8)
        #self.headFeedbackRes = HeadFeedbackResponse() *se tornou um argumento da função (12)

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

    def startComm(self):
        self.portHandler = PortHandler(self.DEVICENAME)

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
        
        self.packetHandler1 = PacketHandler(1.0)
        self.headGroup = GroupSyncWrite(self.portHandler, self.packetHandler1, PROTOCOL_1_INFOS['GOAL_POS_ADDR'], PROTOCOL_1_INFOS['GOAL_POS_LEN'])

        self.packetHandler2 = PacketHandler(2.0)   
        self.bodyGroup = GroupSyncWrite(self.portHandler, self.packetHandler2, PROTOCOL_2_INFOS['GOAL_POS_ADDR'], PROTOCOL_2_INFOS['GOAL_POS_LEN'])  
        self.velocityGroup = GroupSyncWrite(self.portHandler, self.packetHandler2, PROTOCOL_2_INFOS['VELOCITY_ADDR'], PROTOCOL_2_INFOS['VELOCITY_LEN'])  

        for id in range(18):
            self.velocityGroup.addParam(id, VELOCITY.to_bytes(4, byteorder='little'))
        
        self.velocityGroup.txPacket()

    def enableTorque(self, req, enableTorqueRes): 
        
        for _ in range(3):
            if req.motor_ids[0] == -1:
                motor_ids = range(20)
            else:
                motor_ids = req.motor_ids
            
            for motor_id in motor_ids:
                if motor_id in PROTOCOL_1_MOTORS:
                    packetHandler = self.packetHandler1
                    torqueAddr = PROTOCOL_1_INFOS['TORQUE_ADDR']
                    ledAddr = PROTOCOL_1_INFOS['LED_ADDR']

                elif motor_id in PROTOCOL_2_MOTORS:
                    packetHandler = self.packetHandler2
                    torqueAddr = PROTOCOL_2_INFOS['TORQUE_ADDR']
                    ledAddr = PROTOCOL_2_INFOS['LED_ADDR']

                
                packetHandler.write1ByteTxOnly(self.portHandler, motor_id, torqueAddr, req.data)
                packetHandler.write1ByteTxOnly(self.portHandler, motor_id, ledAddr, req.data)

            enableTorqueRes.success = True 
        
        return enableTorqueRes

    def feedbackBodyMotors(self, req, bodyFeedbackRes): #adição do novo argumento 'bodyFeedbackRes' (11)

        try:

            bodyFeedbackRes.pos_vector = [0]*18

            for motor_id in range(18):
                motor_position, comm, hard = self.packetHandler2.read4ByteTxRx(self.portHandler, motor_id, PROTOCOL_2_INFOS['PRES_POS_ADDR'])

                if comm !=0 or hard != 0:
                    bodyFeedbackRes.pos_vector[motor_id] = -1
                else:
                    bodyFeedbackRes.pos_vector[motor_id] = self.pos2rad(motor_position, 2.0)

            return bodyFeedbackRes 

        except:
            time.sleep(1.5)
            self.startComm()
            return self.feedbackBodyMotors(req)

    def feedbackHeadMotors(self, req, headFeedbackRes): #adição do novo argumento 'headFeedbackRes' (12)

        try:

            headFeedbackRes.pos_vector = [0]*2

            for motor_id in range(2):
                motor_position, comm, hard = self.packetHandler1.read2ByteTxRx(self.portHandler, motor_id+18, PROTOCOL_1_INFOS['PRES_POS_ADDR'])

                if comm !=0 or hard != 0:
                    headFeedbackRes.pos_vector[motor_id] = -1
                else:
                    headFeedbackRes.pos_vector[motor_id] = self.pos2rad(motor_position, 1.0)

            return headFeedbackRes 

        except:
            time.sleep(1.5)
            self.startComm()
            return self.feedbackHeadMotors(req)

    def data2body(self, msg):
        self.bodyGroup.clearParam()
        
        for motor_id in range(18):
            motor_position = msg.pos_vector[motor_id]          
            
            value = self.rad2pos(motor_position, 2.0)            
            value = self.checkPositionInLimit(value, motor_id)

            bytes_value = value.to_bytes(4, byteorder='little')

            self.bodyGroup.addParam(motor_id, bytes_value)

        try:
            self.bodyGroup.txPacket()
        except:
            time.sleep(1.5)
            self.startComm()
            self.data2body(msg)

    def data2head(self, msg):
        self.headGroup.clearParam()

        for motor_id in range(2):
            motor_position = msg.pos_vector[motor_id]

            value = self.rad2pos(motor_position, 1.0)
            value = self.checkPositionInLimit(value, motor_id+18)
            bytes_value = value.to_bytes(2, byteorder='little')

            self.headGroup.addParam(motor_id+18, bytes_value)

        try:
            self.headGroup.txPacket()
        except:
            time.sleep(1.5)
            self.startComm()
            self.data2body(msg)
    
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
        #rospy.spin() (9)
        rclpy.spin(u2d2.node) #(9)

def main():
    u2d2 = u2d2Control()
    u2d2.run()
    
if __name__ == '__main__':
   main()
