# This Python file uses the following encoding: utf-8

#VM Activate
#source venv/bin/activate
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Main

class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        #Create session timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.counter = 0

        #Create break timer
        self.break_timer = QTimer(self)
        self.break_timer.timeout.connect(self.update_break_timer)

        self.session_length = 1 * 60
        self.break_length = 5 * 60
        self.timer_running = False

        self.ui.buttonStart.clicked.connect(self.toggle_timer)
        self.ui.buttonReset.clicked.connect(self.reset_timer)
        self.ui.buttonPreset15.clicked.connect(lambda: self.set_preset_time(15))
        self.ui.buttonPreset30.clicked.connect(lambda: self.set_preset_time(30))
        self.ui.buttonPreset45.clicked.connect(lambda: self.set_preset_time(45))

        self.update_timer_ui()
        self.update_preset_buttons()

    def start_timer(self):
        if not self.timer_running:
            self.timer.start(1000)
            self.timer_running = True
            self.ui.buttonStart.setText("Pause")

            self.update_preset_buttons()

    def pause_timer(self):
        if self.timer_running:
            self.timer.stop()
            self.timer_running = False
            self.ui.buttonStart.setText("Start")

    def toggle_timer(self):
        if self.timer_running:
            self.pause_timer()
        else:
            self.start_timer()

    def reset_timer(self):
        self.session_length = 25 * 60
        self.update_timer_ui()
        self.timer.stop()
        self.timer_running = False
        self.update_preset_buttons()
        self.ui.buttonStart.setText("Start")

    def update_timer(self):
        self.session_length -= 1
        self.update_timer_ui()
        if self.session_length == 0:
            self.timer.stop()
            self.counter += 1
            self.ui.labelCounter.setText(f"Counter: {self.counter}")
            self.timer_running = False
            self.break_timer.start(1000)

    def set_preset_time(self, presetTime):
        self.session_length = presetTime * 60
        self.update_timer_ui()

    def update_preset_buttons(self):
        self.ui.buttonPreset15.setEnabled(not self.timer_running)
        self.ui.buttonPreset30.setEnabled(not self.timer_running)
        self.ui.buttonPreset45.setEnabled(not self.timer_running)

    def update_timer_ui(self):
        minutes = self.session_length // 60
        seconds = self.session_length % 60
        self.ui.labelTime.setText(f"{minutes:02d}:{seconds:02d}")
        self.ui.progressBar.setMaximum(self.session_length)
        self.ui.progressBar.setValue(self.session_length)

    #def start_break_timer(self):


    def update_break_timer(self):
        self.break_length -= 1
        self.update_timer_ui()
        if self.break_length == 0:
            self.break_timer.stop()
            #Setup new session
            self.timer_running = False
            self.session_length = 25 * 60
            self.update_timer_ui()
            self.update_preset_buttons()
            self.ui.buttonStart.setText("Start")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main()
    widget.show()
    sys.exit(app.exec())
