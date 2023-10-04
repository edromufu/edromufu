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

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#? Parâmetros da caminhada
zSwingHeight = 0.04 #Altura do pé de balanço (m )
stepTime = 2 #Tempo para "um" passo (s)
doubleSupProportion = 0.3 # Proporção do tempo de um passo em suporte duplo (adim)
stepX = 0.1 #Tamanho de um passo em x (m)
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

def feetPosesCalculator(xCOM, yCOM, zSwing, dxSwing, t,supportFoot):

    xyzCOM = np.c_[xCOM/2, yCOM, np.zeros(len(xCOM))]
    xyzSwing = np.c_[np.linspace(0,dxSwing/2,len(t)), -yCOM, zSwing]

    if supportFoot == -1:
        leftFootPoses = -xyzCOM
    else:
        leftFootPoses = xyzSwing
    
    if supportFoot == 1:
        rightFootPoses = -xyzCOM
    else:
        rightFootPoses = xyzSwing

    return leftFootPoses, rightFootPoses

def callWalk(robot, supFoot, queueTime):
    # SupportFoot = 1 p/ direita; SupportFoot = -1 p/ esquerda;

    #? Obtendo informações relevantes do modelo
    leftFootPos = robot[-2].absolutePosition
    rightFootPos = robot[-1].absolutePosition

    leftFootPosture = robot[-2].absolutePosture
    rightFootPosture = robot[-1].absolutePosture

    absCOM = robot[0].absolutePosition

    #? Definindo variáveis padrões
    [swingFootInitPos, supFootInitPos] = [rightFootPos, leftFootPos] if supFoot == -1 else [leftFootPos, rightFootPos]

    print(f'absCOM:\n{absCOM}')
    print(f'swingFootInitPos:\n{swingFootInitPos}')
    print(f'supFootInitPos:\n{supFootInitPos}')

    t = np.linspace(0.0,stepTime,np.ceil(stepTime/queueTime))
    td = stepTime*doubleSupProportion

    mask1 = t < td
    mask2 = (t >= td) & (t < (stepTime - td))
    mask3 = t >= (stepTime - td)

    t1 = t[mask1]
    t2 = t[mask2]
    t3 = t[mask3]

    #? Seleciona posição final (vetor coluna) do torso e pé de balanço
    newSwingFootPos, newTorsoPos, currentStep = genSwingFootAndTorsoNextPositions(stepX, swingFootInitPos, supFootInitPos)

    print(f'newSwingFootPos:\n{newSwingFootPos}')
    print(f'newTorsoPos:\n{newTorsoPos}')
    print(f'currentStep:\n{currentStep}')

    #? Obtém posições do ZMP e coeficientes angulares da reta que será usado na EDO
    xZMP, yZMP, m1x, m2x, m1y, m2y = genZMPTrajectory(stepTime, td, t1, t2, t3, supFootInitPos, newTorsoPos)

    print(f'xZMP:\n{xZMP}')
    print(f'yZMP:\n{yZMP}')

    #? Obtém um deslocamento relativo em Z para o pé de balanço
    zSwing = genSwingFootZTrajectory(stepTime, td, t1, t2, t3)
    print(f'zSwing:\n{zSwing}')

    #? Obtém a solução da EDO (xCOM e yCOM)
    xCOM, yCOM = genCOMTrajectory(stepTime, td, mask1, mask2, mask3, t1, t2, t3, xZMP, yZMP, m1x, m2x, m1y, m2y)
    
    print(f'xCOM:\n{xCOM}')
    print(f'yCOM:\n{yCOM}')

    #? Transformando o referencial em relativo para os pés
    leftFootPoses, rightFootPoses = feetPosesCalculator(xCOM, yCOM, zSwing, currentStep, t, supFoot)

    print(f'leftFootPoses:\n{leftFootPoses}')
    print(f'rightFootPoses:\n{rightFootPoses}')

    #? Somando à posição inicial dos pés para transformar em absoluto
    walk_poses = np.zeros((len(leftFootPoses),len(robot)))

    for i in range(len(leftFootPoses)):

        newLeftFootPos = leftFootPos+np.array([leftFootPoses[i]]).T
        newRightFootPos = rightFootPos+np.array([rightFootPoses[i]]).T

        currentFoot = -2
        left_joint_angles = callIK(robot, newLeftFootPos, leftFootPosture, currentFoot)
        left_joint_angles = left_joint_angles[7:13]

        currentFoot = -1
        right_joint_angles = callIK(robot, newRightFootPos, rightFootPosture, currentFoot)
        right_joint_angles = right_joint_angles[1:7]

        walk_poses[i][1:7] = right_joint_angles
        walk_poses[i][7:13] = left_joint_angles
    
    return walk_poses

