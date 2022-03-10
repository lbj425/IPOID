import sys

from PyQt5.QtWidgets import QApplication,QWidget

from PyQt5.QtCore import pyqtSlot,pyqtSignal,Qt

from ui_Introduce_panel import Ui_Introduce_panel

class Qmyintroduce_panel(QWidget):
    go_to_information_panel = pyqtSignal(bool)

    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Introduce_panel()
        self.ui.setupUi(self)
        self.ui.btnEnter.setEnabled(False)      
        self.setWindowFlags(Qt.WindowCloseButtonHint)


    @pyqtSlot(bool)
    def on_checkBox_clicked(self,checked):
        self.ui.btnEnter.setEnabled(checked)



    @pyqtSlot(bool)
    def on_btnEnter_clicked(self):
        self.go_to_information_panel.emit(True)
        self.close()


    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Qmyintroduce_panel()
    form.show()
    sys.exit(app.exec_())
