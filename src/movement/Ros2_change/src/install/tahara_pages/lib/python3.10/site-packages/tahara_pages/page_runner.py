#!/usr/bin/env python3
#coding=utf-8


import sys, json, os
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

MAIN_DIR = '/home/'+os.getlogin()+'/edromufu/src/movement/Ros2_change/src/tahara_pages/tahara_pages/'

class MyPublisher(Node):
    def __init__(self):
        super().__init__('page_topic')
        
        self.publisher_ = self.create_publisher(Float32MultiArray, 'pot_py_topic', 10)
        self.subscriber_ = self.create_subscription(Float32MultiArray,'pot_values',self.listener,1)
        self.msg = Float32MultiArray()
        self.pagePoses=Page('walk')


    def listener(self, msg):
        
        self.erro = msg.data
        if all((num <= 5 and num>=-5) for num in self.erro):
            self.messagePose = Float32MultiArray()
            self.messagePose.data= self.pagePoses[0]
            self.publisher_.publish(self.messagePose)
            self.pagePoses.pop(0)
        if len(self.pagePoses)==0:
            self.pagePoses=Page('walk')



def Page(page2Run):

    with open(MAIN_DIR+page2Run+'.json', 'r') as pageFile:
        jsonData = json.loads(pageFile.read())
    
    pagePoses = []
    lenRange = len(jsonData["joints_positions"]["pot_0"])
    for indices in range(0,lenRange):
        vetor = [jsonData["joints_positions"][key][indices] for key in jsonData["joints_positions"]]
        pagePoses.append(vetor)
    

    
    return pagePoses




def main():
    
    rclpy.init()
    node = MyPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()