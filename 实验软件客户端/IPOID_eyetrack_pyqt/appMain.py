##  GUI应用程序主程序入口

import sys

from PyQt5.QtWidgets import  QApplication

from myintroduce_panel import Qmyintroduce_panel

from myInformationDialog import QmyInformationDialog

#from myMainWindow import QmyMainWindow

from mystart_panel import Qmystart_panel

    
app = QApplication(sys.argv)    #创建GUI应用程序

introduce_panel = Qmyintroduce_panel()


Start_panel = Qmystart_panel()

Dialog = QmyInformationDialog()

#PreExp = QmyPreExpPane()

#MainWindow = QmyMainWindow()


introduce_panel.go_to_information_panel.connect(Dialog.beginInformation)
Dialog.beginTest.connect(Start_panel.beginSetting)


introduce_panel.show()

sys.exit(app.exec_()) 
