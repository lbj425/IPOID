
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QLabel
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import pyqtSlot,Qt,QTimer,QPoint

from PyQt5.QtGui import QPainter,QPen,QPixmap,QBrush
import sys

from calibration_result import Ui_Calibration_Result
import math


class MyLabel(QLabel):
    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)
        self.current_rad = 10
        self.list = [(0.5, 0.5), (0.1, 0.1), (0.9, 0.1), (0.9, 0.9), (0.1, 0.9)]
        self.eye_gaze_data = []

    def paintEvent(self, event):
        super().paintEvent(event)
        self.W = self.width()
        self.H = self.height()
        painter = QPainter()
        painter.begin(self)
        pen = QPen(Qt.black,1, Qt.SolidLine)
        painter.setPen(pen)
        brush = QBrush()
        brush.setColor(Qt.white)
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)
        for point in self.list:
             painter.drawEllipse(QPoint(point[0]*self.W,point[1]*self.H),self.current_rad,self.current_rad)
        pen = QPen(Qt.green,3, Qt.SolidLine)
        painter.setPen(pen)
        for gaze_data in self.eye_gaze_data:
             if math.isnan(gaze_data[0]) or math.isnan(gaze_data[1]):
                 continue
             if gaze_data[0]<0 or gaze_data[0]>1 or gaze_data[1]<0 or gaze_data[1]>1:
                 continue
             painter.drawPoint(QPoint(gaze_data[0]*self.W,gaze_data[1]*self.H))      
        painter.end()

class QmyCalibration_Result(QMainWindow):
     def __init__(self,parent=None):
         super().__init__(parent)
         self.ui = Ui_Calibration_Result()
         self.ui.setupUi(self)
         self.ui.splitter = QtWidgets.QSplitter(self.ui.frame)
         self.ui.splitter.setOrientation(QtCore.Qt.Horizontal)
         self.ui.splitter.setObjectName("splitter")
         self.left_result = MyLabel(self.ui.splitter)
         self.left_result.setAlignment(QtCore.Qt.AlignCenter)
         self.left_result.setObjectName("left_result")
         self.left_result.setFrameShape(QtWidgets.QFrame.Panel)
         self.right_result = MyLabel(self.ui.splitter)
         self.right_result.setAlignment(QtCore.Qt.AlignCenter)
         self.right_result.setObjectName("right_result")
         self.right_result.setFrameShape(QtWidgets.QFrame.Panel)
         self.ui.verticalLayout_2.addWidget(self.ui.splitter)
         
         
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyCalibration_Result()
    form.show()
    sys.exit(app.exec_())