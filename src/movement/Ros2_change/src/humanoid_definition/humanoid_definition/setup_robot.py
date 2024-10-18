#!/usr/bin/env python3
#coding=utf-8

import json, os, sys
import numpy as np

import sys, os

#Importação pelo sys
#edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'
#sys.path.append(edrom_dir+'movement/kinematic_functions')

from kinematic_functions.ik_numerical import ForwardKinematics #Importação por ros2 definida no package.xml

from .joint import Joint

class Robot:

    def __init__(self, robot):
        self.setupRobot(robot)
        self.findMother()

        self.robotJoints[0].absolutePosition = self.robotJoints[0].get_mother2SelfVec()
        self.robotJoints[0].absolutePosture = np.identity(3)

        ForwardKinematics(self.robotJoints)
        
        self.motorId2JsonIndex = {}
        self.mapMotorId2Json()
    
    def updateCOMPosturebyFoot(self):
        
        thetaCOM = round(-np.arcsin(-self.robotJoints[-1].absolutePosture[2][0]),3)
        
        self.robotJoints[0].absolutePosture = np.array([[np.cos(thetaCOM),0,np.sin(thetaCOM)],[0,1,0],[-np.sin(thetaCOM),0,np.cos(thetaCOM)]])
        ForwardKinematics(self.robotJoints)

        return thetaCOM

    def updateCOMPositionbyFoot(self):
        
        dzCOM = -self.robotJoints[-1].absolutePosition[2][0]

        self.robotJoints[0].absolutePosition = self.robotJoints[0].absolutePosition + np.array([[0.0,0.0,dzCOM]]).T
        ForwardKinematics(self.robotJoints)

        return dzCOM
    
    def mapMotorId2Json(self):
        for jsonIndex, joint in enumerate(self.robotJoints):
            motor_id = joint.get_id()
            if motor_id != -1:
                self.motorId2JsonIndex[motor_id] = jsonIndex
    
    def updateRobotModel(self, jointsRotation):
        for index, rotation in enumerate(jointsRotation):
            self.robotJoints[index].jointRotation = rotation

        ForwardKinematics(self.robotJoints)

        if self.robotJoints[-1].absolutePosition[2][0] > 0.02:
            print('Atualizando')
            pitch = self.updateCOMPosturebyFoot()
            
            dz = self.updateCOMPositionbyFoot()

            return dz, pitch

        return [None, None]
        
    def setupRobot(self, robot):
        self.loadJson(robot+'.json')
        
        self.robotJoints = []

        for joint_data in self.json_data['leg_joints']:
            is_inverted = False
            is_knee = False
            if joint_data['id'] in self.json_data['inverted_motors_id']:
                is_inverted = True
            
            if joint_data['id'] in self.json_data['knee_ids']:
                is_knee = True

            self.robotJoints.append(Joint(*joint_data.values(),is_inverted, is_knee))

    def loadJson(self, fileName):
        os.chdir('/home/'+os.getlogin()+'/edromufu/src/movement/humanoid_definition/robots_jsons/')

        with open(fileName) as f:
            self.json_data = json.loads(f.read())
    
    def findMother(self,j=0):
        if j != -1:
            if j == 0:
                self.robotJoints[j].set_mom(-1)
            
            if self.robotJoints[j].get_child() != -1:
                self.robotJoints[self.robotJoints[j].get_child()].set_mom(j)
                self.findMother(self.robotJoints[j].get_child())
            
            if self.robotJoints[j].get_sister() != -1:
                self.robotJoints[self.robotJoints[j].get_sister()].set_mom(self.robotJoints[j].get_mom())
                self.findMother(self.robotJoints[j].get_sister())