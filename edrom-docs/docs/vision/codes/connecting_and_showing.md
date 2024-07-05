---
id: connecting_and_showing.py
title: connecting_and_showing.py
desrcion: Nesta seção teremos um explicação sobre o código connecting_and_showing.py
slug: /connecting_and_showing
sidebar_position: 2
---

Nesta seção teremos um explicação detalhada sobre o código connecting_and_showing.py
  

```py title="object_finder/src/connecting_and_showing.py"
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
```


Nesse código temos algumas importações:

- __“rclpy”__ = Biblioteca de Python para o ROS 2

- __“ROS_Image”__ = Tipo de mensagem utilizada pelo webots, que neste caso utilizamos para receber as imagens quando o código é utilizado no webots

- __“cv2”__ = OpenCV, Biblioteca para trabalhar com imagens

- __“CvBridge”__ = Biblioteca que serve para converter as imagens, que neste caso utilizamos para converter as imagens recebidas pelo webots para um formato que o OpenCV trabalha

- __“running_inference”__ = Outro código da visão que será explicado logo em seguida

- __“Ball”__ e __“Webotsmsg”__ = Formatos de mensagem que publicamos para o Behaviour

- __“sys”__ = Biblioteca sys que tem funções de gerenciamento de arquivos

Após as importações temos algumas definições:

- __“sys.setrecursionlimit”__ = Define a profundidade máxima da pilha do interpretador Python para o limite setado.




```py title="object_finder/src/connecting_and_showing.py"
'''import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()
'''
```

```py title="object_finder/src/connecting_and_showing.py"
'''
pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())'''
```

Temos também em seguida, algumas funções auxiliares que são utilizadas para mostrar para nós, o tempo de execução do programa e quanto tempo o programa gasta em cada função do código. Essa função é ótima para ajudar na otimização do nosso código.

##	init()

```py title="object_finder/src/connecting_and_showing.py"
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
        self.feedback = self.declare_parameter('vision/feedback',False).get_parameter_value().bool_value
        
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
```

A função construtora da nossa classe, onde setamos e buscamos algumas informações.

-	__“get_parameter_value”__ = Primeira coisa que fazemos é buscar as informações fornecidas pelo nosso launch e colocar nas variaveis __“self.camera”__, ”__self.ouput_img”__, __“self.ajuste”__, __“self.bright”__

-	__“super().init”__ = Iniciamos aqui o nosso nó vision onde rodarão os processos.
  
-	__“ri.set_model_input”__ = Função do __“running_inference.py”__ que obtém os arquivos que definem a rede neural.
  
-	__“self.searching”__: Inicializamos a nossa variável de procura para __“True”__, para garantir que a detecção está rodando corretamente.

-	__“create_publisher”__: Iniciamos nosso publisher que irá publicar os resultados da nossa detecção.

-	__“get_webcam”__ e __“connect_to_webots”__ = começamos a rodar nossa primeira função dentro desse código. Se queremos que o código rode na robo real utilizamos __"get_webcam()"__ e se quisermos que ele rode dentro do webots utilizamos __"connect_to_webots()"__.

##	Get_webcam()

```py title="object_finder/src/connecting_and_showing.py"
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
            
            #Lê um frame da camera e redimensiona a imagem
            ret, self.current_frame = self.cap.read()
            #self.current_frame = cv2.resize(self.current_frame, (640,480))
            #self.current_frame = cv2.blur(self.current_frame, (10,10))
            #self.current_frame = cv2.resize(self.current_frame, (self.parameters.cameraWidth,self.parameters.cameraHeight))
            
            #Se a leitura da camera falhar imprime uma mensagem e tenta de novo
            if not ret:
                print("\nError capturing frame\n")
                self.get_webcam()
            
            self.classes, self.scores, self.boxes,self.inference_frame = ri.detect_model(self.model,self.current_frame)
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
```

A função *get_webcam* é usada para capturar frames da webcam e usar o modelo de detecção de objetos para detectar objetos em cada frame. A função começa com a impressão de uma mensagem no console informando sobre a detecção de objetos na visão operante.

O loop é iniciado e, dentro dele, a função *cap.read()* é usada para capturar um frame da webcam e retornar o valor *ret* que indica se a captura foi bem-sucedida ou não. O frame capturado é armazenado na variável *self.current_frame*.

