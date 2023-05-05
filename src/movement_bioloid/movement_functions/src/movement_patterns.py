#!/usr/bin/env python3
#coding=utf-8

import numpy as np
import copy

import sys, os
edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'movement_bioloid/kinematic_functions/src')
from ik_numerical import InverseKinematics

sys.path.append(edrom_dir+'movement_bioloid/humanoid_definition/src')
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
    gait_poses = np.zeros((2*stepNumber,20))

    #? Descomentar quando bioloid.json tiver representação dos braços e cabeças
    #for joint in robot:
    #    current_position = joint.jointRotation * np.ones((1,2*stepNumber))
    #    gait_poses[:,joint.get_id()] = current_position

    for step_phase in range(2*stepNumber):
        if leg:
            newFootAbsPosition = robot[-2].absolutePosition + np.array([[0, 0, phase*stepHeight]]).T
            currentFoot = -2
        else:
            newFootAbsPosition = robot[-1].absolutePosition + np.array([[0, 0, phase*stepHeight]]).T
            currentFoot = -1

        joint_angles = callIK(robot, newFootAbsPosition, np.identity(3), currentFoot)
        joint_angles = joint_angles[1:-2]

        for index in range(20):
            for indexInRobotJoints, motor in enumerate(robot):
                if index == motor.get_id():
                    gait_poses[step_phase][index] = joint_angles[indexInRobotJoints-1]
        
        if not phase:
            leg = not leg
        phase = not phase

    return gait_poses
    
if __name__ == '__main__':
    robotInstance = Robot('bioloid').robotJoints
    gait_poses = Gait(robotInstance, 0.05, 20)
    for count, pose in enumerate(gait_poses):
        print(f'{count}:\n {pose}\n')