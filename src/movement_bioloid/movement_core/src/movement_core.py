#!/usr/bin/env python3
#coding=utf-8

import rospy, sys, os

from movement_utils.srv import *
from movement_utils.msg import *

#! Verificar uma maneira mais bonita de importar arquivos
os.chdir(os.path.dirname(__file__))
os.chdir("../../humanoid_definition/src")
sys.path.append(os.getcwd())
from setup_robot import Robot

class Core:

    def __init__(self):
        self.initROS()

        robot_name = rospy.get_param('movement_core/name')
        self.robot = Robot(robot_name)

        self.robot.robotJoints

    def initROS(self):
        rospy.init_node('movement_core')

        self.pub2motors = rospy.Publisher('u2d2_comm/data2motors', motors_data, queue_size=10)
        self.pub2motorsMsg = motors_data()
        self.reqMotorsPos = rospy.ServiceProxy('u2d2_comm/feedbackMotors', position_feedback)

        rospy.Service('movement_core/gait', gait, self.movementManager)
        self.gaitRes = gaitResponse()
    
    def movementManager(self, req):
        #! Adicionar tratamento para concorrência de requisições

        pass


        

if __name__ == '__main__':
    movement = Core()
    rospy.spin()