def genSwingFootAndTorsoNextPositions(stepX, initSwingPos, initSuppPos):
    
    if abs(initSwingPos[0][0]-initSuppPos[0][0]) < stepX/4:
        addInX = stepX/2
    else:
        addInX = stepX

    newSwingFootPos = initSwingPos + np.array([[addInX, 0,0]]).T

    newTorsoPos = np.array([[(newSwingFootPos[0][0]+initSuppPos[0][0])/2, 0,0]]).T

    return newSwingFootPos, newTorsoPos, addInX

def genZMPTrajectory(stepTime, td, t1, t2, t3, supFootInitPos, torsoFinal):    

    xSupFoot = supFootInitPos[0][0]
    ySupFoot = supFootInitPos[1][0]

    xTorso = torsoFinal[0][0]
    yTorso = torsoFinal[1][0]
   
    m1x = xSupFoot/td
    m2x = (xTorso-xSupFoot)/td

    m1y = ySupFoot/td
    m2y = (yTorso-ySupFoot)/td
    
    Xzmp = np.concatenate((m1x*t1, np.full(len(t2), xSupFoot), xSupFoot + m2x*(t3-stepTime+td)))
    Yzmp = np.concatenate((m1y*t1, np.full(len(t2), ySupFoot), ySupFoot + m2y*(t3-stepTime+td)))

    return Xzmp, Yzmp, m1x, m2x, m1y, m2y

def genSwingFootZTrajectory(stepTime, td, t1, t2, t3):

    zSwing = np.concatenate((np.zeros(len(t1)),zSwingHeight*np.sin(np.pi*(t2-td)/(stepTime-2*td)),np.zeros(len(t3))))

    return zSwing

def genCOMTrajectory(stepTime, td, mask1, mask2, mask3, t1, t2, t3, xZMP, yZMP, m1x, m2x, m1y, m2y):
    #? Constantes da resolução da EDO
    lambda_ = np.sqrt(g/zCOM) 

    lambStep = lambda_*stepTime
    denominator = np.exp(lambStep) - np.exp(-lambStep)

    #? Resolução da EDO de x
    k1x = m1x*np.sinh(-lambda_*td)/lambda_
    k2x = m2x*np.sinh(lambda_*td)/lambda_

    c1x = ( k2x - k1x*np.exp(-lambStep) ) / (denominator)
    c2x = ( k1x*np.exp(lambStep) - k2x) / (denominator)

    x1 = xZMP[mask1] + c1x*np.exp(lambda_*t1) + c2x*np.exp(-lambda_*t1) - (m1x*np.sinh(lambda_*(t1-td))/lambda_)
    x2 = xZMP[mask2] + c1x*np.exp(lambda_*t2) + c2x*np.exp(-lambda_*t2)
    x3 = xZMP[mask3] + c1x*np.exp(lambda_*t3) + c2x*np.exp(-lambda_*t3) - (m2x*np.sinh(lambda_*(t3-stepTime+td))/lambda_)

    xCOM = np.concatenate((x1,x2,x3))

    #? Resolução da EDO de y
    k1y = m1y*np.sinh(-lambda_*td)/lambda_
    k2y = m2y*np.sinh(lambda_*td)/lambda_

    c1y = ( k2y - k1y*np.exp(-lambStep) ) / (denominator)
    c2y = ( k1y*np.exp(lambStep) - k2y) / (denominator)

    y1 = yZMP[mask1] + c1y*np.exp(lambda_*t1) + c2y*np.exp(-lambda_*t1) - (m1y*np.sinh(lambda_*(t1-td))/lambda_)
    y2 = yZMP[mask2] + c1y*np.exp(lambda_*t2) + c2y*np.exp(-lambda_*t2)
    y3 = yZMP[mask3] + c1y*np.exp(lambda_*t3) + c2y*np.exp(-lambda_*t3) - (m2y*np.sinh(lambda_*(t3-stepTime+td))/lambda_)

    yCOM = np.concatenate((y1,y2,y3))

    return xCOM, yCOM

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
