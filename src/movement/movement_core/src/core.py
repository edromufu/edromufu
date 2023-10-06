#!/usr/bin/env python3
#coding=utf=8

import rospy
import numpy as np

import sys, os
edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'movement/humanoid_definition/src')
from setup_robot import Robot

sys.path.append(edrom_dir+'movement/movement_functions/src')
from movement_patterns import * 

sys.path.append(edrom_dir+'movement/movement_pages/src')
from page_runner import Page

from movement_utils.srv import *
from movement_utils.msg import *
from sensor_msgs.msg import JointState

QUEUE_TIME = rospy.get_param('/movement_core/queue_time') #Em segundos
PUB2VIS = rospy.get_param('/movement_core/pub2vis')

class Core:
    def __init__(self): 
        
        # Inicialização das variáveis do ROS
        rospy.init_node('movement_central')
        
        # Inicialização das variáveis do ROS para u2d2
        rospy.wait_for_service('u2d2_comm/feedbackBody')
        rospy.wait_for_service('u2d2_comm/enableTorque')
    
        #Estruturas para comunicação com U2D2
        self.motorsFeedback = rospy.ServiceProxy('u2d2_comm/feedbackBody', body_feedback)
        self.motorsTorque = rospy.ServiceProxy('u2d2_comm/enableTorque', enable_torque)
        self.pub2motors = rospy.Publisher('u2d2_comm/data2body', body_motors_data, queue_size=100)
        self.pub2motorsMsg = body_motors_data()

        #Inicialização do torque
        self.motorsTorque(True, [-1])

        self.queue = []

        #Services de requisição de movimento, todos possuem como callback movementManager
        rospy.Service('movement_central/request_gait', gait, self.movementManager)
        rospy.Service('movement_central/request_page', page, self.movementManager)
        rospy.Service('movement_central/request_walk', walk_forward, self.movementManager)

        #Inicialização do objeto (modelo) da robô em código
        robot_name = rospy.get_param('/movement_core/name')

        self.robotInstance = Robot(robot_name)
        self.robotModel = self.robotInstance.robotJoints
        self.motorId2JsonIndex = self.robotInstance.motorId2JsonIndex
        self.motorsCurrentPosition = [0]*18
        
        #Timer para fila de publicações
        rospy.Timer(rospy.Duration(QUEUE_TIME), self.sendFromQueue)
        
        # Definições para visualizador
        if PUB2VIS:
            self.queuevis = []
            self.pub2vis = rospy.Publisher('/joint_states', JointState, queue_size=100)
            self.pub2vismsg = JointState()
            self.pub2vismsg.name = ['COM_height_slider','COM_pitch_joint','RHIP_UZ_joint','RHIP_UX_joint','RHIP_UY_joint','RKNEE_joint',
            'RANKLE_UY_joint','RANKLE_UX_joint','LHIP_UZ_joint','LHIP_UX_joint','LHIP_UY_joint',
            'LKNEE_joint','LANKLE_UY_joint','LANKLE_UX_joint']

            self.currentCOMPitch = 0.0
            self.currentCOMHeight = 0.0

    def callRobotModelUpdate(self, position2update):
        self.motorsCurrentPosition = position2update
        
        sorted2update = self.sortMotorReturn2JsonIndex(position2update)

        dz, pitch = self.robotInstance.updateRobotModel(sorted2update)

        if dz is not None and dz is not None and PUB2VIS:
            self.currentCOMHeight = dz
            self.currentCOMPitch = pitch

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
        
        return sorted2MotorsId

    def keyFromValue(self, dict, value):
        for key, v in dict.items():
            if v == value:
                return key
        return None

    def movementManager(self, req):
        self.motorsTorque(True, [-1])

        if 'gait' in str(req.__class__):

            checked_poses = np.array([self.motorsCurrentPosition])
            gait_poses = Gait(self.robotModel, req.step_height, req.steps_number)
            
            for index, pose in enumerate(gait_poses):
                pose = self.sortJsonIndex2MotorInput(pose)
                checked_poses = np.append(checked_poses, [pose], axis=0)  

            for pose in checked_poses: 
                self.queue.append(pose)

            self.callRobotModelUpdate(checked_poses[-1])

            if PUB2VIS:
                for pose in gait_poses:
                    self.queuevis.append(pose[1:-2])

            response = gaitResponse()
            response.success = True
        
        elif 'page' in str(req.__class__):
            page_poses = Page(req.page_name, QUEUE_TIME)
            
            for pose in page_poses: 
                self.queue.append(pose)
            

            self.callRobotModelUpdate(page_poses[-1])

            if PUB2VIS:
                for pose in page_poses:
                    pose = self.sortMotorReturn2JsonIndex(pose)

                    self.queuevis.append(pose[1:-2])

            response = pageResponse()
            response.success = True
        
        elif 'walk_forward' in str(req.__class__):
            
            checked_poses = np.array([self.motorsCurrentPosition])
    
            supFoot = req.support_foot
            for n in range(req.steps_number): 
                if n:
                    walk_poses = np.vstack((walk_poses,callWalk(self.robotModel,supFoot,QUEUE_TIME)))
                else:
                    walk_poses = callWalk(self.robotModel,supFoot,QUEUE_TIME)
                self.robotInstance.updateRobotModel(walk_poses[-1])
                
                supFoot *= -1
        
            for index, pose in enumerate(walk_poses):
                pose = self.sortJsonIndex2MotorInput(pose)
                checked_poses = np.append(checked_poses, [pose], axis=0)  

            for pose in checked_poses: 
                self.queue.append(pose)
            
            self.callRobotModelUpdate(checked_poses[-1])
            
            if PUB2VIS:
                for pose in walk_poses:
                    self.queuevis.append(pose[1:-2])

            response = walk_forwardResponse()
            response.success = True

        return response
    
    def sendFromQueue(self, event):
        
        if self.queue:
            self.pub2motorsMsg.pos_vector = self.queue.pop(0)
            self.pub2motors.publish(self.pub2motorsMsg)

        if PUB2VIS:
            if self.queuevis:
                self.pub2vismsg.position = np.concatenate((np.array([self.currentCOMHeight, self.currentCOMPitch]),self.queuevis.pop(0)))
                self.pub2vismsg.header.stamp = rospy.Time.now()
                self.pub2vis.publish(self.pub2vismsg)

if __name__ == '__main__':
    np.set_printoptions(precision=3, suppress=True, linewidth=np.inf, threshold=sys.maxsize)
    movement = Core()
    rospy.spin()