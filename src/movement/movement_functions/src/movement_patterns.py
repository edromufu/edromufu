#!/usr/bin/env python3
#coding=utf-8

import numpy as np
import copy

import sys, os
edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'movement/kinematic_functions/src')
from ik_numerical import InverseKinematics

sys.path.append(edrom_dir+'movement/humanoid_definition/src')
from setup_robot import Robot

def callIK(robot, newFootAbsPosition, newFootAbsPosture, currentFoot):
    robotIK = copy.deepcopy(robot)
        
    joint_angles = [0]*len(robot)
    try:
        joint_angles = InverseKinematics(newFootAbsPosition, newFootAbsPosture, currentFoot, robotIK)
    except Exception as e:
        print(e)

    return joint_angles

def Gait(robot, stepHeight, stepNumber, initialLeg=False):
    #leg == False (direita), leg == True (esquerda)
    #phase == True (subida), phase == False (descida)

    leg = initialLeg
    phase = True
    gait_poses = np.zeros((2*stepNumber,len(robot)))

    initial = []
    footInitialPosture = []
    for motor in robot:
        initial.append(motor.jointRotation)
        if 'FOOT' in motor.get_name():
            footInitialPosture.append(motor.absolutePosture)
    initial = np.array(initial)


    for step_phase in range(2*stepNumber):
        if leg:
            newFootAbsPosition = robot[-2].absolutePosition + np.array([[0, 0, phase*stepHeight]]).T
            currentFoot = -2
        else:
            newFootAbsPosition = robot[-1].absolutePosition + np.array([[0, 0, phase*stepHeight]]).T
            currentFoot = -1

        if phase:
            joint_angles = callIK(robot, newFootAbsPosition, footInitialPosture[int(not leg)], currentFoot)
        else:
            joint_angles = initial

        gait_poses[step_phase] = joint_angles
        
        if not phase:
            leg = not leg
        phase = not phase
    
    return gait_poses
    
if __name__ == '__main__':
    robotInstance = Robot('bioloid').robotJoints
    gait_poses = Gait(robotInstance, 0.05, 20)
    for count, pose in enumerate(gait_poses):
        print(f'{count}:\n {pose}\n')