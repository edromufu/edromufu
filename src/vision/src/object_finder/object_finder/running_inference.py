#!/usr/bin/env python3
# coding=utf-8

from ultralytics import YOLO
import os
import cv2
import numpy as np
import time


outline_color_list = [(255, 0, 0), (0, 0, 255), (0, 0, 255)]

def set_model_input(net):
        
    '''Gets the CNN filenames, despite the PC file structure.'''

    #forçando o path dos arquivos
    robocup_folder = os.path.join(os.path.expanduser('~'), "edromufu/src/vision/robocup_cnn_files")

    #config_file = os.path.join(robocup_folder, "yolov4-tiny-obj.cfg")
    #weights_file = os.path.join(robocup_folder, "yolov4-tiny-obj_best.weights")

    #Recebe o modelo no YOLO 
    model = YOLO(net)
    
    
    return model

    

def detect_model(model, current_frame, output_img ):
    
    start_time = time.time()
    '''Conferir se o tamanho da imagem (imgsz) serve e qual device atribuir (640,384 tem o dobro de desempenho que 640,480)'''
    results = model.predict(source=current_frame,
                            conf=0.25,   #conf = limiar de confiança mínima
                            imgsz=(640,480), #imgsz = Tamanho da imagem (h, w) 
                            max_det=1, #max_det = número máximo de detecções por imagem
                            device=0, #device = Escolhe qual dispositivo rodar a detecção (cpu, gpu, cuda)
                            verbose=False) #verbose = Não imprime a saída da função na tela
    
    classes = results[0].boxes.cls.tolist()
    scores = results[0].boxes.conf.tolist() 
    boxes = results[0].boxes.xywh.tolist()  

    finish_time = time.time()
    fps = 1/(finish_time-start_time)
    

    print(f"Classes: {classes}, Scores: {scores}")
    print(f"Boxes: {boxes}")
    print("FPS: ", fps)
    print('\n')


    inference_frame=results[0].plot()

    return classes, scores, boxes, fps, inference_frame

