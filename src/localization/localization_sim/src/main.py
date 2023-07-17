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
    imagens = ['imagem1.png','imagem2.png','imagem3.png','imagem4.png','imagem5.png','imagem6.png']
    SIMULATION = 'SIMULATION'
    IMAGES = 'IMAGES'

    def __init__(self, source):

        self.vision = LocalizationVision()

        if source == Localization.SIMULATION:
            self.camera_receiver = rospy.Subscriber('/webots_natasha/vision_controller', visionSimImage, self.callback_image)
            # self.infos_publisher = rospy.Publisher('/webots_natasha/localization_inference', Webotsmsg, queue_size=100)
            # self.infos_msg = Webotsmsg()
            # self.infos_msg.searching = True
        elif source == Localization.IMAGES:
            self.current_frame = cv.imread("img/" + Localization.imagens[1])
            self.runVision()

    
    def callback_image(self, camera_msg):

        self.opencv_bridge = CvBridge()
        
        try:
            self.current_frame = self.opencv_bridge.imgmsg_to_cv2(camera_msg, desired_encoding="bgr8")
        
        except Exception as e:
            print(f"{e}")
        
        self.runVision()

    def runVision(self):
        self.vision.formatFrame(self.current_frame,size=[Localization.HEIGHT,Localization.WIDTH])
        self.vision.showResults(original=True)




if __name__ == '__main__':

    rospy.init_node('localization_node', anonymous=False)
    robotFinder = Localization(Localization.IMAGES)
    
    rospy.spin()