import numpy as np
import copy

import sys, os
edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'movement/kinematic_functions/src')
from ik_numerical import InverseKinematics

#? Parâmetros da caminhada
zSwingHeight = 0.03 #Altura do pé de balanço (m)
stepTime = 1#Tempo para "um" passo (s)
doubleSupProportion = 0.2 # Proporção do tempo de um passo em suporte duplo (adim)
stepX = 0.055 #Tamanho de um passo em x (m)
g = 9.81 #Gravidade (m/s²)
zCOM = 0.253 #Altura do centro de massa (m)
Y_ZMP_CORRECTION = -0.03 #Correção forçada da posição em Y do ZMP (m)
PAUSE_AFTER_STEP = 0.2 #Pausa após um passo (s)

def callIK(robot, newFootAbsPosition, newFootAbsPosture, currentFoot):
    robotIK = copy.deepcopy(robot)
        
    joint_angles = [0]*len(robot)
    
    joint_angles = InverseKinematics(newFootAbsPosition, newFootAbsPosture, currentFoot, robotIK)

    return joint_angles

def feetPosesCalculator(xCOM, yCOM, zSwing, dxSwing, t1, t2, t3,supportFoot):

    xyzCOM = np.c_[xCOM/2, yCOM, np.zeros(len(xCOM))]

    xSwing = np.concatenate((np.zeros(len(t1)),np.linspace(0,dxSwing/2,len(t2)),(dxSwing/2)*np.ones(len(t3))))
    ySwing = np.zeros(len(t1)+len(t2)+len(t3))

    xyzSwing = np.c_[xSwing, -yCOM-ySwing, zSwing]

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

    #print(f'absCOM:\n{absCOM}')
    #print(f'swingFootInitPos:\n{swingFootInitPos}')
    #print(f'supFootInitPos:\n{supFootInitPos}')

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

    #print(f'newSwingFootPos:\n{newSwingFootPos}')
    #print(f'newTorsoPos:\n{newTorsoPos}')
    #print(f'currentStep:\n{currentStep}')

    #? Obtém posições do ZMP e coeficientes angulares da reta que será usado na EDO
    xZMP, yZMP, m1x, m2x, m1y, m2y = genZMPTrajectory(stepTime, td, t1, t2, t3, supFootInitPos, newTorsoPos, supFoot)

    #print(f'xZMP:\n{xZMP}')
    #print(f'yZMP:\n{yZMP}')

    #? Obtém um deslocamento relativo em Z para o pé de balanço
    zSwing = genSwingFootZTrajectory(stepTime, td, t1, t2, t3)
    #print(f'zSwing:\n{zSwing}')

    #? Obtém a solução da EDO (xCOM e yCOM)
    xCOM, yCOM = genCOMTrajectory(stepTime, td, mask1, mask2, mask3, t1, t2, t3, xZMP, yZMP, m1x, m2x, m1y, m2y)
    
    #print(f'xCOM:\n{xCOM}')
    #print(f'yCOM:\n{yCOM}')

    #? Transformando o referencial em relativo para os pés
    leftFootPoses, rightFootPoses = feetPosesCalculator(xCOM, yCOM, zSwing, currentStep, t1, t2, t3, supFoot)

    #print(f'leftFootPoses:\n{leftFootPoses}')
    #print(f'rightFootPoses:\n{rightFootPoses}')

    #? Somando à posição inicial dos pés para transformar em absoluto
    walk_poses = np.zeros((len(leftFootPoses)+int(np.ceil(PAUSE_AFTER_STEP/queueTime)),len(robot)))

    for i in range(len(t1)+len(t2)):

        newLeftFootPos = leftFootPos+np.array([leftFootPoses[i]]).T
        newRightFootPos = rightFootPos+np.array([rightFootPoses[i]]).T

        try:
            currentFoot = -2
            left_joint_angles = callIK(robot, newLeftFootPos, leftFootPosture, currentFoot)
            left_joint_angles = left_joint_angles[7:13]
            lastLAngles = left_joint_angles
        except Exception as e:
            print(e)
            left_joint_angles = lastLAngles

        try:
            currentFoot = -1
            right_joint_angles = callIK(robot, newRightFootPos, rightFootPosture, currentFoot)
            right_joint_angles = right_joint_angles[1:7]
            lastRAngles = right_joint_angles
        except Exception as e:
            print(e)
            right_joint_angles = lastRAngles

        walk_poses[i][1:7] = right_joint_angles
        walk_poses[i][7:13] = left_joint_angles

    for i in range(len(t1)+len(t2),len(t1)+len(t2)+int(np.ceil(PAUSE_AFTER_STEP/queueTime))):
        walk_poses[i][1:7] = right_joint_angles
        walk_poses[i][7:13] = left_joint_angles
    
    for i in range(len(t1)+len(t2),len(t1)+len(t2)+len(t3)):
        newLeftFootPos = leftFootPos+np.array([leftFootPoses[i]]).T
        newRightFootPos = rightFootPos+np.array([rightFootPoses[i]]).T

        try:
            currentFoot = -2
            left_joint_angles = callIK(robot, newLeftFootPos, leftFootPosture, currentFoot)
            left_joint_angles = left_joint_angles[7:13]
            lastLAngles = left_joint_angles
        except Exception as e:
            print(e)
            left_joint_angles = lastLAngles

        try:
            currentFoot = -1
            right_joint_angles = callIK(robot, newRightFootPos, rightFootPosture, currentFoot)
            right_joint_angles = right_joint_angles[1:7]
            lastRAngles = right_joint_angles
        except Exception as e:
            print(e)
            right_joint_angles = lastRAngles

        walk_poses[i+int(np.ceil(PAUSE_AFTER_STEP/queueTime))][1:7] = right_joint_angles
        walk_poses[i+int(np.ceil(PAUSE_AFTER_STEP/queueTime))][7:13] = left_joint_angles

    return walk_poses

def genSwingFootAndTorsoNextPositions(stepX, initSwingPos, initSuppPos):
    
    if abs(initSwingPos[0][0]-initSuppPos[0][0]) < stepX/4:
        addInX = stepX/2
    else:
        addInX = stepX

    newSwingFootPos = initSwingPos + np.array([[addInX, 0,0]]).T

    newTorsoPos = np.array([[(newSwingFootPos[0][0]+initSuppPos[0][0])/2, 0,0]]).T

    return newSwingFootPos, newTorsoPos, addInX

def genZMPTrajectory(stepTime, td, t1, t2, t3, supFootInitPos, torsoFinal, supFoot):    

    xSupFoot = supFootInitPos[0][0]
    ySupFoot = supFootInitPos[1][0]-supFoot*Y_ZMP_CORRECTION

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