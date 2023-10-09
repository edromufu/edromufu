#!/usr/bin/env python3
#coding=utf-8

import rospy, serial, os, sys
from geometry_msgs.msg import Vector3

edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters

class imuReader():

    def __init__(self):
        
        self.parameters = BehaviourParameters()

        self.accelPub = rospy.Publisher(self.parameters.imuAccelTopic, Vector3, queue_size=10)
        self.accelMsg = Vector3()
        self.gyroPub = rospy.Publisher(self.parameters.imuGyroTopic, Vector3, queue_size=10)
        self.gyroMsg = Vector3()
        
        self.imu = serial.Serial(rospy.get_param('/imu_ros_arduino/port'), 115200)
    
    def run(self):
        while not rospy.is_shutdown():
            try:
                if self.imu.inWaiting():
                    
                    imu_output = self.imu.readline()
                    imu_output = imu_output.strip().split()
                    imu_output = [float(string) for string in imu_output]
                    
                    if max(imu_output) < 10 and min(imu_output) > -10:
                        self.accelMsg.x = imu_output[0]
                        self.accelMsg.y = imu_output[1]
                        self.accelMsg.z = imu_output[2]
                        
                        self.gyroMsg.x = imu_output[3]
                        self.gyroMsg.y = imu_output[4]
                        self.gyroMsg.z = imu_output[5]

                    self.accelPub.publish(self.accelMsg)
                    self.gyroPub.publish(self.gyroMsg)

            except Exception as e:
                print(e)

        self.imu.close()

if __name__ == '__main__':
    rospy.init_node('IMU_node', anonymous=False)
    
    imu = imuReader()
    imu.run()

    rospy.spin()