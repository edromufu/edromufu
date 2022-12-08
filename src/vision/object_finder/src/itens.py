#!/usr/bin/env python3
# coding=utf-8

class Item():

    def __init__(self, tipo_item, width, height, x_center, y_center, confidence):
        self.tipo_item = tipo_item
        self.width = width
        self.height = height
        self.x_center = x_center
        self.y_center = y_center
        self.confidence = confidence