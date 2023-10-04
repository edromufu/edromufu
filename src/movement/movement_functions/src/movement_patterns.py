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
zSwingHeight = 0.04 #Altura do pé de balanço (m )
stepTime = 5 #Tempo para "um" passo (s)
doubleSupProportion = 0.2 # Proporção do tempo de um passo em suporte duplo (adim)
stepX = 0.04 #Tamanho de um passo em x (m)
g = 9.8 #Gravidade (m/s²)
zCOM = 0.28 #Altura do centro de massa (m)

def callIK(robot, newFootAbsPosition, newFootAbsPosture, currentFoot):
    robotIK = copy.deepcopy(robot)
        
    joint_angles = [0]*len(robot)
    try:
        joint_angles = InverseKinematics(newFootAbsPosition, newFootAbsPosture, currentFoot, robotIK)
    except Exception as e:
        print('Erro na callIK da movement_patterns',e)

    return joint_angles

def feetPosesCalculator(robot, stepTime, queueTime, supportFoot, xcom, ycom, xswing, zswing):

    absCOM = robot[0].absolutePosition

    absCOMCalc = np.tile(absCOM, (1,len(xcom))).T

    xyzCOM = np.c_[xcom, ycom, absCOM[2]*np.ones(len(xcom))]
    xyzSwing = np.c_[np.linspace(0.0,xswing,np.ceil(stepTime/queueTime)), np.zeros(len(zswing)), zswing]

    if supportFoot == -1:
        leftFootPoses = absCOMCalc - xyzCOM
    else:
        leftFootPoses = xyzSwing
    
    if supportFoot == 1:
        rightFootPoses = absCOMCalc - xyzCOM
    else:
        rightFootPoses = xyzSwing

    return leftFootPoses, rightFootPoses

def callWalk(robot, supFoot, queueTime):
    # SupportFoot = 1 p/ direita; SupportFoot = -1 p/ esquerda;

    leftFootPos = robot[-2].absolutePosition
    rightFootPos = robot[-1].absolutePosition

    leftFootPosture = robot[-2].absolutePosture
    rightFootPosture = robot[-1].absolutePosture

    supFootPos = rightFootPos if supFoot == 1 else leftFootPos

    newSwingFootPos, newTorsoPos, currentStep = genSwingFootAndTorsoNextPositions(stepX, leftFootPos, rightFootPos, supFoot)
    xZMP, yZMP, m1x, m2x, m1y, m2y = genZMPTrajectory(queueTime, stepTime, doubleSupProportion, supFootPos, newTorsoPos)
    zSwing = genSwingFootZTrajectory(queueTime, stepTime, doubleSupProportion)
    
    xCOM, yCOM = genCOMTrajectory(queueTime, stepTime, doubleSupProportion, xZMP, yZMP, m1x, m2x, m1y, m2y)

    leftFootPoses, rightFootPoses = feetPosesCalculator(robot, stepTime, queueTime, supFoot, xCOM, yCOM, currentStep, zSwing)
    
    walk_poses = np.zeros((len(leftFootPoses),len(robot)))

    for i in range(len(leftFootPoses)):
        leftFootAbsPosition = leftFootPos+np.array([leftFootPoses[i]]).T
        rightFootAbsPosition = rightFootPos+np.array([rightFootPoses[i]]).T

        currentFoot = -2
        left_joint_angles = callIK(robot, leftFootAbsPosition, leftFootPosture, currentFoot)
        left_joint_angles = left_joint_angles[7:13]

        currentFoot = -1
        right_joint_angles = callIK(robot, rightFootAbsPosition, rightFootPosture, currentFoot)
        right_joint_angles = right_joint_angles[1:7]

        walk_poses[i][1:7] = right_joint_angles
        walk_poses[i][7:13] = left_joint_angles
    
    return walk_poses

def genZMPTrajectory(queueTime, stepTime, doubleSupProportion, supFootPos, torsoPos):
     #! to achando que ta mandando torsoPos errado
    
    t = np.linspace(0.0,stepTime,np.ceil(stepTime/queueTime))
    td = stepTime*doubleSupProportion

    mask1 = t < td
    mask2 = (t >= td) & (t < (stepTime - td))
    mask3 = t >= (stepTime - td)

    xSupFoot = supFootPos[0]
    ySupFoot = supFootPos[1]
    xTorso = torsoPos[0]
    yTorso = torsoPos[1]
   
    m1x = xSupFoot/td
    m2x = (xTorso-xSupFoot)/td

    m1y = ySupFoot/td
    m2y = (yTorso-ySupFoot)/td

    #! ta faltando o xtorso na formula e esse xtorso acredito que seria o inicial e não o que voce ta recebendo igual colocou no ytorso
    Xzmp = np.concatenate((m1x*t[mask1], np.full(len(t[mask2]), xSupFoot), xSupFoot + m2x*(t[mask3]-stepTime+td)))
    Yzmp = np.concatenate((yTorso+m1y*t[mask1], np.full(len(t[mask2]), ySupFoot), ySupFoot + m2y*(t[mask3]-stepTime+td)))
    #!  a falta do xtorso ali deve estar fazendo aquele salto de valor das coordenadas x do supfoot
    return Xzmp, Yzmp, m1x, m2x, m1y, m2y

