# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 18:10:19 2021

@author: Caboosicle
"""

import time
import threading 
import sys

import PyQt5

from PyQt5.QtWidgets import QMessageBox,QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout

class popUpGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 600
        
        
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Timing/Interupt Button v0')
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.window=QWidget()
      
        self.overallLayout = QVBoxLayout(self)
        self.window.setLayout(self.overallLayout)
        self.setCentralWidget(self.window)
        
        self.takeMeas = QPushButton("Take a Measurement Now", clicked=self.beginWait)
        
        self.overallLayout.addWidget(self.takeMeas)
        
    def beginWait(self):
        self.popupMessage()
        
        
        
    def takeMeasurement(self):
        print("Test")
 
    
    def popupMessage(self):
        
        takeMeasNow = QMessageBox.warning(self,("Press OK to Continue"),("Please wait 5 minutes for next measurement or press 'OK' to take the measurement now."))
        takeMeasNow.buttonClicked(self.takeMeasurement)
        
        

if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = popUpGUI()
    ex.show()
    sys.exit(app.exec_())  