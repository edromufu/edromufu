#!/usr/bin/env python3

from movement_utils.msg import *
from movement_utils.srv import *
import rospy

def handle_enable_torque(req):
    return enable_torqueResponse(True)

def handle_feedback_motors(req):
    global COUNT
    COUNT += 1
    return body_feedbackResponse([COUNT]*18)

def server():
    rospy.init_node('u2d2')
    rospy.Service('u2d2_comm/enableTorque', enable_torque, handle_enable_torque)
    rospy.Service('u2d2_comm/feedbackBody', body_feedback, handle_feedback_motors)

    rospy.spin()

if __name__ == "__main__":
    global COUNT
    COUNT = 0 
    server()