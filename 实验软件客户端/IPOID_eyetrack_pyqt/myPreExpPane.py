import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from PyQt5.QtCore import pyqtSlot, Qt, QTimer, pyqtSignal

from PyQt5.QtGui import QPixmap

from myPreScorePage import QmyScorePage

import PyQt5.QtCore as QtCore

from ui_MainWindow import Ui_MainWindow

from PIL import Image
import numpy as np

import os

import datetime


class QmyPreExpPane(QMainWindow):
    PreExpFinished = pyqtSignal(bool)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.__IfScorePage = False
        self.currentNum = 1
        self.currentImagePart = 0
        self.Testnumber = "测试专用"
        self.timer = QTimer()
        self.timer.stop()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.do_timer_timeout)
        self.IsTestTime = True
        self.IsEnterEnable = False
        self.ScoreList = []
        self.DataDir = './database'
        self.ScoreDirPath = './scores'
        self.scantimeAll = 30
        self.scantimePart = 30
        self.scantimeRest = 2
        self.is_first_direct = True
        self.IsRight = True


    @pyqtSlot(str, str)
    def beginTest(self, num, path):
        self.showFullScreen()
        if self.is_first_direct:
            dlgTitle = "预热试验提示框"
            strInfo = "您将首先进入一段预热实验，其目的在于帮助您更好的熟悉实验的流程。你只需要根据提示进行操作即可"
            QMessageBox.information(self, dlgTitle, strInfo)

            dlgTitle = "预热试验提示框"
            strInfo = "首先您将看到一张完整的图，你需要在一定的时间内观察他的好坏"
            QMessageBox.information(self, dlgTitle, strInfo)

        self.Testnumber = num
        self.datadir = path
        self.DataDir = os.path.join(path, 'PreImg')

        self.get_image_info()
        self.one_image_test_get()
        self.one_image_score()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Return and self.IsEnterEnable == True:
            if self.__IfScorePage == False:
                self.__ScorePage = QmyScorePage(self)
                self.__ScorePage.OneImageFinish.connect(self.OneImageFinish)
                self.__IfScorePage = True
            self.timer.stop()
            self.__ScorePage.show()
            t = datetime.datetime.now().strftime('%H:%M:%S.%f')
            self.curPixmap = QPixmap()
            self.ui.imageShow.setStyleSheet("background-color:#808080")
            self.ui.imageShow.setPixmap(self.curPixmap)
            self.__ScorePage.ui.finishedEdit.setText("%d/%d" % (self.currentNum, self.testNum))
            if self.currentNum == 1 and self.currentImagePart == 0:
                 self.__ScorePage.ui.plainTextEdit.clear()
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("可以看出，刚才显示的照片的质量很不错")
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("因此您可以去拖动左边的滑块，选择一个较高的分数")
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("例如：")
                 self.__ScorePage.ui.lineEdit.setText("85分")
            elif self.currentNum == 2 and self.currentImagePart == 0:
                 self.__ScorePage.ui.plainTextEdit.clear()
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("可以看出，刚才显示的照片的质量一般")
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("因此您可以去拖动左边的滑块，选择一个中等的分数")
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("例如：")
                 self.__ScorePage.ui.lineEdit.setText("50分")
            elif self.currentNum == 3 and self.currentImagePart == 0:
                 self.__ScorePage.ui.plainTextEdit.clear()
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("可以看出，刚才显示的照片的质量很差")
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("因此您可以去拖动左边的滑块，选择一个较低的分数")
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("例如：")
                 self.__ScorePage.ui.lineEdit.setText("15分")
            else:
                 self.__ScorePage.ui.plainTextEdit.clear()
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("你可以根据你的观察给予合适的局部评分")
                 self.__ScorePage.ui.lineEdit.setText("")        
            if self.currentImagePart == 0:
                self.__ScorePage.ui.currentPartEdit.setText("整体")
            else:
                self.__ScorePage.ui.currentPartEdit.setText("局部%d" % self.currentImagePart)
        if event.key() == Qt.Key_Q:
            self.timer.stop()
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
        self.labelList = os.listdir(self.label_dir)
        if len(self.imageList) != len(self.labelList):
             dlgTitle ="信息框"
             strInfo ="标签和图片数目不匹配"
             QMessageBox.information(self,dlgTitle,strInfo)
             self.close()
             self.IsRight = False
             return
        self.testNum = len(self.imageList)

    def one_image_test_get(self):
        if self.IsRight:
            self.imagePath = os.path.join(self.image_dir, self.imageList[self.currentNum - 1])
            self.labelPath = os.path.join(self.label_dir, self.labelList[self.currentNum - 1])
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
                [x1, y1] = np.where(label == i + 1)
                [x2, y2] = np.where(label != i + 1)
                image_part[x1, y1, :] = image[x1, y1, :]
                image_part[x2, y2, :] = image[x2, y2, :] * 0.15
                img_pil = Image.fromarray(np.uint8(image_part)).convert('RGB')
                img_pix = img_pil.toqpixmap()
                self.CurrentImageList.append(img_pix)

    def one_image_score(self):
        if self.IsRight:
            self.ui.imageShow.setStyleSheet("background-color:#808080")
            self.curPixmap = self.CurrentImageList[self.currentImagePart]
            self.ui.imageShow.setPixmap(self.curPixmap)
            self.IsEnterEnable = False
            if self.currentImagePart == 0:
                self.restime = self.scantimeAll
            else:
                self.restime = self.scantimePart
            self.timer.start()

    def do_timer_timeout(self):
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

            self.__ScorePage.show()
            
            self.curPixmap = QPixmap()
            self.ui.imageShow.setStyleSheet("background-color:#808080")
            self.ui.imageShow.setPixmap(self.curPixmap)
            self.__ScorePage.ui.finishedEdit.setText("%d/%d" % (self.currentNum, self.testNum))
            if self.currentNum == 1 and self.currentImagePart == 0:
                 self.__ScorePage.ui.plainTextEdit.clear()
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("可以看出，刚才显示的照片的质量很不错")
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("因此您可以去拖动左边的滑块，选择一个较高的分数")
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("例如：")
                 self.__ScorePage.ui.lineEdit.setText("85分")
            elif self.currentNum == 2 and self.currentImagePart == 0:
                 self.__ScorePage.ui.plainTextEdit.clear()
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("可以看出，刚才显示的照片的质量一般")
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("因此您可以去拖动左边的滑块，选择一个中等的分数")
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("例如：")
                 self.__ScorePage.ui.lineEdit.setText("50分")
            elif self.currentNum == 3 and self.currentImagePart == 0:
                 self.__ScorePage.ui.plainTextEdit.clear()
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("可以看出，刚才显示的照片的质量很差")
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("因此您可以去拖动左边的滑块，选择一个较低的分数")
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("例如：")
                 self.__ScorePage.ui.lineEdit.setText("15分")
            else:
                 self.__ScorePage.ui.plainTextEdit.clear()
                 self.__ScorePage.ui.plainTextEdit.appendPlainText("你可以根据你的观察给予合适的局部评分")
                 self.__ScorePage.ui.lineEdit.setText("")   
            if self.currentImagePart == 0:
                self.__ScorePage.ui.currentPartEdit.setText("整体")
            else:
                self.__ScorePage.ui.currentPartEdit.setText("局部%d" % self.currentImagePart)

            if self.is_first_direct:
                dlgTitle = "预热试验提示框"
                strInfo = "相信您对这张图片已经有了一定的了解，那么请滑动左侧的滑块，给出您心目中他的分数"
                QMessageBox.information(self, dlgTitle, strInfo)
            self.is_first_direct = False

    @pyqtSlot(int)
    def OneImageFinish(self, Score):

        self.ScoreList.append(self.imageList[self.currentNum - 1] + ' ' + str(self.currentImagePart) + ' %d' % Score)
        if self.currentImagePart == self.PartNum:
            self.currentImagePart = 0
            if self.currentNum == self.testNum:
                dlgTitle = "预实验结束信息框"
                strInfo = "预实验测试已经结束，下面即将开始正式实验"
                QMessageBox.information(self, dlgTitle, strInfo)
                self.PreExpFinished.emit(True)
                self.close()
            else:
                self.currentNum = self.currentNum + 1
                self.one_image_test_get()
                self.one_image_score()
        else:
            self.currentImagePart = self.currentImagePart + 1
            self.one_image_score()




if __name__=='__main__':
    app = QApplication(sys.argv)
    form = QmyPreExpPane()
    form.show()
    form.beginTest('123', './database')


    sys.exit(app.exec_())

