#digital alarm clock
#display the current time 
#get time from the user and set the alarm
#stop watch integrated 

import sys 
from pathlib import Path
from PyQt5.QtWidgets import  QApplication, QTimeEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QStackedWidget
from PyQt5.QtCore import QTime, QTimer, Qt
import pygame
from stop_watch import StopWatch 

ALARM_SOUND = Path(__file__).with_name("deafening-alarm-sound.mp3")



class AlarmCLock(QWidget):
    def __init__(self):
        super().__init__()
        self.current_time= QLabel(self)
        self.alarm_status_label = QLabel("Alarm not set", self)
        self.timer = QTimer(self)
        #add a time edit 
        self.time_edit = QTimeEdit(self)
        self.time_edit.setDisplayFormat("hh:mm:ss")
        self.time_edit.setTime(QTime.currentTime())
        #create some buttons 
        self.setAlarm_button = QPushButton("Set Alarm", self)
        self.enable_button = QPushButton("Enable", self)
        self.disable_button = QPushButton("Disable", self)
        self.stop_button = QPushButton("Stop", self)
        self.stop_button.hide()
        self.stop_watch_button = QPushButton("Stopwatch", self)

        self.alarm_active = False  
        self.alarm_time = None
        self.alarm_ringing = False

       
        self.gUI()


    def gUI(self):
        self.setGeometry(350,150,300,300)
        self.setWindowTitle("Alarm-clock")
        #show current time as vbox 
        vbox = QVBoxLayout()
        vbox.addWidget(self.current_time)
        self.current_time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #show time edit 
        vbox.addWidget(self.time_edit)
        vbox.addWidget(self.alarm_status_label)
        self.alarm_status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #set the vbox layout 
        self.setLayout(vbox)
        #create horizontal layout for the buttons 
        hbox = QHBoxLayout()
        hbox.addWidget(self.setAlarm_button)
        hbox.addWidget(self.enable_button)
        hbox.addWidget(self.disable_button)
        #set the layout 
        vbox.addLayout(hbox)

        vbox.addWidget(self.stop_button)

        self.setLayout(vbox)

        vbox.addWidget(self.stop_watch_button)
        self.setLayout(vbox)

        vbox.setSpacing(15)
        vbox.setContentsMargins(20, 20, 20, 20)
        hbox.setSpacing(10)

        #connecting the buttons to their functionality 
        #updating display each second 
        self.timer.timeout.connect(self.update_display)
        self.timer.start(1000)
        self.setAlarm_button.clicked.connect(self.set_alarm)
        self.enable_button.clicked.connect(self.enable)
        self.disable_button.clicked.connect(self.disable)
        self.stop_button.clicked.connect(self.stop_alarm)
        

        #set the style sheet
        self.setStyleSheet("""
    QWidget {
        background-color: #1e1e2e;
        font-family: 'Segoe UI', sans-serif;
    }
    QLabel {
        color: #cdd6f4;
        font-size: 26px;
        font-weight: 600;
    }
    QTimeEdit {
        background-color: #313244;
        color: #cdd6f4;
        border-radius: 8px;
        padding: 6px;
        font-size: 18px;
    }
    QPushButton {
        background-color: #89b4fa;
        color: #1e1e2e;
        border-radius: 8px;
        padding: 8px 16px;
        font-size: 16px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #74c7ec;
    }
    QPushButton:pressed {
        background-color: #45475a;
    }
""")
      
    def set_alarm(self):
        self.alarm_time = self.time_edit.time()
        self.alarm_active = True 
        self.alarm_status_label.setText(f"Alarm is set for {self.time_format(self.alarm_time)}")

    def enable(self):
        if self.alarm_time is None:
            self.alarm_status_label.setText("No Alarm is set yet")
            return 
        self.alarm_active = True 
        self.alarm_status_label.setText(f"Alarm is set for {self.time_format(self.alarm_time)}")

    def disable(self):
        self.alarm_active = False 
        self.alarm_status_label.setText("alarm is disabled")

    def stop_alarm(self):
        self.alarm_ringing = False
        self.alarm_active = False
        #stop the alarm music
        pygame.mixer.music.stop()
        self.stop_button.hide()
        self.alarm_status_label.setText("Alarm Stopped")
        
    def time_format(self,time):
        #set the time foramt 
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()

        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def update_display(self):
        #update display every time sec 1000
        current = QTime.currentTime()
        #compare current time to alarms et time 
        self.current_time.setText(self.time_format(current))
        
        #set some conditions for the alarm to play the alarm sound 
        if self.alarm_active and not self.alarm_ringing and self.alarm_time is not None:
            if (current.hour() == self.alarm_time.hour()
                and current.minute() == self.alarm_time.minute()
                and current.second() == self.alarm_time.second()):
                self.trigger_alarm()



    def trigger_alarm(self):
        self.alarm_ringing = True 
        self.alarm_status_label.setText("ALARM! ALARM! ALARM!")
        self.stop_button.show()
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(str(ALARM_SOUND))
            pygame.mixer.music.play(-1)
        except pygame.error as e:
             self.alarm_status_label.setText(f"Alarm sound failed: {e}")
     
    

class MainWindow(QWidget):
    """Container that switches between Alarm and Stopwatch."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Alarm & Stopwatch")
        self.setGeometry(350, 150, 350, 400)

        # Main layout
        main_layout = QVBoxLayout(self)

        # Stacked widget to hold both views
        self.stack = QStackedWidget()
        main_layout.addWidget(self.stack)

        # ---- Create the alarm widget (your existing class) ----
        self.alarm_widget = AlarmCLock()
        self.stack.addWidget(self.alarm_widget)   # index 0

        # Wrap the StopWatch widget so we can add a "Back" button
        stop_watch_page = QWidget()
        sw_layout = QVBoxLayout(stop_watch_page)
        back_btn = QPushButton("← Back to Alarm")
        back_btn.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        sw_layout.addWidget(back_btn)
        self.stop_watch_widget = StopWatch()
        sw_layout.addWidget(self.stop_watch_widget)
        self.stack.addWidget(stop_watch_page)       # index 1

        # ---- Connect the alarm's Stopwatch button to switch views ----
        self.alarm_widget.stop_watch_button.clicked.connect(
            lambda: self.stack.setCurrentIndex(1)
        )

        # Start with the alarm view
        self.stack.setCurrentIndex(0)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
