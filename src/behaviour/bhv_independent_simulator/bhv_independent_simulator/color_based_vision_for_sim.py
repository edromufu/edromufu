#!/usr/bin/env python3
# coding=utf-8

##!!! CÓDIGO PROVISÓRIO DEVIDO À PROBLEMA NA VISÃO, RETORNAR À DETECÇÃO PELA REDE NEURAL ASSIM QUE POSSIVEL

#import rospy (1)
import rclpy, sys #(1)
import cv2
import imutils
import numpy as np

from cv_bridge import CvBridge

#from sensor_msgs.msg import Image as visionSimImage (2)
from sensor_msgs.msg import Image as VisionSimImage #(2)
from vision_msgs.msg import Webotsmsg

ORANGE_MAX = [255, 255, 255]
ORANGE_MIN = [130, 60, 50]

[HEIGHT,WIDTH] = [416,416]

class BallFinder(object):

    def __init__(self):

        #self.camera_receiver = rospy.Subscriber('/webots_natasha/vision_controller', visionSimImage, self.callback_image) (3)
        self.camera_receiver = self.node.create_subscription(VisionSimImage, '/webots_natasha/vision_controller', self.callback_image, rclpy.qos.QoSProfile()) #(3)
        #self.infos_publisher = rospy.Publisher('/webots_natasha/vision_inference', Webotsmsg, queue_size=100) (4)
        self.infos_publisher = self.node.create_publisher(Webotsmsg, '/webots_natasha/vision_inference', 100) #(4)
        
        self.infos_msg = Webotsmsg()
        self.infos_msg.searching = True
    
    def callback_image(self, camera_msg):

        self.opencv_bridge = CvBridge()
        
        try:
            self.current_frame = self.opencv_bridge.imgmsg_to_cv2(camera_msg, desired_encoding="bgr8")
        
        except Exception as e:
            print(f"{e}")
        
        self.findBall(ORANGE_MIN, ORANGE_MAX)

    def findBall(self, minColor, maxColor):

        # Pega o frame, muda seu tamanho e o embaça (para melhorar o processamento) e o converte de RGB para HSV
        self.frame = self.current_frame
        self.frame = imutils.resize(self.frame, width=WIDTH, height=HEIGHT)
        blurred = cv2.GaussianBlur(self.frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        # Cria a mascara para a cor definida, e remove "chiados" para melhorar a identificação da bola
        lowerColor = np.array(minColor)
        upperColor = np.array(maxColor)
        mask = cv2.inRange(hsv, lowerColor, upperColor)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # Encontra todos os contornos das areas brancas da mascara
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        center = None

        # Inicializa algumas variaveis para que possam ser referenciadas mesmo se o if não for executado
        x = 0
        y = 0
        radius = 0

        # Caso seja encontrado algum contorno, entra no if, então é calculado e desenhado o menor circulo que engloba o maior contorno encontrado
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            if radius > 2:
                cv2.circle(self.frame, (int(x), int(y)), int(radius), (0, 0, 255), 2)
                cv2.circle(self.frame, center, 5, (0, 0, 255), -1)

        # As informações da bola são retornadas
        self.infos_msg.ball.found = len(cnts)>0
        self.infos_msg.ball.x = int(x)
        self.infos_msg.ball.y  = int(y)
        self.infos_msg.ball.roi_height = int(2*radius)
        self.infos_msg.ball.roi_width = int(2*radius)

        # A imagem é exibida
        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)

        self.infos_publisher.publish(self.infos_msg)

if __name__ == '__main__':

    #rospy.init_node('Bhv_simulated_vision_node', anonymous=False) (5)
    rclpy.init(args=sys.argv) #(5)
    node = rclpy.create_node('Bhv_simulated_vision_node') #(5)

    finder = BallFinder()

    #rospy.spin() (6)
    rclpy.spin(node) #(6)