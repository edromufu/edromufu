---
id: running_inference.py
title: running_inference.py
description: Nesta seção teremos um explicação sobre o código running_inference.py
slug: /running_inference
sidebar_position: 3
---

Nesta seção teremos um explicação detalhada sobre o código running_inference.py
  

```py title="object_finder/src/running_inference.py"
#!/usr/bin/env python3
# coding=utf-8

from ultralytics import YOLO
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

- "ultralytics" = Função da biblioteca YOLO utilizada para implementação e execução de algoritmos de detecção de objetos.


## Set_model_input()

```py title="object_finder/src/running_inference.py"

def set_model_input():
        
    '''Gets the CNN filenames, despite the PC file structure.'''
    
    robocup_folder = os.path.join(os.path.expanduser('~'), "edromufu/src/vision/robocup_cnn_files")
    net = os.path.join(robocup_folder, "yolov8n-vision.pt")
    
    model = YOLO(net)
    
    return model
```

Esta função define a entrada do modelo de uma rede neural convolucional (CNN) utilizando a biblioteca OpenCV. Ela recebe nenhum argumento e retorna uma instância do modelo YOLO carregado com os arquivos de configuração e pesos especificados. Inicialmente, o caminho para os arquivos é construído concatenando o diretório home do usuário com a pasta específica onde os arquivos estão localizados. Os arquivos específicos dentro desta pasta são "yolov8n-vision.pt". Em seguida, a função carrega o modelo YOLO com o arquivo especificado utilizando a classe YOLO. O modelo carregado é então retornado.


## Detect_model()

```py title="object_finder/src/running_inference.py"

def detect_model(model, current_frame):
    
    start_time = time.time()
    results = model.predict(source=current_frame,
                            conf=0.25,  
                            imgsz=(640,448), 
                            max_det=10, 
                            device=0, 
                            verbose=False) 
    
    classes = results[0].boxes.cls.tolist()
    scores = results[0].boxes.conf.tolist() 
    boxes = results[0].boxes.xywh.tolist()  

    finish_time = time.time()
    fps_inf = 1/(finish_time-start_time)
    
    print(f"Classes: {classes}, Scores: {scores}")
    print(f"Boxes: {boxes}")
    print(f'FPS da inferência: {fps_inf}')


    inference_frame=results[0].plot()

    return classes, scores, boxes, inference_frame
```

Esta função detecta objetos em uma imagem utilizando um modelo de rede neural convolucional (CNN) previamente configurado. Ela recebe dois argumentos: o modelo configurado (model) e o quadro atual (current_frame). A função inicia uma contagem de tempo para medir o desempenho do modelo utilizando a função time.time(). Em seguida, a função chama o método predict() do modelo para realizar a detecção de objetos na imagem atual. Os parâmetros fornecidos para predict() incluem o quadro de origem (source), o limiar de confiança mínima (conf), o tamanho da imagem (imgsz), o número máximo de detecções por imagem (max_det), o dispositivo de execução (device) e a opção de verbose (verbose). A função então extrai as classes (índices de cada objeto identificado), scores (nível de confiança respectivo a cada objeto identificado) e caixas delimitadoras (coordenadas x e y do centro, altura e comprimeto para cada objeto) das detecções realizadas. Posteriormente, calcula a taxa de quadros por segundo (FPS) como o inverso da diferença entre o tempo final e o tempo inicial. Por fim, a função retorna as classes, scores, caixas delimitadoras e uma representação visual do resultado da inferência.
