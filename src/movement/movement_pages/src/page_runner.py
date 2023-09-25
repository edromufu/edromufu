#!/usr/bin/env python3
#coding=utf-8

import os, json
import numpy as np

MAIN_DIR = '/home/'+os.getlogin()+'/edromufu/src/movement/movement_pages/pages/'

def Page(page2Run, queueTime, startPose, toPose1Time=0.6):

    with open(MAIN_DIR+page2Run+'.json', 'r') as pageFile:
        jsonData = json.loads(pageFile.read())
    
    for motor_id, motor_pos in enumerate(startPose):
        jsonData['joints_positions'][f'motor_{motor_id}'].insert(0, motor_pos)
    
    jsonData['time_between_poses'].insert(0, toPose1Time)

    pagePoses = pageInterpol(jsonData['joints_positions'], jsonData['time_between_poses'], queueTime)

    return pagePoses

def pageInterpol(positions, time, deltaT):

    for motor_id in range(18):
        motor_n_positions = positions[f'motor_{motor_id}']
        motor_n_interpol = []

        for index, position in enumerate(motor_n_positions):

            if index != 0:

                last_position = motor_n_positions[index-1]
                pose_time = time[index-1]

                count = 0
                while count * deltaT < pose_time:                    
                    interpol_func_value = (1-np.cos((count+1)*deltaT*np.pi/pose_time))/2
                    interpoled_position = last_position + (position - last_position)*interpol_func_value

                    motor_n_interpol.append(round(interpoled_position,4))
                    count += 1

            else:
                motor_n_interpol.append(position)
        
        positions[f'motor_{motor_id}'] = motor_n_interpol
    
    poses = interpolOrganization(positions)

    return poses

def interpolOrganization(data):

    return np.column_stack(list(data.values()))
