#!/usr/bin/env python3
#coding=utf-8

import numpy as np

from direct_kinematics import ForwardKinematics

IK_ITERATIONS_LIMIT = 100

def FindRoute(targetJoint, robot):

    i = robot[targetJoint].get_mom()
    if i == 0:
        indexes = [targetJoint]
    else:
        indexes = FindRoute(i, robot) + [targetJoint]

    return indexes

def rot2omega(R):

    el = np.array([R[2,1]-R[1,2], R[0,2]-R[2,0], R[1,0]-R[0,1]])
    norm_el = np.linalg.norm(el)
    eps = np.finfo(float).eps

    if norm_el > eps:
        w = np.arctan2(norm_el, np.trace(R)-1)/norm_el * el
    elif R[0,0]>0 and R[1,1]>0 and R[2,2]>0:
        w = np.array([0, 0, 0])
    else:
        w = np.pi/2*np.array([R[0,0]+1, R[1,1]+1, R[2,2]+1])
        
    return w

def CalcVWerr(PositionRef, PostureRef, Cnow):
    perr = PositionRef - Cnow.absolutePosition

    Rerr = np.dot(Cnow.absolutePosture.T, PostureRef)
    werr = np.dot(Cnow.absolutePosture, np.array([[Rerr[2,1] - Rerr[1,2]], [Rerr[0,2] - Rerr[2,0]], [Rerr[1,0] - Rerr[0,1]]]))

    err = np.array([perr[0], perr[1], perr[2], werr[0], werr[1], werr[2]])

    return err

def CalcJacobian(indexes, robot):

    jsize = len(indexes)
    target = robot[indexes[-1]].absolutePosition
    J = np.zeros((6, jsize))

    for n in range(jsize):
        j = indexes[n]

        a = np.matmul(robot[j].absolutePosture, robot[j].get_jointAxis())
        crossArgument = (target - robot[j].absolutePosition).T[0]
        cross = np.array([np.cross(a.T[0], crossArgument)]).T

        J[:,n] = np.array([cross[0], cross[1], cross[2], a[0], a[1], a[2]]).T
    
    return J

def VirtuallyMoveJoints(indexes, dq, robot):

    for n in range(len(indexes)):

        j = indexes[n]

        qNew = robot[j].jointRotation + dq[n]
        qNew = np.mod(qNew + np.pi, 2*np.pi) - np.pi
        
        if robot[j].get_id() == -1:
            qNew = 0
        if robot[j].is_knee():
            if qNew > -0.01:
                qNew = 0
                
        robot[j].jointRotation = qNew
    
def InverseKinematics(newFootAbsPosition, newFootAbsPosture, currentFoot, robotik):
    targetAbsPosition = newFootAbsPosition
    targetAbsPosture = newFootAbsPosture
    
    lambda_val = 0.7
    indexes = FindRoute(currentFoot, robotik)
    err = CalcVWerr(targetAbsPosition, targetAbsPosture, robotik[currentFoot])
    
    count = 0
    while np.linalg.norm(err) > 1E-4:
        J = CalcJacobian(indexes, robotik)

        dq = lambda_val*np.linalg.lstsq(J, err,rcond=None)[0]
        
        VirtuallyMoveJoints(indexes, dq, robotik)
        ForwardKinematics(robotik)

        err = CalcVWerr(targetAbsPosition, targetAbsPosture, robotik[currentFoot])

        count += 1

        if count > IK_ITERATIONS_LIMIT:
            raise Exception(f"A cinemática inversa de {robotik[currentFoot].get_name()} para {targetAbsPosition.T}" +
            f" não convergiu após {IK_ITERATIONS_LIMIT} iterações, a posição/postura desejada provavelmente estão fora" +
            f" do espaço de trabalho da robô.")

    joint_angles = np.zeros(len(robotik))
    for i in range(len(robotik)):
        joint_angles[i] = robotik[i].jointRotation

    return joint_angles