# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calibration_result.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calibration_Result(object):
    def setupUi(self, Calibration_Result):
        Calibration_Result.setObjectName("Calibration_Result")
        Calibration_Result.resize(960, 480)
        self.centralwidget = QtWidgets.QWidget(Calibration_Result)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addWidget(self.frame)
        Calibration_Result.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calibration_Result)
        QtCore.QMetaObject.connectSlotsByName(Calibration_Result)

    def retranslateUi(self, Calibration_Result):
        _translate = QtCore.QCoreApplication.translate
        Calibration_Result.setWindowTitle(_translate("Calibration_Result", "MainWindow"))

