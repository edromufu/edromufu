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
    imagens = ['field.jpg','imagem1.png','imagem2.png','imagem3.png','imagem4.png','imagem5.png','imagem6.png']
    SIMULATION = 'SIMULATION'
    IMAGES = 'IMAGES'
    ratio = 3
    

    def __init__(self, source, debug=False):

        self.vision = LocalizationVision()
        self.source = source
        self.debug = debug
        if self.source == Localization.SIMULATION:
            self.camera_receiver = rospy.Subscriber('/webots_natasha/vision_controller', visionSimImage, self.callback_image)
            # self.infos_publisher = rospy.Publisher('/webots_natasha/localization_inference', Webotsmsg, queue_size=100)
            # self.infos_msg = Webotsmsg()
            # self.infos_msg.searching = True
        elif self.source == Localization.IMAGES:
            self.current_frame = cv.imread("img/" + Localization.imagens[1])
            self.runVision()
        self.cont = 0

    def callback_image(self, camera_msg):

        self.opencv_bridge = CvBridge()
        
        try:
            self.current_frame = self.opencv_bridge.imgmsg_to_cv2(camera_msg, desired_encoding="bgr8")
        
        except Exception as e:
            print(f"{e}")
        
        # Reduz o fps para manter a fluidez
        if self.cont%Localization.ratio == 0:
            self.runVision()
        self.cont = self.cont+1

    def runVision(self):
        self.vision.setFrame(self.current_frame)
        #self.vision.formatFrame(size=[Localization.HEIGHT,Localization.WIDTH])
        self.vision.getMasks()
        self.vision.findLines()
        self.vision.findIntersections(filtering=True)
        self.vision.drawResults(drawLines=True, drawIntersections=True, drawNeighbours=True)

        # Para debug de interseções
        if self.debug:
            for i in self.vision.getIntersections():
                print(i)
            cv.imshow("Tie break",self.vision.tieBreaker())
        self.vision.showResults(mask=True, resultColored=True, dilatedMask=True, source=self.source)

    def runParticleFilter(self):
        pass

if __name__ == '__main__':

    rospy.init_node('localization_node', anonymous=False)
    robotFinder = Localization(Localization.SIMULATION, debug=False)
    rospy.spin()