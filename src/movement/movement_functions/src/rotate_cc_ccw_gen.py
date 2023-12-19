import numpy as np
import copy

import sys, os
edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'movement/kinematic_functions/src')
from ik_numerical import InverseKinematics

#? Parâmetros da caminhada
zSwingHeight = 0.05 #Altura do pé de balanço (m)
stepTime = 1 #Tempo para "um" passo (s)
doubleSupProportion = 0.3 # Proporção do tempo de um passo em suporte duplo (adim)
rotationTheta = np.deg2rad(5) #Incremento de uma rotação (rad)

import matplotlib.pyplot as plt

def callIK(robot, newFootAbsPosition, newFootAbsPosture, currentFoot):
    robotIK = copy.deepcopy(robot)
        
    joint_angles = [0]*len(robot)
    
    joint_angles = InverseKinematics(newFootAbsPosition, newFootAbsPosture, currentFoot, robotIK)

    return joint_angles

def callRotate(robot, direction, phase, queueTime):
    # Direction = 1 p/ horário; Direction = -1 p/ antihorário;
    # Phase: Inicia-se sempre em -1, muda-se para 1 para a próxima etapa da rotação

    #? Obtendo informações relevantes do modelo
    leftFootPos = robot[-2].absolutePosition
    rightFootPos = robot[-1].absolutePosition

    leftFootPosture = robot[-2].absolutePosture
    rightFootPosture = robot[-1].absolutePosture

    #? Definindo variáveis padrão
    supFootInitPos = leftFootPos if direction*phase == -1 else rightFootPos

    t = np.linspace(0.0,stepTime,np.ceil(stepTime/queueTime)+1)
    td = stepTime*doubleSupProportion

    mask1 = t <= td
    mask2 = (t >= td) & (t < (stepTime - td))
    mask3 = t >= (stepTime - td)

    t1 = t[mask1]
    t2 = t[mask2]
    t3 = t[mask3]

    swingFootRelativePositions, comPositions = genSwingFootAndCOMPositions(supFootInitPos, t1, t2, t3)

    leftFootPostures, rightFootPostures = genLeftAndRightFootPostures(leftFootPosture, rightFootPosture, direction*phase, t1, t2, t3, direction)

    leftFootPositions, rightFootPositions = feetPosesCalculator(comPositions, swingFootRelativePositions, direction*phase)

    #? Somando à posição inicial e forçando rotação dos pés para transformar em absoluto
    rotation_poses = np.zeros((len(leftFootPositions),len(robot)))

    for i in range(len(leftFootPositions)):

        newLeftFootPosition = leftFootPos+np.array([leftFootPositions[i]]).T
        newRightFootPosition = rightFootPos+np.array([rightFootPositions[i]]).T

        newLeftFootPosture = leftFootPostures[i]
        newRightFootPosture = rightFootPostures[i]

        try:
            currentFoot = -2
            left_joint_angles = callIK(robot, newLeftFootPosition, newLeftFootPosture, currentFoot)
            left_joint_angles = left_joint_angles[7:13]
            lastLAngles = left_joint_angles
        except Exception as e:
            print(e)
            left_joint_angles = lastLAngles

        try:
            currentFoot = -1
            right_joint_angles = callIK(robot, newRightFootPosition, newRightFootPosture, currentFoot)
            right_joint_angles = right_joint_angles[1:7]
            lastRAngles = right_joint_angles
        except Exception as e:
            print(e)
            right_joint_angles = lastRAngles

        rotation_poses[i][1:7] = right_joint_angles
        rotation_poses[i][7:13] = left_joint_angles
    
    return rotation_poses

def feetPosesCalculator(com, swing, dirphase):

    if dirphase == -1:
        leftFootPositions = -com
        rightFootPositions = swing-com

    else:
        rightFootPositions = -com
        leftFootPositions = swing-com

    return leftFootPositions, rightFootPositions
    
