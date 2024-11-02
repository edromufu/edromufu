#!/usr/bin/env python3
#coding=utf-8


import sys, json, os
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

MAIN_DIR = '/home/'+os.getlogin()+'/edromufu/src/movement/movement_pages/pages_tahara/'

class MyPublisher(Node):
    def __init__(self):
        super().__init__('page_topic')
        self.publisher_ = self.create_publisher(Float32MultiArray, 'pot_py_topic', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)  # Chama a callback a cada 1 segundo
        self.msg = Float32MultiArray()

    def timer_callback(self):
        
        self.publisher_.publish(self.msg)


def Page(page2Run, queueTime):

    with open(MAIN_DIR+page2Run+'.json', 'r') as pageFile:
        jsonData = json.loads(pageFile.read())

    pagePoses = pageInterpol(jsonData['joints_positions'], jsonData['time_between_poses'], queueTime)

    return pagePoses

def pageInterpol(positions, time, deltaT):

    for motor_id in range(8):
        motor_n_positions = positions[f'pot_{motor_id}']
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
