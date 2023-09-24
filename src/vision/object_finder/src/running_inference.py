#!/usr/bin/env python3
# coding=utf-8

import os
import cv2
import numpy as np
import time


outline_color_list = [(255, 0, 0), (0, 0, 255), (0, 0, 255)]

def get_cnn_files():
    '''Gets the CNN filenames, despite the PC file structure.'''

    #forçando o path dos arquivos
    robocup_folder = os.path.join(os.path.expanduser('~'), "edromufu/src/vision/robocup_cnn_files")

    config_file = os.path.join(robocup_folder, "yolov4-tiny-obj.cfg")
    weights_file = os.path.join(robocup_folder, "yolov4-tiny-obj_best.weights")

    return read_cnn_architecture(config_file, weights_file)

def read_cnn_architecture(config_file, weights_file):

    net = cv2.dnn.readNet(config_file, weights_file, "darknet")

    return net

def set_model_input(net):


    model = cv2.dnn.DetectionModel(net)
    model.setInputParams(size=(416,416), scale=1/255, swapRB=True)
    
    return model

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

def draw_results(frame, classes, scores, boxes):

    # Draw the bounding boxes

    for i in range(len(boxes)):
        [x_top, y_top, roi_width, roi_height] = boxes[i]
        p1 = (x_top, y_top)
        p2 = (x_top + roi_width, y_top + roi_height)
        p3 = (x_top, y_top - 5)

        x_center = round(x_top+(roi_width/2))
        y_center = round(y_top+(roi_height/2))
        radius = round((roi_width+roi_height)/4)
        
        cv2.rectangle(frame, p1, p2, outline_color_list[classes[i]], 2)
        #cv2.circle (frame,(int(x_center),int(y_center)),radius, outline_color_list[classes[i]],2 )
        confidence = str(round(float(scores[i]), 2))
        
        label = "Ball"

        cv2.putText(frame, label+" " + confidence, p3, cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1)
