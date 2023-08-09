
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class newPoseFrame():

    def __init__(self, poseScrollAreaLayout, index, parent):
        
        self.posePositionsLineEdit = []

        if index != 1:
            self.initTimeFrame()
            self.configTimeFrameLayout()
            self.insertFrame(self.time_frame, poseScrollAreaLayout)

        self.initPoseFrame()
        self.configPoseFrameLayout(index, parent)
        self.insertFrame(self.pose_frame, poseScrollAreaLayout)

    def initPoseFrame(self):
        self.pose_frame = QtWidgets.QFrame()
        self.pose_frame.setMinimumSize(QtCore.QSize(83, 0))
        self.pose_frame.setMaximumSize(QtCore.QSize(83, 1000))
        self.pose_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.pose_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    
    def initTimeFrame(self):
        self.time_frame = QtWidgets.QFrame()
        self.time_frame.setMinimumSize(QtCore.QSize(70, 0))
        self.time_frame.setMaximumSize(QtCore.QSize(70, 1000))
        self.time_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.time_frame.setFrameShadow(QtWidgets.QFrame.Plain)

    def configPoseFrameLayout(self, index, parent):
        # Configuração do layout vertical
        self.pose_frame_layout = QtWidgets.QVBoxLayout(self.pose_frame)
        self.pose_frame_layout.setContentsMargins(2, 0, 2, 0)
        self.pose_frame_layout.setSpacing(3)

        # Configuração da checkbox da pose
        self.checkBox = QtWidgets.QCheckBox()
        self.checkBox.setText('Pose ' + str(index))
        self.checkBox.setFixedSize(QtCore.QSize(83, 32))
        self.checkBox.clicked.connect(lambda: parent.selectedCheckBoxChanged(index, self.checkBox.checkState()))
        self.pose_frame_layout.addWidget(self.checkBox)

        # Configuração da linha separadora
        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setFixedSize(QtCore.QSize(83, 3))
        self.pose_frame_layout.addWidget(line)

        # Configuração e adição à lista de cada LineEdit que guarda a posição de cada motor nessa pose
        for _ in range(18):
            lineEdit = QtWidgets.QLineEdit()
            lineEdit.setMinimumSize(QtCore.QSize(10, 31))
            lineEdit.setMaximumSize(QtCore.QSize(500, 32))
            self.posePositionsLineEdit.append(lineEdit)
            self.pose_frame_layout.addWidget(lineEdit)
    
    def configTimeFrameLayout(self):
        # Configuração do layout vertical
        self.time_frame_layout = QtWidgets.QVBoxLayout(self.time_frame)
        self.time_frame_layout.setContentsMargins(2, 0, 2, 0)
        self.time_frame_layout.setSpacing(0)

        # Primeiro espaçador para separar
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.time_frame_layout.addItem(spacerItem)

        # Frame para deixar junto LineEdit e label com "s"
        frameSecs = QtWidgets.QFrame(self.time_frame)
        frameSecs.setFrameShape(QtWidgets.QFrame.NoFrame)
        frameSecs.setFrameShadow(QtWidgets.QFrame.Raised)

        # Layout horizontal do Frame para deixar junto
        timeHorLayout = QtWidgets.QHBoxLayout(frameSecs)
        timeHorLayout.setContentsMargins(2, 0, 2, 0)
        timeHorLayout.setSpacing(2)

        # LineEdit para o tempo
        self.timeEdit = QtWidgets.QLineEdit()
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        timeHorLayout.addWidget(self.timeEdit)

        # Label para o "s"
        secs = QtWidgets.QLabel(frameSecs)
        secs.setText(' s')
        timeHorLayout.addWidget(secs)
        self.time_frame_layout.addWidget(frameSecs)

        # Imagem da seta
        label = QtWidgets.QLabel()
        label.setFixedSize(QtCore.QSize(66, 60))
        label.setText("")
        label.setPixmap(QtGui.QPixmap(":/Seta/setaTempo.png"))
        label.setScaledContents(True)
        self.time_frame_layout.addWidget(label)

        # Segundo espaçador para separar
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.time_frame_layout.addItem(spacerItem)

    #Insere o novo Widget na posição correta
    def insertFrame(self, frame, scrollLayout):
        index = scrollLayout.indexOf(scrollLayout.itemAt(scrollLayout.count() - 1).widget())
        scrollLayout.insertWidget(index,frame)