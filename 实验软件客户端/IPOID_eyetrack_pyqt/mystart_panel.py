from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QLabel,QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import pyqtSlot,Qt,QTimer,QPoint,pyqtSignal,QRect

from PyQt5.QtGui import QPainter,QPen,QPixmap,QBrush,QPalette


import sys
import math
import os

from start_panel import Ui_start_panel
from mycalibration_panel import Qmycalibration_panel
from mycalibration_result import QmyCalibration_Result
from myfrequency_setting import QmyFrequency_setting
from myMainWindow import QmyMainWindow
from myPreExpPane import QmyPreExpPane

import tobii_research as tr

global_user_position_guide = []
def user_position_guide_callback(gaze_data):
     global global_user_position_guide
     global_user_position_guide = gaze_data

class MyLabel(QLabel):
    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)
        self.current_point_x = [0.5,0.5,0.5]
        self.current_point_y = [0.5,0.5,0.5]
        self.current_rad = 10
        self.IsPainter = False

    def paintEvent(self, event):
         super().paintEvent(event)
         if self.IsPainter == True:
             self.W = self.width()
             self.H = self.height()*0.8
             painter = QPainter()
             painter.begin(self)
             pen = QPen(Qt.white, 1, Qt.SolidLine)
             painter.setPen(pen)
             brush = QBrush()
             brush.setColor(Qt.white)
             brush.setStyle(Qt.SolidPattern)
             painter.setBrush(brush)
             rect1 = QRect(0,0.9*self.height(),self.width(),0.1*self.height())
             rect2 = QRect(0,0,self.width(),0.9*self.height())
             painter.fillRect(rect2,Qt.black)
             eye_find = 0
             if math.isnan(self.current_point_x[0]) or math.isnan(self.current_point_x[1]):
                 painter.fillRect(rect1,Qt.red)
             else:
                 relative_x = 1-self.current_point_x[0]
                 relative_y = self.current_point_x[1]
                 if relative_x<=1 and relative_y<=1:
                     painter.drawEllipse(QPoint(relative_x*self.W,relative_y*self.H),self.current_rad,self.current_rad)
                     eye_find = eye_find + 1
                 else:
                     painter.fillRect(rect1,Qt.red)
             if math.isnan(self.current_point_y[0]) or math.isnan(self.current_point_y[1]):
                 painter.fillRect(rect1,Qt.red)
             else:
                 relative_x = 1-self.current_point_y[0]
                 relative_y = self.current_point_y[1]
                 if relative_x<=1 and relative_y<=1:
                     painter.drawEllipse(QPoint(relative_x*self.W,relative_y*self.H),self.current_rad,self.current_rad)
                     eye_find = eye_find +1 
                 else:
                     painter.fillRect(rect1,Qt.red)
             if eye_find == 2:
                 painter.fillRect(rect1,Qt.green)
             painter.end()

