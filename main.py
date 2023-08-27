# This Python file uses the following encoding: utf-8

# VM Activate
# source venv/bin/activate
# .\env\Scripts\activate
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, QCoreApplication


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py
#     pyside6-uic settings.ui -o ui_settings.py

from ui_form import Ui_Main


class Main(QMainWindow):
    # Initializer
    def __init__(self, parent=None):
        # Init UI
        super().__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.settings_dialog = self.init_settings_form()

        # Create session timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.counter = 0

        # Create break timer
        self.break_timer = QTimer(self)
        self.break_timer.timeout.connect(self.update_break_timer)

        self.session_length = 25 * 60
        self.break_length = 5 * 60
        self.long_break_length = 15 * 60
        self.timer_running = False
        self.is_break = False

        # Connect signals and slots
        self.ui.buttonStart.clicked.connect(self.toggle_timer)
        self.ui.buttonReset.clicked.connect(self.reset_timer)

        self.ui.actionSettings.triggered.connect(self.open_settings)
        self.ui.actionQuit.triggered.connect(QCoreApplication.quit)

        self.ui.progressBar.setMaximum(self.session_length)
        self.update_timer_ui(self.session_length)

    # Timer controls

    def start_timer(self):
        if not self.timer_running:
            self.setWindowTitle("It is working time!")
            self.ui.progressBar.setMaximum(self.session_length)
            self.timer.start(100)
            self.timer_running = True
            self.ui.buttonStart.setText("Pause")

    def pause_timer(self):
        if self.timer_running:
            self.timer.stop()
            self.timer_running = False
            self.ui.buttonStart.setText("Start")

    def reset_timer(self):
        self.session_length = 25 * 60
        self.ui.progressBar.setMaximum(self.session_length)
        self.update_timer_ui(self.session_length)

        self.timer.stop()
        self.timer_running = False

        self.break_timer.stop()
        self.is_break = False

        self.ui.buttonStart.setText("Start")
        self.ui.buttonStart.setEnabled(True)

    def start_break_timer(self):
        if self.is_break:
            self.setWindowTitle("It is time to relax")
            self.ui.progressBar.setMaximum(self.break_length)
            self.break_timer.start(1000)
            self.ui.buttonStart.setEnabled(False)

    # Update timers

    def update_timer(self):
        self.session_length -= 1
        self.update_timer_ui(self.session_length)
        if self.session_length == 0:
            self.timer.stop()
            self.counter += 1
            self.ui.labelCounter.setText(f"Counter: {self.counter}")
            self.timer_running = True
            self.is_break = True
            self.start_break_timer()

    def update_break_timer(self):
        if self.counter % 4 == 0:
            self.break_length = self.long_break_length
        self.break_length -= 1
        self.update_timer_ui(self.break_length)
        if self.break_length == 0:
            self.is_break = False
            self.break_timer.stop()
            # Setup new session
            self.timer_running = True
            self.session_length = 25 * 60
            self.ui.progressBar.setMaximum(self.session_length)
            self.update_timer_ui(self.session_length)
            self.ui.buttonStart.setText("Start")

    # UI update methods
    def update_timer_ui(self, remaining):
        minutes = remaining // 60
        seconds = remaining % 60
        self.ui.labelTime.setText(f"{minutes:02d}:{seconds:02d}")
        self.ui.progressBar.setValue(remaining)

    # Helper methods

    def toggle_timer(self):
        if self.timer_running:
            self.pause_timer()
        else:
            self.start_timer()

    # Settings dialog

    def open_settings(self):
        self.settings_dialog.show()

    def set_custom_session(self, session_length):
        self.session_length = session_length
        self.ui.progressBar.setMaximum(self.session_length)
        self.update_timer_ui(self.session_length)

    def set_custom_break(self, break_length):
        self.break_length = break_length

    def set_custom_long_break(self, long_break_length):
        self.long_break_length = long_break_length

    def init_settings_form(self):
        from settings import SettingsForm

        return SettingsForm(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main()
    widget.show()
    sys.exit(app.exec())
