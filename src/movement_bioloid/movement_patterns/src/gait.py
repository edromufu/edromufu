#!/usr/bin/env python3
#coding=utf-8

import numpy as np

import  sys
os.chdir(os.path.dirname(__file__))
os.chdir("../../kinematic_functions/src")
sys.path.append(os.getcwd())
import inverse_kinematics

def gaitRun(robotJoints, steps_number, step_height, step_resolution):
    
    for index, joint in enumerate(robotJoints):
        if id == 6:
            index_COM = robotJoints[joint.get_mom()].get_id()
            index_right_hip = index
        elif id == 7:
            index_left_hip = index
        elif id == 12:
            index_knee = index
        elif id == 14:
            index_foot_joint = joint.get_id()
            index_foot = robotJoints[joint.get_child()].get_id()

    body2RightHip = robotJoint[index_right_hip].get_mother2SelfVec()
    body2LeftHip  = robotJoint[index_left_hip].get_mother2SelfVec()
    hip2Knee      = np.linalg.norm(robotJoint[index_left_hip].get_mother2SelfVec())
    knee2Foot     = np.linalg.norm(robotJoint[index_foot].get_mother2SelfVec()+robotJoint[index_foot_joint].get_mother2SelfVec())

    comPosition = robotJoint[index_COM].absolutePostion()
    comPosture =  robotJoint[index_COM].absolutePosture()

    gaitPoses = []

    leg = 0
    stage = 1
    stepsCount = 0

    while stepsCount < 2*steps_number:
        if leg:
            body2Hip = body2LeftHip
        else:
            body2Hip = body2LeftHip

        stageCount = 0
        while stageCount < step_resolution:
            newFootPosition = robotJoint[index_foot].absolutePostion + np.array([[0, 0, step_height/step_resolution]]).T

            gaitPoses.append(inverse_kinematics.ikLeg(comPosition,comPosture,body2Hip,hip2Knee,knee2Foot,newFootPosition,np.eye(3)))
            
    return 