A seguir, a função *ri.detect_model* é chamada para detectar objetos no frame capturado. O modelo é passado como primeiro argumento e o frame capturado é passado como segundo argumento. A função retorna quatro valores: *classes*, *scores*, *boxes* e *fps*. Esses valores são armazenados nas respectivas variáveis de instância do objeto.

Se a variável *self.output_img* for *True*, a função *self.show_result_frame* é chamada para mostrar o resultado da detecção de objetos na tela. Se a variável *self.ajuste* for *True*, a função *self.ajuste_camera* é chamada para ajustar o brilho da webcam.

Por fim, a função *self.publish_results* é chamada para publicar os resultados da detecção de objetos. O loop é repetido até que a tecla __"q"__ seja pressionada, momento em que o recurso da webcam é liberado e todas as janelas do OpenCV são destruídas.

## Publish_result_frame()

```py title="object_finder/src/connecting_and_showing.py"
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
    
```

Esta função itera sobre a lista de caixas de objetos detectados, armazenados em "self.boxes", e calcula a posição x e y de cada objeto como o ponto central da caixa de ROI (região de interesse). Além disso, a função armazena a classe de cada objeto detectado em "self.classes" em um dicionário "self.dict_of_xs" com a classe como a chave e as posições x e y como valores.

Se a classe de um objeto não estiver presente na lista de classes __"self.list_of_classes_in_current_frame"__, ela é adicionada a esta lista e, se a classe for *"0"*, os resultados são usados para preencher um objeto da classe __"Ball"__.

Se houver duas classes iguais na lista de classes __"self.list_of_classes_in_current_frame"__, a função determina as posições x mais alta e mais baixa e, em seguida, altera as classes dos objetos nessas posições.

Finalmente, o objeto __"objects_msg"__ é publicado usando um objeto publisher __"self.publisher"__.

## Connect_to_webots() e convert_ros_image_to_cv2()

```py title="object_finder/src/connecting_and_showing.py"
def connect_to_webots(self):

    '''Pega o topico da visão que está sendo enviado da visão e se inscreve nele.'''
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

        self.opencv_bridge = CvBridge()
        
        try:
          self.current_frame = self.opencv_bridge.imgmsg_to_cv2(message, desired_encoding="bgr8")
        
        except Exception as e:
           print(f"{e}")

        self.send_current_frame_to_inference()
        

```

A primeira função, __"connect_to_webots()"__, é usada para se conectar ao tópico *"vision_controller"* publicado pelo behaviour que pega do Webots (um simulador para robôs) e se inscreve nele. A função faz um loop enquanto a variável de instância *"topic_found"* for falsa. Dentro do loop, a função usa o método *rospy.get_published_topics()* para obter uma lista de tópicos publicados no namespace "/". Em seguida, percorre a lista procurando por "vision_controller" e armazena o nome do tópico encontrado na variável de instância "vision_topic". Em seguida, se inscreve no tópico usando o *rospy.Subscriber()* e passando o nome do tópico e a função "callback" para ser chamada quando novos dados são publicados no tópico. 

A segunda função, __"convert_ros_image_to_cv2()"__, é usada para converter a imagem publicada no tópico "vision_controller" para um formato que o OpenCV possa ler. Ela é passada como "callback" para o *rospy.Subscriber()* na primeira função. A função usa a classe *CvBridge()* da biblioteca roscpp_opencv para fazer a conversão e armazena

## Ajuste_camera()

```py title="object_finder/src/connecting_and_showing.py"
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
```

Esta função ajusta as configurações de brilho de uma câmera usando o OpenCV. Enquanto o usuário não pressionar a tecla __"w"__, o loop irá continuar verificando se o usuário pressionou as teclas __"+"__ ou __"-"__. Se o usuário pressionar __"+"__, o brilho da câmera será aumentado em 10 e, se o valor de brilho for menor que 64, o brilho será ajustado. Caso contrário, o valor de brilho será mantido em 64. O mesmo processo é seguido quando o usuário pressiona __"-"__, mas neste caso o brilho é diminuído em 10. A cada iteração do loop, a função também atualiza o frame da câmera e mostra a imagem atual. Quando o usuário pressiona __"w"__, a função sai do loop e define a variável de instância *"ajuste"* como falso.


