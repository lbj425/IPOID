from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QLabel
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import pyqtSlot,Qt,QTimer,QPoint,pyqtSignal

from PyQt5.QtGui import QPainter,QPen,QPixmap,QBrush

from calibration_panel import Ui_calibration_panel


import sys

import tobii_research as tr

import time
import datetime

def gaze_data_callback(gaze_data):
     global global_gaze_data
     global_gaze_data.append(gaze_data)
class MyLabel(QLabel):
    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)
        self.current_point_x = 0.5
        self.current_point_y = 0.5
        self.current_rad = 0

    def paintEvent(self, event):
        super().paintEvent(event)
        self.W = self.width()
        self.H = self.height()
        painter = QPainter()
        painter.begin(self)
        pen = QPen(Qt.red, 1, Qt.SolidLine)
        painter.setPen(pen)
        brush = QBrush()
        brush.setColor(Qt.red)
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawEllipse(QPoint(self.current_point_x*self.W,self.current_point_y*self.H),self.current_rad,self.current_rad)
        painter.end()


class Qmycalibration_panel(QMainWindow):
    OneCalibrationFinish = pyqtSignal(list,list)
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_calibration_panel()
        self.ui.setupUi(self)
        self.point_Show = MyLabel(self.ui.centralwidget)
        self.point_Show.setLineWidth(0)
        self.point_Show.setText("")
        self.point_Show.setAlignment(QtCore.Qt.AlignCenter)
        self.point_Show.setObjectName("point_Show")
        self.ui.horizontalLayout.addWidget(self.point_Show)
        self.point_Show.setStyleSheet("background-color:#808080")
        self.list = [(0.5, 0.5), (0.1, 0.1), (0.9, 0.1), (0.9, 0.9), (0.1, 0.9)]
        self.timer = QTimer()
        self.timer.stop()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.do_timer_timeout)
        self.timer.start()
        self.currentpoint = 0
        self.current_timer = 0
        self.eyetracker = None
        
        
    def calibration_step(self):
        self.calibration = tr.ScreenBasedCalibration(self.eyetracker)
        self.calibration.enter_calibration_mode()

           
         
    def do_timer_timeout(self):
        if self.currentpoint < 5:
            self.point_Show.current_point_x = self.list[self.currentpoint][0]
            self.point_Show.current_point_y = self.list[self.currentpoint][1]
            self.point_Show.current_rad = 40.0 - self.current_timer*4.0
            self.point_Show.update()
            if self.current_timer == 5:
                 self.calibration.collect_data(self.point_Show.current_point_x, self.point_Show.current_point_y)
                 time.sleep(0.5)
            self.current_timer = self.current_timer + 1
            if self.current_timer == 10:
                 self.currentpoint = self.currentpoint + 1
                 self.current_timer = 0
        else:
            self.timer.stop()
            self.calibration_result = self.calibration.compute_and_apply()
            self.calibration.leave_calibration_mode()
            left_gaze_data = []
            right_gaze_data = []
            for calibration_point in self.calibration_result.calibration_points:
                 for calibration_samples in calibration_point._CalibrationPoint__calibration_samples:
                     left_data = calibration_samples._CalibrationSample__left_eye._CalibrationEyeData__position_on_display_area
                     right_data = calibration_samples._CalibrationSample__right_eye._CalibrationEyeData__position_on_display_area
                     left_gaze_data.append(left_data)
                     right_gaze_data.append(right_data)
            self.OneCalibrationFinish.emit(left_gaze_data,right_gaze_data)
            self.close()        
            

        



    def keyReleaseEvent(self,event):
        if event.key() == Qt.Key_Q:
            self.close()
    
    




if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Qmycalibration_panel()
    form.showFullScreen()
    sys.exit(app.exec_())
