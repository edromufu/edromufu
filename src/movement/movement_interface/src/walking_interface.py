#!/usr/bin/env python3
#coding=utf-8
from walking_ui_config import Ui_MainWindow
from movement_msgs.srv import WalkTestParametersSrv
from movement_msgs.msg import ApprovedMovementMsg

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys, rospy, time, json, os

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Interface de Teste de Caminhada')

        self.pub_walk = rospy.Publisher('/movement/approved_movement', ApprovedMovementMsg, queue_size=10)
        self.pub_walk_msg = ApprovedMovementMsg()

        self.client_parameters = rospy.ServiceProxy('/movement_interface/walking_params', WalkTestParametersSrv)
        rospy.Service('/walk_creator/walking_params', WalkTestParametersSrv, self.receiveParameters)

        self.ui.gain_window_btn.clicked.connect(lambda: self.ui.windows.setCurrentWidget(self.ui.gain_page))
        self.ui.walk_window_btn.clicked.connect(lambda: self.ui.windows.setCurrentWidget(self.ui.walk_page))
        self.ui.parameters_window_btn.clicked.connect(lambda: self.ui.windows.setCurrentWidget(self.ui.parameters_page))
        
        self.ui.save_action.triggered.connect(self.save)
        self.ui.load_action.triggered.connect(self.load)

        self.ui.update_window_btn.clicked.connect(self.sendParameters)

        self.parameters_list = ['currentWalk', 'stepGain', 'lateralGain', 'turnGain','freq', 'supportPhaseRatio', 'footYOffset', 'riseGain', 'trunkZOffset', 'swingGain', 'swingRollGain', 'swingPhase', 'stepUpVel', 'stepDownVel', 'riseUpVel', 'riseDownVel', 'swingPause', 'swingVel', 'trunkXOffset', 'trunkYOffset', 'trunkPitch', 'trunkRoll', 'extraLeftX', 'extraLeftY', 'extraLeftZ', 'extraRightX', 'extraRightY', 'extraRightZ', 'extraLeftYaw', 'extraLeftPitch', 'extraLeftRoll', 'extraRightYaw', 'extraRightPitch', 'extraRightRoll']
        self.parameters_dict = dict.fromkeys(self.parameters_list)

        for object_name, object_variable in self.ui.__dict__.items():
            if ('SpinBox' in object_name):
                if ('65' not in object_name) and ('66' not in object_name) and ('76' not in object_name):
                    object_variable.setRange(-999,999)
                object_variable.setDecimals(4)      

    def load(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 
            "Carregar", os.environ['HOME']+"/edrom/src/movement/movement_utils/walk_test_jsons/", "Arquivos de parâmetros de caminhada(*.json)")

        if fileName:
            with open(fileName, 'r') as file:
                load = json.load(file)

            self.loadParametersPage(load)
            self.loadGainPage(load)

    def loadParametersPage(self, load):
        for widget in self.ui.scrollAreaWidgetContents.findChildren(QFrame):
            if 'label' in widget.objectName():
                text = widget.text()
                if text in self.parameters_list:
                    frame = widget.parent()
                    spin_box = frame.findChild(QDoubleSpinBox)
                    spin_box.setValue(load['walk_parameters'][text])
    
    def loadGainPage(self, load):
        for widget in self.ui.gain_page.findChildren(QFrame):
            if 'label' in widget.objectName():
                text = widget.text()
                if text in self.parameters_list:
                    frame = widget.parent()
                    spin_box = frame.findChild(QDoubleSpinBox)
                    spin_box.setValue(load['step_parameters'][text])

    def save(self):
        self.saveStructuralParameters()
        self.saveParametersPage()
        self.saveGainPage()

        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, 
            "Salvar", os.environ['HOME']+"/edrom/src/movement/movement_utils/walk_test_jsons/", "Arquivos de parâmetros de caminhada(*.json)")
        
        if fileName:
            with open(fileName if '.json' in fileName else fileName + ".json", "w") as write_file:
                json.dump(self.save_dict, write_file, indent=4)

    def saveStructuralParameters(self):
        fileName = os.environ['HOME']+"/edrom/src/movement/movement_utils/walk_test_jsons/default.json"
        with open(fileName, 'r') as file:
            self.save_dict = json.load(file)

    def saveParametersPage(self):
        for widget in self.ui.scrollAreaWidgetContents.findChildren(QFrame):
            if 'label' in widget.objectName():
                text = widget.text()
                
                if text in self.parameters_list:
                    frame = widget.parent()
                    label_current_value = frame.findChildren(QLabel)[1]

                    self.save_dict["walk_parameters"][text] = round(float(label_current_value.text()),4)
    
    def saveGainPage(self):
        for widget in self.ui.gain_page.findChildren(QFrame):

            if 'label' in widget.objectName():
                text = widget.text()

                if text in self.parameters_list:
                    frame = widget.parent()
                    label_current_value = frame.findChildren(QLabel)[1]

                    self.save_dict["step_parameters"][text] = round(float(label_current_value.text()),4)

    def receiveParameters(self, req):
        try:
            self.dict_req = dict(zip(req.__slots__, req.__getstate__()))
            self.setCurrentParametersPageValues()
            self.setCurrentGainPageValues()

            return True
        except Exception as e:
            return e

    def setCurrentParametersPageValues(self):
        for widget in self.ui.scrollAreaWidgetContents.findChildren(QFrame):
            if 'label' in widget.objectName():
                text = widget.text()
                
                if text in self.parameters_list:
                    frame = widget.parent()
                    label_current_value = frame.findChildren(QLabel)[1]

                    label_current_value.setText(str(round(self.dict_req[text],4)))   

    def setCurrentGainPageValues(self):
        for widget in self.ui.gain_page.findChildren(QFrame):

            if 'label' in widget.objectName():
                text = widget.text()

                if text in self.parameters_list:
                    frame = widget.parent()
                    label_current_value = frame.findChildren(QLabel)[1]

                    label_current_value.setText(str(round(self.dict_req[text],4)))

    def sendParameters(self):
        
        self.captureParametersPageValues()
        self.captureGainPageValues()
        self.parameters_dict['currentWalk'] = self.ui.buttonGroup.checkedButton().text()

        if self.parameters_dict['currentWalk'] != 'emergency_shutdown':
            self.client_parameters(*self.parameters_dict.values())
            self.pub_walk_msg.approved_movement = self.parameters_dict['currentWalk']
            self.pub_walk.publish(self.pub_walk_msg)
        
    def captureParametersPageValues(self):
        for widget in self.ui.scrollAreaWidgetContents.findChildren(QFrame):
            if 'label' in widget.objectName():
                text = widget.text()
                if text in self.parameters_list:
                    frame = widget.parent()
                    spin_box = frame.findChild(QDoubleSpinBox)
                    self.parameters_dict[text] = spin_box.value()     

    def captureGainPageValues(self):

        for widget in self.ui.gain_page.findChildren(QFrame):
            if 'label' in widget.objectName():
                text = widget.text()
                if text in self.parameters_list:
                    frame = widget.parent()
                    spin_box = frame.findChild(QDoubleSpinBox)
                    self.parameters_dict[text] = spin_box.value() 

if __name__ == '__main__':
    app = QApplication(sys.argv)

    rospy.init_node('Walking_interface_node', anonymous=False)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())