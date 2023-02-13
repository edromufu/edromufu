#!/usr/bin/env python3
#coding=utf-8

import numpy as np

jointAxisPredef = {'x':np.array([[1, 0, 0]]).T,
                   'y':np.array([[0, 1, 0]]).T,
                   'z':np.array([[0, 0, 1]]).T
                  }

class Joint:

    def __init__(self, name, sister, child, mother2SelfVec, jointAxis, jointRotation=0):

        self.__name = name
        self.__sister = sister
        self.__child = child
        self.__mother2SelfVec = mother2SelfVec
        self.__jointAxis = jointAxisPredef[jointAxis]

        self.jointRotation = jointRotation
        self.absolutePostion = None
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
    
    def set_mom(self, mom):
        self.__mom = mom