import sys

from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QFileDialog

from PyQt5.QtCore import pyqtSlot,pyqtSignal

from frequency_setting import Ui_frequency_setting

class QmyFrequency_setting(QMainWindow):
     Frequency_changed = pyqtSignal(int)
     def __init__(self,parent=None):
         super().__init__(parent)
         self.ui = Ui_frequency_setting()
         self.ui.setupUi(self)
     
     @pyqtSlot()
     def on_btnClear_pressed(self):
         dlgTitle = "信息框"
         strInfo = "是否确定使用该频率"
         defaultBtn = QMessageBox.NoButton
         result = QMessageBox.question(self, dlgTitle, strInfo,QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel,defaultBtn)
         if (result==QMessageBox.Yes):
             if (self.ui.radio_60HZ.isChecked()):
                 chosed_HZ = 60
             elif (self.ui.radio_120HZ.isChecked()):
                 chosed_HZ = 120
             elif (self.ui.radio_250HZ.isChecked()):
                 chosed_HZ = 250
             elif (self.ui.radio_300HZ.isChecked()):
                 chosed_HZ = 300
             self.Frequency_changed.emit(chosed_HZ)
             
         
         
         
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QmyFrequency_setting()
    form.show()
    sys.exit(app.exec_())

