#!/usr/bin/env python3
#coding=utf-8

import sys, rospy

from movement_utils.msg import *
from movement_utils.srv import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui import Ui_MainWindow

GREEN_BGC = 'background-color: rgb(138, 226, 52);'
RED_BGC   = 'background-color: rgb(204, 0, 0);'

class MainWindow(QMainWindow):

    def __init__(self):
        # Inicialização da interface do Qt
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(3000)

        # Variáveis de controle de código
        self.allTorqueStatus = False
        self.motorsTorqueStatus = [False]*18        

        # Variáveis do ROS
        rospy.init_node('page_interface')
        self.motorsTorque = rospy.ServiceProxy('u2d2_comm/enableTorque', enable_torque)
        self.motorsFeedback = rospy.ServiceProxy('u2d2_comm/feedbackBody', body_feedback)

        #rospy.wait_for_service('u2d2_comm/enableTorque')

        # Integração dos botões
        self.ui.torqueButton.clicked.connect(lambda: self.toggleAllTorque())
        self.motorsTorqueConnect()
    
    def timerEvent(self):
        feedback = self.motorsFeedback(True).pos_vector
        
        for id, btn in enumerate(self.ui.scrollMotorsContent.findChildren(QPushButton)):
            btn.setText(f'Motor {id}\nAtual: {round(feedback[id],3)}\nMáxima: \nMínima: ')
        

    def motorsTorqueConnect(self):
        self.ui.motor0.clicked.connect(lambda: self.toggleOneTorque(0))
        self.ui.motor1.clicked.connect(lambda: self.toggleOneTorque(1))
        self.ui.motor2.clicked.connect(lambda: self.toggleOneTorque(2))
        self.ui.motor3.clicked.connect(lambda: self.toggleOneTorque(3))
        self.ui.motor4.clicked.connect(lambda: self.toggleOneTorque(4))
        self.ui.motor5.clicked.connect(lambda: self.toggleOneTorque(5))
        self.ui.motor6.clicked.connect(lambda: self.toggleOneTorque(6))
        self.ui.motor7.clicked.connect(lambda: self.toggleOneTorque(7))
        self.ui.motor8.clicked.connect(lambda: self.toggleOneTorque(8))
        self.ui.motor9.clicked.connect(lambda: self.toggleOneTorque(9))
        self.ui.motor10.clicked.connect(lambda: self.toggleOneTorque(10))
        self.ui.motor11.clicked.connect(lambda: self.toggleOneTorque(11))
        self.ui.motor12.clicked.connect(lambda: self.toggleOneTorque(12))
        self.ui.motor13.clicked.connect(lambda: self.toggleOneTorque(13))
        self.ui.motor14.clicked.connect(lambda: self.toggleOneTorque(14))
        self.ui.motor15.clicked.connect(lambda: self.toggleOneTorque(15))
        self.ui.motor16.clicked.connect(lambda: self.toggleOneTorque(16))
        self.ui.motor17.clicked.connect(lambda: self.toggleOneTorque(17))

    def toggleAllTorque(self):       
        
        self.allTorqueStatus = not self.allTorqueStatus
        self.motorsTorqueStatus = [self.allTorqueStatus]*18

        newBcgColor = GREEN_BGC if self.allTorqueStatus else RED_BGC

        for btn in self.ui.scrollMotorsContent.findChildren(QPushButton):
            btn.setStyleSheet(newBcgColor)

        self.motorsTorque(self.allTorqueStatus, list(range(20)))

    def toggleOneTorque(self, motor_id):
        
        self.motorsTorqueStatus[motor_id] = not self.motorsTorqueStatus[motor_id] 

        newBcgColor = GREEN_BGC if self.motorsTorqueStatus[motor_id] else RED_BGC

        for btn in self.ui.scrollMotorsContent.findChildren(QPushButton):
            if str(motor_id) in btn.objectName():
                btn.setStyleSheet(newBcgColor)
                break
        
        self.motorsTorque(self.motorsTorqueStatus[motor_id], list([motor_id]))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())