def genSwingFootAndCOMPositions(supFootInitPos, t1, t2, t3):
    "OLHAR DE CABO A RABO"
    "COORDENADAS DO TORSO?"
    xSup = supFootInitPos[0][0]
    ySup = supFootInitPos[1][0]

    #? Cálculo para colocar o COM no pé de balanço
    xCOM1 = xSup*np.sin(np.pi*t1/(2*t2[0]))
    xCOM2 = xSup*np.ones(len(t2))
    xCOM3 = xSup*np.sin(np.pi*(-t3+2*t2[0]+(stepTime-2*t2[0]))/(2*t2[0]))

    xCOM = np.concatenate((xCOM1,xCOM2,xCOM3))

    yCOM1 = ySup*np.sin(np.pi*t1/(2*t2[0]))
    yCOM2 = ySup*np.ones(len(t2))
    yCOM3 = ySup*np.sin(np.pi*(-t3+2*t2[0]+(stepTime-2*t2[0]))/(2*t2[0]))

    yCOM = np.concatenate((yCOM1,yCOM2,yCOM3))
    
    zCOM = np.zeros(len(yCOM))

    com = np.c_[xCOM,yCOM,zCOM]

    #? Cálculo das posições do pé de balanço subindo

    td = stepTime*doubleSupProportion
    zSwing = np.concatenate((np.zeros(len(t1)),zSwingHeight*np.sin(np.pi*(t2-td)/(stepTime-2*td)),np.zeros(len(t3))))
    xSwing = np.zeros(len(zSwing))
    ySwing = np.zeros(len(zSwing))

    swingFootPosition = np.c_[xSwing,ySwing,zSwing]

    return swingFootPosition, com

def genLeftAndRightFootPostures(leftFootPosture, rightFootPosture, dirphase, t1, t2, t3, direction):
    
    if dirphase == 1:
        rightFootPostures = np.array([rightFootPosture]*(len(t1)+len(t2)+len(t3)))

        theta = np.arcsin(-leftFootPosture[2][0])
        phi = np.arcsin(leftFootPosture[2][1]/np.cos(theta))
        psi = np.arcsin(leftFootPosture[1][0]/np.cos(theta))

        deltaPsi = np.linspace(psi,psi-direction*rotationTheta, len(t2))

        leftPostures1 = np.array([leftFootPosture]*len(t1))
        leftPostures2 = np.array([calcAbsPostureMatrix(phi, theta, currentPsi) for currentPsi in deltaPsi])
        leftPostures3 = np.array([leftPostures2[-1]]*len(t3))

        leftFootPostures = np.concatenate((leftPostures1,leftPostures2,leftPostures3))

    else:
        leftFootPostures = np.array([leftFootPosture]*(len(t1)+len(t2)+len(t3)))

        theta = np.arcsin(-rightFootPosture[2][0])
        phi = np.arcsin(rightFootPosture[2][1]/np.cos(theta))
        psi = np.arcsin(rightFootPosture[1][0]/np.cos(theta))

        deltaPsi = np.linspace(psi,psi-direction*rotationTheta, len(t2))

        rightPostures1 = np.array([rightFootPosture]*len(t1))
        rightPostures2 = np.array([calcAbsPostureMatrix(phi, theta, currentPsi) for currentPsi in deltaPsi])
        rightPostures3 = np.array([rightPostures2[-1]]*len(t3))

        rightFootPostures = np.concatenate((rightPostures1,rightPostures2,rightPostures3))
    
    return leftFootPostures, rightFootPostures

def calcAbsPostureMatrix(phi, theta, psi):
    ctheta = np.cos(theta)
    stheta = np.sin(theta)

    cphi = np.cos(phi)
    sphi = np.sin(phi)

    cpsi = np.cos(psi)
    spsi = np.sin(psi)

    line1 = [cpsi*ctheta, -spsi*cphi+cpsi*stheta*sphi, spsi*sphi+cpsi*stheta*cphi]
    line2 = [spsi*ctheta, cpsi*cphi+spsi*stheta*sphi, -cpsi*sphi+spsi*stheta*cphi]
    line3 = [-stheta, ctheta*sphi, ctheta*cphi]
    
    return np.array([line1, line2, line3])