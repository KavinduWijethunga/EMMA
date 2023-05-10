import sys
import os 
import threading
import socket
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import time
from chat_main_cmd import chat_engin
import numpy as np


#implement main UI

class myclass(QWidget):
    def __init__(self):
        super(myclass,self).__init__()
        loadUi('form.ui',self)
        self.setWindowTitle('medical chatbot')
        self.pushButton.clicked.connect(self.onsendcl)
        #self.sendandrec.keyPressEvent(self, QKeyEvent)
    def onsendcl(self):    
        # soc.send(bytes(self.sendtext.text()+"\n",'utf-8'))


        humen = self.sendtext.text()
        re_bot,report = chat_engin(humen)
        print('GUI chat class - ID - person mentality state report - ', report)
        self.sendandrec.append('\n'+'you: ' + self.sendtext.text( ) + '\n\n' + re_bot)



app = QApplication(sys.argv)
widget = myclass()
widget.show()
sys.exit(app.exec())           
soc.close()