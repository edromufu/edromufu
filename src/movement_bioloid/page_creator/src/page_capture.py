#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy, os
import numpy as np

from movement_utils.srv import position_feedback, enable_torque

class PageCapture():

    def __init__(self):
        
        self.req_torque = rospy.ServiceProxy('u2d2_comm/enableTorque', enable_torque)
        rospy.wait_for_service('u2d2_comm/enableTorque')

        self.req_pos_feedback =rospy.ServiceProxy('u2d2_comm/feedbackMotors', position_feedback)
        rospy.wait_for_service('u2d2_comm/feedbackMotors')
        
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

    def currentPositionCaptureRequest(self):
        response = self.req_pos_feedback(False)
        self.final_page.append([round(num,3) for num in response.pos_vector])
        
    def torqueToggle(self):
        self.req_torque(self.torque_state,[-1])
        self.torque_state = not self.torque_state
    
    def removeCapturedPosition(self):
        position_index = int(input("\nNúmero do vetor de posições a ser removido: "))
        self.final_page.pop(position_index)
    
    def savePage(self):
        print('\n!!! CUIDADO, CASO UTILIZE NOME JÁ EXISTENTE, O ARQUIVO SERÁ SOBRESCRITO !!!\n')
        page_name = input("Digite o nome da page: ")

        if os.path.dirname(__file__):
            os.chdir(os.path.dirname(__file__))
        os.chdir("../pages")
        
        with open(page_name+'.page','w') as f:
            np.savetxt(f, self.final_page, fmt='%f')
        
if __name__ == "__main__":
    rospy.init_node('Page_capture_node', anonymous=False)

    capture_page = PageCapture()
    capture_page.start()