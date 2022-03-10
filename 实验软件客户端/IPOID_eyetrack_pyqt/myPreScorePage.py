import sys

from PyQt5.QtWidgets import QApplication,QMainWindow

from PyQt5.QtCore import pyqtSlot,pyqtSignal,Qt

from preScorePage import Ui_ScorePage

import time

class QmyScorePage(QMainWindow):
    OneImageFinish = pyqtSignal(int)
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_ScorePage()
        self.ui.setupUi(self)
        self.ui.finishedEdit.setReadOnly(True)
        self.ui.currentPartEdit.setReadOnly(True)
        self.ui.btnSure.clicked.connect(self.emit_Score)
        self.setWindowFlag(Qt.FramelessWindowHint)

    @pyqtSlot(int)
    def on_scoreSlider_valueChanged(self,value):
        self.ui.scoreEdit.setText("%d"%value)

    @pyqtSlot()
    def emit_Score(self):
        Score = self.ui.scoreSlider.value()
        t= int(round(time.time()*1000))
        self.OneImageFinish.emit(Score)
        self.ui.scoreSlider.setValue(50)
        self.ui.scoreEdit.setText("50")
        self.close()

    def keyReleaseEvent(self,event):
        if event.key() == Qt.Key_Up:
            value = self.ui.scoreSlider.value()
            self.ui.scoreSlider.setValue(value+1)
        if event.key() == Qt.Key_Down:
            value = self.ui.scoreSlider.value()
            self.ui.scoreSlider.setValue(value-1)
        if event.key() == Qt.Key_Control:
            self.emit_Score()

    def changeSliderColor(self):
        num = self.ui.scoreSlider.value() // 10
        if 0 <= num < 2:
            self.ui.scoreSlider.setStyleSheet("QSlider {\n"
                                              "    padding-top: 15px;\n"
                                              "    padding-bottom: 15px;\n"
                                              "    border-radius: 5px;\n"
                                              "}\n"
                                              " \n"
                                              "QSlider::add-page:vertical {\n"
                                              "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f5af19, stop:1 #f12711);\n"
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
        elif 2 <= num < 4:
            self.ui.scoreSlider.setStyleSheet("QSlider {\n"
                                              "    padding-top: 15px;\n"
                                              "    padding-bottom: 15px;\n"
                                              "    border-radius: 5px;\n"
                                              "}\n"
                                              " \n"
                                              "QSlider::add-page:vertical {\n"
                                              "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffff00, stop:1 #f5af19);\n"
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
        elif 4 <= num < 6:
            self.ui.scoreSlider.setStyleSheet("QSlider {\n"
                                              "    padding-top: 15px;\n"
                                              "    padding-bottom: 15px;\n"
                                              "    border-radius: 5px;\n"
                                              "}\n"
                                              " \n"
                                              "QSlider::add-page:vertical {\n"
                                              "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #DCE35B, stop:1 #ffff00);\n"
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
        elif 6 <= num < 8:
            self.ui.scoreSlider.setStyleSheet("QSlider {\n"
                                              "    padding-top: 15px;\n"
                                              "    padding-bottom: 15px;\n"
                                              "    border-radius: 5px;\n"
                                              "}\n"
                                              " \n"
                                              "QSlider::add-page:vertical {\n"
                                              "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #38ef7d, stop:1 #DCE35B);\n"
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
        else:
            self.ui.scoreSlider.setStyleSheet("QSlider {\n"
                                              "    padding-top: 15px;\n"
                                              "    padding-bottom: 15px;\n"
                                              "    border-radius: 5px;\n"
                                              "}\n"
                                              " \n"
                                              "QSlider::add-page:vertical {\n"
                                              "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #11998e, stop:1 #38ef7d);\n"
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
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyScorePage()
    form.show()
    sys.exit(app.exec_())
