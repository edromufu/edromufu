#!/usr/bin/env python3
#coding=utf-8
import re

[filter1, shouldReverse1] = ['fitness', True]
[filter2, shouldReverse2] = ['dX', False]
inputTxt = "vz=[0.24;0.36] vx=[0;0.02].txt" 
outputTxt = "resultsPedro.txt"

def paramtersSave(run):
        txt = ( '------------------------------------------------------------------------------------------\n' +
                'Velocidades: [' + str(run['vx']) + ']  ' + '[' + str(run['vy']) + ']  ' + '[' + str(run['vz']) + ']\n' +
                'Distancias: [' + str(run['dX']) + ']  ' + '[' + str(run['dY']) + ']  ' + '[' + str(run['dZ']) + ']\n' +
                'Passos Esquerda: [' + str(run['lStep']) + ']  ' + 'Passos Direita: [' + str(run['rStep']) + ']\n' +
                'Tempo de caminhada: [' + str(run['time']) +'] ' + 'Fitness: [' + str(run['fitness']) + ']\n' +
                '------------------------------------------------------------------------------------------\n\n'
              )
        
        with open(outputTxt, "ab") as f:
          	f.write(txt.encode('utf-8', 'ignore'))

with open(inputTxt, "r") as file:
    txt = file.readlines()

count = 0
dataRun = []

keys = ['vx', 'vy', 'vz', 'dX', 'dY','dZ', 'lStep', 'rStep', 'time', 'fitness']

while count < len(txt):
    [vx,vy,vz] = re.findall("\[(.*?)\]", txt[count+1])
    [vx,vy,vz] = [float(vx), float(vy), float(vz)]

    [deltaX, deltaY, deltaZ] = re.findall("\[(.*?)\]", txt[count+2])
    [deltaX, deltaY, deltaZ] = [float(deltaX), float(deltaY), float(deltaZ)]

    [lStep, rStep] = re.findall("\[(.*?)\]", txt[count+3])
    [lStep, rStep] = [int(lStep), int(rStep)]

    [time] = re.findall("\[(.*?)\]", txt[count+4])
    time = float(time)

    if time == 26 and vz < 0.38:
        fitness = deltaY / ((lStep+rStep)/2) 

        valuesRun = [vx, vy, vz, abs(deltaX), deltaY, deltaZ, lStep, rStep, time, fitness]
        dictRun = dict(zip(keys, valuesRun))
        dataRun.append(dictRun)

    count += 7

bestFitness = sorted(dataRun,key=lambda k: k[filter1], reverse=shouldReverse1)

bestDx = []
for index in range(10):
    bestDx += [bestFitness[index]]

bestDx = sorted(bestDx,key=lambda k: k[filter2], reverse=shouldReverse2)

for run in bestDx:
    paramtersSave(run)

