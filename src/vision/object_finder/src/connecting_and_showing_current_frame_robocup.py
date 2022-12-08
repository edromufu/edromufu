#!/usr/bin/env python3
# coding=utf-8

import rospy
from sensor_msgs.msg import Image as ROS_Image

import cv2
from cv_bridge import CvBridge
import running_inference_robocup as ri

from vision_msgs.msg import Ball
#from vision_msgs.msg import Leftgoalpost
#from vision_msgs.msg import Rightgoalpost
from vision_msgs.msg import Webotsmsg

'''import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()
'''
class Node():

    # Inicializando o nó
    def __init__(self, nome_no):

        self.camera = rospy.get_param('vision/camera')
        self.output_img = rospy.get_param('vision/img_output')

        #Iniciando o nó e obtendo os arquivos que definem a rede neural
        rospy.init_node(nome_no, anonymous = True)
        self.net = ri.get_cnn_files()
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)   
        self.model = ri.set_model_input(self.net)
        self.searching = True

        self.publisher = rospy.Publisher('/webots_natasha/vision_inference', Webotsmsg, queue_size=100)

        #SE FOR NO REAL
        self.get_webcam()

        #SE FOR NO WEBOTS
        #self.connect_to_webots()

    def connect_to_webots(self):
        '''Gets the Vision topic sent from Behavior, and subscribe it.'''

        self.topic_found = False
        while self.topic_found == False:
            try:
                for sublist in rospy.get_published_topics(namespace = "/"):
                    for item in sublist:
                        if "vision_controller" in item:
                            self.vision_topic = item

                rospy.Subscriber(self.vision_topic, ROS_Image, callback = self.convert_ros_image_to_cv2)
                self.topic_found = True
                rospy.spin()
            except Exception:
                pass


    def convert_ros_image_to_cv2(self, message):
        '''Converts the sensor_msgs/Image to Numpy Array'''

        self.opencv_bridge = CvBridge()
        
        try:
            self.current_frame = self.opencv_bridge.imgmsg_to_cv2(message, desired_encoding="bgr8")
        
        except Exception as e:
            print(f"{e}")

        self.send_current_frame_to_inference()

    def get_webcam(self):
        '''Converts the sensor_msgs/Image to Numpy Array'''

        self.opencv_bridge = CvBridge()
        while True:

            self.current_frame = cv2.VideoCapture(f"/dev/video{self.camera}")
            _, self.current_frame = self.current_frame.read()
            self.current_frame = cv2.resize(self.current_frame, (416,416))
            #self.current_frame = cv2.blur(self.current_frame, (10,10))

            key = cv2.waitKey(1)
            

            if key == 27:      #tecla ESC fecha as janelas
                break


            self.send_current_frame_to_inference()

    def send_current_frame_to_inference(self):
        '''Sends the current frame to the inference code.'''
        #self.binary_image = ri.create_binary_image(self.net, self.current_frame)


        self.classes, self.scores, self.boxes, self.fps = ri.detect_model(self.model, self.current_frame)
        if self.output_img:
            self.show_result_frame() # comentar
        self.publish_results() 


    def show_result_frame(self):
        '''Shows the result frame obtained from neural network on OpenCV window.'''

        ri.draw_results(self.current_frame, self.classes, self.scores, self.boxes)
        cv2.imshow("Current Frame", self.current_frame)
        cv2.waitKey(1)

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

            

            # A mesma classe de trave é reconhecida para as duas traves
            # Sabendo disso, a trave direita é a com maior x
            self.dict_of_xs[i] = {"classe": self.classes[i], "x": x}
            print(self.dict_of_xs)

            if self.classes[i] not in self.list_of_classes_in_current_frame:
                self.list_of_classes_in_current_frame.append(self.classes[i])

                if self.classes[i]== 1:
                    ball = Ball()
                    [ball.found, ball.x, ball.y, ball.roi_width, ball.roi_height] = results
                    objects_msg.ball = ball

                '''elif self.classes[i] == 0:
                    leftgoalpost = Leftgoalpost()
                    [leftgoalpost.found, leftgoalpost.x, leftgoalpost.y, leftgoalpost.roi_width, leftgoalpost.roi_height] = results
                    objects_msg.leftgoalpost = leftgoalpost

                else:
                    rightgoalpost = Rightgoalpost()
                    [rightgoalpost.found, rightgoalpost.x, rightgoalpost.y, rightgoalpost.roi_width, rightgoalpost.roi_height] = results
                    objects_msg.rightgoalpost = rightgoalpost'''
            
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


                print("Detectei duas iguais!")
                print(self.dict_of_xs)

        self.publisher.publish(objects_msg)
        '''
        pr.disable()
        s = io.StringIO()
        sortby = SortKey.CUMULATIVE
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())'''

no_visao = Node('visao')
