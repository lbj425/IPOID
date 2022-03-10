# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Introduce_panel.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Introduce_panel(object):
    def setupUi(self, Introduce_panel):
        Introduce_panel.setObjectName("Introduce_panel")
        Introduce_panel.resize(795, 567)
        self.widget = QtWidgets.QWidget(Introduce_panel)
        self.widget.setGeometry(QtCore.QRect(0, 0, 807, 563))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(100, 20, 581, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setLineWidth(2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(30, 70, 751, 431))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(30, 510, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.btnEnter = QtWidgets.QPushButton(self.widget)
        self.btnEnter.setGeometry(QtCore.QRect(570, 510, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnEnter.setFont(font)
        self.btnEnter.setObjectName("btnEnter")

        self.retranslateUi(Introduce_panel)
        QtCore.QMetaObject.connectSlotsByName(Introduce_panel)

    def retranslateUi(self, Introduce_panel):
        _translate = QtCore.QCoreApplication.translate
        Introduce_panel.setWindowTitle(_translate("Introduce_panel", "Form"))
        self.label.setText(_translate("Introduce_panel", "基于眼动的局部图像质量评价测试"))
        self.textEdit.setHtml(_translate("Introduce_panel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">相关介绍内容</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">欢迎参加主观质量评价实验</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">本次实验评分方法为SS法，即不会有对照图片，请你根据自己的判断对每张图片评分，评分过程中先评价整体图片再评价局部图片。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">评分阶段为全屏显示，目的是适应1080图片大小。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">所有评分操作可以通过键盘完成。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">具体操作如下：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">每张图的最小评分时间结束后，按回车键进入评分页面。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">评分界面中，按Up和Down键可以滑动评分，也可以通过鼠标滚轮滚动。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">单幅评分结束后按Control键确定评分，也可以鼠标点击确认评分按钮。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">在评分过程中请保持身体端正。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">在评分过程中想中途退出请按Q</span></p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("Introduce_panel", "相关介绍内容"))
        self.checkBox.setText(_translate("Introduce_panel", "我已阅读"))
        self.btnEnter.setText(_translate("Introduce_panel", "进入信息填写界面"))