class Qmystart_panel(QMainWindow):
    beginTest = pyqtSignal(str,str)
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_start_panel()
        self.ui.setupUi(self)
        self.eye_show = MyLabel(self.ui.frame_2)
        self.eye_show.setGeometry(QtCore.QRect(20, 50, 330, 270))
        self.eye_show.setMinimumSize(QtCore.QSize(330, 270))
        self.eye_show.setMaximumSize(QtCore.QSize(330, 270))
        self.eye_show.setFrameShape(QtWidgets.QFrame.Box)
        self.eye_show.setText("")
        self.eye_show.setObjectName("eye_show")
        self.__isCalibration = False
        self.desktop_width = 0
        self.desktop_height = 0
        self.IsPainter = False
        self.__isFrequency_setting = False
        self.ui.btn_Calibration.setEnabled(False)
        self.eyetracker_frequency = 60
        self.save_data_dir = 'AllData/测试专用'
        self.DataDir = ''
        self.ui.btnStart.setEnabled(False)
        self.ui.btnPreStart.setEnabled(False)
        self.eyetracker = None
        self.__isExpStart = None
    
    @pyqtSlot()   
    def on_btn_EyetrackStart_pressed(self):
         self.eyetrackers = tr.find_all_eyetrackers()
         if not self.eyetrackers :
             self.ui.eye_tracker_info.clear()
             self.ui.eye_tracker_info.appendPlainText('This is no eyetracker detected, please check your connection or click it again!')
         else:
             self.eyetracker = self.eyetrackers[0]
             self.eyetracker.set_gaze_output_frequency(self.eyetracker_frequency)
             self.ui.eye_tracker_info.clear()
             self.ui.eye_tracker_info.appendPlainText("Address: " + self.eyetracker.address)
             self.ui.eye_tracker_info.appendPlainText("Model: " + self.eyetracker.model)
             self.ui.eye_tracker_info.appendPlainText("Name (It's OK if this is empty): " + self.eyetracker.device_name)
             self.ui.eye_tracker_info.appendPlainText("Serial number: " + self.eyetracker.serial_number)
             self.ui.eye_tracker_info.appendPlainText("Gaze output frequency: " + str(self.eyetracker.get_gaze_output_frequency()))
             self.eyetracker.subscribe_to(tr.EYETRACKER_USER_POSITION_GUIDE, user_position_guide_callback, as_dictionary=True)
             self.track_box = self.eyetracker.get_track_box()
             self.z5 = self.track_box.back_upper_right[2]
             self.z1 = self.track_box.front_upper_right[2]
             self.eye_show.IsPainter = True
             self.timer = QTimer()
             self.timer.stop()
             self.timer.setInterval(20)
             self.timer.timeout.connect(self.do_timer_timeout)
             self.timer.start()
             self.ui.btn_Calibration.setEnabled(True)  
    @pyqtSlot()
    def on_btn_Calibration_pressed(self):
        dlgTitle = "信息框"
        strInfo = "是否进入校准页面"
        defaultBtn = QMessageBox.NoButton
        result = QMessageBox.question(self, dlgTitle, strInfo,QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel,defaultBtn)
        if (result==QMessageBox.Yes):
            if self.__isCalibration == False:
                self.__Calibration_panel = Qmycalibration_panel(self)
                self.__Calibration_panel.OneCalibrationFinish.connect(self.OneCalibrationFinish)
                self.__isCalibration = True
            self.__Calibration_panel.eyetracker = self.eyetracker
            #self.eyetracker.unsubscribe_from(tr.EYETRACKER_USER_POSITION_GUIDE, user_position_guide_callback)
            self.timer.stop()
            self.__Calibration_panel.currentpoint = 0
            self.__Calibration_panel.point_Show.current_point_x = 0.5
            self.__Calibration_panel.point_Show.current_point_y = 0.5
            self.__Calibration_panel.point_Show.current_rad = 0
            self.__Calibration_panel.timer.start()
            self.__Calibration_panel.showFullScreen()
            self.__Calibration_panel.calibration_step()
    
    @pyqtSlot(list,list)
    def OneCalibrationFinish(self,left_gaze_data,right_gaze_data):
        self.result = QmyCalibration_Result()
        self.result.left_result.eye_gaze_data = left_gaze_data
        self.result.right_result.eye_gaze_data = right_gaze_data
        self.result.show()
    
    def do_timer_timeout(self):
        if global_user_position_guide:
             left_data = global_user_position_guide['left_user_position']
             right_data = global_user_position_guide['right_user_position']
             self.eye_show.current_point_x= left_data
             self.eye_show.current_point_y = right_data    
             self.eye_show.update()
             left_z = 0
             right_z = 0
             if not math.isnan(left_data[2]):
                 left_z = left_data[2]*(self.z5-self.z1)+self.z1
             if not math.isnan(right_data[2]):
                 right_z = right_data[2]*(self.z5-self.z1)+self.z1
             distance = int(0.5*(left_z + right_z)/10)
             plet = self.ui.distance_text.palette()
             if distance < 45:
                 self.ui.distance_show.setValue(45)
                 self.ui.distance_text.setText(str(45))
             elif distance > 75:
                 self.ui.distance_show.setValue(75)
                 self.ui.distance_text.setText(str(75))
             else:
                 self.ui.distance_show.setValue(distance)
                 self.ui.distance_text.setText(str(distance))
                 
                 
    @pyqtSlot()
    def on_action_frequency_triggered(self):
         if (self.__isFrequency_setting == False):
             self.__Frequency_setting = QmyFrequency_setting(self)
             self.__isFrequency_setting == True
             self.__Frequency_setting.Frequency_changed.connect(self.do_change_frequency)
         self.__Frequency_setting.show()
    @pyqtSlot(int) 
    def do_change_frequency(self,f):
         self.eyetracker_frequency = f
    
    @pyqtSlot()
    def on_btnDirget_pressed(self):
        dirStr = QFileDialog.getExistingDirectory()
        if (dirStr == ""):
            return
        self.ui.lineEdit.setText(dirStr)

    @pyqtSlot()
    def on_btnApply_pressed(self):
        self.DataDir = self.ui.lineEdit.text()
        isExists=os.path.exists(self.DataDir)
        if not isExists:
             dlgTitle ="信息框"
             strInfo ="路径错误"
             QMessageBox.information(self,dlgTitle,strInfo)
             return             
        self.ui.btnStart.setEnabled(False)
        self.ui.btnPreStart.setEnabled(True)


    @pyqtSlot(str)
    def beginSetting(self,data_dir):
        self.save_data_dir = data_dir 
        self.show()

    @pyqtSlot()
    def on_btnStart_pressed(self):
        if self.DataDir =='':
            dlgTitle ="信息框"
            strInfo ="未填写数据库地址或未点击应用"
            QMessageBox.information(self,dlgTitle,strInfo)
            return
        if self.eyetracker == None:
            dlgTitle ="信息框"
            strInfo ="未启动眼动仪"
            QMessageBox.information(self,dlgTitle,strInfo)
            return
        if self.__isExpStart == None:
             self.__MainWindow = QmyMainWindow(self)
             self.__MainWindow.ExpFinished.connect(self.ExpFinished)
             self.__MainWindow.ExpError.connect(self.ExpError)
             self.__MainWindow.eyetracker = self.eyetracker
             self.__isExpStart = True
             self.__MainWindow.beginTest(self.save_data_dir,self.DataDir,self.eyetracker_frequency)
        else:
             self.__MainWindow.IsRight = True
             self.__MainWindow.showFullScreen()
             self.__MainWindow.one_image_score()
    
    @pyqtSlot()
    def on_btnPreStart_pressed(self):
        if self.DataDir == '':
            dlgTitle ="信息框"
            strInfo ="未填写数据库地址或未点击应用"
            QMessageBox.information(self,dlgTitle,strInfo)
            return
        self.__PreExpPane = QmyPreExpPane(self)
        self.__PreExpPane.PreExpFinished.connect(self.PreExpFinished)
        self.__PreExpPane.IsRight = True
        self.__PreExpPane.beginTest(self.save_data_dir,self.DataDir)
    @pyqtSlot(bool)
    def PreExpFinished(self):
        self.ui.btnStart.setEnabled(True)
        self.ui.btnPreStart.setEnabled(False) 
    @pyqtSlot(bool)
    def ExpFinished(self):
        self.close()
    
    @pyqtSlot(bool)
    def ExpError(self):
        self.timer.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Qmystart_panel()
    form.show()
    sys.exit(app.exec_())




