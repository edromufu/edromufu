#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy, os
import numpy as np
from PyQt5.QtWidgets import QApplication, QFileDialog

from movement_msgs.msg import OpencmResponseMsg
from movement_msgs.srv import CommandToOpenCMSrv

class PageCapture():

    def __init__(self):
        
        rospy.Subscriber('opencm/response', OpencmResponseMsg, self.currentPositionCapture)
        self.client_to_request_opencm_command = rospy.ServiceProxy('opencm/request_command', CommandToOpenCMSrv)
        
        self.final_page = [] 
        self.torque_state = True

    def start(self):
        while not rospy.is_shutdown():
            os.system('clear')
            print('Posições capturadas')
                        
            for index, position_vector in enumerate(self.final_page):
                print(f'[{index}]: {position_vector}')

            print('_______________________________________________________________________________________________________________________________')
            print('[c]: Capturar posição atual \n[d]: Selecionar vetor a remover \n[s]: Salvar page \n[t]: Desligar/ligar torque \n[r]: Recarregar\n[q]: Encerrar')

            page_cap_command = 0

            page_cap_command = input("\nPróximo comando: ")

            if page_cap_command:
                if page_cap_command == 'c':
                    self.currentPositionCaptureRequest()
                elif page_cap_command == 't':
                    self.torqueToggle()
                elif page_cap_command == 'd':
                    self.removeCapturedPosition()
                elif page_cap_command == 's':
                    self.savePage()
                elif page_cap_command == 'q':
                    return

            else:
                print(page_cap_command)
    
    def currentPositionCapture(self, msg):
        self.final_page.append(list(msg.motors_position))

    def currentPositionCaptureRequest(self):
        self.client_to_request_opencm_command('feedback')
        
    def torqueToggle(self):
        self.client_to_request_opencm_command('shutdown_now' if self.torque_state else 'reborn')
        self.torque_state = not self.torque_state
    
    def removeCapturedPosition(self):
        position_index = int(input("\nNúmero do vetor de posições a ser removido: "))
        self.final_page.pop(position_index)
    
    def savePage(self, directory='./', filters="All files (*)"):
        app = QApplication([directory])
        path, _ = QFileDialog.getSaveFileName(caption="Salvar page",
                                              directory=os.getenv('HOME')+'/edrom/src/movement/movement_utils/pages/',
                                                filter=filters)
        
        final_page_file = open(path+'.txt', 'w')
        np.savetxt(final_page_file, self.final_page, fmt='%d')
        final_page_file.close()
        self.final_page = []

if __name__ == "__main__":
    rospy.init_node('Page_capture_node', anonymous=False)

    capture_page = PageCapture()
    capture_page.start()