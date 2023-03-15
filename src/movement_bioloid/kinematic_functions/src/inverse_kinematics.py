#!/usr/bin/env python3
#coding=utf-8

import numpy as np

def Rpitch(theta):
    c = np.cos(theta)
    s = np.sin(theta)

    Ry = np.array([[c, 0, s],[0, 1, 0],[-s, 0, c]])

    return Ry

def Rroll(phi):
    c = np.cos(phi)
    s = np.sin(phi)

    R = np.array([[1,0,0],[0,c,-s],[0,s,c]])

    return R


def ikLeg(absPositionCOM, absPostureCOM, body2Hip, hip2Knee, knee2Foot, newFootPosition, newFootPosture):

    absPositionHip = absPositionCOM +  np.matmul(absPostureCOM,np.array([[0, body2Hip, 0]]).T)
    foot2COMvect = np.matmul(newFootPosture.T, (absPositionHip - newFootPosition))
    foot2COMdist = np.linalg.norm(foot2COMvect)

    c5 = (foot2COMdist**2 - hip2Knee**2 - knee2Foot**2)/(2*hip2Knee*knee2Foot)
    if c5 >= 1:
        q5 = 0
    elif c5 <= -1:
        q5 = np.pi
    else:
        q5 = np.arccos(c5)

    alpha = np.arcsin(hip2Knee*np.sin(np.pi-q5)/foot2COMdist)

    q7 = np.arctan2(foot2COMvect[1][0], foot2COMvect[2][0])
    q6 = -np.arctan2(foot2COMvect[0][0], np.sign(foot2COMvect[2][0])*np.sqrt(foot2COMvect[1][0]**2 + foot2COMvect[2][0]**2)) - alpha

    R = np.matmul(np.matmul(np.matmul(absPostureCOM.T,newFootPosture),Rroll(-q7)),Rpitch(-q6-q5))
    q2 = np.arctan2(-R[0][1], R[1][1])
    q3 = np.arctan2(R[2][1], -R[0][2]*np.sin(q2) + R[1][1]*np.cos(q2))
    q4 = np.arctan2(-R[2][0], R[2][2])    

    q = np.around(np.array([[q2,q3,q4,q5,q6,q7]]).T, decimals=4)
    return q