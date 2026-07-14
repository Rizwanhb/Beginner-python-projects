#stop watch for clock programe 

import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QTime, Qt 

#creating a stopwatch class and assigning it as widget because it is a widget 
class StopWatch(QWidget):
    #defining init
    def __init__(self):
        #function will inherit from parent class 
        super().__init__()
        #Add button (start, stop, reset) 
        #time adn Timer one's are important too for tehir use in this program latter.
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00",self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)

        self.initUI()


    def initUI(self):

        #set window title 
        self.setWindowTitle("Stop Watch")

        #set box vertical box style for time laabel only 
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        #setting time label in the center 
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #adding buttons horizontally 
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        vbox.setSpacing(15)
        vbox.setContentsMargins(20, 20, 20, 20)
        hbox.setSpacing(10)

        #setting up some colors and font for stopwatch
        self.setStyleSheet("""
        QWidget {
        background-color: #1e1e2e;
        font-family: 'Segoe UI', sans-serif;
        }
        QLabel{
        color: #cdd6f4;
        font-size: 25px;
        font-weight: 600;
        }
        QPushButton{
        background-color: #89b4fa;
        color: #1e1e2e;
        border-radius: 8px;
        padding: 8px 16px;
        font-size: 16px;
        font-weight: bold;
        }
        QPushButton:hover{
        background-color: #74c7ec;
        }
        QPushButton:pressed{
        background-color: #45475a;
        }

        """)

         
              #Telling what to do when button is cllicked 
        #connecting each button to it's function 

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)


    def start(self):
        self.timer.start(10)  

    def stop(self):
        self.timer.stop()
         

    def reset(self):
        #reseting stopwatch 1.stop it complety, 2. start again from 0
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.time_format(self.time))

    def time_format(self, time):
        #setting up time format for easier understanding
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10

        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        #updates display after after Maec 10
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.time_format(self.time))




if __name__ == "__main__":
    #creating GUI for the stopwatch 
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    #last one help sto keep GUI until we decide to close it 
    sys.exit(app.exec_()) 
