#!/usr/bin/env python3
#coding=utf-8

from joint import Joint

class Robot:

    def __init__(self, robot):
        self.setupRobot(robot)
        
    def setupRobot(self, robot):
        # Lê json e configura lista na qual cada elemento é uma joint
        self.robotJoints = None
    
    def findMother(self,j=0):
        if j != -1:
            if j == 0:
                self.robotJoints[j].set_mom(-1)
            
            if self.robotJoints[j].get_child() != -1:
                self.robotJoints[self.robotJoints[j].get_child()].set_mom(j)
                findMother(self.robotJoints[j].get_child())
            
            if self.robotJoints[j].get_sister() != -1:
                self.robotJoints[self.robotJoints[j].get_sister()].set_mom(self.robotJoints[j].get_mom())
                findMother(self.robotJoints[j].get_sister())