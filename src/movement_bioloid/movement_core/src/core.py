#!/usr/bin/env python3
#coding=utf=8

import rospy

import sys, os
edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'movement_bioloid/humanoid_definition/src')
from setup_robot import Robot

sys.path.append(edrom_dir+'movement_bioloid/movement_functions/src')
from movement_patterns import Gait

from movement_utils.srv import *
from movement_utils.msg import *

QUEUE_TIME = 1 #Em segundos

class Core:
    def __init__(self): 
        #Inicialização do objeto (modelo) da robô em código
        robot_name = rospy.get_param('/movement_core/name')
        
        self.robotInstance = Robot(robot_name)
        self.robotModel = self.robotInstance.robotJoints
        
        # Inicialização das variáveis do ROS
        rospy.init_node('movement_central')

        #Services de requisição de movimento, todos possuem como callback movementManager
        rospy.Service('movement_central/request_gait', gait, self.movementManager)
        
        #Estruturas para comunicação com U2D2
        self.motorsFeedback = rospy.ServiceProxy('u2d2_comm/feedbackMotors', position_feedback)
        self.pub2motors = rospy.Publisher('u2d2_comm/data2motors', motors_data, queue_size=100)
        self.pub2motorsMsg = motors_data()

        #Timer para fila de publicações
        rospy.Timer(rospy.Duration(QUEUE_TIME), self.sendFromQueue)
        self.queue = []

    def invertMotorsPosition(self, toInvert):
        for motor in self.robotModel:
            if motor.is_inverted():
                toInvert[motor.get_id()] *= -1 

        inverted = toInvert

        return inverted

    def callRobotModelUpdate(self):
        motorsCurrentPosition = self.motorsFeedback(True).pos_vector

        motorsCurrentPosition = self.invertMotorsPosition(motorsCurrentPosition)

        self.robotInstance.updateRobotModel(motorsCurrentPosition)

    def movementManager(self, req):
        #self.callRobotModelUpdate()

        if 'gait' in str(req.__class__):
            gait_poses = Gait(self.robotModel, req.step_height, req.steps_number)

            for pose in gait_poses:
                self.queue.append(pose)

            response = gaitResponse()
            response.success = True
        
        return response
    
    def sendFromQueue(self, event):
        print(event.current_expected)
        print(event.last_duration)
        if self.queue:
            self.pub2motorsMsg.pos_vector = self.queue.pop(0)
            self.pub2motors.publish(self.pub2motorsMsg)
            
if __name__ == '__main__':
    movement = Core()
    rospy.spin()