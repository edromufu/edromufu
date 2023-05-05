#!/usr/bin/env python3
#coding=utf=8

import rospy
import numpy as np

import sys, os
edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'movement_bioloid/humanoid_definition/src')
from setup_robot import Robot

sys.path.append(edrom_dir+'movement_bioloid/movement_functions/src')
from movement_patterns import Gait

from movement_utils.srv import *
from movement_utils.msg import *

QUEUE_TIME = 0.5 #Em segundos

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

            self.interpolation(gait_poses, 1.5)

            response = gaitResponse()
            response.success = True
        
        return response
    
    def sendFromQueue(self, event):

        if self.queue:
            self.pub2motorsMsg.pos_vector = self.queue.pop(0)
            self.pub2motors.publish(self.pub2motorsMsg)
     
    def interpolation(self, matrixToInterpol, stepDuration):
        '''
        newPosesNumber = int(stepDuration/QUEUE_TIME)

        t = np.linspace(0,stepDuration,newPosesNumber)
        interpolFunc = (1-np.cos(t*np.pi/stepDuration))/2

        #?motorsCurrentPosition = self.motorsFeedback(True).pos_vector
        motorsCurrentPosition = [0]*20

        (n,_) = matrixToInterpol.shape
        jointsInterpolation = np.zeros((n*newPosesNumber,20))

        for index, pose in enumerate(matrixToInterpol):
            for motor_id, motorRotation in enumerate(pose):
                if index == 0:
                    initialPosition = motorsCurrentPosition[motor_id]
                else:
                    initialPosition = matrixToInterpol[index-1][motor_id]
                finalPosition = motorRotation
                
                motorInterpol = initialPosition + (finalPosition - initialPosition)*interpolFunc
                for i in range(newPosesNumber):
                    jointsInterpolation[i+index][motor_id] = motorInterpol[i]    

        print(jointsInterpolation)
        '''
        #!! Criar interpolação, toda a matriz interpolada deve estar pronta antes de começar a ser colocada na fila.

if __name__ == '__main__':
    movement = Core()
    rospy.spin()