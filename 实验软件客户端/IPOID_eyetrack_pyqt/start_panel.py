# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_panel.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_start_panel(object):
    def setupUi(self, start_panel):
        start_panel.setObjectName("start_panel")
        start_panel.resize(843, 570)
        start_panel.setMinimumSize(QtCore.QSize(0, 0))
        start_panel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(start_panel)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 829, 501))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.tab)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(400, 450))
        self.frame.setMaximumSize(QtCore.QSize(400, 450))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_EyetrackStart = QtWidgets.QPushButton(self.frame)
        self.btn_EyetrackStart.setGeometry(QtCore.QRect(140, 400, 113, 29))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_EyetrackStart.setFont(font)
        self.btn_EyetrackStart.setObjectName("btn_EyetrackStart")
        self.eye_tracker_info = QtWidgets.QPlainTextEdit(self.frame)
        self.eye_tracker_info.setEnabled(False)
        self.eye_tracker_info.setGeometry(QtCore.QRect(20, 50, 361, 271))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.eye_tracker_info.setFont(font)
        self.eye_tracker_info.setFrameShape(QtWidgets.QFrame.Panel)
        self.eye_tracker_info.setFrameShadow(QtWidgets.QFrame.Plain)
        self.eye_tracker_info.setObjectName("eye_tracker_info")
        self.frame_2 = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(400, 450))
        self.frame_2.setMaximumSize(QtCore.QSize(400, 450))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btn_Calibration = QtWidgets.QPushButton(self.frame_2)
        self.btn_Calibration.setGeometry(QtCore.QRect(160, 400, 92, 29))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_Calibration.setFont(font)
        self.btn_Calibration.setObjectName("btn_Calibration")
        self.distance_show = QtWidgets.QProgressBar(self.frame_2)
        self.distance_show.setGeometry(QtCore.QRect(370, 50, 21, 271))
        self.distance_show.setMinimum(45)
        self.distance_show.setMaximum(75)
        self.distance_show.setProperty("value", 60)
        self.distance_show.setOrientation(QtCore.Qt.Vertical)
        self.distance_show.setObjectName("distance_show")
        self.distance_text = QtWidgets.QLabel(self.frame_2)
        self.distance_text.setGeometry(QtCore.QRect(370, 330, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.distance_text.setFont(font)
        self.distance_text.setText("")
        self.distance_text.setObjectName("distance_text")
        self.verticalLayout.addWidget(self.splitter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 801, 181))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setToolTipDuration(-1)
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    font: 20px \"黑体\";\n"
"    background-color: rgb(240, 240, 240);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(255, 0, 0);\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(28, 120, 167);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 60, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(140, 70, 641, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.btnDirget = QtWidgets.QPushButton(self.groupBox)
        self.btnDirget.setGeometry(QtCore.QRect(480, 120, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnDirget.setFont(font)
        self.btnDirget.setObjectName("btnDirget")
        self.btnApply = QtWidgets.QPushButton(self.groupBox)
        self.btnApply.setGeometry(QtCore.QRect(650, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnApply.setFont(font)
        self.btnApply.setObjectName("btnApply")
        self.btnStart = QtWidgets.QPushButton(self.tab_2)
        self.btnStart.setGeometry(QtCore.QRect(330, 410, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnStart.setFont(font)
        self.btnStart.setObjectName("btnStart")
        self.btnPreStart = QtWidgets.QPushButton(self.tab_2)
        self.btnPreStart.setGeometry(QtCore.QRect(330, 320, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnPreStart.setFont(font)
        self.btnPreStart.setObjectName("btnPreStart")
        self.tabWidget.addTab(self.tab_2, "")
        start_panel.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(start_panel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        start_panel.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(start_panel)
        self.statusbar.setObjectName("statusbar")
        start_panel.setStatusBar(self.statusbar)
        self.action_frequency = QtWidgets.QAction(start_panel)
        self.action_frequency.setObjectName("action_frequency")
        self.action_filter = QtWidgets.QAction(start_panel)
        self.action_filter.setObjectName("action_filter")
        self.menu.addAction(self.action_frequency)
        self.menu.addAction(self.action_filter)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(start_panel)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(start_panel)

    def retranslateUi(self, start_panel):
        _translate = QtCore.QCoreApplication.translate
        start_panel.setWindowTitle(_translate("start_panel", "MainWindow"))
        self.btn_EyetrackStart.setText(_translate("start_panel", "启动眼动仪"))
        self.btn_Calibration.setText(_translate("start_panel", "开始矫正"))
        self.distance_show.setFormat(_translate("start_panel", "%v"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("start_panel", "眼动仪"))
        self.groupBox.setTitle(_translate("start_panel", "数据库"))
        self.label.setText(_translate("start_panel", "数据库地址："))
        self.btnDirget.setText(_translate("start_panel", "设置地址"))
        self.btnApply.setText(_translate("start_panel", "应用"))
        self.btnStart.setText(_translate("start_panel", "开始实验"))
        self.btnPreStart.setText(_translate("start_panel", "开始预热实验"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("start_panel", "主观实验"))
        self.menu.setTitle(_translate("start_panel", "设置"))
        self.action_frequency.setText(_translate("start_panel", "设置频率"))
        self.action_filter.setText(_translate("start_panel", "设置滤波器"))

