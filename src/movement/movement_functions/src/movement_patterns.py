#!/usr/bin/env python3
#coding=utf-8

import numpy as np
import copy

import sys, os
edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'


YCOM_FINAL = 0.05

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

def feetPosesCalculator(robot, supportFoot): #xcom, ycom, xswing, yswing, zswing, 

    absCOM = robot[0].absolutePosition

    ysignal = 1 if supportFoot == -2 else -1

    #! PARA TESTES
    # ---------------------------------
    ycom = np.linspace(0.0,ysignal*YCOM_FINAL,11)
    xcom = np.zeros(len(ycom))
    xswing=np.zeros(len(ycom))
    yswing=np.zeros(len(ycom))
    zswing=np.zeros(len(ycom))
    # ---------------------------------


    absCOMCalc = np.tile(absCOM, (1,len(xcom))).T
    xyzCOM = np.c_[xcom, ycom, absCOM[2]*np.ones(len(xcom))]
    xyzSwing = np.c_[xswing, yswing, zswing]

    if 'L' in robot[supportFoot].get_name():
        leftFootPoses = absCOMCalc - xyzCOM
    else:
        leftFootPoses = absCOMCalc - xyzCOM + xyzSwing
    
    if 'R' in robot[supportFoot].get_name():
        rightFootPoses = absCOMCalc - xyzCOM
    else:
        rightFootPoses = absCOMCalc - xyzCOM + xyzSwing

    return leftFootPoses, rightFootPoses

def callbalance(robot, leftFootPoses, rightFootPoses):

    balance_poses = np.zeros((len(leftFootPoses),len(robot)))

    initial = []
    footInitialPosture = []
    for motor in robot:
        
        if 'FOOT' in motor.get_name():
            initial.append(motor.absolutePosition)
            footInitialPosture.append(motor.absolutePosture)
    initial = np.array(initial)

    for phase in range(len(leftFootPoses)):

        leftFootAbsPosition = initial[0] + np.array([leftFootPoses[phase]]).T
        currentFoot = -2
        left_joint_angles = callIK(robot, leftFootAbsPosition, footInitialPosture[0], currentFoot)
        left_joint_angles = left_joint_angles[7:13]

        rightFootAbsPosition = initial[1] + np.array([rightFootPoses[phase]]).T
        currentFoot = -1
        right_joint_angles = callIK(robot, rightFootAbsPosition, footInitialPosture[1], currentFoot)
        right_joint_angles = right_joint_angles[1:7]

        balance_poses[phase][1:7] = right_joint_angles
        balance_poses[phase][7:13] = left_joint_angles

    return balance_poses


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