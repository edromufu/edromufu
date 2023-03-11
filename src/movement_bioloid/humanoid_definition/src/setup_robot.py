#!/usr/bin/env python3
#coding=utf-8

import json, os
import numpy as np

from joint import Joint

class Robot:

    def __init__(self, robot):
        self.setupRobot(robot)
        self.findMother()

        self.robotJoints[0].absolutePostion = self.robotJoints[0].get_mother2SelfVec()
        self.robotJoints[0].absolutePosture = np.identity(3)
        
    def setupRobot(self, robot):
        self.loadJson(robot+'.json')
        
        self.robotJoints = []

        for joint_data in self.json_data['leg_joints']:
            self.robotJoints.append(Joint(*joint_data.values()))
        
    def loadJson(self, fileName):
        os.chdir(os.path.dirname(__file__))
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
    
if __name__ == '__main__':

    nova = Robot('nova')