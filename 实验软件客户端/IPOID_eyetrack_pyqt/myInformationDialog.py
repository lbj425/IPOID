import sys

import os

from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox,QFileDialog

from PyQt5.QtCore import pyqtSlot,pyqtSignal

from ui_InformationDialog import Ui_InformationDialog

class QmyInformationDialog(QDialog):
    beginTest = pyqtSignal(str)
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_InformationDialog()
        self.ui.setupUi(self)
        self.list = []
        self.inforpath ='./AllData'

    def on_btnYes_pressed(self):
        if (self.ui.nameEdit.text() == ""):
            dlgTitle ="信息框"
            strInfo ="未填写姓名"
            QMessageBox.information(self,dlgTitle,strInfo)
            return
        if (self.ui.ageEdit.text() == ""):
            dlgTitle ="信息框"
            strInfo ="未填写年龄"
            QMessageBox.information(self,dlgTitle,strInfo)
            return
        if (self.ui.numberEdit.text() == ""):
            dlgTitle ="信息框"
            strInfo ="未填写编号"
            QMessageBox.information(self,dlgTitle,strInfo)
            return
        if (self.ui.majorEdit.text() == ""):
            dlgTitle ="信息框"
            strInfo ="未填写专业"
            QMessageBox.information(self,dlgTitle,strInfo)
            return
        dlgTitle ="信息框"
        strInfo ="信息填写已完成，是否确认"
        result = QMessageBox.question(self,dlgTitle,strInfo,QMessageBox.Yes|
                                      QMessageBox.Cancel)
        if (result == QMessageBox.Yes):
            self.list = []
            self.list.append(str(self.ui.nameEdit.text()))
            self.list.append(str(self.ui.ageEdit.text()))
            self.list.append(str(self.ui.numberEdit.text()))
            self.list.append(str(self.ui.majorEdit.text()))
            if (self.ui.manButton.isChecked()):
                self.list.append("男")
            else:
                self.list.append("女")
             
            data_path = self.inforpath+'/'+self.ui.numberEdit.text()
            isExists=os.path.exists(data_path)
            if not isExists:
                 os.makedirs(data_path)
                 f = open('%s/information.txt'%(data_path),mode='w')
                 sep = ","
                 f.write(sep.join(self.list))
                 f.close()
                 self.beginTest.emit(data_path)
                 self.close()
            else:
                 dlgTitle ="信息框"
                 strInfo ="该编号已经存在，是否覆盖"
                 result_new = QMessageBox.question(self,dlgTitle,strInfo,QMessageBox.Yes|QMessageBox.Cancel)
                 if (result_new == QMessageBox.Yes):     
                     f = open('%s/information.txt'%(data_path),mode='w')
                     f.truncate(0)
                     sep = ","
                     f.write(sep.join(self.list))
                     f.close()
                     self.beginTest.emit(data_path)
                     self.close()
                 else:
                     dlgTitle ="信息框"
                     strInfo ="你可以重新填写信息"
                     QMessageBox.information(self,dlgTitle,strInfo)
                     return            
        if (result == QMessageBox.Cancel):
            dlgTitle ="信息框"
            strInfo ="你可以重新填写信息"
            QMessageBox.information(self,dlgTitle,strInfo)
            return

    @pyqtSlot(bool)
    def beginInformation(self,begin):
        self.show()

    
    def on_btnSetInfoPath_pressed(self):
        dirStr = QFileDialog.getExistingDirectory()
        if (dirStr == ""):
            return
        self.ui.InfoPathEdit.setText(dirStr)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyInformationDialog()
    form.show()
    sys.exit(app.exec_())
