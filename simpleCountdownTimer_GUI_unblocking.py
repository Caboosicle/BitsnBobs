import traceback
import time
import sys

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class simpleCountdownTimer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.left = 100
        self.top = 100
        self.width = 300
        self.height = 300
        
        self.initUI()

    def setInitValues(self):
        print('init')
        time_minutes=float(self.timerEntryValue.text())
        time_seconds= time_minutes *60
        intTimeSeconds= int(time_seconds)
        mins=intTimeSeconds//60
        secs=intTimeSeconds%60
        self.minuteValue.setText(str(mins))
        self.secondValue.setText(str(secs))
        self.countDown()



    def intermed(self):
        reply = QMessageBox.question(self, 'Time Elapsed', 'The time has elapsed, please insert a new DUT and press "OK" to continue measurements', QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
        if reply == QMessageBox.Ok:
            self.setInitValues()
                
        else:
                
            print("Exiting")
        

    def display(self):

        currentMinutesRemaining = int(self.minuteValue.text())
        currentSecondsRemaining = int(self.secondValue.text())
  
        intTimeSeconds = (currentMinutesRemaining *60)+ int(currentSecondsRemaining)

        timeformat = '{:02d}:{:02d}'.format(currentMinutesRemaining,currentSecondsRemaining)
        #print(timeformat)

        intTimeSeconds -=1

        mins=intTimeSeconds//60
        secs=intTimeSeconds%60
        
        self.minuteValue.setText(str(mins))
        self.secondValue.setText(str(secs))

        if intTimeSeconds==0:
            self.timer.stop()
            self.intermed()

        

    def countDown(self):
            self.timer = QTimer()
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.display)
            self.timer.start()


    def initUI(self):

        
        self.setWindowTitle('Simple Countdown Timer')
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.window=QWidget()

        
        self.overallLayout = QVBoxLayout(self)
        self.window.setLayout(self.overallLayout)
        self.setCentralWidget(self.window)

        self.inputLayout = QHBoxLayout(self)
        self.inputLayout.addStretch()
        self.overallLayout.addLayout(self.inputLayout)
        
        self.outputLayout = QHBoxLayout(self)
        self.outputLayout.addStretch()
        self.overallLayout.addLayout(self.outputLayout)
        
        self.summaryLayout = QHBoxLayout(self)
        self.summaryLayout.addStretch()
        self.overallLayout.addLayout(self.summaryLayout)
        


        self.timeEntryLabel = QLabel('Enter the desired time in minutes',self)
        self.timerEntryValue=QLineEdit(self)

        self.timeOutLabel = QLabel('Countdown Timer Output',self)
        self.minuteValue=QLineEdit(self)
        self.secondValue=QLineEdit(self)

        self.startTimer = QPushButton("Start Timer!", clicked=self.setInitValues)


        self.inputLayout.addWidget(self.timeEntryLabel)
        self.inputLayout.addWidget(self.timerEntryValue)

        self.outputLayout.addWidget(self.timeOutLabel)
        self.outputLayout.addWidget(self.minuteValue)
        self.outputLayout.addWidget(self.secondValue)
        self.summaryLayout.addWidget(self.startTimer)
        

if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = simpleCountdownTimer()
    ex.show()
    sys.exit(app.exec_())    
        
