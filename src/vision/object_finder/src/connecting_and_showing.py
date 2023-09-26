#!/usr/bin/env python3
# coding=utf-8

import rospy, os, sys


import cv2
#from cv_bridge import CvBridge
import running_inference as ri


edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters

#from sensor_msgs.msg import Image as ROS_Image
from vision_msgs.msg import Ball
from vision_msgs.msg import Webotsmsg

sys.setrecursionlimit(100000)

'''import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()
'''

class Node():
        #Init
    def __init__(self,nome_no):

        #Iniciando o ROS
        #Capturar parametros (qual camera e se queremos output de imagem) do launch
        self.camera = rospy.get_param('vision/camera')
        self.output_img = rospy.get_param('vision/img_output')
        self.ajuste = rospy.get_param('vision/ajuste')
        self.bright = rospy.get_param('vision/brilho')

        #Pegando os parametros do behaviour
        self.parameters = BehaviourParameters()
        
        #Iniciando o nó e obtendo os arquivos que definem a rede neural
        rospy.init_node(nome_no, anonymous = True)
        self.net = ri.get_cnn_files()
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)   
        self.model = ri.set_model_input(self.net)
        self.searching = True
        self.cap = cv2.VideoCapture(self.camera,cv2.CAP_ANY)
        self.cap.set(cv2.CAP_PROP_BRIGHTNESS, (self.bright))
        self.publisher = rospy.Publisher(self.parameters.vision2BhvTopic, Webotsmsg, queue_size=100)
        
        #SE FOR NO REAL
        self.get_webcam()

        #SE FOR NO WEBOTS
        #self.connect_to_webots()
        
        


    def get_webcam(self):

        print("\nVisão Operante\n")
        if self.ajuste == True:
            print("Ajuste de Brilho '=' para aumentar e '-' para diminuir.\n")
            print("Para continuar a detecção. Aperte W.\n")

        while not rospy.is_shutdown():
            ret , self.current_frame = self.cap.read()

            if not ret:
                print("\nError capturing frame\n")
                break

                    
            self.current_frame = cv2.resize(self.current_frame, (self.parameters.cameraWidth,self.parameters.cameraHeight))
            self.classes, self.scores, self.boxes, self.fps = ri.detect_model(self.model,self.current_frame)
                
            if self.output_img == True:
                self.show_result_frame()

            if self.ajuste == True:
                self.ajuste_camera()


            self.publish_results()

            if cv2.waitKey(1) == ord("q") :
                self.cap.release()
                cv2.destroyAllWindows()


    def show_result_frame(self):
        '''Shows the result frame obtained from neural network on OpenCV window.'''
        ri.draw_results(self.current_frame, self.classes, self.scores, self.boxes)
        cv2.imshow("Current Frame", self.current_frame)


        
    def publish_results(self):

        objects_msg = Webotsmsg()
        objects_msg.searching = self.searching
        objects_msg.fps = self.fps

        self.list_of_classes_in_current_frame = []
        self.dict_of_xs = dict()

        for i in range(len(self.boxes)):
            [x_top, y_top, roi_width, roi_height] = self.boxes[i]

            x = int(x_top + roi_width/2)
            y = int(y_top + roi_height/2)
            
            results = [True, x, y, roi_width, roi_height]

            

            self.dict_of_xs[i] = {"classe": self.classes[i], "x": x}


            if self.classes[i] not in self.list_of_classes_in_current_frame:
                self.list_of_classes_in_current_frame.append(self.classes[i])

                if self.classes[i]== 1:
                    ball = Ball()
                    [ball.found, ball.x, ball.y, ball.roi_width, ball.roi_height] = results
                    objects_msg.ball = ball
            
            else:
                self.maior_x = -1
                self.menor_x = 500
                for key in self.dict_of_xs.keys():
                    if self.dict_of_xs[key]['classe'] != 0:
                        if self.dict_of_xs[key]['x'] >= self.maior_x:
                            self.maior_x = self.dict_of_xs[key]['x']
                            self.pos_maior_x = key

                        if self.dict_of_xs[key]['x'] < self.menor_x:
                            self.menor_x = self.dict_of_xs[key]['x']
                            self.pos_menor_x = key

                if self.dict_of_xs[self.pos_maior_x]['classe'] == 2:
                    self.dict_of_xs[self.pos_menor_x]['classe'] = 1

                elif self.dict_of_xs[self.pos_maior_x]['classe'] == 1:
                    self.dict_of_xs[self.pos_maior_x]['classe'] = 2

                
        self.publisher.publish(objects_msg)


    def connect_to_webots(self):
        '''Gets the Vision topic sent from Behavior, and subscribe it.'''

        self.topic_found = False
        while self.topic_found == False:
            try:
                for sublist in rospy.get_published_topics(namespace = "/"):
                    for item in sublist:
                        if "vision_controller" in item:
                            self.vision_topic = item

                #rospy.Subscriber(self.vision_topic, ROS_Image, callback = self.convert_ros_image_to_cv2)
                self.topic_found = True
                rospy.spin()
            except Exception:
                pass
            
    def convert_ros_image_to_cv2(self, message):
        '''Converts the sensor_msgs/Image to Numpy Array'''

        #self.opencv_bridge = CvBridge()
        
        #try:
        #    self.current_frame = self.opencv_bridge.imgmsg_to_cv2(message, desired_encoding="bgr8")
        
        #except Exception as e:
        #    print(f"{e}")

        #self.send_current_frame_to_inference()
        #Diferencias códigos da camera e do Webots

    #Configurações da imagem (Brilho) (Parametro passado launch)

    def ajuste_camera(self):
        
        while cv2.waitKey(1) != ord("w"):
            
            if cv2.waitKey(1) == ord('='):
                self.bright = self.bright + 10
                if self.cap.get(cv2.CAP_PROP_BRIGHTNESS) < 64:
                    self.cap.set(cv2.CAP_PROP_BRIGHTNESS, (self.bright))
                else:
                    self.bright = 64                
                print("Brightness property current value:", self.cap.get(cv2.CAP_PROP_BRIGHTNESS))

            if cv2.waitKey(1) == ord('-'):
                self.bright = self.bright - 10
                if self.cap.get(cv2.CAP_PROP_BRIGHTNESS) > -64:
                    self.cap.set(cv2.CAP_PROP_BRIGHTNESS, (self.bright))
                else:
                    self.bright = -64     
                print("Brightness property current value:", self.cap.get(cv2.CAP_PROP_BRIGHTNESS))

            #Atualizar Frame
            _ , self.current_frame = self.cap.read()
            cv2.imshow("Current Frame", self.current_frame)
        self.ajuste = False
        

no_visao = Node('visao')

'''
pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())'''
