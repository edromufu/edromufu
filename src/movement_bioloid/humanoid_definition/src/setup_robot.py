#!/usr/bin/env python3
#coding=utf-8

import json, os
import numpy as np


from joint import Joint

###!!! Retirar esses imports do código final
import sys
os.chdir(os.path.dirname(__file__))
os.chdir("../../kinematic_functions/src")
sys.path.append(os.getcwd())
from direct_kinematics import ForwardKinematics
from ik_numerical import InverseKinematics
os.chdir('../../humanoid_definition/src')

import copy
###!!!

class Robot:

    def __init__(self, robot):
        self.setupRobot(robot)
        self.findMother()

        self.robotJoints[0].absolutePosition = self.robotJoints[0].get_mother2SelfVec()
        self.robotJoints[0].absolutePosture = np.identity(3)

        ForwardKinematics(self.robotJoints)
        
    def setupRobot(self, robot):
        self.loadJson(robot+'.json')
        
        self.robotJoints = []

        for joint_data in self.json_data['leg_joints']:
            is_inverted = False
            if joint_data['id'] in self.json_data['inverted_motors_id']:
                is_inverted = True

            self.robotJoints.append(Joint(*joint_data.values(),is_inverted))

    def loadJson(self, fileName):
        os.chdir("../robots_jsons")

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
    
###!!! Retirar essa função do código final
    def IK(self):
        
        newFootPos = self.robotJoints[13].absolutePosition + np.array([[0.18, 0, 0.05]]).T
        currentFoot = 13

        robotIK = copy.deepcopy(self.robotJoints)
        
        q = [0]*len(self.robotJoints)
        try:
            q = InverseKinematics(newFootPos, np.identity(3), 13, robotIK)
        except Exception as e:
            print(e)

        for index, motor in enumerate(self.robotJoints):
            motor.jointRotation = q[index] 
        
        ForwardKinematics(self.robotJoints)

if __name__ == '__main__':
    robotInstance = Robot('bioloid')
    robotInstance.IK()