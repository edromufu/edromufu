#!/usr/bin/env python3
#coding=utf-8

import numpy as np

def Rodrigues(w, dt):
    norm_w = np.linalg.norm(w)

    if norm_w < np.finfo(float).eps:
        R = np.identity(3)
    else:
        wn = w/norm_w
        th = norm_w*dt
        w_wedge = np.array([[0, -wn[2][0], wn[1][0]],[wn[2][0], 0, -wn[0][0]],[-wn[1][0], wn[0][0], 0]])
        R = np.identity(3) + w_wedge * np.sin(th) + np.linalg.matrix_power(w_wedge, 2) * (1-np.cos(th))

    return R

def ForwardKinematics(robotJoints, current_id=0):
    
    if current_id == -1:
        return
    if current_id != 0:
        mom = robotJoints[current_id].get_mom()

        robotJoints[current_id].absolutePostion = np.matmul(robotJoints[mom].absolutePosture,robotJoints[current_id].get_mother2SelfVec()) + robotJoints[mom].absolutePostion
        
        robotJoints[current_id].absolutePosture = np.matmul(robotJoints[mom].absolutePosture,Rodrigues(robotJoints[current_id].get_jointAxis(), robotJoints[current_id].jointRotation))

    ForwardKinematics(robotJoints, robotJoints[current_id].get_sister())
    ForwardKinematics(robotJoints, robotJoints[current_id].get_child())