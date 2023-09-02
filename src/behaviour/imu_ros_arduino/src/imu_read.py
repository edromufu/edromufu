#!/usr/bin/env python3
#coding=utf-8

import rospy, serial
from geometry_msgs.msg import Vector3

def run(imu, publisher, msg):
    
    while not rospy.is_shutdown():
        cc = str(imu.readline())
        print(f'cc: {cc}')

        cleaned_str = str(cc[2:][:-5])
        try:
            angles_str = cleaned_str.split(",")
            angles_float = [float(angle) for angle in angles_str]
            [msg.x, msg.y, msg.z] = angles_float
        except:
            [msg.x, msg.y, msg.z] = [-9999,-9999,-9999]
        
        publisher.publish(msg)

def connect():
    return serial.Serial('/dev/ttyUSB0', 9600)

if __name__ == '__main__':
    rospy.init_node('IMU_node', anonymous=False)

    imu = connect()
    imupub = rospy.Publisher('/behaviour/imu', Vector3, queue_size=10)
    imumsg = Vector3()

    run(imu, imupub, imumsg)  #Inicia a publicação dos dados  
    rospy.spin()
    imu.close()