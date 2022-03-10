# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScorePage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ScorePage(object):
    def setupUi(self, ScorePage):
        ScorePage.setObjectName("ScorePage")
        ScorePage.resize(908, 837)
        self.centralwidget = QtWidgets.QWidget(ScorePage)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(223, 11, 461, 815))
        self.groupBox_7.setMaximumSize(QtCore.QSize(461, 16777215))
        self.groupBox_7.setAutoFillBackground(False)
        self.groupBox_7.setStyleSheet("")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.scoreEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.scoreEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.scoreEdit.setFont(font)
        self.scoreEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreEdit.setReadOnly(True)
        self.scoreEdit.setObjectName("scoreEdit")
        self.horizontalLayout_8.addWidget(self.scoreEdit)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setMinimumSize(QtCore.QSize(411, 274))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.scoreSlider = QtWidgets.QSlider(self.groupBox_4)
        self.scoreSlider.setMinimumSize(QtCore.QSize(50, 0))
        self.scoreSlider.setStyleSheet("QSlider {\n"
"    padding-top: 15px;\n"
"    padding-bottom: 15px;\n"
"    border-radius: 5px;\n"
"}\n"
" \n"
"QSlider::add-page:vertical {\n"
"    background-color: rgb(85, 170, 255);\n"
"    width:5px;\n"
"    border-radius: 2px;\n"
"}\n"
" \n"
"QSlider::sub-page:vertical {\n"
"    \n"
"    background-color: rgb(229, 229, 229);\n"
"    width:5px;\n"
"    border-radius: 2px;\n"
"}\n"
" \n"
"QSlider::groove:vertical {\n"
"    background:transparent;\n"
"    width:80px;\n"
"}\n"
" \n"
"QSlider::handle:vertical {\n"
"    height: 20px;\n"
"    width: 20px;\n"
"    margin: 0px -4px 0px -4px;\n"
"    border-radius: 10px;\n"
"    background: rgb(255, 255, 255);\n"
"}")
        self.scoreSlider.setMaximum(100)
        self.scoreSlider.setSingleStep(1)
        self.scoreSlider.setPageStep(2)
        self.scoreSlider.setProperty("value", 50)
        self.scoreSlider.setSliderPosition(50)
        self.scoreSlider.setOrientation(QtCore.Qt.Vertical)
        self.scoreSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.scoreSlider.setObjectName("scoreSlider")
        self.horizontalLayout_6.addWidget(self.scoreSlider)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setMaximumSize(QtCore.QSize(271, 16777215))
        self.groupBox_5.setStyleSheet("border:none;")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout.setContentsMargins(-1, 15, -1, 15)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 18pt \"微软雅黑\";\n"
"background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #11998e, stop:1 #38ef7d);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 18pt \"微软雅黑\";\n"
"background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #38ef7d, stop:1 #DCE35B);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 18pt \"微软雅黑\";\n"
"background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #DCE35B, stop:1 #ffff00);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 18pt \"微软雅黑\";\n"
"background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffff00, stop:1 #f5af19);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 18pt \"微软雅黑\";\n"
"background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f5af19, stop:1 #f12711);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout_6.addWidget(self.groupBox_5)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_11.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setObjectName("groupBox_11")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_11)
        self.formLayout.setObjectName("formLayout")
        self.label_13 = QtWidgets.QLabel(self.groupBox_11)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.finishedEdit = QtWidgets.QLineEdit(self.groupBox_11)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.finishedEdit.setFont(font)
        self.finishedEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.finishedEdit.setReadOnly(False)
        self.finishedEdit.setObjectName("finishedEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.finishedEdit)
        self.label_14 = QtWidgets.QLabel(self.groupBox_11)
        self.label_14.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.currentPartEdit = QtWidgets.QLineEdit(self.groupBox_11)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.currentPartEdit.setFont(font)
        self.currentPartEdit.setText("")
        self.currentPartEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.currentPartEdit.setObjectName("currentPartEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.currentPartEdit)
        self.verticalLayout_5.addWidget(self.groupBox_11)
        self.btnSure = QtWidgets.QPushButton(self.centralwidget)
        self.btnSure.setGeometry(QtCore.QRect(720, 390, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnSure.setFont(font)
        self.btnSure.setObjectName("btnSure")
        ScorePage.setCentralWidget(self.centralwidget)

        self.retranslateUi(ScorePage)
        self.scoreSlider.valueChanged['int'].connect(ScorePage.changeSliderColor)
        QtCore.QMetaObject.connectSlotsByName(ScorePage)

    def retranslateUi(self, ScorePage):
        _translate = QtCore.QCoreApplication.translate
        ScorePage.setWindowTitle(_translate("ScorePage", "MainWindow"))
        self.groupBox_2.setTitle(_translate("ScorePage", "评分界面"))
        self.label.setText(_translate("ScorePage", "你当前选择的分数为："))
        self.scoreEdit.setText(_translate("ScorePage", "50"))
        self.label_2.setText(_translate("ScorePage", "很好"))
        self.label_3.setText(_translate("ScorePage", "好"))
        self.label_4.setText(_translate("ScorePage", "一般"))
        self.label_5.setText(_translate("ScorePage", "差"))
        self.label_6.setText(_translate("ScorePage", "很差"))
        self.groupBox_11.setTitle(_translate("ScorePage", "进度显示"))
        self.label_13.setText(_translate("ScorePage", "当前评价图片："))
        self.label_14.setText(_translate("ScorePage", "当前所评价图片区域："))
        self.btnSure.setText(_translate("ScorePage", "确认评分"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScorePage = QtWidgets.QMainWindow()
    ui = Ui_ScorePage()
    ui.setupUi(ScorePage)
    ScorePage.show()
    sys.exit(app.exec_())
