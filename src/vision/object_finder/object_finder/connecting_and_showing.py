#!/usr/bin/env python3
# coding=utf-8

import rclpy, os, sys
from rclpy.node import Node
import time 
import cv2
#from cv_bridge import CvBridge
import sys
import numpy as np

import pyrealsense2 as rs
import object_finder.running_inference as ri    #Importa o arquivo python do diretorio de execução para não acontecer erros devido a execução em ROS2 ou em python3


edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'
sys.path.append(edrom_dir+'behaviour/transitions_and_states/transitions_and_states')
from behaviour_parameters import BehaviourParameters

from sensor_msgs.msg import Image as ROS_Image
from vision_msgs.msg import *

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
        self.camera = self.declare_parameter('vision/camera',0).get_parameter_value().integer_value # Escolhe qual opção de camera usar, caso exista mais de uma conectada
        self.output_img = self.declare_parameter('vision/img_output',True).get_parameter_value().bool_value # Escolhe se retorna a imagem na tela
        self.ajuste = self.declare_parameter('vision/ajuste',False).get_parameter_value().bool_value # Ajuste manual de brilho
        self.bright = self.declare_parameter('vision/brilho',4).get_parameter_value().integer_value # Definição do brilho de forma direta
        self.feedback = self.declare_parameter('vision/feedback',False).get_parameter_value().bool_value # 
        
        #Retorna os valores para verificação
        print(f"\nCamera:{self.camera}\nOutput:{self.output_img}\nAjuste:{self.ajuste}\nBrilho:{self.bright}\n")

        #Pegando os parametros do behaviour
        #self.parameters = BehaviourParameters()
             
        #Obtendo os arquivos que definem a rede neural
        
        self.model = ri.set_model_input()
        self.searching = True

        self.parameters = BehaviourParameters()

        self.publisher = self.create_publisher(Webotsmsg,self.parameters.vision2BhvTopic, 100)

        #SE FOR NO REAL
        print("\n==Visão Operante==\n")
        self.get_webcam()

        #SE FOR NO WEBOTS
        #self.connect_to_webots()

    def initialize_camera(self):
        # Configuração do pipeline
        pipeline = rs.pipeline()
        config = rs.config()

        config.enable_stream(rs.stream.depth, 848, 480, rs.format.z16, 30)
        config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

        # Começa a captura
        pipeline.start(config)

        return pipeline
        
    def get_webcam(self):

        #!self.cap = cv2.VideoCapture(self.camera,cv2.CAP_ANY)
        #!self.cap.set(cv2.CAP_PROP_BRIGHTNESS, (self.bright))
        
        pipeline = self.initialize_camera()

        if self.ajuste == True:
            print("Ajuste de Brilho '=' para aumentar e '-' para diminuir.\n")
            print("Para continuar a detecção. Aperte W.\n")
            self.ajuste_camera()

        #Enquato o nó estiver ativo o looping é executado
        while rclpy.ok():
            start_time=time.time()
            
            #Lê um frame da camera monocular e redimensiona a imagem
            #ret, self.current_frame = self.cap.read()


            # Wait for a coherent pair of frames: depth and color
            frames = pipeline.wait_for_frames()
            self.depth_frame = frames.get_depth_frame()
            self.intrinsics = self.depth_frame.profile.as_video_stream_profile().intrinsics
            color_frame = frames.get_color_frame()
            
            if not self.depth_frame or not color_frame:
                print("\nError capturing frame\n")
                continue

            # Convert images to numpy arrays
            depth_image = np.asanyarray(self.depth_frame.get_data())
            self.current_frame = np.asanyarray(color_frame.get_data())
            
            #Se a leitura da camera falhar imprime uma mensagem e tenta de novo
            #!if not ret:
            #!    print("\nError capturing frame\n")
            #!    self.get_webcam()
            
            self.classes, self.scores, self.boxes,self.inference_frame = ri.detect_model(self.model,self.current_frame)
            #Para testar a eficiencia da inferencia utiliza-se a linha abaixo e compara a execução a inferencia
            #self.classes, self.scores, self.boxes, self.fps,self.inference_frame = 1,1,1,1,self.current_frame
            
            if self.output_img:
                # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
                depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

                cv2.imshow("Current Frame", self.inference_frame)
                cv2.imshow("Current Depth Frame", depth_colormap)

            
            #Calculo do fps de cada loop (envolve tanto o tempo da inferencia quanto o da camera)
            finish_time=time.time()
            self.fps=1/(finish_time-start_time)
            print(f'FPS total: {self.fps}\n')

            #Acessa a função que publicará os resultados
            self.publish_results()

            #Ao apertar a tecla 'q' libera a camera, destroi janelas do opencv abertas e desliga o nó
            if cv2.waitKey(1) == ord("q") :
                #!self.cap.release()
                pipeline.stop()
                cv2.destroyAllWindows()
                self.get_logger().warn('Tecla "q" pressionada. Encerrando.')
                rclpy.shutdown()

    def setup_object(self, obj_data):
        obj = Objects()
        [obj.found, obj.x, obj.y, obj.roi_width, obj.roi_height, _] = obj_data
        [obj.x_position, obj.y_position, obj.z_position] = self.pos_object_3d(obj.x, obj.y)
        return obj
    
    def pos_object_3d(self,x,y):

        depth_value = self.depth_frame.get_distance(x, y) # retorna a distância em metros para o ponto específico (x, y) na imagem de profundidade.
        # Converte para coordenadas 3D (utiliza a função rs.rs2_deproject_pixel_to_point)
        point = rs.rs2_deproject_pixel_to_point(self.intrinsics, (x,y), depth_value) #  converte as coordenadas do pixel para coordenadas 3D, utilizando as informações de intrínsecos da câmera.
        return point
        
    def pos_multi_objects_3d(self, x_coords, y_coords):
        # Inicializa listas para armazenar as posições x, y e z
        x_positions = []
        y_positions = []
        z_positions = []

        # Itera sobre as coordenadas de pixel e calcula a posição 3D para cada par
        for x, y in zip(x_coords, y_coords):
            point = self.pos_object_3d(x, y)  # Retorna [x_position, y_position, z_position] para cada par (x, y)
            x_positions.append(point[0])
            y_positions.append(point[1])
            z_positions.append(point[2])

        # Retorna três listas: x_positions, y_positions, z_positions
        return x_positions, y_positions, z_positions


    # Função de preenchimento de MultiObjects
    def create_multi_objects(self,detection_list):
        # Inicializa a mensagem MultiObjects
        multi_objects = MultiObjects()
        multi_objects.found = True  # Define como encontrado (True)

        # Desempacota os valores para atribuir aos vetores
        multi_objects.x = [obj[1] for obj in detection_list]
        multi_objects.y = [obj[2] for obj in detection_list]
        multi_objects.roi_width = [obj[3] for obj in detection_list]
        multi_objects.roi_height = [obj[4] for obj in detection_list]
        
        multi_objects.x_position, multi_objects.y_position, multi_objects.z_position = self.pos_multi_objects_3d(multi_objects.x,multi_objects.y) 


        return multi_objects

    '''
    # Exemplo de uso para cada tipo de objeto de interseção
    if x_intersection_objects:
        objects_msg.x_intersection = create_multi_objects(x_intersection_objects)
    
    if l_intersection_objects:
        objects_msg.l_intersection = create_multi_objects(l_intersection_objects)
    
    if t_intersection_objects:
        objects_msg.t_intersection = create_multi_objects(t_intersection_objects)
    
    if center_objects:
        objects_msg.center = create_multi_objects(center_objects)'''


    def publish_results(self):

        objects_msg = Webotsmsg()
        objects_msg.searching = self.searching
        objects_msg.fps = int(self.fps)

        self.list_of_classes_in_current_frame = []
        self.dict_of_xs = dict()

        ball_objects = []
        robot_objects = []
        right_goal_objects = []
        left_goal_objects = []
        x_intersection_objects = []
        l_intersection_objects = []
        t_intersection_objects = []
        center_objects = []
        
        for i in range(len(self.boxes)):
            [x, y, roi_width, roi_height] = self.boxes[i]

            results = [True, int(x), int(y), int(roi_width), int(roi_height), int(self.scores[i])]

            self.dict_of_xs[i] = {"classe": self.classes[i], "x": x}

            if self.classes[i] not in self.list_of_classes_in_current_frame:
                self.list_of_classes_in_current_frame.append(self.classes[i])

            if self.classes[i] == 0:
                ball_objects.append(results)
            elif self.classes[i] == 1:
                robot_objects.append(results)
            elif self.classes[i] == 2:
                right_goal_objects.append(results)
            elif self.classes[i] == 3:
                left_goal_objects.append(results)
            elif self.classes[i] == 4:
                l_intersection_objects.append(results)
            elif self.classes[i] == 5:
                t_intersection_objects.append(results)
            elif self.classes[i] == 6:
                x_intersection_objects.append(results)
            elif self.classes[i] == 7:
                center_objects.append(results)
               
        ball_objects.sort(key=lambda obj: obj[5])  # ordenar em relação ao nivel de confiança
        robot_objects.sort(key=lambda obj: obj[5])  # ordenar em relação a posição x
        right_goal_objects.sort(key=lambda obj: obj[1])  # ordenar em relação a posição x
        left_goal_objects.sort(key=lambda obj: obj[1])  # ordenar em relação a posição x

        
        if ball_objects:
            objects_msg.ball = self.setup_object(ball_objects[-1]) # bola com maior nivel de confiança

		#! Conferir o q fazer com essas mensagem
        if robot_objects:
            objects_msg.robot = self.setup_object(robot_objects[-1])
        
        if right_goal_objects:
            objects_msg.rightgoal = self.setup_object(right_goal_objects[-1])

        if left_goal_objects:
            objects_msg.leftgoal = self.setup_object(left_goal_objects[0])  # trave mais a esquerda)

        if x_intersection_objects:
            objects_msg.x_intersection = self.create_multi_objects(x_intersection_objects)

        if l_intersection_objects:
            objects_msg.l_intersection = self.create_multi_objects(l_intersection_objects)

        if t_intersection_objects:
            objects_msg.t_intersection = self.create_multi_objects(t_intersection_objects)

        if center_objects:
            objects_msg.center = self.create_multi_objects(center_objects)

        # Cálculo da posição central do gol
        if objects_msg.ball.found:
            if objects_msg.rightgoal.found and objects_msg.leftgoal.found:
                center_goal = (objects_msg.rightgoal.x + objects_msg.leftgoal.x) / 2
                objects_msg.center_goal = center_goal
            
            elif objects_msg.rightgoal.found:
                objects_msg.center_goal = objects_msg.rightgoal.x / 2  # suposição do centro do gol quando se encontra apenas a trave direita

            elif objects_msg.leftgoal.found:
                camera_rightmost_x = self.intrinsics.width  # exemplo, depende da resolução da câmera
                objects_msg.center_goal = (camera_rightmost_x + objects_msg.leftgoal.x) / 2  # suposição do centro do gol quando se encontra apenas a trave esquerda

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