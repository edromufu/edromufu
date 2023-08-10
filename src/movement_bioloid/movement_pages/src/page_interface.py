#!/usr/bin/env python3
#coding=utf-8

import sys, rospy, os, json

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
MAIN_DIR = '/home/'+os.getlogin()+'/edromufu/src/movement_bioloid/movement_pages/pages/'


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
        self.copiedContent = [None]*18
        self.fileName = None

        # Variáveis do ROS
        rospy.init_node('page_interface')
        self.motorsTorque = rospy.ServiceProxy('u2d2_comm/enableTorque', enable_torque)
        self.motorsFeedback = rospy.ServiceProxy('u2d2_comm/feedbackBody', body_feedback)

        rospy.wait_for_service('u2d2_comm/enableTorque')

        # Integração dos botões
        self.ui.torqueButton.clicked.connect(self.toggleAllTorque)

        self.ui.saveCurrentPose.clicked.connect(self.generateNewCard)

        for i, btn in enumerate(self.ui.scrollMotorsContent.findChildren(QPushButton)):
            btn.clicked.connect(lambda _, index=i: self.toggleOneTorque(index))    

        self.ui.actionSaveAs.triggered.connect(lambda: self.save(As=True))
        self.ui.actionSave.triggered.connect(self.save)

        self.shortcutsConfig()
        
    def shortcutsConfig(self):
        # Atalho de captura de pose
        shortcutCapturePose = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_Q), self)
        shortcutCapturePose.activated.connect(self.ui.saveCurrentPose.click)

        # Atalho de deleção de pose
        shortcutDeletePose = QShortcut(QKeySequence(Qt.SHIFT + Qt.Key_Delete), self)
        shortcutDeletePose.activated.connect(lambda: self.deletePose(self.currentCheckedPose))

        # Atalho de desfazer captura de pose
        shortcutUndoPoseCap = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_Z), self)
        shortcutUndoPoseCap.activated.connect(lambda: self.deletePose(len(self.poseObjects)-1))

        # Atalho de ligar/desligar todos os torques
        shortcutToggleTorque = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_T), self)
        shortcutToggleTorque.activated.connect(self.toggleAllTorque)

        # Atalho de copiar posição de todos os motores de uma pose
        shortcutCopyPose = QShortcut(QKeySequence(Qt.CTRL + Qt.SHIFT + Qt.Key_C), self)
        shortcutCopyPose.activated.connect(self.copyWholePoseContent)

        # Atalho de colar posição de todos os motores em uma pose (desde que copiado)
        shortcutPastePose = QShortcut(QKeySequence(Qt.CTRL + Qt.SHIFT + Qt.Key_V), self)
        shortcutPastePose.activated.connect(self.pasteWholePoseContent)

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
            if self.currentCheckedPose is not None:
                self.poseObjects[self.currentCheckedPose].checkBox.setChecked(False)

            self.currentCheckedPose = (index - 1)

        else:
            self.currentCheckedPose = None
    
    def generateNewCard(self):
        current_position = list(self.motorsFeedback(True).pos_vector)
        
        self.currentPoseNumber += 1
        self.poseObjects.append(newPoseFrame(self.ui.horizontalLayout_8, self.currentPoseNumber, self))
        
        for index, lineEdit in enumerate(self.poseObjects[-1].posePositionsLineEdit):
            lineEdit.setText(str(current_position[index]))
    
    def deletePose(self, poseSelectedIndex):

        # Checa se tem alguma pose selecionada
        if poseSelectedIndex is not None:

            # Deleção comum do campo que salva as posições
            cardToBeDeleted = self.poseObjects[poseSelectedIndex]
            self.ui.horizontalLayout_8.removeWidget(cardToBeDeleted.pose_frame)
            cardToBeDeleted.pose_frame.hide()

            # Retirada do time frame, é diferente pois há apenas a partir do segundo elemento
            if poseSelectedIndex != 0:
                self.ui.horizontalLayout_8.removeWidget(cardToBeDeleted.time_frame)
                cardToBeDeleted.time_frame.hide()
            elif len(self.poseObjects) > 1:
                firstTimeFrame = self.poseObjects[poseSelectedIndex+1].time_frame
                self.ui.horizontalLayout_8.removeWidget(firstTimeFrame)
                firstTimeFrame.hide()
            
            # Atualização dos objetos de card de pose após remoção
            for poseNumber, poseCard in enumerate(self.poseObjects):
                if poseNumber > poseSelectedIndex:
                    poseCard.updatePoseCard(poseNumber)

            # Remoção do objeto do card da lista de objetos
            cardDeleted = self.poseObjects.pop(poseSelectedIndex)
            del cardDeleted

            # Desfaz a seleção do card que não existe mais
            self.currentCheckedPose = None
            self.currentPoseNumber -= 1
    
    def copyWholePoseContent(self):
        
        if self.currentCheckedPose is not None:
            
            for index, lineEdit in enumerate(self.poseObjects[self.currentCheckedPose].posePositionsLineEdit):
                self.copiedContent[index] = float(lineEdit.text())
    
    def pasteWholePoseContent(self):

        if self.currentCheckedPose is not None and type(self.copiedContent[0]) == float:
            for index, lineEdit in enumerate(self.poseObjects[self.currentCheckedPose].posePositionsLineEdit):
                lineEdit.setText(str(self.copiedContent[index]))

    def save(self, As=False):
        # Captura dos dados na GUI
        pageData = {'joints_positions': {}, 'time_between_poses': []}
        for n in range(18):
            pageData['joints_positions'][f'motor_{n}'] = []
        
        for poseId, poseObject in enumerate(self.poseObjects):
            for index, lineEdit in enumerate(poseObject.posePositionsLineEdit):
                pageData['joints_positions'][f'motor_{index}'].append(float(lineEdit.text()))

            if poseId != 0:
                pageData['time_between_poses'].append(float(poseObject.timeEdit.text()))
        
        # Seleção do nome do arquivo
        if self.fileName is None or As:
            self.fileName, _ = QFileDialog.getSaveFileName(self,"Salvar em", MAIN_DIR,"Page Files (*)")

        # Salva os dados da GUI no arquivo selecionado
        with open(self.fileName, 'w') as file:
            json.dump(pageData, file, indent=4) 

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())