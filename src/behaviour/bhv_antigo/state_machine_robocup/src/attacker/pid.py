#!/usr/bin/env python3
import rospy
from vision_msgs.msg import Ball
from movement_msgs.msg import MotorRequestMsg, OpencmResponseMsg
from behaviour_msgs.msg import PIDHeadMsg

import time

import numpy as np

posicao_do_motor_18 = 0
posicao_do_motor_19 = 0

def callback_movimento(msg):
    global posicao_do_motor_18
    global posicao_do_motor_19
    posicao_do_motor_18 = msg.data[18]
    posicao_do_motor_19 = msg.data[19]

def callback_visao(msg):
    pass

degrau = 0.523599
final_time = 1.0
Ts = 0.02/50

if __name__ == '__main__':
    rospy.init_node("PID_Behaviour", anonymous = True)

    pub_movimento = rospy.Publisher('/motor_comm/request', MotorRequestMsg)

    rospy.Subscriber('/opencm/response', OpencmResponseMsg, callback = callback_movimento)
    rospy.Subscriber('/topico_da_visao_do_PID', Ball, callback = callback_visao)

    # Enviando o degrau pro motor
    msg_pub_movimento = PIDHeadMsg()
    msg_pub_movimento.head = 0
    msg_pub_movimento.neck = degrau

    while not rospy.is_shutdown():
        tempo1 = time.time()
        print("==============")
        print(posicao_do_motor_18)
        print(posicao_do_motor_19)
        print(time.time() - tempo1)

        pub_movimento.publish(msg_pub_movimento)

    rospy.spin()