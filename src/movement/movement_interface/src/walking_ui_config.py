# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'walking_interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QSize(800, 16777215))
        MainWindow.setStyleSheet(u"")
        self.save_action = QAction(MainWindow)
        self.save_action.setObjectName(u"save_action")
        self.load_action = QAction(MainWindow)
        self.load_action.setObjectName(u"load_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.change_window_frame = QFrame(self.centralwidget)
        self.change_window_frame.setObjectName(u"change_window_frame")
        self.change_window_frame.setMinimumSize(QSize(160, 0))
        self.change_window_frame.setMaximumSize(QSize(160, 16777215))
        self.change_window_frame.setStyleSheet(u"")
        self.change_window_frame.setFrameShape(QFrame.Box)
        self.change_window_frame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout = QVBoxLayout(self.change_window_frame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 10, 0, 10)
        self.walk_window_btn = QPushButton(self.change_window_frame)
        self.walk_window_btn.setObjectName(u"walk_window_btn")
        self.walk_window_btn.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.walk_window_btn)

        self.gain_window_btn = QPushButton(self.change_window_frame)
        self.gain_window_btn.setObjectName(u"gain_window_btn")
        self.gain_window_btn.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.gain_window_btn)

        self.parameters_window_btn = QPushButton(self.change_window_frame)
        self.parameters_window_btn.setObjectName(u"parameters_window_btn")
        self.parameters_window_btn.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.parameters_window_btn)

        self.verticalSpacer = QSpacerItem(20, 431, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.update_window_btn = QPushButton(self.change_window_frame)
        self.update_window_btn.setObjectName(u"update_window_btn")
        self.update_window_btn.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.update_window_btn)


        self.horizontalLayout.addWidget(self.change_window_frame)

        self.change_variables_frame = QFrame(self.centralwidget)
        self.change_variables_frame.setObjectName(u"change_variables_frame")
        self.change_variables_frame.setFrameShape(QFrame.NoFrame)
        self.change_variables_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.change_variables_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.windows = QStackedWidget(self.change_variables_frame)
        self.windows.setObjectName(u"windows")
        self.walk_page = QWidget()
        self.walk_page.setObjectName(u"walk_page")
        self.horizontalLayout_4 = QHBoxLayout(self.walk_page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_4 = QFrame(self.walk_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.walk_forward_btn = QRadioButton(self.frame_4)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.walk_forward_btn)
        self.walk_forward_btn.setObjectName(u"walk_forward_btn")
        self.walk_forward_btn.setMinimumSize(QSize(250, 40))
        self.walk_forward_btn.setStyleSheet(u"QRadioButton{\n"
"font: 24px;\n"
"}")

        self.verticalLayout_5.addWidget(self.walk_forward_btn)

        self.rotate_clockwise_btn = QRadioButton(self.frame_4)
        self.buttonGroup.addButton(self.rotate_clockwise_btn)
        self.rotate_clockwise_btn.setObjectName(u"rotate_clockwise_btn")
        self.rotate_clockwise_btn.setMinimumSize(QSize(250, 40))
        self.rotate_clockwise_btn.setStyleSheet(u"QRadioButton{\n"
"font: 24px;\n"
"}")

        self.verticalLayout_5.addWidget(self.rotate_clockwise_btn)

        self.rotate_c_clockwise_btn = QRadioButton(self.frame_4)
        self.buttonGroup.addButton(self.rotate_c_clockwise_btn)
        self.rotate_c_clockwise_btn.setObjectName(u"rotate_c_clockwise_btn")
        self.rotate_c_clockwise_btn.setMinimumSize(QSize(250, 40))
        self.rotate_c_clockwise_btn.setStyleSheet(u"QRadioButton{\n"
"font: 24px;\n"
"}")

        self.verticalLayout_5.addWidget(self.rotate_c_clockwise_btn)

        self.emercy_shutdown_btn = QRadioButton(self.frame_4)
        self.buttonGroup.addButton(self.emercy_shutdown_btn)
        self.emercy_shutdown_btn.setObjectName(u"emercy_shutdown_btn")
        self.emercy_shutdown_btn.setMinimumSize(QSize(250, 40))
        self.emercy_shutdown_btn.setStyleSheet(u"QRadioButton{\n"
"font: 24px;\n"
"}")
        self.emercy_shutdown_btn.setChecked(True)

        self.verticalLayout_5.addWidget(self.emercy_shutdown_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.windows.addWidget(self.walk_page)
        self.gain_page = QWidget()
        self.gain_page.setObjectName(u"gain_page")
        self.verticalLayout_6 = QVBoxLayout(self.gain_page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.gain_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 35))
        self.frame_5.setMaximumSize(QSize(16777215, 45))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(158, 0))
        self.label_4.setMaximumSize(QSize(158, 16777215))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.line_4 = QFrame(self.frame_5)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_4)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(158, 0))
        self.label_5.setMaximumSize(QSize(158, 16777215))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.line_5 = QFrame(self.frame_5)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_5)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(158, 0))
        self.label_6.setMaximumSize(QSize(158, 16777215))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_6)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.line_6 = QFrame(self.gain_page)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_6)

        self.frame_66 = QFrame(self.gain_page)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(465, 40))
        self.frame_66.setMaximumSize(QSize(465, 40))
        self.frame_66.setFrameShape(QFrame.NoFrame)
        self.frame_66.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_68.setSpacing(5)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 5, 0)
        self.label_135 = QLabel(self.frame_66)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setMinimumSize(QSize(158, 0))
        self.label_135.setMaximumSize(QSize(158, 16777215))
        self.label_135.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_68.addWidget(self.label_135)

        self.label_136 = QLabel(self.frame_66)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setMinimumSize(QSize(158, 0))
        self.label_136.setMaximumSize(QSize(158, 16777215))
        self.label_136.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_68.addWidget(self.label_136)

        self.doubleSpinBox_65 = QDoubleSpinBox(self.frame_66)
        self.doubleSpinBox_65.setObjectName(u"doubleSpinBox_65")
        self.doubleSpinBox_65.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_65.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_65.setStyleSheet(u"")
        self.doubleSpinBox_65.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox_65.setMaximum(100.000000000000000)
        self.doubleSpinBox_65.setValue(0.000000000000000)

        self.horizontalLayout_68.addWidget(self.doubleSpinBox_65)


        self.verticalLayout_6.addWidget(self.frame_66)

        self.frame_67 = QFrame(self.gain_page)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(465, 40))
        self.frame_67.setMaximumSize(QSize(465, 40))
        self.frame_67.setFrameShape(QFrame.NoFrame)
        self.frame_67.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_69.setSpacing(5)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 5, 0)
        self.label_137 = QLabel(self.frame_67)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setMinimumSize(QSize(158, 0))
        self.label_137.setMaximumSize(QSize(158, 16777215))
        self.label_137.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.label_137)

        self.label_138 = QLabel(self.frame_67)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setMinimumSize(QSize(158, 0))
        self.label_138.setMaximumSize(QSize(158, 16777215))
        self.label_138.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.label_138)

        self.doubleSpinBox_66 = QDoubleSpinBox(self.frame_67)
        self.doubleSpinBox_66.setObjectName(u"doubleSpinBox_66")
        self.doubleSpinBox_66.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_66.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_66.setStyleSheet(u"")
        self.doubleSpinBox_66.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox_66.setValue(0.000000000000000)

        self.horizontalLayout_69.addWidget(self.doubleSpinBox_66)


        self.verticalLayout_6.addWidget(self.frame_67)

        self.frame_77 = QFrame(self.gain_page)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(465, 40))
        self.frame_77.setMaximumSize(QSize(465, 40))
        self.frame_77.setFrameShape(QFrame.NoFrame)
        self.frame_77.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_79.setSpacing(5)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 5, 0)
        self.label_157 = QLabel(self.frame_77)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setMinimumSize(QSize(158, 0))
        self.label_157.setMaximumSize(QSize(158, 16777215))
        self.label_157.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_79.addWidget(self.label_157)

        self.label_158 = QLabel(self.frame_77)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setMinimumSize(QSize(158, 0))
        self.label_158.setMaximumSize(QSize(158, 16777215))
        self.label_158.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_79.addWidget(self.label_158)

        self.doubleSpinBox_76 = QDoubleSpinBox(self.frame_77)
        self.doubleSpinBox_76.setObjectName(u"doubleSpinBox_76")
        self.doubleSpinBox_76.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_76.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_76.setStyleSheet(u"")
        self.doubleSpinBox_76.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox_76.setDecimals(2)
        self.doubleSpinBox_76.setValue(0.000000000000000)

        self.horizontalLayout_79.addWidget(self.doubleSpinBox_76)


        self.verticalLayout_6.addWidget(self.frame_77)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.windows.addWidget(self.gain_page)
        self.parameters_page = QWidget()
        self.parameters_page.setObjectName(u"parameters_page")
        self.gridLayout = QGridLayout(self.parameters_page)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.parameters_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 466, 1200))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_55 = QFrame(self.scrollAreaWidgetContents)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(465, 40))
        self.frame_55.setMaximumSize(QSize(465, 40))
        self.frame_55.setFrameShape(QFrame.NoFrame)
        self.frame_55.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_57.setSpacing(5)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 5, 0)
        self.label_113 = QLabel(self.frame_55)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMinimumSize(QSize(158, 0))
        self.label_113.setMaximumSize(QSize(158, 16777215))
        self.label_113.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.label_113)

        self.label_114 = QLabel(self.frame_55)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMinimumSize(QSize(158, 0))
        self.label_114.setMaximumSize(QSize(158, 16777215))
        self.label_114.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.label_114)

        self.doubleSpinBox_54 = QDoubleSpinBox(self.frame_55)
        self.doubleSpinBox_54.setObjectName(u"doubleSpinBox_54")
        self.doubleSpinBox_54.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_54.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_54.setStyleSheet(u"")
        self.doubleSpinBox_54.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.doubleSpinBox_54)


        self.verticalLayout_4.addWidget(self.frame_55)

        self.frame_49 = QFrame(self.scrollAreaWidgetContents)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(465, 40))
        self.frame_49.setMaximumSize(QSize(465, 40))
        self.frame_49.setFrameShape(QFrame.NoFrame)
        self.frame_49.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_51.setSpacing(5)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 5, 0)
        self.label_101 = QLabel(self.frame_49)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setMinimumSize(QSize(158, 0))
        self.label_101.setMaximumSize(QSize(158, 16777215))
        self.label_101.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.label_101)

        self.label_102 = QLabel(self.frame_49)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setMinimumSize(QSize(158, 0))
        self.label_102.setMaximumSize(QSize(158, 16777215))
        self.label_102.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.label_102)

        self.doubleSpinBox_48 = QDoubleSpinBox(self.frame_49)
        self.doubleSpinBox_48.setObjectName(u"doubleSpinBox_48")
        self.doubleSpinBox_48.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_48.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_48.setStyleSheet(u"")
        self.doubleSpinBox_48.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.doubleSpinBox_48)


        self.verticalLayout_4.addWidget(self.frame_49)

        self.frame_53 = QFrame(self.scrollAreaWidgetContents)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(465, 40))
        self.frame_53.setMaximumSize(QSize(465, 40))
        self.frame_53.setFrameShape(QFrame.NoFrame)
        self.frame_53.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_55.setSpacing(5)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 5, 0)
        self.label_109 = QLabel(self.frame_53)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setMinimumSize(QSize(158, 0))
        self.label_109.setMaximumSize(QSize(158, 16777215))
        self.label_109.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_55.addWidget(self.label_109)

        self.label_110 = QLabel(self.frame_53)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setMinimumSize(QSize(158, 0))
        self.label_110.setMaximumSize(QSize(158, 16777215))
        self.label_110.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_55.addWidget(self.label_110)

        self.doubleSpinBox_52 = QDoubleSpinBox(self.frame_53)
        self.doubleSpinBox_52.setObjectName(u"doubleSpinBox_52")
        self.doubleSpinBox_52.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_52.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_52.setStyleSheet(u"")
        self.doubleSpinBox_52.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_55.addWidget(self.doubleSpinBox_52)


        self.verticalLayout_4.addWidget(self.frame_53)

        self.frame_63 = QFrame(self.scrollAreaWidgetContents)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(465, 40))
        self.frame_63.setMaximumSize(QSize(465, 40))
        self.frame_63.setFrameShape(QFrame.NoFrame)
        self.frame_63.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_65.setSpacing(5)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 5, 0)
        self.label_129 = QLabel(self.frame_63)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMinimumSize(QSize(158, 0))
        self.label_129.setMaximumSize(QSize(158, 16777215))
        self.label_129.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.label_129)

        self.label_130 = QLabel(self.frame_63)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setMinimumSize(QSize(158, 0))
        self.label_130.setMaximumSize(QSize(158, 16777215))
        self.label_130.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.label_130)

        self.doubleSpinBox_62 = QDoubleSpinBox(self.frame_63)
        self.doubleSpinBox_62.setObjectName(u"doubleSpinBox_62")
        self.doubleSpinBox_62.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_62.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_62.setStyleSheet(u"")
        self.doubleSpinBox_62.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.doubleSpinBox_62)


        self.verticalLayout_4.addWidget(self.frame_63)

        self.frame_46 = QFrame(self.scrollAreaWidgetContents)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(465, 40))
        self.frame_46.setMaximumSize(QSize(465, 40))
        self.frame_46.setFrameShape(QFrame.NoFrame)
        self.frame_46.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_48.setSpacing(5)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 5, 0)
        self.label_95 = QLabel(self.frame_46)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setMinimumSize(QSize(158, 0))
        self.label_95.setMaximumSize(QSize(158, 16777215))
        self.label_95.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.label_95)

        self.label_96 = QLabel(self.frame_46)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setMinimumSize(QSize(158, 0))
        self.label_96.setMaximumSize(QSize(158, 16777215))
        self.label_96.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.label_96)

        self.doubleSpinBox_45 = QDoubleSpinBox(self.frame_46)
        self.doubleSpinBox_45.setObjectName(u"doubleSpinBox_45")
        self.doubleSpinBox_45.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_45.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_45.setStyleSheet(u"")
        self.doubleSpinBox_45.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.doubleSpinBox_45)


        self.verticalLayout_4.addWidget(self.frame_46)

        self.frame_65 = QFrame(self.scrollAreaWidgetContents)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMinimumSize(QSize(465, 40))
        self.frame_65.setMaximumSize(QSize(465, 40))
        self.frame_65.setFrameShape(QFrame.NoFrame)
        self.frame_65.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_67.setSpacing(5)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 5, 0)
        self.label_133 = QLabel(self.frame_65)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setMinimumSize(QSize(158, 0))
        self.label_133.setMaximumSize(QSize(158, 16777215))
        self.label_133.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_67.addWidget(self.label_133)

        self.label_134 = QLabel(self.frame_65)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setMinimumSize(QSize(158, 0))
        self.label_134.setMaximumSize(QSize(158, 16777215))
        self.label_134.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_67.addWidget(self.label_134)

        self.doubleSpinBox_64 = QDoubleSpinBox(self.frame_65)
        self.doubleSpinBox_64.setObjectName(u"doubleSpinBox_64")
        self.doubleSpinBox_64.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_64.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_64.setStyleSheet(u"")
        self.doubleSpinBox_64.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_67.addWidget(self.doubleSpinBox_64)


        self.verticalLayout_4.addWidget(self.frame_65)

        self.frame_47 = QFrame(self.scrollAreaWidgetContents)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(465, 40))
        self.frame_47.setMaximumSize(QSize(465, 40))
        self.frame_47.setFrameShape(QFrame.NoFrame)
        self.frame_47.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_49.setSpacing(5)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 5, 0)
        self.label_97 = QLabel(self.frame_47)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMinimumSize(QSize(158, 0))
        self.label_97.setMaximumSize(QSize(158, 16777215))
        self.label_97.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.label_97)

        self.label_98 = QLabel(self.frame_47)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMinimumSize(QSize(158, 0))
        self.label_98.setMaximumSize(QSize(158, 16777215))
        self.label_98.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.label_98)

        self.doubleSpinBox_46 = QDoubleSpinBox(self.frame_47)
        self.doubleSpinBox_46.setObjectName(u"doubleSpinBox_46")
        self.doubleSpinBox_46.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_46.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_46.setStyleSheet(u"")
        self.doubleSpinBox_46.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.doubleSpinBox_46)


        self.verticalLayout_4.addWidget(self.frame_47)

        self.frame_62 = QFrame(self.scrollAreaWidgetContents)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(465, 40))
        self.frame_62.setMaximumSize(QSize(465, 40))
        self.frame_62.setFrameShape(QFrame.NoFrame)
        self.frame_62.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_64.setSpacing(5)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 5, 0)
        self.label_127 = QLabel(self.frame_62)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMinimumSize(QSize(158, 0))
        self.label_127.setMaximumSize(QSize(158, 16777215))
        self.label_127.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_64.addWidget(self.label_127)

        self.label_128 = QLabel(self.frame_62)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMinimumSize(QSize(158, 0))
        self.label_128.setMaximumSize(QSize(158, 16777215))
        self.label_128.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_64.addWidget(self.label_128)

        self.doubleSpinBox_61 = QDoubleSpinBox(self.frame_62)
        self.doubleSpinBox_61.setObjectName(u"doubleSpinBox_61")
        self.doubleSpinBox_61.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_61.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_61.setStyleSheet(u"")
        self.doubleSpinBox_61.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_64.addWidget(self.doubleSpinBox_61)


        self.verticalLayout_4.addWidget(self.frame_62)

        self.frame_61 = QFrame(self.scrollAreaWidgetContents)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(465, 40))
        self.frame_61.setMaximumSize(QSize(465, 40))
        self.frame_61.setFrameShape(QFrame.NoFrame)
        self.frame_61.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_63.setSpacing(5)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 5, 0)
        self.label_125 = QLabel(self.frame_61)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMinimumSize(QSize(158, 0))
        self.label_125.setMaximumSize(QSize(158, 16777215))
        self.label_125.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.label_125)

        self.label_126 = QLabel(self.frame_61)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMinimumSize(QSize(158, 0))
        self.label_126.setMaximumSize(QSize(158, 16777215))
        self.label_126.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.label_126)

        self.doubleSpinBox_60 = QDoubleSpinBox(self.frame_61)
        self.doubleSpinBox_60.setObjectName(u"doubleSpinBox_60")
        self.doubleSpinBox_60.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_60.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_60.setStyleSheet(u"")
        self.doubleSpinBox_60.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.doubleSpinBox_60)


        self.verticalLayout_4.addWidget(self.frame_61)

        self.frame_51 = QFrame(self.scrollAreaWidgetContents)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(465, 40))
        self.frame_51.setMaximumSize(QSize(465, 40))
        self.frame_51.setFrameShape(QFrame.NoFrame)
        self.frame_51.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_53.setSpacing(5)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 5, 0)
        self.label_105 = QLabel(self.frame_51)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setMinimumSize(QSize(158, 0))
        self.label_105.setMaximumSize(QSize(158, 16777215))
        self.label_105.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.label_105)

        self.label_106 = QLabel(self.frame_51)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setMinimumSize(QSize(158, 0))
        self.label_106.setMaximumSize(QSize(158, 16777215))
        self.label_106.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.label_106)

        self.doubleSpinBox_50 = QDoubleSpinBox(self.frame_51)
        self.doubleSpinBox_50.setObjectName(u"doubleSpinBox_50")
        self.doubleSpinBox_50.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_50.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_50.setStyleSheet(u"")
        self.doubleSpinBox_50.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.doubleSpinBox_50)


        self.verticalLayout_4.addWidget(self.frame_51)

        self.frame_57 = QFrame(self.scrollAreaWidgetContents)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMinimumSize(QSize(465, 40))
        self.frame_57.setMaximumSize(QSize(465, 40))
        self.frame_57.setFrameShape(QFrame.NoFrame)
        self.frame_57.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_59.setSpacing(5)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 5, 0)
        self.label_117 = QLabel(self.frame_57)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMinimumSize(QSize(158, 0))
        self.label_117.setMaximumSize(QSize(158, 16777215))
        self.label_117.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_59.addWidget(self.label_117)

        self.label_118 = QLabel(self.frame_57)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMinimumSize(QSize(158, 0))
        self.label_118.setMaximumSize(QSize(158, 16777215))
        self.label_118.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_59.addWidget(self.label_118)

        self.doubleSpinBox_56 = QDoubleSpinBox(self.frame_57)
        self.doubleSpinBox_56.setObjectName(u"doubleSpinBox_56")
        self.doubleSpinBox_56.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_56.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_56.setStyleSheet(u"")
        self.doubleSpinBox_56.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_59.addWidget(self.doubleSpinBox_56)


        self.verticalLayout_4.addWidget(self.frame_57)

        self.frame_45 = QFrame(self.scrollAreaWidgetContents)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(465, 40))
        self.frame_45.setMaximumSize(QSize(465, 40))
        self.frame_45.setFrameShape(QFrame.NoFrame)
        self.frame_45.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_44.setSpacing(5)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 5, 0)
        self.label_87 = QLabel(self.frame_45)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setMinimumSize(QSize(158, 0))
        self.label_87.setMaximumSize(QSize(158, 16777215))
        self.label_87.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.label_87)

        self.label_88 = QLabel(self.frame_45)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMinimumSize(QSize(158, 0))
        self.label_88.setMaximumSize(QSize(158, 16777215))
        self.label_88.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.label_88)

        self.doubleSpinBox_41 = QDoubleSpinBox(self.frame_45)
        self.doubleSpinBox_41.setObjectName(u"doubleSpinBox_41")
        self.doubleSpinBox_41.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_41.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_41.setStyleSheet(u"")
        self.doubleSpinBox_41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.doubleSpinBox_41)


        self.verticalLayout_4.addWidget(self.frame_45)

        self.frame_59 = QFrame(self.scrollAreaWidgetContents)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMinimumSize(QSize(465, 40))
        self.frame_59.setMaximumSize(QSize(465, 40))
        self.frame_59.setFrameShape(QFrame.NoFrame)
        self.frame_59.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_61.setSpacing(5)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 5, 0)
        self.label_121 = QLabel(self.frame_59)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMinimumSize(QSize(158, 0))
        self.label_121.setMaximumSize(QSize(158, 16777215))
        self.label_121.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_61.addWidget(self.label_121)

        self.label_122 = QLabel(self.frame_59)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMinimumSize(QSize(158, 0))
        self.label_122.setMaximumSize(QSize(158, 16777215))
        self.label_122.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_61.addWidget(self.label_122)

        self.doubleSpinBox_58 = QDoubleSpinBox(self.frame_59)
        self.doubleSpinBox_58.setObjectName(u"doubleSpinBox_58")
        self.doubleSpinBox_58.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_58.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_58.setStyleSheet(u"")
        self.doubleSpinBox_58.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_61.addWidget(self.doubleSpinBox_58)


        self.verticalLayout_4.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.scrollAreaWidgetContents)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(465, 40))
        self.frame_60.setMaximumSize(QSize(465, 40))
        self.frame_60.setFrameShape(QFrame.NoFrame)
        self.frame_60.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_62.setSpacing(5)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 5, 0)
        self.label_123 = QLabel(self.frame_60)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setMinimumSize(QSize(158, 0))
        self.label_123.setMaximumSize(QSize(158, 16777215))
        self.label_123.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.label_123)

        self.label_124 = QLabel(self.frame_60)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMinimumSize(QSize(158, 0))
        self.label_124.setMaximumSize(QSize(158, 16777215))
        self.label_124.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.label_124)

        self.doubleSpinBox_59 = QDoubleSpinBox(self.frame_60)
        self.doubleSpinBox_59.setObjectName(u"doubleSpinBox_59")
        self.doubleSpinBox_59.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_59.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_59.setStyleSheet(u"")
        self.doubleSpinBox_59.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.doubleSpinBox_59)


        self.verticalLayout_4.addWidget(self.frame_60)

        self.frame_58 = QFrame(self.scrollAreaWidgetContents)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(465, 40))
        self.frame_58.setMaximumSize(QSize(465, 40))
        self.frame_58.setFrameShape(QFrame.NoFrame)
        self.frame_58.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_60.setSpacing(5)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 5, 0)
        self.label_119 = QLabel(self.frame_58)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMinimumSize(QSize(158, 0))
        self.label_119.setMaximumSize(QSize(158, 16777215))
        self.label_119.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.label_119)

        self.label_120 = QLabel(self.frame_58)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMinimumSize(QSize(158, 0))
        self.label_120.setMaximumSize(QSize(158, 16777215))
        self.label_120.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.label_120)

        self.doubleSpinBox_57 = QDoubleSpinBox(self.frame_58)
        self.doubleSpinBox_57.setObjectName(u"doubleSpinBox_57")
        self.doubleSpinBox_57.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_57.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_57.setStyleSheet(u"")
        self.doubleSpinBox_57.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.doubleSpinBox_57)


        self.verticalLayout_4.addWidget(self.frame_58)

        self.frame_76 = QFrame(self.scrollAreaWidgetContents)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(465, 40))
        self.frame_76.setMaximumSize(QSize(465, 40))
        self.frame_76.setFrameShape(QFrame.NoFrame)
        self.frame_76.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_78.setSpacing(5)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 5, 0)
        self.label_155 = QLabel(self.frame_76)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setMinimumSize(QSize(158, 0))
        self.label_155.setMaximumSize(QSize(158, 16777215))
        self.label_155.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_78.addWidget(self.label_155)

        self.label_156 = QLabel(self.frame_76)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setMinimumSize(QSize(158, 0))
        self.label_156.setMaximumSize(QSize(158, 16777215))
        self.label_156.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_78.addWidget(self.label_156)

        self.doubleSpinBox_75 = QDoubleSpinBox(self.frame_76)
        self.doubleSpinBox_75.setObjectName(u"doubleSpinBox_75")
        self.doubleSpinBox_75.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_75.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_75.setStyleSheet(u"")
        self.doubleSpinBox_75.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_78.addWidget(self.doubleSpinBox_75)


        self.verticalLayout_4.addWidget(self.frame_76)

        self.frame_75 = QFrame(self.scrollAreaWidgetContents)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(465, 40))
        self.frame_75.setMaximumSize(QSize(465, 40))
        self.frame_75.setFrameShape(QFrame.NoFrame)
        self.frame_75.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_77.setSpacing(5)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 5, 0)
        self.label_153 = QLabel(self.frame_75)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setMinimumSize(QSize(158, 0))
        self.label_153.setMaximumSize(QSize(158, 16777215))
        self.label_153.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_77.addWidget(self.label_153)

        self.label_154 = QLabel(self.frame_75)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setMinimumSize(QSize(158, 0))
        self.label_154.setMaximumSize(QSize(158, 16777215))
        self.label_154.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_77.addWidget(self.label_154)

        self.doubleSpinBox_74 = QDoubleSpinBox(self.frame_75)
        self.doubleSpinBox_74.setObjectName(u"doubleSpinBox_74")
        self.doubleSpinBox_74.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_74.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_74.setStyleSheet(u"")
        self.doubleSpinBox_74.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_77.addWidget(self.doubleSpinBox_74)


        self.verticalLayout_4.addWidget(self.frame_75)

        self.frame_74 = QFrame(self.scrollAreaWidgetContents)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMinimumSize(QSize(465, 40))
        self.frame_74.setMaximumSize(QSize(465, 40))
        self.frame_74.setFrameShape(QFrame.NoFrame)
        self.frame_74.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_76.setSpacing(5)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 5, 0)
        self.label_151 = QLabel(self.frame_74)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setMinimumSize(QSize(158, 0))
        self.label_151.setMaximumSize(QSize(158, 16777215))
        self.label_151.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_76.addWidget(self.label_151)

        self.label_152 = QLabel(self.frame_74)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setMinimumSize(QSize(158, 0))
        self.label_152.setMaximumSize(QSize(158, 16777215))
        self.label_152.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_76.addWidget(self.label_152)

        self.doubleSpinBox_73 = QDoubleSpinBox(self.frame_74)
        self.doubleSpinBox_73.setObjectName(u"doubleSpinBox_73")
        self.doubleSpinBox_73.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_73.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_73.setStyleSheet(u"")
        self.doubleSpinBox_73.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_76.addWidget(self.doubleSpinBox_73)


        self.verticalLayout_4.addWidget(self.frame_74)

        self.frame_73 = QFrame(self.scrollAreaWidgetContents)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(465, 40))
        self.frame_73.setMaximumSize(QSize(465, 40))
        self.frame_73.setFrameShape(QFrame.NoFrame)
        self.frame_73.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_75.setSpacing(5)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 5, 0)
        self.label_149 = QLabel(self.frame_73)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setMinimumSize(QSize(158, 0))
        self.label_149.setMaximumSize(QSize(158, 16777215))
        self.label_149.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_75.addWidget(self.label_149)

        self.label_150 = QLabel(self.frame_73)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setMinimumSize(QSize(158, 0))
        self.label_150.setMaximumSize(QSize(158, 16777215))
        self.label_150.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_75.addWidget(self.label_150)

        self.doubleSpinBox_72 = QDoubleSpinBox(self.frame_73)
        self.doubleSpinBox_72.setObjectName(u"doubleSpinBox_72")
        self.doubleSpinBox_72.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_72.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_72.setStyleSheet(u"")
        self.doubleSpinBox_72.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_75.addWidget(self.doubleSpinBox_72)


        self.verticalLayout_4.addWidget(self.frame_73)

        self.frame_56 = QFrame(self.scrollAreaWidgetContents)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(465, 40))
        self.frame_56.setMaximumSize(QSize(465, 40))
        self.frame_56.setFrameShape(QFrame.NoFrame)
        self.frame_56.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_58.setSpacing(5)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 5, 0)
        self.label_115 = QLabel(self.frame_56)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMinimumSize(QSize(158, 0))
        self.label_115.setMaximumSize(QSize(158, 16777215))
        self.label_115.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_58.addWidget(self.label_115)

        self.label_116 = QLabel(self.frame_56)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMinimumSize(QSize(158, 0))
        self.label_116.setMaximumSize(QSize(158, 16777215))
        self.label_116.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_58.addWidget(self.label_116)

        self.doubleSpinBox_55 = QDoubleSpinBox(self.frame_56)
        self.doubleSpinBox_55.setObjectName(u"doubleSpinBox_55")
        self.doubleSpinBox_55.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_55.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_55.setStyleSheet(u"")
        self.doubleSpinBox_55.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_58.addWidget(self.doubleSpinBox_55)


        self.verticalLayout_4.addWidget(self.frame_56)

        self.frame_72 = QFrame(self.scrollAreaWidgetContents)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(465, 40))
        self.frame_72.setMaximumSize(QSize(465, 40))
        self.frame_72.setFrameShape(QFrame.NoFrame)
        self.frame_72.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_74.setSpacing(5)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 5, 0)
        self.label_147 = QLabel(self.frame_72)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setMinimumSize(QSize(158, 0))
        self.label_147.setMaximumSize(QSize(158, 16777215))
        self.label_147.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_74.addWidget(self.label_147)

        self.label_148 = QLabel(self.frame_72)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setMinimumSize(QSize(158, 0))
        self.label_148.setMaximumSize(QSize(158, 16777215))
        self.label_148.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_74.addWidget(self.label_148)

        self.doubleSpinBox_71 = QDoubleSpinBox(self.frame_72)
        self.doubleSpinBox_71.setObjectName(u"doubleSpinBox_71")
        self.doubleSpinBox_71.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_71.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_71.setStyleSheet(u"")
        self.doubleSpinBox_71.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_74.addWidget(self.doubleSpinBox_71)


        self.verticalLayout_4.addWidget(self.frame_72)

        self.frame_52 = QFrame(self.scrollAreaWidgetContents)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(465, 40))
        self.frame_52.setMaximumSize(QSize(465, 40))
        self.frame_52.setFrameShape(QFrame.NoFrame)
        self.frame_52.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_54.setSpacing(5)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 5, 0)
        self.label_107 = QLabel(self.frame_52)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setMinimumSize(QSize(158, 0))
        self.label_107.setMaximumSize(QSize(158, 16777215))
        self.label_107.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_54.addWidget(self.label_107)

        self.label_108 = QLabel(self.frame_52)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setMinimumSize(QSize(158, 0))
        self.label_108.setMaximumSize(QSize(158, 16777215))
        self.label_108.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_54.addWidget(self.label_108)

        self.doubleSpinBox_51 = QDoubleSpinBox(self.frame_52)
        self.doubleSpinBox_51.setObjectName(u"doubleSpinBox_51")
        self.doubleSpinBox_51.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_51.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_51.setStyleSheet(u"")
        self.doubleSpinBox_51.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_54.addWidget(self.doubleSpinBox_51)


        self.verticalLayout_4.addWidget(self.frame_52)

        self.frame_50 = QFrame(self.scrollAreaWidgetContents)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(465, 40))
        self.frame_50.setMaximumSize(QSize(465, 40))
        self.frame_50.setFrameShape(QFrame.NoFrame)
        self.frame_50.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_52.setSpacing(5)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 5, 0)
        self.label_103 = QLabel(self.frame_50)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setMinimumSize(QSize(158, 0))
        self.label_103.setMaximumSize(QSize(158, 16777215))
        self.label_103.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.label_103)

        self.label_104 = QLabel(self.frame_50)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setMinimumSize(QSize(158, 0))
        self.label_104.setMaximumSize(QSize(158, 16777215))
        self.label_104.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.label_104)

        self.doubleSpinBox_49 = QDoubleSpinBox(self.frame_50)
        self.doubleSpinBox_49.setObjectName(u"doubleSpinBox_49")
        self.doubleSpinBox_49.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_49.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_49.setStyleSheet(u"")
        self.doubleSpinBox_49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.doubleSpinBox_49)


        self.verticalLayout_4.addWidget(self.frame_50)

        self.frame_64 = QFrame(self.scrollAreaWidgetContents)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(465, 40))
        self.frame_64.setMaximumSize(QSize(465, 40))
        self.frame_64.setFrameShape(QFrame.NoFrame)
        self.frame_64.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_66.setSpacing(5)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 5, 0)
        self.label_131 = QLabel(self.frame_64)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setMinimumSize(QSize(158, 0))
        self.label_131.setMaximumSize(QSize(158, 16777215))
        self.label_131.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.label_131)

        self.label_132 = QLabel(self.frame_64)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setMinimumSize(QSize(158, 0))
        self.label_132.setMaximumSize(QSize(158, 16777215))
        self.label_132.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.label_132)

        self.doubleSpinBox_63 = QDoubleSpinBox(self.frame_64)
        self.doubleSpinBox_63.setObjectName(u"doubleSpinBox_63")
        self.doubleSpinBox_63.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_63.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_63.setStyleSheet(u"")
        self.doubleSpinBox_63.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.doubleSpinBox_63)


        self.verticalLayout_4.addWidget(self.frame_64)

        self.frame_71 = QFrame(self.scrollAreaWidgetContents)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMinimumSize(QSize(465, 40))
        self.frame_71.setMaximumSize(QSize(465, 40))
        self.frame_71.setFrameShape(QFrame.NoFrame)
        self.frame_71.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_73.setSpacing(5)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 5, 0)
        self.label_145 = QLabel(self.frame_71)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setMinimumSize(QSize(158, 0))
        self.label_145.setMaximumSize(QSize(158, 16777215))
        self.label_145.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_73.addWidget(self.label_145)

        self.label_146 = QLabel(self.frame_71)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setMinimumSize(QSize(158, 0))
        self.label_146.setMaximumSize(QSize(158, 16777215))
        self.label_146.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_73.addWidget(self.label_146)

        self.doubleSpinBox_70 = QDoubleSpinBox(self.frame_71)
        self.doubleSpinBox_70.setObjectName(u"doubleSpinBox_70")
        self.doubleSpinBox_70.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_70.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_70.setStyleSheet(u"")
        self.doubleSpinBox_70.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_73.addWidget(self.doubleSpinBox_70)


        self.verticalLayout_4.addWidget(self.frame_71)

        self.frame_54 = QFrame(self.scrollAreaWidgetContents)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(465, 40))
        self.frame_54.setMaximumSize(QSize(465, 40))
        self.frame_54.setFrameShape(QFrame.NoFrame)
        self.frame_54.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_56.setSpacing(5)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 5, 0)
        self.label_111 = QLabel(self.frame_54)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setMinimumSize(QSize(158, 0))
        self.label_111.setMaximumSize(QSize(158, 16777215))
        self.label_111.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.label_111)

        self.label_112 = QLabel(self.frame_54)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setMinimumSize(QSize(158, 0))
        self.label_112.setMaximumSize(QSize(158, 16777215))
        self.label_112.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.label_112)

        self.doubleSpinBox_53 = QDoubleSpinBox(self.frame_54)
        self.doubleSpinBox_53.setObjectName(u"doubleSpinBox_53")
        self.doubleSpinBox_53.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_53.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_53.setStyleSheet(u"")
        self.doubleSpinBox_53.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.doubleSpinBox_53)


        self.verticalLayout_4.addWidget(self.frame_54)

        self.frame_70 = QFrame(self.scrollAreaWidgetContents)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(465, 40))
        self.frame_70.setMaximumSize(QSize(465, 40))
        self.frame_70.setFrameShape(QFrame.NoFrame)
        self.frame_70.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_72.setSpacing(5)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 5, 0)
        self.label_143 = QLabel(self.frame_70)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setMinimumSize(QSize(158, 0))
        self.label_143.setMaximumSize(QSize(158, 16777215))
        self.label_143.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_72.addWidget(self.label_143)

        self.label_144 = QLabel(self.frame_70)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setMinimumSize(QSize(158, 0))
        self.label_144.setMaximumSize(QSize(158, 16777215))
        self.label_144.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_72.addWidget(self.label_144)

        self.doubleSpinBox_69 = QDoubleSpinBox(self.frame_70)
        self.doubleSpinBox_69.setObjectName(u"doubleSpinBox_69")
        self.doubleSpinBox_69.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_69.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_69.setStyleSheet(u"")
        self.doubleSpinBox_69.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_72.addWidget(self.doubleSpinBox_69)


        self.verticalLayout_4.addWidget(self.frame_70)

        self.frame_48 = QFrame(self.scrollAreaWidgetContents)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(465, 40))
        self.frame_48.setMaximumSize(QSize(465, 40))
        self.frame_48.setFrameShape(QFrame.NoFrame)
        self.frame_48.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_50.setSpacing(5)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 5, 0)
        self.label_99 = QLabel(self.frame_48)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setMinimumSize(QSize(158, 0))
        self.label_99.setMaximumSize(QSize(158, 16777215))
        self.label_99.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.label_99)

        self.label_100 = QLabel(self.frame_48)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setMinimumSize(QSize(158, 0))
        self.label_100.setMaximumSize(QSize(158, 16777215))
        self.label_100.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.label_100)

        self.doubleSpinBox_47 = QDoubleSpinBox(self.frame_48)
        self.doubleSpinBox_47.setObjectName(u"doubleSpinBox_47")
        self.doubleSpinBox_47.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_47.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_47.setStyleSheet(u"")
        self.doubleSpinBox_47.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.doubleSpinBox_47)


        self.verticalLayout_4.addWidget(self.frame_48)

        self.frame_69 = QFrame(self.scrollAreaWidgetContents)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(465, 40))
        self.frame_69.setMaximumSize(QSize(465, 40))
        self.frame_69.setFrameShape(QFrame.NoFrame)
        self.frame_69.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_71.setSpacing(5)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 5, 0)
        self.label_141 = QLabel(self.frame_69)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setMinimumSize(QSize(158, 0))
        self.label_141.setMaximumSize(QSize(158, 16777215))
        self.label_141.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_71.addWidget(self.label_141)

        self.label_142 = QLabel(self.frame_69)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setMinimumSize(QSize(158, 0))
        self.label_142.setMaximumSize(QSize(158, 16777215))
        self.label_142.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_71.addWidget(self.label_142)

        self.doubleSpinBox_68 = QDoubleSpinBox(self.frame_69)
        self.doubleSpinBox_68.setObjectName(u"doubleSpinBox_68")
        self.doubleSpinBox_68.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_68.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_68.setStyleSheet(u"")
        self.doubleSpinBox_68.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_71.addWidget(self.doubleSpinBox_68)


        self.verticalLayout_4.addWidget(self.frame_69)

        self.frame_68 = QFrame(self.scrollAreaWidgetContents)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(465, 40))
        self.frame_68.setMaximumSize(QSize(465, 40))
        self.frame_68.setFrameShape(QFrame.NoFrame)
        self.frame_68.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_70.setSpacing(5)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 5, 0)
        self.label_139 = QLabel(self.frame_68)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setMinimumSize(QSize(158, 0))
        self.label_139.setMaximumSize(QSize(158, 16777215))
        self.label_139.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_70.addWidget(self.label_139)

        self.label_140 = QLabel(self.frame_68)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setMinimumSize(QSize(158, 0))
        self.label_140.setMaximumSize(QSize(158, 16777215))
        self.label_140.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_70.addWidget(self.label_140)

        self.doubleSpinBox_67 = QDoubleSpinBox(self.frame_68)
        self.doubleSpinBox_67.setObjectName(u"doubleSpinBox_67")
        self.doubleSpinBox_67.setMinimumSize(QSize(130, 0))
        self.doubleSpinBox_67.setMaximumSize(QSize(130, 16777215))
        self.doubleSpinBox_67.setStyleSheet(u"")
        self.doubleSpinBox_67.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_70.addWidget(self.doubleSpinBox_67)


        self.verticalLayout_4.addWidget(self.frame_68)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1)

        self.frame = QFrame(self.parameters_page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 35))
        self.frame.setMaximumSize(QSize(16777215, 45))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(158, 0))
        self.label.setMaximumSize(QSize(158, 16777215))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(158, 0))
        self.label_2.setMaximumSize(QSize(158, 16777215))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(158, 0))
        self.label_3.setMaximumSize(QSize(158, 16777215))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.line_3 = QFrame(self.parameters_page)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 1)

        self.windows.addWidget(self.parameters_page)

        self.verticalLayout_2.addWidget(self.windows)


        self.horizontalLayout.addWidget(self.change_variables_frame)

        self.motor_infos_frame = QFrame(self.centralwidget)
        self.motor_infos_frame.setObjectName(u"motor_infos_frame")
        self.motor_infos_frame.setMinimumSize(QSize(160, 0))
        self.motor_infos_frame.setMaximumSize(QSize(160, 16777215))
        self.motor_infos_frame.setFrameShape(QFrame.StyledPanel)
        self.motor_infos_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.motor_infos_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.file_menu = QMenu(self.menubar)
        self.file_menu.setObjectName(u"file_menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.file_menu.menuAction())
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.load_action)

        self.retranslateUi(MainWindow)

        self.windows.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        MainWindow.setWindowFilePath("")
        self.save_action.setText(QCoreApplication.translate("MainWindow", u"Salvar..", None))
        self.load_action.setText(QCoreApplication.translate("MainWindow", u"Carregar...", None))
        self.walk_window_btn.setText(QCoreApplication.translate("MainWindow", u"Caminhada", None))
        self.gain_window_btn.setText(QCoreApplication.translate("MainWindow", u"Ganho", None))
        self.parameters_window_btn.setText(QCoreApplication.translate("MainWindow", u"Parametros", None))
        self.update_window_btn.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.walk_forward_btn.setText(QCoreApplication.translate("MainWindow", u"walk_forward", None))
        self.rotate_clockwise_btn.setText(QCoreApplication.translate("MainWindow", u"rotate_clockwise", None))
        self.rotate_c_clockwise_btn.setText(QCoreApplication.translate("MainWindow", u"rotate_counter_clockwise", None))
        self.emercy_shutdown_btn.setText(QCoreApplication.translate("MainWindow", u"emergency_shutdown", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Par\u00e2metro</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Valor<br/>atual</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Novo<br/>valor</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_135.setToolTip(QCoreApplication.translate("MainWindow", u"Footstep forward (X) length (in meters). <0 goes backward. Note that you may have to find the actual value offset for the robot neutral.", None))
#endif // QT_CONFIG(tooltip)
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"stepGain", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_137.setToolTip(QCoreApplication.translate("MainWindow", u"Footstep lateral (Y) length (in meters). =0 goes straight. >0 makes lateral steps on the left. <0 makes lateral steps on the right.", None))
#endif // QT_CONFIG(tooltip)
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"lateralGain", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_157.setToolTip(QCoreApplication.translate("MainWindow", u"Footstep rotation angle (in radians). =0 goes straight. >0 turns on the left. <0 turns steps on the right.", None))
#endif // QT_CONFIG(tooltip)
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"turnGain", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_113.setToolTip(QCoreApplication.translate("MainWindow", u"Complete walk cycle (two steps) frequency (in Hertz).", None))
#endif // QT_CONFIG(tooltip)
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"freq", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_101.setToolTip(QCoreApplication.translate("MainWindow", u"The length of the double support phase in walk cycle. =0 is full single support, no double support phase. =1 is full double support phase.", None))
#endif // QT_CONFIG(tooltip)
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"supportPhaseRatio", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_109.setToolTip(QCoreApplication.translate("MainWindow", u"Lateral distance offset between the two foot (in meters).", None))
#endif // QT_CONFIG(tooltip)
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"footYOffset", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_129.setToolTip(QCoreApplication.translate("MainWindow", u"Foot height (Z) during flying backward to forward (in meters).", None))
#endif // QT_CONFIG(tooltip)
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"riseGain", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_95.setToolTip(QCoreApplication.translate("MainWindow", u"Amplitude of lateral oscillation of the trunk with respect to the feet (in meters).", None))
#endif // QT_CONFIG(tooltip)
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"swingGain", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"swingRollGain", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_97.setToolTip(QCoreApplication.translate("MainWindow", u"Phase shift used to desynchronize the lateral trunk oscillation and footsteps movement.", None))
#endif // QT_CONFIG(tooltip)
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"swingPhase", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_127.setToolTip(QCoreApplication.translate("MainWindow", u"Trunk forward (X) translation with respect to the feet (in meters). >0 goes forward. <0 goes backward.", None))
#endif // QT_CONFIG(tooltip)
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"trunkXOffset", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_125.setToolTip(QCoreApplication.translate("MainWindow", u"Trunk lateral (Y) translation with respect to the feet (in meters). >0 goes on the left. <0 goes on the right.", None))
#endif // QT_CONFIG(tooltip)
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"trunkYOffset", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_105.setToolTip(QCoreApplication.translate("MainWindow", u"Trunk height from the ground. =0 is maximum height (in meters). >0 is lower to the ground.", None))
#endif // QT_CONFIG(tooltip)
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"trunkZOffset", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_117.setToolTip(QCoreApplication.translate("MainWindow", u"Trunk pitch (Y) orientation. >0 bends forward (in radians). <0 bends backward.", None))
#endif // QT_CONFIG(tooltip)
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"trunkPitch", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_87.setToolTip(QCoreApplication.translate("MainWindow", u"Trunk roll (X) orientation. >0 bends on the left (in radians). <0 bends on the right.", None))
#endif // QT_CONFIG(tooltip)
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"trunkRoll", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"swingPause", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"swingVel", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"stepUpVel", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"stepDownVel", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"riseUpVel", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"riseDownVel", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"extraLeftX", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"extraLeftY", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"extraLeftZ", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"extraRightX", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"extraRightY", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_131.setToolTip(QCoreApplication.translate("MainWindow", u"Additional offset on left and right foot target orientation (in radians). They must be set to zero if not used.", None))
#endif // QT_CONFIG(tooltip)
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"extraRightZ", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"extraLeftYaw", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"extraLeftPitch", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"extraLeftRoll", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"extraRightYaw", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"extraRightPitch", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"extraRightRoll", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Par\u00e2metro</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Valor<br/>atual</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Novo<br/>valor</span></p></body></html>", None))
        self.file_menu.setTitle(QCoreApplication.translate("MainWindow", u"Arquivos", None))
    # retranslateUi

