#!/usr/bin/env python3
#coding=utf-8

import rclpy
from rclpy.node import Node
import serial, os, sys
from geometry_msgs.msg import Vector3

edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters

class ImuReader(Node):

    def __init__(self):
        super().__init__('IMU_node')
        
        self.parameters = BehaviourParameters()

        self.accelPub = self.create_publisher(Vector3, self.parameters.imuAccelTopic, 10)
        self.accelMsg = Vector3()
        self.gyroPub = self.create_publisher(Vector3, self.parameters.imuGyroTopic, 10)
        self.gyroMsg = Vector3()
        
        self.imu = serial.Serial(self.get_parameter('imu_ros_arduino_port').get_parameter_value().string_value, 115200)
        self.create_timer(0.1, self.read_imu_data)

    def read_imu_data(self):
        try:
            if self.imu.inWaiting():
                imu_output = self.imu.readline()
                imu_output = imu_output.strip().split()
                imu_output = [float(string) for string in imu_output]
                
                if max(imu_output) < 10 and min(imu_output) > -10:
                    self.accelMsg.x = imu_output[0]
                    self.accelMsg.y = imu_output[1]
                    self.accelMsg.z = imu_output[2]
                    
                    self.accelPub.publish(self.accelMsg)

        except Exception as e:
            pass

    def close_serial(self):
        self.imu.close()

def main(args=None):
    rclpy.init(args=args)
    
    imu_reader = ImuReader()
    
    try:
        rclpy.spin(imu_reader)
    except KeyboardInterrupt:
        pass
    finally:
        imu_reader.close_serial()
        imu_reader.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
