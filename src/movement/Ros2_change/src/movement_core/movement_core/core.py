#!/usr/bin/env python3
#coding=utf=8

#ADENDO MANGA: TESTE PARA SABER SE VAI DAR MERDA. kk

import rclpy
import numpy as np
import sys

#Importação pelo sys
#import os
#edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'
#sys.path.append(edrom_dir+'movement/humanoid_definition/src')
#sys.path.append(edrom_dir+'movement/movement_functions/src')
#sys.path.append(edrom_dir+'movement/movement_pages/src')

from humanoid_definition.setup_robot import Robot


from movement_functions.gait_gen import Gait
from movement_functions.walk_forward_gen import callWalk
from movement_functions.rotate_cc_ccw_gen import callRotate


from movement_pages.page_runner import Page

from movement_utils.srv import *
from movement_utils.msg import *
from sensor_msgs.msg import JointState

#QUEUE_TIME = rospy.get_param('/movement_core/queue_time') #Em segundos (11)
#PUB2VIS = rospy.get_param('/movement_core/pub2vis')    (12)



class Core: 
    def __init__(self): 
        
        # Inicialização das variáveis do ROS
        #rospy.init_node('movement_central')        (5)

        rclpy.init(args=sys.argv)                   #(5)
        self.node = rclpy.create_node('movement_central')

        self.QUEUE_TIME = self.node.declare_parameter('/movement_core/queue_time').get_parameter_value().double_value #Em segundos #(11)
        self.PUB2VIS =self.node.declare_parameter('/movement_core/pub2vis').get_parameter_value().bool_value   #(12)
        

        # Inicialização das variáveis do ROS para u2d2
        #rospy.wait_for_service('u2d2_comm/feedbackBody') (1)
        #rospy.wait_for_service('u2d2_comm/enableTorque') (2)

        while not self.motorsFeedback.wait_for_service(timeout_sec=1.0):    #(1)
            self.node.get_logger().info('service not available, waiting again...')

        while not self.motorsTorque.wait_for_service(timeout_sec=1.0):      #(2)
            self.node.get_logger().info('service not available, waiting again...')

    
        #Estruturas para comunicação com U2D2

        #self.motorsFeedback = rospy.ServiceProxy('u2d2_comm/feedbackBody', body_feedback)      (3)
        #self.motorsTorque = rospy.ServiceProxy('u2d2_comm/enableTorque', enable_torque)        (4)

        #self.pub2motors = rospy.Publisher('u2d2_comm/data2body', BodyMotorsData, queue_size=100)  (10)
        self.pub2motors = self.node.create_subscription(BodyMotorsData, 'u2d2_comm/data2body', queue_size=100)  #(10)
        self.pub2motorsMsg = BodyMotorsData()

        
        self.motorsFeedback = self.create_client(BodyFeedback, 'u2d2_comm/feedbackBody')       #(3)
        self.motorsTorque = self.create_client(EnableTorque, 'u2d2_comm/enableTorque')         #(4)

        #Inicialização do torque
        resp = self.motorsTorque.call_async(True, [-1])
        rclpy.spin_until_future_complete(self.node, resp)

        self.queue = []

        #Services de requisição de movimento, todos possuem como callback movementManager
        #node.Service('movement_central/request_gait', Gait, self.movementManager) (6)
        #rospy.Service('movement_central/request_page', Page, self.movementManager) (7)
        #rospy.Service('movement_central/request_walk', WalkForward, self.movementManager) (8)
        #rospy.Service('movement_central/request_rotation', rotate, self.movementManager)   (9)

        self.node.create_service(Gait, 'movement_central/request_gait', self.movementManager)    #(6)
        self.node.create_service(Page, 'movement_central/request_page', self.movementManager)    #(7)
        self.node.create_service(WalkForward, 'movement_central/request_walk', self.movementManager) #(8)
        #self.node.create_service('movement_central/request_rotation', rotate, self.movementManager)    #(9)

        #Inicialização do objeto (modelo) da robô em código
        #robot_name = rospy.get_param('/movement_core/name') (14)
        robot_name =self.node.declare_parameter('/movement_core/name').get_parameter_value().string_value   #(14)

        self.robotInstance = Robot(robot_name)
        self.robotModel = self.robotInstance.robotJoints
        self.motorId2JsonIndex = self.robotInstance.motorId2JsonIndex
        self.motorsCurrentPosition = [0]*18
        
        #Timer para fila de publicações
        #rospy.Timer(rospy.Duration(self.QUEUE_TIME), self.sendFromQueue) (20)
        self.timer = self.node.create_timer(self.QUEUE_TIME, self.sendFromQueue) #(20)
        
        # Definições para visualizador
        if self.PUB2VIS:
            self.queuevis = []
            #self.pub2vis = rospy.Publisher('/joint_states', JointState, queue_size=100)    (15)
            self.pub2vis = self.node.create_subscription(JointState, '/joint_states', queue_size=100)#(15)
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

        if dz is not None and dz is not None and self.PUB2VIS:
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

    def movementManager(self, req,response):    #(16)(17)(18)(19)
        self.motorsTorque(True, [-1])

        if 'Gait' in str(req.__class__):

            checked_poses = np.array([self.motorsCurrentPosition])
            gait_poses = Gait(self.robotModel, req.step_height, req.steps_number)
            
            for index, pose in enumerate(gait_poses):
                pose = self.sortJsonIndex2MotorInput(pose)
                checked_poses = np.append(checked_poses, [pose], axis=0)  

            for pose in checked_poses: 
                self.queue.append(pose)

            self.callRobotModelUpdate(checked_poses[-1])

            if self.PUB2VIS:
                for pose in gait_poses:
                    self.queuevis.append(pose[1:-2])

            #response = gaitResponse() (16) Response virou argumento da função
            response.success = True
        
        elif 'Page' in str(req.__class__):
            page_poses = Page(req.page_name, self.QUEUE_TIME)
            
            for pose in page_poses: 
                self.queue.append(pose)
            

            self.callRobotModelUpdate(page_poses[-1])

            if self.PUB2VIS:
                for pose in page_poses:
                    pose = self.sortMotorReturn2JsonIndex(pose)

                    self.queuevis.append(pose[1:-2])

            #response = pageResponse() (17) Response virou argumento da função
            response.success = True
        
        elif 'WalkForward' in str(req.__class__):
            
            checked_poses = np.array([self.motorsCurrentPosition])
    
            supFoot = req.support_foot
            for n in range(req.steps_number): 
                if n:
                    walk_poses = np.vstack((walk_poses,callWalk(self.robotModel,supFoot,self.QUEUE_TIME)))
                else:
                    walk_poses = callWalk(self.robotModel,supFoot,self.QUEUE_TIME)
                self.robotInstance.updateRobotModel(walk_poses[-1])
                
                supFoot *= -1
        
            for index, pose in enumerate(walk_poses):
                pose = self.sortJsonIndex2MotorInput(pose)
                checked_poses = np.append(checked_poses, [pose], axis=0)  

            for pose in checked_poses: 
                self.queue.append(pose)
            
            self.callRobotModelUpdate(checked_poses[-1])
            
            if self.PUB2VIS:
                for pose in walk_poses:
                    self.queuevis.append(pose[1:-2])

            #response = walk_forwardResponse() (18) Response virou argumento da função
            response.success = True

        elif 'rotate' in str(req.__class__):
            
            checked_poses = np.array([self.motorsCurrentPosition])

            phase = -1
            for n in range(req.steps_number): 
                if n:
                    rotate_poses = np.vstack((rotate_poses,callRotate(self.robotModel, req.direction, phase, self.QUEUE_TIME)))
                else:
                    rotate_poses = callRotate(self.robotModel, req.direction, phase, self.QUEUE_TIME)

                if phase == 1:
                    self.robotInstance.updateRobotModel(rotate_poses[0])
                    rotate_poses = np.vstack((rotate_poses,rotate_poses[0]))
                else:
                    self.robotInstance.updateRobotModel(rotate_poses[-1])
                    
                phase *= -1

            for index, pose in enumerate(rotate_poses):
                pose = self.sortJsonIndex2MotorInput(pose)
                checked_poses = np.append(checked_poses, [pose], axis=0)  

            for pose in checked_poses: 
                self.queue.append(pose)
            
            self.callRobotModelUpdate(checked_poses[-1])
            
            if self.PUB2VIS:
                for pose in rotate_poses:
                    self.queuevis.append(pose[1:-2])

            #response = rotateResponse() (19) Response virou argumento da função
            response.success = True

        return response
    
    def sendFromQueue(self, event):
        
        if self.queue:
            self.pub2motorsMsg.pos_vector = self.queue.pop(0)
            self.pub2motors.publish(self.pub2motorsMsg)

        if self.PUB2VIS:
            if self.queuevis:
                self.pub2vismsg.position = np.concatenate((np.array([self.currentCOMHeight, self.currentCOMPitch]),self.queuevis.pop(0)))
                #self.pub2vismsg.header.stamp = rospy.Time.now() (21)
                self.pub2vismsg.header.stamp = self.node.get_clock().now()  #(21)
                
                self.pub2vis.publish(self.pub2vismsg)

if __name__ == '__main__':
    np.set_printoptions(precision=4, suppress=True, linewidth=np.inf, threshold=sys.maxsize)
    movement = Core()
    #rospy.spin() (13)
    rclpy.spin(movement.node)   #(13)