#!/usr/bin/env python3
#coding=utf-8

import numpy as np
import os, json

MAIN_DIR = '/home/'+os.getlogin()+'/edromufu/src/movement_bioloid/movement_pages/pages/'

def Page(page2Run, queueTime):

    with open(MAIN_DIR+page2Run+'.json', 'r') as pageFile:
        jsonData = json.loads(pageFile.read())
        print(jsonData)