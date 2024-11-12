#!/usr/bin/env python3
# coding=utf-8

import rospy
import serial
from geometry_msgs.msg import Vector3
import os
import sys

edrom_dir = '/home/' + os.getlogin() + '/edromufu/src/'

sys.path.append(edrom_dir + 'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters

class ImuReader():

    def __init__(self):
        self.parameters = BehaviourParameters()

        # Criando os publishers para os dados do acelerômetro e giroscópio
        self.accel_pub = rospy.Publisher(self.parameters.imuAccelTopic, Vector3, queue_size=10)
        self.accel_msg = Vector3()
        self.gyro_pub = rospy.Publisher(self.parameters.imuGyroTopic, Vector3, queue_size=10)
        self.gyro_msg = Vector3()
        self.roll_pub = rospy.Publisher(self.parameters.imuRollTopic, Vector3, queue_size=10)
        
        # Inicializando o serial com a porta especificada no parâmetro ROS
        self.imu = serial.Serial('/dev/ttyUSB0', 115200)

    def run(self):
        while not rospy.is_shutdown():
            try:
                if self.imu.in_waiting == 0:
                    # Lendo e processando a linha de dados recebida do Arduino
                    imu_output = self.imu.readline().decode().strip()
                    data = imu_output.split('|')
                    print(data)
                    # Convertendo os valores para float e verificando o range dos dados
                    rollC, AcX, AcY, AcZ, GyX, GyY, GyZ = map(float, data)

                    if -200 < rollC < 200:
                        # Publicando os dados do acelerômetro
                        self.accel_msg.x = AcX
                        self.accel_msg.y = AcY
                        self.accel_msg.z = AcZ
                        self.accel_pub.publish(self.accel_msg)

                        # Publicando os dados do giroscópio
                        self.gyro_msg.x = GyX
                        self.gyro_msg.y = GyY
                        self.gyro_msg.z = GyZ
                        self.gyro_pub.publish(self.gyro_msg)

                            # Publicando o valor de roll calculado
                        roll_msg = Vector3()
                        rospy.get_param('/imu_ros_arduino/port')
                        roll_msg.x = rollC
                        self.roll_pub.publish(roll_msg)
                rospy.sleep(0.1)  # Delay para não sobrecarregar a CPU
            except Exception as e:
                rospy.logerr("Error reading IMU data: %s", e)
                pass

        self.imu.close()

if __name__ == '__main__':
    rospy.init_node('imu_node', anonymous=False)
    
    imu_reader = ImuReader()
    imu_reader.run()

    rospy.spin()