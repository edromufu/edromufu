#!/usr/bin/env python3
# coding=utf-8

import rospy
import cv2 as cv
import imutils
import numpy as np

from cv_bridge import CvBridge

from sensor_msgs.msg import Image as visionSimImage
from vision_msgs.msg import Webotsmsg

from LocalizationVision import LocalizationVision



class Localization:

    HEIGHT = 416
    WIDTH = 416
    imagens = ['teste1.jpg','teste2.jpg','teste3.jpg']
    REAL = 'REAL'
    IMAGES = 'IMAGES'

    def __init__(self, source):

        self.vision = LocalizationVision()

        if source == Localization.REAL:
            self.camera = cv.VideoCapture(0)
            # self.infos_publisher = rospy.Publisher('/webots_natasha/localization_inference', Webotsmsg, queue_size=100)
            # self.infos_msg = Webotsmsg()
            # self.infos_msg.searching = True
            while True:
                _, self.current_frame = self.camera.read()
                self.runVision()
            
        elif source == Localization.IMAGES:
            self.current_frame = cv.imread("img/" + Localization.imagens[1])
            self.runVision()


    def runVision(self):
        self.vision.setFrame(self.current_frame)
        self.vision.formatFrame(size=[Localization.HEIGHT,Localization.WIDTH])
        self.vision.getMasks()
        self.vision.findLines()
        self.vision.findIntersections(filtering=False)
        self.vision.drawResults(drawLines=True, drawIntersections=True, drawNeighbours=True)

        for i in self.vision.getIntersections():
            print(i)

        cv.imshow("Tie break",self.vision.tieBreaker())
        self.vision.showResults(resultColored=True, dilatedMask=True)




if __name__ == '__main__':

    rospy.init_node('localization_node', anonymous=False)
    robotFinder = Localization(Localization.REAL)
    
    rospy.spin()