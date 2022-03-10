# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InformationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InformationDialog(object):
    def setupUi(self, InformationDialog):
        InformationDialog.setObjectName("InformationDialog")
        InformationDialog.resize(578, 428)
        self.groupBox = QtWidgets.QGroupBox(InformationDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 551, 371))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 60, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 260, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.nameEdit = QtWidgets.QLineEdit(self.groupBox)
        self.nameEdit.setGeometry(QtCore.QRect(150, 60, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nameEdit.setFont(font)
        self.nameEdit.setObjectName("nameEdit")
        self.ageEdit = QtWidgets.QLineEdit(self.groupBox)
        self.ageEdit.setGeometry(QtCore.QRect(150, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ageEdit.setFont(font)
        self.ageEdit.setMaxLength(2)
        self.ageEdit.setObjectName("ageEdit")
        self.numberEdit = QtWidgets.QLineEdit(self.groupBox)
        self.numberEdit.setGeometry(QtCore.QRect(150, 200, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.numberEdit.setFont(font)
        self.numberEdit.setMaxLength(10)
        self.numberEdit.setObjectName("numberEdit")
        self.majorEdit = QtWidgets.QLineEdit(self.groupBox)
        self.majorEdit.setGeometry(QtCore.QRect(130, 260, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.majorEdit.setFont(font)
        self.majorEdit.setObjectName("majorEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(330, 40, 191, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.manButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.manButton.setGeometry(QtCore.QRect(20, 50, 61, 31))
        self.manButton.setChecked(True)
        self.manButton.setObjectName("manButton")
        self.womanButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.womanButton.setGeometry(QtCore.QRect(110, 50, 61, 31))
        self.womanButton.setObjectName("womanButton")
        self.btnYes = QtWidgets.QPushButton(self.groupBox)
        self.btnYes.setGeometry(QtCore.QRect(430, 310, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnYes.setFont(font)
        self.btnYes.setObjectName("btnYes")

        self.retranslateUi(InformationDialog)
        QtCore.QMetaObject.connectSlotsByName(InformationDialog)

    def retranslateUi(self, InformationDialog):
        _translate = QtCore.QCoreApplication.translate
        InformationDialog.setWindowTitle(_translate("InformationDialog", "Dialog"))
        self.groupBox.setTitle(_translate("InformationDialog", "请填写您的测试信息"))
        self.label.setText(_translate("InformationDialog", "姓名："))
        self.label_2.setText(_translate("InformationDialog", "年龄："))
        self.label_3.setText(_translate("InformationDialog", "测试编号："))
        self.label_4.setText(_translate("InformationDialog", "专业："))
        self.ageEdit.setInputMask(_translate("InformationDialog", "99;_"))
        self.numberEdit.setInputMask(_translate("InformationDialog", "9999999999;_"))
        self.groupBox_2.setTitle(_translate("InformationDialog", "性别"))
        self.manButton.setText(_translate("InformationDialog", "男"))
        self.womanButton.setText(_translate("InformationDialog", "女"))
        self.btnYes.setText(_translate("InformationDialog", "确定"))
