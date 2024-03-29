#!/usr/bin/env python3
#coding=utf-8

import numpy as np

jointAxisPredef = {'UX':np.array([[1, 0, 0]]).T,
                   'UY':np.array([[0, 1, 0]]).T,
                   'UZ':np.array([[0, 0, 1]]).T
                  }

class Joint:

    def __init__(self, name, motor_id, sister, child, mother2SelfVec, jointAxis, jointRotation, is_inverted, is_knee):

        self.__name = name
        self.__sister = sister
        self.__child = child
        self.__mother2SelfVec = np.array([mother2SelfVec]).T
        self.__jointAxis = -jointAxisPredef[jointAxis] if is_inverted else jointAxisPredef[jointAxis]
        self.__motor_id = motor_id
        self.__is_knee = is_knee
        self.__mom = None

        self.jointRotation = jointRotation
        self.absolutePosition = None
        self.absolutePosture = None
    
    def get_name(self):
        return self.__name
    
    def get_sister(self):
        return self.__sister
    
    def get_child(self):
        return self.__child

    def get_mother2SelfVec(self):
        return self.__mother2SelfVec
    
    def get_jointAxis(self):
        return self.__jointAxis

    def get_mom(self):
        return self.__mom
    
    def get_id(self):
        return self.__motor_id
    
    def is_knee(self):
        return self.__is_knee
    
    def set_mom(self, mom):
        self.__mom = mom