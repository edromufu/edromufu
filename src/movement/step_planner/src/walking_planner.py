#!/usr/bin/env python3
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import math as m

STEP_TIME = 1 #s

def WalkVx(distX, vX, robot, plot=True, footDimX=0.05, footDimY=0.03):
    
    for motor in robot:
        if 'RFOOT' in motor.get_name():
            rFootXYPositions = motor.absolutePosition[:-1].T
        elif 'LFOOT' in motor.get_name():
            lFootXYPositions = motor.absolutePosition[:-1].T

    stepNumber = m.ceil(distX/(2*STEP_TIME*vX))
    stepIncrementX = np.array([STEP_TIME*vX, 0])
    leg = True

    for currentStep in range(stepNumber):

        if leg:
            rFootXYPositions = np.append(rFootXYPositions, [rFootXYPositions[-1] + 2*stepIncrementX - int(not currentStep)*stepIncrementX], axis=0)
            lFootXYPositions = np.append(lFootXYPositions, [lFootXYPositions[-1]], axis=0)
        else:
            lFootXYPositions = np.append(lFootXYPositions, [lFootXYPositions[-1] + 2*stepIncrementX - int(not currentStep)*stepIncrementX], axis=0)
            rFootXYPositions = np.append(rFootXYPositions, [rFootXYPositions[-1]], axis=0)

        leg = not leg

    if plot:
    
        fig, ax = plt.subplots()

        for i in range(len(rFootXYPositions)):
            ax.add_patch(plt.Rectangle((rFootXYPositions[i][0]-footDimX/2, rFootXYPositions[i][1]-footDimY/2), footDimX, footDimY, fill=False, edgecolor='g'))

        for i in range(len(lFootXYPositions)):
            ax.add_patch(plt.Rectangle((lFootXYPositions[i][0]-footDimX/2, lFootXYPositions[i][1]-footDimY/2), footDimX, footDimY, fill=False, edgecolor='r'))

        plt.show()

        print(rFootXYPositions)
        print(lFootXYPositions)

    #! yz0 e yzf = 0, ys = ypésuporte (x variou da última)
    #! xz0 = média entre x anterior dos dois pés , xzs= xpésuporte (x variou da última), xzf = media entre x atual dos dois pé