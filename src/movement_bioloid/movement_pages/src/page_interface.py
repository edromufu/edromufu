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
from new_pose import newPoseFrame

GREEN_BGC = 'background-color: rgb(138, 226, 52);'
RED_BGC   = 'background-color: rgb(204, 0, 0);'


class MainWindow(QMainWindow):

    def __init__(self):
        # Inicialização da interface do Qt
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Variáveis de controle de código
        self.allTorqueStatus = False
        self.motorsTorqueStatus = [False]*18   
        self.currentPoseNumber = 0
        self.poseObjects = [] 
        self.currentCheckedPose = None

        # Variáveis do ROS
        rospy.init_node('page_interface')
        self.motorsTorque = rospy.ServiceProxy('u2d2_comm/enableTorque', enable_torque)
        self.motorsFeedback = rospy.ServiceProxy('u2d2_comm/feedbackBody', body_feedback)

        rospy.wait_for_service('u2d2_comm/enableTorque')

        # Integração dos botões
        self.ui.torqueButton.clicked.connect(lambda: self.toggleAllTorque())

        self.ui.saveCurrentPose.clicked.connect(lambda: self.generateNewCard())

        for i, btn in enumerate(self.ui.scrollMotorsContent.findChildren(QPushButton)):
            btn.clicked.connect(lambda _, index=i: self.toggleOneTorque(index))    

    def generateNewCard(self):
        current_position = list(self.motorsFeedback(True).pos_vector)
        
        self.currentPoseNumber += 1
        self.poseObjects.append(newPoseFrame(self.ui.horizontalLayout_8, self.currentPoseNumber, self))
        
        for index, lineEdit in enumerate(self.poseObjects[-1].posePositionsLineEdit):
            lineEdit.setText(str(current_position[index]))

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

    def selectedCheckBoxChanged(self, index, state):

        if state:
            self.currentCheckedPose = (index - 1)

            for i, poseObejct in enumerate(self.poseObjects):
                if i != (index-1):
                    poseCheckbox = poseObejct.checkBox
                    poseCheckbox.setChecked(False)
        else:
            self.currentCheckedPose = None
            
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())