def genSwingFootAndTorsoNextPositions(stepX, leftFootAbsPos, rightFootAbsPos, supFoot):
    # SupportFoot = 1 p/ direita; SupportFoot = -1 p/ esquerda;

    xLeftAbsPos = leftFootAbsPos[0]
    xRightAbsPos = rightFootAbsPos[0]
    
    if abs(xLeftAbsPos-xRightAbsPos) < stepX/2:
        addInX = stepX/2
    else:
        addInX = stepX

    [swingFootPos, supFootPos] = [rightFootAbsPos, leftFootAbsPos] if supFoot == -1 else [leftFootAbsPos, rightFootAbsPos]
    newSwingFootPos = swingFootPos + np.array([[addInX, 0,0]]).T

    newTorsoPos = np.array([(newSwingFootPos[0]+supFootPos[0])/2, 0,0]).T

    return newSwingFootPos, newTorsoPos, addInX

def genCOMTrajectory(queueTime, stepTime, doubleSupProportion, xZMP, yZMP, m1x, m2x, m1y, m2y):
    #? Constantes da resolução da EDO
    td = stepTime*doubleSupProportion
    lambda_ = np.sqrt(g/zCOM) 

    lambStep = lambda_*stepTime
    denominator = np.exp(lambStep) - np.exp(-lambStep)

    t = np.linspace(0.0,stepTime,np.ceil(stepTime/queueTime))

    t1 = t[t < td]
    t2 = t[(t >= td) & (t < (stepTime - td))]
    t3 = t[t >= (stepTime - td)]

    #? Resolução da EDO de x
    k1x = m1x*np.sinh(-lambda_*td)/lambda_
    k2x = m2x*np.sinh(lambda_*td)/lambda_

    c1x = ( k2x - k1x*np.exp(-lambStep) ) / (denominator)
    c2x = ( k1x*np.exp(lambStep) - k2x) / (denominator)

    x1 = xZMP[t < td] + c1x*np.exp(lambda_*t1) + c2x*np.exp(-lambda_*t1) - (m1x*np.sinh(lambda_*(t1-td))/lambda_)
    x2 = xZMP[(t >= td) & (t < (stepTime - td))] + c1x*np.exp(lambda_*t2) + c2x*np.exp(-lambda_*t2)
    x3 = xZMP[t >= (stepTime - td)] + c1x*np.exp(lambda_*t3) + c2x*np.exp(-lambda_*t3) - (m2x*np.sinh(lambda_*(t3-stepTime+td))/lambda_)

    xCOM = np.concatenate((x1,x2,x3))

    #? Resolução da EDO de y
    k1y = m1y*np.sinh(-lambda_*td)/lambda_
    k2y = m2y*np.sinh(lambda_*td)/lambda_

    c1y = ( k2y - k1y*np.exp(-lambStep) ) / (denominator)
    c2y = ( k1y*np.exp(lambStep) - k2y) / (denominator)

    y1 = yZMP[t < td] + c1y*np.exp(lambda_*t1) + c2y*np.exp(-lambda_*t1) - (m1y*np.sinh(lambda_*(t1-td))/lambda_)
    y2 = yZMP[(t >= td) & (t < (stepTime - td))] + c1y*np.exp(lambda_*t2) + c2y*np.exp(-lambda_*t2)
    y3 = yZMP[t >= (stepTime - td)] + c1y*np.exp(lambda_*t3) + c2y*np.exp(-lambda_*t3) - (m2y*np.sinh(lambda_*(t3-stepTime+td))/lambda_)

    yCOM = np.concatenate((y1,y2,y3))

    return xCOM, yCOM

def genSwingFootZTrajectory(queueTime, stepTime, doubleSupProportion):
    t = np.linspace(0.0,stepTime,np.ceil(stepTime/queueTime))
    td = stepTime*doubleSupProportion

    mask1 = t < td
    mask2 = (t >= td) & (t < (stepTime - td))
    mask3 = t >= (stepTime - td)

    zSwing = np.concatenate((np.zeros(len(t[mask1])),zSwingHeight*np.sin(np.pi*(t[mask2]-td)/(stepTime-2*td)),np.zeros(len(t[mask3]))))

    return zSwing

def backup():

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
