import sys

from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox

from PyQt5.QtCore import pyqtSlot,Qt,QTimer,pyqtSignal

from PyQt5.QtGui import QPixmap

from myScorePage import QmyScorePage

import PyQt5.QtCore as QtCore

from ui_MainWindow import Ui_MainWindow
import tobii_research as tr
from random import shuffle,sample
from PIL import Image
import numpy as np

import os

import datetime

global_gaze_data = []
global_error_count = 0
current_gaze_data = []
def gaze_data_callback(gaze_data):
     global global_gaze_data
     global current_gaze_data
     current_gaze_data = gaze_data
     global_gaze_data.append(gaze_data)


class QmyMainWindow(QMainWindow):
    ExpFinished = pyqtSignal(bool)
    ExpError = pyqtSignal(bool)
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.__IfScorePage = False
        self.currentNum = 1
        self.currentImagePart =0
        self.Testnumber = "测试专用"
        self.timer = QTimer()
        self.timer.stop()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.do_timer_timeout)
        self.IsTestTime =True
        self.IsEnterEnable = False
        self.ScoreList = []
        self.EyeTrackTime = []
        self.DataDir = './database'
        self.save_data_dir = 'AllData/测试专用'
        self.scantimeAll = 30
        self.scantimePart = 30
        self.scantimeRest = 2
        self.eyetracker = None
        self.IsRight = True
        


    @pyqtSlot(str,str,int)
    def beginTest(self,save_data_dir,path,frequency):
        self.save_data_dir = save_data_dir
        self.DataDir = path
        self.eyetracker_frequency = frequency
        self.error_detect_timer = QTimer()
        self.error_detect_timer.stop()
        self.error_detect_timer.timeout.connect(self.do_error_detection)
        self.error_detect_timer.setInterval(1000/self.eyetracker_frequency)
        self.showFullScreen()
        self.get_image_info()
        self.one_image_test_get()
        self.one_image_score()
        #创建一个分数文件夹记录分数
        group_name = path.split('/')
        group_name = group_name[-1]
        self.save_name = 'scores_' + group_name
      #  f = open('%s/%s.txt'%(self.ScoreDirPath,self.Testnumber),mode='w')
        f = open('%s/%s.txt'%(self.save_data_dir,self.save_name),mode='w')
        f.truncate(0)
        f.close()


    def keyReleaseEvent(self,event):
        global global_gaze_data
        if event.key() == Qt.Key_Return and self.IsEnterEnable ==True:
            if self.__IfScorePage == False:
                self.__ScorePage = QmyScorePage(self)
                self.__ScorePage.OneImageFinish.connect(self.OneImageFinish)
                self.__IfScorePage = True
            self.eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
            self.timer.stop()
            self.error_detect_timer.stop()
           # fid = open('%s/%s.txt'%(self.save_data_dir,self.imageList[self.currentNum-1].split('.')[0]),mode='a')
            fid = open(self.current_eye_save_name,mode='a')
            fid.write('当前评价区域'+str(self.currentImagePart)+'\n')
            for gaze_data_sample in global_gaze_data:
                 for gaze_dataf in gaze_data_sample:
                     data= gaze_data_sample[gaze_dataf]
                     fid.write(str(data)+' ')
                 fid.write('\n')
            fid.close()
            global_gaze_data = []
            self.__ScorePage.show()
            t = datetime.datetime.now().strftime('%H:%M:%S.%f')
            self.EyeTrackTime.append(t)  
                        
            self.curPixmap = QPixmap()
            self.ui.imageShow.setStyleSheet("background-color:#808080")
            self.ui.imageShow.setPixmap(self.curPixmap)
            self.__ScorePage.ui.finishedEdit.setText("%d/%d"%(self.currentNum,self.testNum))
            if self.currentImagePart ==0:
                self.__ScorePage.ui.currentPartEdit.setText("整体")
            else:
                self.__ScorePage.ui.currentPartEdit.setText("局部%d" % self.currentImagePart)
        if event.key() == Qt.Key_Q:
            self.timer.stop()
            self.error_detect_timer.stop()
            self.eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
            global_gaze_data = []
            del(self.EyeTrackTime[-1])
            self.close()
            

    def get_image_info(self):
        self.image_dir = os.path.join(self.DataDir, 'images')
        self.label_dir = os.path.join(self.DataDir, 'labels')
        isExists=os.path.exists(self.image_dir)
        if not isExists:
             dlgTitle ="信息框"
             strInfo ="路径下未找到图片文件"
             QMessageBox.information(self,dlgTitle,strInfo)
             self.close()
             self.IsRight = False
             return
        isExists=os.path.exists(self.label_dir)
        if not isExists:
             dlgTitle ="信息框"
             strInfo ="路径下未找到标签文件"
             QMessageBox.information(self,dlgTitle,strInfo)
             self.close()
             self.IsRight = False
             return
        self.imageList = os.listdir(self.image_dir)
        currentNum = len(self.imageList)
        resultList=sample(range(0,currentNum),3)
        for i in range(3):
             self.imageList.append(self.imageList[resultList[i]])
        shuffle(self.imageList)
        self.labelList = os.listdir(self.label_dir)
        self.testNum = len(self.imageList)


    def one_image_test_get(self):
        if self.IsRight:
            self.imagePath = os.path.join(self.image_dir,self.imageList[self.currentNum-1])
         #  self.labelPath = os.path.join(self.label_dir,self.labelList[self.currentNum-1])
            image_name = self.imageList[self.currentNum-1]
            image_name = image_name[3:5]
            label_name = 'Label'+image_name+'.bmp'
            self.labelPath = os.path.join(self.label_dir,label_name)
            if not os.path.isfile(self.labelPath):
                 dlgTitle ="结束信息框"
                 strInfo ="路径错误："+self.labelPath
                 QMessageBox.information(self,dlgTitle,strInfo)
                 self.IsRight = False
                 self.close()
                 return
            image = Image.open(self.imagePath)
            label = Image.open(self.labelPath)
            image = np.array(image)
            label = np.array(label)
            image_x = np.size(image, 0)
            image_y = np.size(image, 1)
            label_x = np.size(label, 0)
            label_y = np.size(label, 1)
            label_flatten = label.flatten()
            label_flatten = label_flatten.tolist()
            label_flatten = set(label_flatten)
            part_num = len(label_flatten)
            self.PartNum = part_num
            self.CurrentImageList = []
            img_pil = Image.fromarray(image)
            img_pix = img_pil.toqpixmap()
            self.CurrentImageList.append(img_pix)
            for i in range(part_num):
                image_part = np.zeros((image_x, image_y, 3))
                [x1,y1] = np.where(label==i+1)
                [x2,y2] = np.where(label!=i+1)
                image_part[x1, y1, :] = image[x1, y1, :]
                image_part[x2, y2, :] = image[x2, y2, :] * 0.15
                img_pil = Image.fromarray(np.uint8(image_part)).convert('RGB')
                img_pix = img_pil.toqpixmap()
                self.CurrentImageList.append(img_pix)
            self.current_eye_save_name = self.save_data_dir +'/'+ self.imageList[self.currentNum-1].split('.')[0] + '.txt'
          #  print(self.current_eye_save_name)
            isExists=os.path.exists(self.current_eye_save_name)
            if isExists:
                 self.current_eye_save_name = self.current_eye_save_name = self.save_data_dir +'/Re_'+ self.imageList[self.currentNum-1].split('.')[0] + '.txt'
            fid = open(self.current_eye_save_name,mode='w')
            fid.truncate(0)
            fid.close()

    def one_image_score(self):
        global global_error_count
        global global_gaze_data
        if self.IsRight:
            self.ui.imageShow.setStyleSheet("background-color:#808080")
            self.curPixmap = self.CurrentImageList[self.currentImagePart]
            self.ui.imageShow.setPixmap(self.curPixmap)
            global_error_count = 0
            try:
                 self.eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
            except:
                 #print('ERROR!')
                 self.eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
                 global_gaze_data = []
                 self.eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
            self.error_detect_timer.start()
            ti = datetime.datetime.now().strftime('%H:%M:%S.%f')
            self.EyeTrackTime.append(ti)
            self.IsEnterEnable = False
            if self.currentImagePart == 0:
                self.restime = self.scantimeAll
            else:
                self.restime = self.scantimePart
            self.timer.start()
    
    def do_error_detection(self):
         global global_gaze_data
         global global_error_count
         global current_gaze_data
         if current_gaze_data == []:
             return
         if np.isnan(current_gaze_data['left_gaze_point_on_display_area'][0]) and np.isnan(current_gaze_data['right_gaze_point_on_display_area'][0]):
             global_error_count = global_error_count + 1
         else:
             global_error_count = 0
         if global_error_count == int(self.eyetracker_frequency*0.75):
             self.error_detect_timer.stop()
             self.timer.stop()
             self.eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
             global_gaze_data = []
             del(self.EyeTrackTime[-1])
             global_error_count = 0
             dlgTitle ="信息框"
             strInfo ="眼动仪捕捉眼动信息失败，请调整坐姿"
             QMessageBox.information(self,dlgTitle,strInfo)
             self.close()
             self.ExpError.emit(True)
        
    def do_timer_timeout(self):
        global global_gaze_data
        self.restime = self.restime - 1
        if self.currentImagePart == 0:
            if self.restime <= self.scantimeAll - self.scantimeRest:
                self.IsEnterEnable = True
            else:
                self.IsEnterEnable = False
        else:
            if self.restime <= self.scantimePart - self.scantimeRest:
                self.IsEnterEnable = True
            else:
                self.IsEnterEnable = False

        if self.restime == 0:
            if self.__IfScorePage == False:
                self.__ScorePage = QmyScorePage(self)
                self.__ScorePage.OneImageFinish.connect(self.OneImageFinish)
                self.__IfScorePage = True
            self.timer.stop()
            self.error_detect_timer.stop()
            self.eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
            self.__ScorePage.show()
            t = datetime.datetime.now().strftime('%H:%M:%S.%f')
            self.EyeTrackTime.append(t)
           # fid = open('%s/%s.txt'%(self.save_data_dir,self.imageList[self.currentNum-1].split('.')[0]),mode='a')
            fid = open(self.current_eye_save_name,mode='a')
            fid.write('当前评价区域'+str(self.currentImagePart)+'\n')
            for gaze_data_sample in global_gaze_data:
                 for gaze_dataf in gaze_data_sample:
                     data= gaze_data_sample[gaze_dataf]
                     fid.write(str(data)+' ')
                 fid.write('\n')
            fid.close()
            global_gaze_data = []
            self.curPixmap = QPixmap()
            self.ui.imageShow.setStyleSheet("background-color:#808080")
            self.ui.imageShow.setPixmap(self.curPixmap)
            self.__ScorePage.ui.finishedEdit.setText("%d/%d"%(self.currentNum,self.testNum))
            if self.currentImagePart ==0:
                self.__ScorePage.ui.currentPartEdit.setText("整体")
            else:
                self.__ScorePage.ui.currentPartEdit.setText("局部%d"%self.currentImagePart)

    @pyqtSlot(int)
    def OneImageFinish(self,Score):  
        #self.ScoreList.append(self.imageList[self.currentNum-1]+' '+str(self.currentImagePart)+' %d'%Score)
        f = open('%s/%s.txt'%(self.save_data_dir,self.save_name),mode='a')
        f.write(self.imageList[self.currentNum-1]+'_'+str(self.currentImagePart)+' %d'%Score+'\n')
        f.close()
        if self.currentImagePart == self.PartNum:
            self.currentImagePart = 0
            if self.currentNum == self.testNum:
                dlgTitle ="结束信息框"
                strInfo ="本次测试已经结束，感谢您的参与"
                QMessageBox.information(self,dlgTitle,strInfo)
               # f = open('%s/scores.txt'%(self.save_data_dir),mode='w')
               # f.truncate(0)
               # for list_score in self.ScoreList:
               #     f.write(list_score+'\n')
               # f.close()
                m = open('%s/eyetracker_time.txt'%(self.save_data_dir),mode='w')
                m.truncate(0)
                for t in self.EyeTrackTime:
                    m.write(str(t)+'\n')
                m.close()
                self.ExpFinished.emit(True)                
                self.close()
            else:
                self.currentNum = self.currentNum + 1
                self.one_image_test_get()
                self.one_image_score()
        else:
            self.currentImagePart= self.currentImagePart + 1
            self.one_image_score()

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.show()
    eyetracker_address = "tet-tcp://169.254.78.123"
    form.eyetracker = tr.EyeTracker(eyetracker_address)
    form.beginTest('AllData/测试专用', './database',60)
    sys.exit(app.exec_())
