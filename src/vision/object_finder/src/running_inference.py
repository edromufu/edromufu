#!/usr/bin/env python3
# coding=utf-8

from ultralytics import YOLO
import os
import cv2
import numpy as np
import time

'''Retirou função Draw_results e paramatros em set_model_input, embutidos na detecção
Alguns comentários em vermelho são lembretes para modificar o código depois'''

outline_color_list = [(255, 0, 0), (0, 0, 255), (0, 0, 255)]

def get_cnn_files():
    '''Gets the CNN filenames, despite the PC file structure.'''

    #forçando o path dos arquivos
    robocup_folder = os.path.join(os.path.expanduser('~'), "edromufu/src/vision/robocup_cnn_files")

    '''Modificar os nomes dos arquivos de treinamento'''

    config_file = os.path.join(robocup_folder, "yolov4-tiny-obj.cfg")
    weights_file = os.path.join(robocup_folder, "yolov4-tiny-obj_best.weights")

    return read_cnn_architecture(config_file, weights_file)

def read_cnn_architecture(config_file, weights_file):

    net = cv2.dnn.readNet(config_file, weights_file, "darknet")

    return net

def set_model_input(net):

    #Recebe o modelo no YOLO 
    model = YOLO(net)
    
    return model

def detect_model(model, current_frame, output_img ):
    
    start_time = time.time()
    '''Conferir se o tamanho da imagem (imgsz) está certo e qual device atribuir'''
    results = model.predict(source=current_frame,conf=0.85,imgsz=(480,640),max_det=1,show=output_img,device=)
    '''Corrigir as atribuições dessas variáveis abaixo'''
    classes, scores, boxes = results[0].boxes.xywh
    '''Organizar a descrição dos argumentos'''
    #conf = limiar de confiança mínima
    #imgsz = Tamanho da imagem (h, w) 
    #max_det = número máximo de detecções por imagem
    #show = mostra imagens marcadas na detecção
    #device = Escolhe qual dispositivo rodar a detecção (cpu, gpu, cuda)

    finish_time = time.time()
    fps = 1/(finish_time-start_time)
    
    #print(f"Classes: {classes}, Scores: {scores}")
    #print(f"Boxes: {boxes}")
    #print("FPS: ", fps)
    #print('\n')

    return classes, scores, boxes, int(fps)

