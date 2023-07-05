#!/usr/bin/env python3
#coding=utf=8

import rospy, timeit
import numpy as np

import sys, os
edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'movement_bioloid/humanoid_definition/src')
from setup_robot import Robot

sys.path.append(edrom_dir+'movement_bioloid/movement_functions/src')
from movement_patterns import Gait

from movement_utils.srv import *
from movement_utils.msg import *

QUEUE_TIME = 0.2 #Em segundos

class Core:
    def __init__(self): 
        #Inicialização do objeto (modelo) da robô em código
        robot_name = rospy.get_param('/movement_core/name')
        
        self.robotInstance = Robot(robot_name)
        self.robotModel = self.robotInstance.robotJoints
        self.motorId2JsonIndex = self.robotInstance.motorId2JsonIndex
        
        # Inicialização das variáveis do ROS
        rospy.init_node('movement_central')

        #Services de requisição de movimento, todos possuem como callback movementManager
        rospy.Service('movement_central/request_gait', gait, self.movementManager)
        
        #Estruturas para comunicação com U2D2
        self.motorsFeedback = rospy.ServiceProxy('u2d2_comm/feedbackMotors', position_feedback)
        rospy.wait_for_service('u2d2_comm/feedbackMotors')
        self.pub2motors = rospy.Publisher('u2d2_comm/data2body', body_motors_data, queue_size=100)
        self.pub2motorsMsg = body_motors_data()

        #Timer para fila de publicações
        rospy.Timer(rospy.Duration(QUEUE_TIME), self.sendFromQueue)
        self.queue = []  
        self.queue.append(np.array([0]*10 + [-0.65, 0.65, 0.84, 0.84, -0.3, -0.3] + [0]*2))

    def callRobotModelUpdate(self):
        self.motorsCurrentPosition = list(self.motorsFeedback(True).pos_vector)

        positions2Update = self.motorsCurrentPosition
        
        positions2Update = self.sortMotorReturn2JsonIndex(positions2Update)

        positions2Update  = self.invertMotorsPosition(positions2Update)

        self.robotInstance.updateRobotModel(positions2Update)

    def sortMotorReturn2JsonIndex(self, toSort):

        sorted2JsonIndexPositions = [0]*len(self.robotModel)
        for motor_id, motor_position in enumerate(toSort):
            if motor_id in self.motorId2JsonIndex.keys():
                jsonIndex = self.motorId2JsonIndex[motor_id]
                sorted2JsonIndexPositions[jsonIndex] = motor_position
        
        return sorted2JsonIndexPositions
    
    def sortJsonIndex2MotorInput(self, toSort):
        
        sorted2MotorsId = self.motorsCurrentPosition

        for json_id, position in enumerate(toSort):
            if json_id in self.motorId2JsonIndex.values():
                motor_id = self.keyFromValue(self.motorId2JsonIndex, json_id)
                sorted2MotorsId[motor_id] = position
        
        return sorted2MotorsId[:-2]

    def keyFromValue(self, dict, value):
        for key, v in dict.items():
            if v == value:
                return key
        return None
    
    def invertMotorsPosition(self, toInvert):
        for jsonIndex, joint in enumerate(self.robotModel):
            if joint.is_inverted():
                toInvert[jsonIndex] *= -1
        
        return toInvert

    def movementManager(self, req):
        
        self.callRobotModelUpdate()
        if 'gait' in str(req.__class__):

            gait_poses = Gait(self.robotModel, req.step_height, req.steps_number)
            new_poses = []

            for index, pose in enumerate(gait_poses):
                pose = self.invertMotorsPosition(pose)
                pose = self.sortJsonIndex2MotorInput(pose)
                new_poses.append(pose)            

            for pose in new_poses:
                self.queue.append(pose)

            response = gaitResponse()
            response.success = True
        
        return response
    
    def sendFromQueue(self, event):

        if self.queue:
            self.pub2motorsMsg.pos_vector = self.queue.pop(0)
            self.pub2motors.publish(self.pub2motorsMsg)
     
    def interpolation(self, matrixToInterpol, changingPosesTime):
        newPosesNumber = round(changingPosesTime/QUEUE_TIME)

        motorsCurrentPosition = self.motorsFeedback(True).pos_vector

        t = np.linspace(0,changingPosesTime-QUEUE_TIME,newPosesNumber)
        interpolFunc = (1-np.cos(t*np.pi/changingPosesTime))/2

        [m,n] = matrixToInterpol.shape
        jointsInterpolation = np.zeros((20,m*newPosesNumber))

        for i in range(m):
            for motor_id in range(n):
                if i == 0:
                    initialPosition = motorsCurrentPosition[motor_id]
                else:
                    initialPosition = matrixToInterpol[i-1][motor_id]
                finalPosition = matrixToInterpol[i][motor_id]

                motorInterpol = initialPosition + (finalPosition - initialPosition)*interpolFunc
                
                jointsInterpolation[motor_id][i*newPosesNumber:i*newPosesNumber+len(motorInterpol)] = motorInterpol

        jointsInterpolation = np.vstack([jointsInterpolation.T,matrixToInterpol[-1][:]])
        
        for position in jointsInterpolation:
            self.queue.append(position)

if __name__ == '__main__':
    np.set_printoptions(precision=3, suppress=True, linewidth=np.inf, threshold=sys.maxsize)
    movement = Core()
    rospy.spin()