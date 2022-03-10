# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frequency_setting.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frequency_setting(object):
    def setupUi(self, frequency_setting):
        frequency_setting.setObjectName("frequency_setting")
        frequency_setting.resize(395, 326)
        frequency_setting.setMinimumSize(QtCore.QSize(395, 326))
        frequency_setting.setMaximumSize(QtCore.QSize(395, 326))
        self.centralwidget = QtWidgets.QWidget(frequency_setting)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(70, 50, 231, 211))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radio_60HZ = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radio_60HZ.setFont(font)
        self.radio_60HZ.setChecked(True)
        self.radio_60HZ.setObjectName("radio_60HZ")
        self.verticalLayout_2.addWidget(self.radio_60HZ)
        self.radio_120HZ = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radio_120HZ.setFont(font)
        self.radio_120HZ.setObjectName("radio_120HZ")
        self.verticalLayout_2.addWidget(self.radio_120HZ)
        self.radio_250HZ = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radio_250HZ.setFont(font)
        self.radio_250HZ.setObjectName("radio_250HZ")
        self.verticalLayout_2.addWidget(self.radio_250HZ)
        self.radio_300HZ = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radio_300HZ.setFont(font)
        self.radio_300HZ.setObjectName("radio_300HZ")
        self.verticalLayout_2.addWidget(self.radio_300HZ)
        self.btnClear = QtWidgets.QPushButton(self.frame)
        self.btnClear.setGeometry(QtCore.QRect(150, 270, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.verticalLayout.addWidget(self.frame)
        frequency_setting.setCentralWidget(self.centralwidget)

        self.retranslateUi(frequency_setting)
        QtCore.QMetaObject.connectSlotsByName(frequency_setting)

    def retranslateUi(self, frequency_setting):
        _translate = QtCore.QCoreApplication.translate
        frequency_setting.setWindowTitle(_translate("frequency_setting", "MainWindow"))
        self.label.setText(_translate("frequency_setting", "频率设置"))
        self.radio_60HZ.setText(_translate("frequency_setting", "60Hz"))
        self.radio_120HZ.setText(_translate("frequency_setting", "120Hz"))
        self.radio_250HZ.setText(_translate("frequency_setting", "250Hz"))
        self.radio_300HZ.setText(_translate("frequency_setting", "300Hz"))
        self.btnClear.setText(_translate("frequency_setting", "确认"))

