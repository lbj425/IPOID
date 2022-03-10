# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calibration_panel.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_calibration_panel(object):
    def setupUi(self, calibration_panel):
        calibration_panel.setObjectName("calibration_panel")
        calibration_panel.resize(1919, 1080)
        self.centralwidget = QtWidgets.QWidget(calibration_panel)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        calibration_panel.setCentralWidget(self.centralwidget)

        self.retranslateUi(calibration_panel)
        QtCore.QMetaObject.connectSlotsByName(calibration_panel)

    def retranslateUi(self, calibration_panel):
        _translate = QtCore.QCoreApplication.translate
        calibration_panel.setWindowTitle(_translate("calibration_panel", "MainWindow"))
