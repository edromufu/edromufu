#!/usr/bin/env python3
#coding=utf-8

import re, os, time
import rospy

from movement_msgs.msg import WebotsMsg
from movement_msgs.srv import PredefinedMovementSrv, PredefinedMovementSrvResponse

dt = 0.07

class movementPredefined():

    def __init__(self):
        
        #Dados enviados para Api
        velocityArray = [2]*18
        velocityArray += [0.5]*2
        self.pubToController = rospy.Publisher('/opencm/conversion', WebotsMsg, queue_size=1000)

        #Definição da mensagem
        self.controllerMsg = WebotsMsg()
        self.controllerMsg.velocity = velocityArray
        self.controllerMsg.control = 'conversion_mode'
        self.controllerMsg.motor_name = ['RARM_0 [shoulder]', 'LARM_0 [shoulder]', 'RARM_1', 'LARM_1', 'LARM_2', 'RARM_2', 'RLEG_0', 'LLEG_0', 'RLEG_1 [hip]', 'LLEG_1 [hip]', 'RLEG_2', 'LLEG_2', 'RLEG_3', 'LLEG_3', 'RLEG_4', 'LLEG_4', 'RFOOT', 'LFOOT', 'HEAD_0', 'HEAD_1']


        #Service da requisição
        rospy.Service('movement_predefined/request_txt', PredefinedMovementSrv, self.txtRequested)
        self.SrvPredefined = PredefinedMovementSrvResponse()
    
    def txtRequested(self, req):

        if(req.request == 'turn_left' or req.request == 'turn_right'):
            dt = 0.078
        else:
            dt = 0.04

        os.chdir('/robotica_ufu/src/simulacao/movement_predefined/source_files')
        inputTxt = req.request + '.txt'
        
        with open(inputTxt, "r") as file:
            txt = file.readlines()

        count = 0
        while count < len(txt):
            
            vectorPositions = re.findall("\ (.*?)\,", txt[count])

            for i in range(len(vectorPositions)):
                vectorPositions[i] = float(vectorPositions[i])
            
            if(req.request == 'turn_right'):
                vectorPositions = self.invertLegs(vectorPositions)

            self.controllerMsg.position = vectorPositions

            self.pubToController.publish(self.controllerMsg)
            #rospy.Rate(14)
            time.sleep(dt)
            count += 2
        
        self.SrvPredefined.sucess = True
        return self.SrvPredefined
    
    def invertLegs(self, vector):
        for i in range(len(vector)):
            if(not i%2 and i > 4 and i < 18):
                if(i == 10):     
                    temp = vector[i]
                    vector[i] = vector[i+1]
                    vector[i+1] = temp
                else:
                    temp = vector[i]
                    vector[i] = -vector[i+1]
                    vector[i+1] = -temp

        return vector


if __name__ == '__main__':
    rospy.init_node('Predefined_movement_node', anonymous=False)
    predefined = movementPredefined()
    rospy.spin()
