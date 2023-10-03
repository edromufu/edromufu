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

#? Parâmetros da caminhada
zSwingHeight = 0.02 #m 
stepTime = 0.5 #s

def callIK(robot, newFootAbsPosition, newFootAbsPosture, currentFoot):
    robotIK = copy.deepcopy(robot)
        
    joint_angles = [0]*len(robot)
    try:
        joint_angles = InverseKinematics(newFootAbsPosition, newFootAbsPosture, currentFoot, robotIK)
    except Exception as e:
        print('Erro na callIK da movement_patterns',e)

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

def callWalk(robot, stepX, supFoot, queueTime):
    # SupportFoot = 1 p/ direita; SupportFoot = -1 p/ esquerda;

    leftFootPos = robot[-2].absolutePosition
    rightFootPos = robot[-1].absolutePosition

    leftFootPosture = robot[-2].absolutePosture
    rightFootPosture = robot[-1].absolutePosture

    newLeftPos, newRightPos = genNewFootPositions(stepX, leftFootPos, rightFootPos, supFoot)

    zSwing = genSwingFootZTrajectory(stepTime, queueTime)
    xSwing = np.zeros(len(zSwing))
    ySwing = np.zeros(len(zSwing))
    swingFoot = np.c_[xSwing,ySwing,zSwing]

    xLeft = np.linspace(leftFootPos[0],newLeftPos[0],len(zSwing))
    yLeft = np.linspace(leftFootPos[1],newLeftPos[1],len(zSwing))
    zLeft = np.linspace(leftFootPos[2],newLeftPos[2],len(zSwing))
    leftFoot = np.c_[xLeft,yLeft,zLeft]

    xRight = np.linspace(rightFootPos[0],newRightPos[0],len(zSwing))
    yRight = np.linspace(rightFootPos[1],newRightPos[1],len(zSwing))
    zRight = np.linspace(rightFootPos[2],newRightPos[2],len(zSwing))
    rightFoot = np.c_[xRight,yRight,zRight]

    swing_poses = np.zeros((len(swingFoot),len(robot)))

    for i in range(len(swingFoot)):
        currentSwing = np.array([swingFoot[i]]).T
        currentLeft = np.array([leftFoot[i]]).T
        currentRight = np.array([rightFoot[i]]).T

        leftFootAbsPosition = currentLeft+currentSwing if supFoot == 1 else currentLeft
        rightFootAbsPosition = currentRight+currentSwing if supFoot == -1 else currentRight

        currentFoot = -2
        left_joint_angles = callIK(robot, leftFootAbsPosition, leftFootPosture, currentFoot)
        left_joint_angles = left_joint_angles[7:13]

        currentFoot = -1
        right_joint_angles = callIK(robot, rightFootAbsPosition, rightFootPosture, currentFoot)
        right_joint_angles = right_joint_angles[1:7]

        swing_poses[i][1:7] = right_joint_angles
        swing_poses[i][7:13] = left_joint_angles

    return swing_poses

    #genCOMTrajectory()

def genSwingFootZTrajectory(stepTime, queueTime):
    t = np.linspace(0.0,stepTime,np.ceil(stepTime/queueTime))

    return zSwingHeight*np.sin(np.pi*t/stepTime)

def genNewFootPositions(stepX, leftFootAbsPos, rightFootAbsPos, supportFoot):
    # SupportFoot = 1 p/ direita; SupportFoot = -1 p/ esquerda;

    xLeftAbsPos = leftFootAbsPos[0]
    xRightAbsPos = rightFootAbsPos[0]
    
    if abs(xLeftAbsPos-xRightAbsPos) < stepX/2:
        addInX = stepX/2
    else:
        addInX = stepX

    newRightX = rightFootAbsPos + np.array([[-supportFoot*addInX, 0,0]]).T
    newLeftX = leftFootAbsPos + np.array([[supportFoot*addInX, 0,0]]).T

    return newLeftX, newRightX 

def backup():
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