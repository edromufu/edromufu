---
id: running_inference.py
title: running_inference.py
desrcion: Nesta seção teremos um explicação sobre o código running_inference.py
slug: /running_inference
sidebar_position: 3
---

Nesta seção teremos um explicação detalhada sobre o código running_inference.py
  

```py title="object_finder/src/running_inference.py"
#!/usr/bin/env python3
# coding=utf-8

import os
import cv2
import numpy as np
import time


outline_color_list = [(255, 0, 0), (0, 0, 255), (0, 0, 255)]
```


Nesse código temos algumas importações:

- “os” = Biblioteca que possui algumas funções que imitam as do sistema operacional

- “cv2” = OpenCV, Biblioteca para trabalhar com imagens

- “Numpy” = Biblioteca para o processamento de grandes números, vetores e matrizes.

- “time” = Biblioteca que trabalha que possui várias funções referentes ao tempo.


##	get_cnn_files()

```py title="object_finder/src/running_inference.py"
def get_cnn_files():

    robocup_folder = os.path.join(os.path.expanduser('~'), "edromufu/src/vision/robocup_cnn_files")

    config_file = os.path.join(robocup_folder, "yolov4-tiny-obj.cfg")
    weights_file = os.path.join(robocup_folder, "yolov4-tiny-obj_best.weights")

    return read_cnn_architecture(config_file, weights_file)
```

Esta função recupera os nomes dos arquivos de uma rede neural convolucional (CNN) especificando as rotas dos arquivos de configuração e pesos. A função usa a biblioteca os para juntar o caminho do diretório home do usuário com a pasta "visão/robocup_cnn_files" específica onde os arquivos estão localizados. Os arquivos específicos dentro desta pasta são "yolov4-tiny-obj.cfg" e "yolov4-tiny-obj_best.weights". A função então retorna a saída da função *read_cnn_architecture()*, passando os arquivos config_file e weights_file como argumentos.


##	read_cnn_architecture()

```py title="object_finder/src/running_inference.py"
def read_cnn_architecture(config_file, weights_file):

    net = cv2.dnn.readNet(config_file, weights_file, "darknet")

    return net
```

Esta função lê a arquitetura e os pesos de uma rede neural convolucional (CNN) usando a biblioteca OpenCV. Ele recebe dois argumentos, o caminho do arquivo de configuração e o caminho do arquivo de pesos. A função, então, usa a função *cv2.dnn.readNet()* da biblioteca OpenCV para carregar a rede com o config_file e o weights_file dados e passando a string "darknet" como terceiro argumento. Esta função retorna o modelo CNN carregado representado pela variável "net".

## Set_model_input()

```py title="object_finder/src/running_inference.py"
def set_model_input(net):

    model = cv2.dnn.DetectionModel(net)
    model.setInputParams(size=(416,416), scale=1/255, swapRB=True)
    
    return model
```

Esta função define a entrada do modelo de uma rede neural convolucional (CNN) usando a biblioteca OpenCV. Ela recebe um argumento, que é o modelo da rede neural carregado anteriormente (net). A função cria uma variável model, que é uma instância da classe *cv2.dnn.DetectionModel* e passa a rede neural carregada (net) como argumento. Em seguida, é utilizado o método setInputParams da classe model para definir os parâmetros de entrada da rede neural, que são o tamanho da imagem de entrada (416x416 pixels), a escala dos valores de pixel (1/255) e a troca do canal de cor vermelho e azul (swapRB=True). Por fim, a função retorna o modelo configurado.

## Detect_model()

```py title="object_finder/src/running_inference.py"
def detect_model(model, current_frame):
    
    start_time = time.time()
    classes, scores, boxes = model.detect(current_frame, 0.85, 0.4)
    finish_time = time.time()
    fps = 1/(finish_time-start_time)
    
    #print(f"Classes: {classes}, Scores: {scores}")
    #print(f"Boxes: {boxes}")
    #print("FPS: ", fps)
    #print('\n')

    return classes, scores, boxes, int(fps)
```

Esta função detecta objetos em uma imagem usando um modelo de rede neural convolucional (CNN) previamente configurado. Ela recebe dois argumentos, o modelo configurado (model) e a imagem atual (current_frame). A função inicia uma contagem de tempo, chamando a função *time.time()*, para medir o desempenho do modelo. Então, a função usa o método *detect()* do modelo para detectar objetos na imagem atual e obtém três variáveis de saída: classes (as classes dos objetos detectados), scores (a confiança das detecções) e boxes (as caixas delimitadoras dos objetos detectados). Os parâmetros 0.85 e 0.4 passados para *detect()* são respectivamente o limiar de confiança mínima e o limiar de maxima supressão. Em seguida, a função calcula a taxa de quadros por segundo (FPS) como 1 dividido pela diferença entre o tempo final e o tempo inicial. A função retorna as classes, scores, boxes e FPS.

## Draw_results()

```py title="object_finder/src/running_inference.py"
def draw_results(frame, classes, scores, boxes):

    # Draw the bounding boxes

    for i in range(len(boxes)):
        [x_top, y_top, roi_width, roi_height] = boxes[i]
        #p1 = (x_top, y_top)
        #p2 = (x_top + roi_width, y_top + roi_height)
        p3 = (x_top, y_top - 5)

        x_center = round(x_top+(roi_width/2))
        y_center = round(y_top+(roi_height/2))
        radius = round((roi_width+roi_height)/4)
        
        #cv2.rectangle(frame, p1, p2, outline_color_list[classes[i]], 2)
        cv2.circle (frame,(x_center,y_center),radius, outline_color_list[classes[i]],2 )
        confidence = str(round(float(scores[i]), 2))
        
        label = "Ball"

        cv2.putText(frame, label+" " + confidence, p3, cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1)
```

Esta função desenha as detecções de objetos em uma imagem. Ela recebe quatro argumentos: a imagem (frame), as classes dos objetos detectados (classes), as confianças das detecções (scores) e as caixas delimitadoras dos objetos detectados (boxes). A função usa um loop para percorrer todas as caixas delimitadoras e, para cada uma, extrai as coordenadas x e y do canto superior esquerdo, bem como a largura e a altura da caixa. Em seguida, calcula o centro da caixa e o raio. Em vez de desenhar uma caixa em volta do objeto detectado, o código desenha um círculo no centro do objeto com o raio calculado. Em seguida, o código adiciona o texto "Bola" junto com a confiança da detecção na imagem, logo acima do objeto detectado. A função não retorna nenhum valor, pois modifica a imagem passada como argumento.

