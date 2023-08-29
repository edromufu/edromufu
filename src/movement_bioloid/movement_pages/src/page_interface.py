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
        self.pageRunner = rospy.ServiceProxy('movement_central/request_page', page)

        rospy.wait_for_service('u2d2_comm/enableTorque')

        # Integração dos botões
        self.ui.torqueButton.clicked.connect(self.toggleAllTorque)

        self.ui.saveCurrentPose.clicked.connect(lambda: self.generateNewCard(requestFeedback=True))

        self.ui.playFromFirst.clicked.connect(self.playPage)
        self.ui.playFromSelected.clicked.connect(lambda: self.playPage(selected=True))

        for i, btn in enumerate(self.ui.scrollMotorsContent.findChildren(QPushButton)):
            btn.clicked.connect(lambda _, index=i: self.toggleOneTorque(index))    

        self.ui.actionSaveAs.triggered.connect(lambda: self.save(As=True))
        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionOpenPage.triggered.connect(self.open)
        self.ui.actionShortcutsInfo.triggered.connect(lambda: self.showInfo('shortcuts'))
        self.ui.actionAbout.triggered.connect(lambda: self.showInfo('about'))
        self.ui.actionHelp.triggered.connect(lambda: self.showInfo('help'))

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

        # Atalho de rodar a page a partir da primeira
        shortcutPlayPage = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_P), self)
        shortcutPlayPage.activated.connect(self.playPage)

        # Atalho de rodar a page a partir da selecionada
        shortcutPlayPageFromSelected = QShortcut(QKeySequence(Qt.CTRL + Qt.SHIFT + Qt.Key_P), self)
        shortcutPlayPageFromSelected.activated.connect(lambda: self.playPage(selected=True))

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
    
    def generateNewCard(self, requestFeedback=True):
        if requestFeedback:
            current_position = list(self.motorsFeedback(True).pos_vector)
        else:
            current_position = [-1]*18

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

    def save(self, As=False, selected=0):
        # Captura dos dados na GUI
        pageData = {'joints_positions': {}, 'time_between_poses': []}
        for n in range(18):
            pageData['joints_positions'][f'motor_{n}'] = []
        
        for poseId, poseObject in enumerate(self.poseObjects):
            if poseId >= selected:
                for index, lineEdit in enumerate(poseObject.posePositionsLineEdit):
                    pageData['joints_positions'][f'motor_{index}'].append(float(lineEdit.text()))

                if poseId != selected:
                    pageData['time_between_poses'].append(float(poseObject.timeEdit.text()))
        
        # Seleção do nome do arquivo
        if self.fileName is None or As:
            self.fileName, _ = QFileDialog.getSaveFileName(self,"Salvar em", MAIN_DIR,"Page Files (*.json)")
            if '.json' not in self.fileName:
                self.fileName += '.json'

        # Salva os dados da GUI no arquivo selecionado
        with open(self.fileName, 'w') as file:
            json.dump(pageData, file, indent=4)
    
    def open(self):
        # Obtem os dados do arquivo selecionado
        self.fileName, _ = QFileDialog.getOpenFileName(self,"Abrir...", MAIN_DIR, "Page Files (*.json)")
        
        with open(self.fileName, 'r') as pageFile:
            pageData = json.loads(pageFile.read())

        # Reseta a interface e a prepara para receber o que estava no arquivo salvo
        while self.currentPoseNumber > 0:
            self.deletePose(0)
        
        for _ in range(len(pageData['joints_positions']['motor_0'])):
            self.generateNewCard(requestFeedback=False)

        # Insere os dados do arquivo na GUI
        for poseId, poseObject in enumerate(self.poseObjects):
            for index, lineEdit in enumerate(poseObject.posePositionsLineEdit):
                lineEdit.setText(str(pageData['joints_positions'][f'motor_{index}'][poseId]))
            
            if poseId != 0:
                poseObject.timeEdit.setText(str(pageData['time_between_poses'][poseId-1]))

    def playPage(self, selected=False):
        
        currentFileName = self.fileName
        self.fileName = MAIN_DIR+'temp2run.json'
        if selected and self.currentCheckedPose is not None:
            self.save(selected=self.currentCheckedPose)
        else:   
            self.save()

        self.pageRunner('temp2run')
        os.remove(self.fileName)
        self.fileName = currentFileName

    def showInfo(self, info):
        msg_box = QMessageBox(self)

        if info == 'shortcuts':
            msg_box.setWindowTitle("Atalhos da GUI")
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("CTRL+Q: Captura a pose atual.\nSHIFT+DELETE: Deleta a pose selecionada.\n" \
                            "CTRL+Z: Remove a última pose.\nCTRL+SHIFT+C: Copia as posições da pose selecionada.\n" \
                            "CTRL+SHIFT+V: Cola as posições na pose selecionada (se copiado).\nCTRL+P: Reproduz a page da primeira pose.\n" \
                            "CTRL+SHIFT+P: Reproduz a page da pose selecionada."
                           )
                           
        elif info == 'about':
            msg_box.setWindowTitle("Sobre")
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText('Interface gráfica finalizada em 28/08 para a LARC 2023.' \
                            '\nESTA INTERFACE NÃO EXECUTA DURANTE OS JOGOS.\nContatos:' \
                            '\nDiretor responsável: Luis Costa (lipemenezescosta@gmail.com)'
                           )
            
        elif info == 'help':
            msg_box.setWindowTitle("Ajuda")
            msg_box.setText("Link para página da documentação sobre pages.")
        
        msg_box.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())