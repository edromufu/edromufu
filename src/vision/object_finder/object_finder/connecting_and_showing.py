#!/usr/bin/env python3
# coding=utf-8

import rclpy, os, sys
from rclpy.node import Node
import time 
import cv2
#from cv_bridge import CvBridge
import sys

import object_finder.running_inference as ri    #Importa o arquivo python do diretorio de execução para não acontecer erros devido a execução em ROS2 ou em python3


edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'
sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
#from behaviour_parameters import BehaviourParameters

from sensor_msgs.msg import Image as ROS_Image
from vision_msgs.msg import Ball
from vision_msgs.msg import Webotsmsg

sys.setrecursionlimit(100000)

'''
import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()
'''



class Visao(Node):

        #Init
    def __init__(self,nome_no):
        ######Iniciando o nó
        super().__init__(nome_no)
        self.get_logger().info('Nó, iniciado')

        #Iniciando o ROS
        #Capturar parametros (qual camera e se queremos output de imagem) do launch

        #Declara a existência dos parametros e recebe os valores padrões ou definidos pelo ros        
        self.camera = self.declare_parameter('vision/camera',0).get_parameter_value().integer_value
        self.output_img = self.declare_parameter('vision/img_output',False).get_parameter_value().bool_value
        self.ajuste = self.declare_parameter('vision/ajuste',False).get_parameter_value().bool_value
        self.bright = self.declare_parameter('vision/brilho',4).get_parameter_value().integer_value
        
        #Retorna os valores para verificação
        print(f"\nCamera:{self.camera}\nOutput:{self.output_img}\nAjuste:{self.ajuste}\nBrilho:{self.bright}\n")

        #Pegando os parametros do behaviour
        #self.parameters = BehaviourParameters()
             
        #Obtendo os arquivos que definem a rede neural
        
        self.model = ri.set_model_input()
        self.searching = True


        self.publisher = self.create_publisher(Webotsmsg,'vision2BhvTopic', 100)

        #SE FOR NO REAL
        print("\n==Visão Operante==\n")
        self.get_webcam()

        #SE FOR NO WEBOTS
        #self.connect_to_webots()
        
        
    def get_webcam(self):

        self.cap = cv2.VideoCapture(self.camera,cv2.CAP_ANY)
        self.cap.set(cv2.CAP_PROP_BRIGHTNESS, (self.bright))
        
        if self.ajuste == True:
            print("Ajuste de Brilho '=' para aumentar e '-' para diminuir.\n")
            print("Para continuar a detecção. Aperte W.\n")
            self.ajuste_camera()

        #Enquato o nó estiver ativo o looping é executado
        while rclpy.ok():
            start_time=time.time()
            
            #Le um frame da camera e redimensiona a imagem
            ret, self.current_frame = self.cap.read()
            #self.current_frame = cv2.resize(self.current_frame, (640,480))
            #self.current_frame = cv2.blur(self.current_frame, (10,10))
            #self.current_frame = cv2.resize(self.current_frame, (self.parameters.cameraWidth,self.parameters.cameraHeight))
            
            #Se a leitura da camera falhar imprime uma mensagem e tenta de novo
            if not ret:
                print("\nError capturing frame\n")
                self.get_webcam()
            
            self.classes, self.scores, self.boxes,self.inference_frame = ri.detect_model(self.model,self.current_frame,self.output_img)
            #Para testar a eficiencia da inferencia utiliza-se a linha abaixo e compara a execução a inferencia
            #self.classes, self.scores, self.boxes, self.fps,self.inference_frame = 1,1,1,1,self.current_frame
            
            if self.output_img:
                cv2.imshow("Current Frame", self.inference_frame)
            
            #Calculo do fps de cada loop (envolve tanto o tempo da inferencia quanto o da camera)
            finish_time=time.time()
            self.fps=1/(finish_time-start_time)
            print(f'FPS total: {self.fps}\n')

            #Acessa a função que publicará os resultados
            self.publish_results()

            #Ao apertar a tecla 'q' libera a camera, destroi janelas do opencv abertas e desliga o nó
            if cv2.waitKey(1) == ord("q") :
                self.cap.release()
                cv2.destroyAllWindows()
                self.get_logger().warn('Tecla "q" pressionada. Encerrando.')
                rclpy.shutdown()


        
    def publish_results(self):

        objects_msg = Webotsmsg()
        objects_msg.searching = self.searching
        objects_msg.fps = int(self.fps)

        self.list_of_classes_in_current_frame = []
        self.dict_of_xs = dict()

        for i in range(len(self.boxes)):
            
            [x, y, roi_width, roi_height] = self.boxes[i]

            results = [True, int(x), int(y), int(roi_width), int(roi_height)]

            self.dict_of_xs[i] = {"classe": self.classes[i], "x": x}


            if self.classes[i] not in self.list_of_classes_in_current_frame:
                self.list_of_classes_in_current_frame.append(self.classes[i])

                if self.classes[i]== 0: #0 é o indice da bola
                    ball = Ball()
                    [ball.found, ball.x, ball.y, ball.roi_width, ball.roi_height] = results
                    objects_msg.ball = ball

            else:
                self.maior_x = -1
                self.menor_x = 500
                for key in self.dict_of_xs.keys():
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

    #Não está atualizado para Ros2
    def connect_to_webots(self):
        '''Gets the Vision topic sent from Behavior, and subscribe it.'''

        self.topic_found = False
        while self.topic_found == False:
            try:
                for sublist in rclpy.get_published_topics(namespace = "/"):
                    for item in sublist:
                        if "vision_controller" in item:
                            self.vision_topic = item

                #rclpy.create_subscriber(self.vision_topic, ROS_Image, callback = self.convert_ros_image_to_cv2)
                self.topic_found = True
                rclpy.spin()
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

        #Realiza um loop para acessar a imagem da camera e, ao apertar uma tecla, aumenta ou diminui o brilho ou sai do ajuste

        while True:
            
            key=cv2.waitKey(1)

            if key== ord("w"):
                break

            if key == ord('='):
                self.bright = self.bright + 10
                if self.cap.get(cv2.CAP_PROP_BRIGHTNESS) < 64:
                    self.cap.set(cv2.CAP_PROP_BRIGHTNESS, (self.bright))
                else:
                    self.bright = 64                
                print("Brightness property current value:", self.cap.get(cv2.CAP_PROP_BRIGHTNESS))

            if key == ord('-'):
                self.bright = self.bright - 10
                if self.cap.get(cv2.CAP_PROP_BRIGHTNESS) > -64:
                    self.cap.set(cv2.CAP_PROP_BRIGHTNESS, (self.bright))
                else:
                    self.bright = -64     
                print("Brightness property current value:", self.cap.get(cv2.CAP_PROP_BRIGHTNESS))

            #Atualizar Frame
            _ , self.current_frame = self.cap.read()
            self.current_frame = cv2.resize(self.current_frame, (640,480))
            cv2.imshow("Brightness", self.current_frame)
        
        self.ajuste = False
        

def main():
    rclpy.init()

    no_visao = Visao('Visao')


    '''
    pr.disable()
    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
    '''
    
if __name__=='__main__':
    main()