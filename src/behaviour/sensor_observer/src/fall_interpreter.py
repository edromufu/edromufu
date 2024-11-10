#!/usr/bin/env python3
# coding=utf-8

import rospy
from geometry_msgs.msg import Vector3, PoseStamped
import os
import sys

edrom_dir = '/home/' + os.getlogin() + '/edromufu/src/'

sys.path.append(edrom_dir + 'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters

class FallInterpreter:

    def __init__(self):
        """
        Construtor:
        - Define as variáveis do ROS
        - Define e inicializa variáveis do código
        """
        self.parameters = BehaviourParameters()

        # Variáveis do ROS
        rospy.Subscriber(self.parameters.imuAccelTopic, Vector3, self.callback_sensor_accel)
        rospy.Subscriber(self.parameters.imuGyroTopic, Vector3, self.callback_sensor_gyro)
        rospy.Subscriber(self.parameters.imuRollTopic, Vector3, self.callback_sensor_roll)
        
        # Publicador para o estado de queda
        self.fall_pub = rospy.Publisher(self.parameters.fallStateTopic, PoseStamped, queue_size=10)

        # Variáveis de estado do sistema de detecção de queda
        self.fallState = self.parameters.up  # Estado da queda do robô (up = em pé)
        self.countFalled = 0  # Contador de quedas interpretadas para segurança
        self.accel_data = Vector3()
        self.gyro_data = Vector3()
        self.roll = 0.0

    def callback_sensor_accel(self, msg):
        """
        Callback do acelerômetro:
        - Recebe os dados do acelerômetro e atualiza a variável de aceleração
        """
        self.accel_data = msg
        self.evaluate_fall()

    def callback_sensor_gyro(self, msg):
        """
        Callback do giroscópio:
        - Recebe os dados do giroscópio e atualiza a variável de rotação
        """
        self.gyro_data = msg

    def callback_sensor_roll(self, msg):
        """
        Callback do roll:
        - Recebe o valor de roll calculado e atualiza a variável de roll
        """
        self.roll = msg.x

    def evaluate_fall(self):
        """
        Avalia se houve queda e determina a direção:
        - Interpreta os dados do acelerômetro e giroscópio
        - Interpreta o valor de roll para avaliar o estado de inclinação
        """
        # Contagem de quedas consecutivas para segurança
        if abs(self.accel_data.x) > self.parameters.xGravitySecurity or abs(self.accel_data.y) > self.parameters.yGravitySecurity:
            self.countFalled += 1
        else:
            self.fallState = self.parameters.up
            self.countFalled = 0

        # Avaliação de queda após contagem para evitar falsos positivos
        if self.countFalled > self.parameters.timerCountLimit:
            if self.accel_data.x < self.parameters.xSensorBack:
                # Caiu de costas
                self.fallState = self.parameters.back
            elif self.accel_data.x > self.parameters.xSensorFront:
                # Caiu de frente     
                self.fallState = self.parameters.front
            elif self.accel_data.y < self.parameters.ySensorRight:
                # Caiu sobre o lado direito    
                self.fallState = self.parameters.right
            elif self.accel_data.y > self.parameters.ySensorLeft:
                # Caiu sobre o lado esquerdo    
                self.fallState = self.parameters.left

            # Publicação do estado de queda
            self.publish_fall_state()

    def publish_fall_state(self):
        """
        Publica o estado de queda atual e os dados IMU associados
        """
        fall_msg = PoseStamped()
        fall_msg.header.stamp = rospy.Time.now()
        fall_msg.pose.position.x = self.accel_data.x
        fall_msg.pose.position.y = self.accel_data.y
        fall_msg.pose.position.z = self.accel_data.z
        fall_msg.pose.orientation.x = self.gyro_data.x
        fall_msg.pose.orientation.y = self.gyro_data.y
        fall_msg.pose.orientation.z = self.gyro_data.z
        fall_msg.pose.orientation.w = self.roll

        self.fall_pub.publish(fall_msg)

if __name__ == '__main__':
    rospy.init_node('fall_interpreter', anonymous=False)
    
    fall_interpreter = FallInterpreter()
    rospy.spin()
