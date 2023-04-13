#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy, os, time

from movement_utils.msg import motors_data

class PageRun():

    def __init__(self):
        
        self.pub_to_u2d2 = rospy.Publisher('u2d2_comm/data2motors', motors_data, queue_size=10)
        self.pub_to_u2d2_msg = motors_data()
        
        self.current_page_running = [] 
        self.rate = rospy.Rate(5)

    def newPageRequest(self):
        if os.path.dirname(__file__):
            os.chdir(os.path.dirname(__file__))
        os.chdir("../pages")
        with open('hi.page','r') as file:
            file_lines = file.read().split('\n')

        # Iterando até penúltimo elemento pois último elemento é vazio
        if not len(file_lines) == 1:
            file_lines = file_lines[:-1]
        for line in file_lines:
            row = (line.split(' '))
            row = [float(coordinate) for coordinate in row]

            self.current_page_running.append(row)
        
        self.sendPageMovement()

    def sendPageMovement(self):
        for pose in self.current_page_running:
            self.pub_to_u2d2_msg.pos_vector = pose
            self.pub_to_u2d2.publish(self.pub_to_u2d2_msg)
            time.sleep(0.55)
        self.current_page_running = [] 
        time.sleep(3)

if __name__ == "__main__":
    rospy.init_node('Page_run_node', anonymous=False)

    page_runner = PageRun()

    while not rospy.is_shutdown():
        page_runner.newPageRequest()

    rospy.spin()