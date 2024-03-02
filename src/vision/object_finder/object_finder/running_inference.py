#!/usr/bin/env python3
# coding=utf-8

from ultralytics import YOLO
import os
import cv2
import numpy as np
import time


outline_color_list = [(255, 0, 0), (0, 0, 255), (0, 0, 255)]

def set_model_input():
        
    '''Gets the CNN filenames, despite the PC file structure.'''

    #Forçando o path dos arquivos e passando o nome do modelo pré-treinado para uma variável
    robocup_folder = os.path.join(os.path.expanduser('~'), "edromufu/src/vision/robocup_cnn_files")
    net = os.path.join(robocup_folder, "yolov8-larc23.pt")

    #Recebe o modelo no YOLO 
    model = YOLO(net)
    
    
    return model

    

def detect_model(model, current_frame, output_img ):
    
    start_time = time.time()
    #Testar imgsz=(640,448), ver se não prejudica a detecção comparado a (640,480)

    results = model.predict(source=current_frame,
                            conf=0.25,   #conf = limiar de confiança mínima
                            imgsz=(640,448), #imgsz = Tamanho da imagem (h, w) 
                            max_det=10, #max_det = número máximo de detecções por imagem
                            device=0, #device = Escolhe qual dispositivo rodar a detecção (cpu, gpu, cuda)
                            verbose=False) #verbose = Não imprime a saída da função na tela
    
    classes = results[0].boxes.cls.tolist()
    scores = results[0].boxes.conf.tolist() 
    boxes = results[0].boxes.xywh.tolist()  
    print(results[0].boxes)

    finish_time = time.time()
    fps_inf = 1/(finish_time-start_time)
    

    print(f"Classes: {classes}, Scores: {scores}")
    print(f"Boxes: {boxes}")
    print(f'FPS da inferência: {fps_inf}')


    inference_frame=results[0].plot()

    return classes, scores, boxes, inference_frame
