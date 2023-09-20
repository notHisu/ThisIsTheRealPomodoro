# This Python file uses the following encoding: utf-8

# App path for testing
# "C:\Users\Hisu\AppData\Roaming\Spotify\Spotify.exe"
# /Applications/Brave Browser.app
# /Applications/Spotify.app

import subprocess
import os
import json
import requests
import random
import textwrap

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, QCoreApplication


"""
Important:
You need to run the following command to generate the ui_form.py file
    pyside6-uic form.ui -o ui_form.py
    pyside6-uic settings.ui -o ui_settings.py
    pyside6-uic task_scheduler_view.ui -o ui_task_scheduler_view.py
    pyside6-uic calendar.ui -o ui_calendar.py
    pyside6-uic spotify_player.ui -o ui_spotify.py
"""

from gui.ui_form import Ui_Main


class Main(QMainWindow):
    # Initializer
    def __init__(self, parent=None):
        # Init UI
        super().__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.settings_dialog = self.init_settings_form()
        self.task_view_dialog = self.init_task_view_form()
        self.calender_dialog = self.init_calendar_form()
        self.spotify_dialog = self.init_spotify_form()

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

        # App to open during break
        self.break_app_path = None
        self.break_app_name = None

        # Connect signals and slots
        self.ui.buttonStart.clicked.connect(self.toggle_timer)
        self.ui.buttonReset.clicked.connect(self.reset_timer)
        self.ui.buttonQuote.clicked.connect(self.fetch_quotes)

        self.ui.actionSettings.triggered.connect(self.open_settings)
        self.ui.actionQuit.triggered.connect(QCoreApplication.quit)
        self.ui.actionTask.triggered.connect(self.open_task)
        self.ui.actionCalendar.triggered.connect(self.open_calendar)
        self.ui.actionSpotify.triggered.connect(self.open_spotify)

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
            self.break_timer.start(100)
            self.ui.buttonStart.setEnabled(False)
            self.open_break_app()

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
            self.close_break_app()
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

    def open_task(self):
        self.task_view_dialog.show()

    def open_calendar(self):
        self.calender_dialog.show()

    def open_spotify(self):
        self.spotify_dialog.show()

    def set_custom_session(self, session_length):
        self.session_length = session_length
        self.ui.progressBar.setMaximum(self.session_length)
        self.update_timer_ui(self.session_length)

    def set_break_app(self, break_app_path):
        self.break_app_path = break_app_path.replace('"', "")
        self.break_app_name = os.path.basename(self.break_app_path)
        print(self.break_app_name)

    def open_break_app(self):
        try:
            subprocess.run(["open", "-a", self.break_app_path])
            # subprocess.Popen(self.break_app_path)
            print(f"{self.break_app_path} has been opened")
        except FileNotFoundError:
            print(f"Failed to open{self.break_app_path}. File not found.")
        except Exception as e:
            print(f"Failed to open {self.break_app_path}. Error: {str(e)}")

    def close_break_app(self):
        try:
            subprocess.run(["pkill", "-f", self.break_app_name])
            # subprocess.run(["taskkill", "/F", "/IM", self.break_app_name])
            print(f"{self.break_app_name} has been closed.")
        except subprocess.CalledProcessError:
            print(f"Failed to close {self.break_app_name}.")

    def set_custom_break(self, break_length):
        self.break_length = break_length

    def set_custom_long_break(self, long_break_length):
        self.long_break_length = long_break_length

    def init_settings_form(self):
        from settings import SettingsForm

        return SettingsForm(self)

    def init_task_view_form(self):
        from task_view import TaskViewForm

        return TaskViewForm(self)

    def init_calendar_form(self):
        from calendar_view import CalendarForm

        return CalendarForm(self)

    def init_spotify_form(self):
        from spotify_player import SpotifyForm

        return SpotifyForm(self)

    def fetch_quotes(self):
        res = requests.get("https://zenquotes.io/api/quotes")
        quotes = json.loads(res.text)
        # print(response)
        random_quote = random.choice(quotes)
        quote_text = random_quote["q"]
        author_text = random_quote["a"]

        wrapped_quote = textwrap.wrap(quote_text, width=50)
        if len(wrapped_quote) > 1:
            quotes_part1 = wrapped_quote[0]
            quote_part2 = wrapped_quote[1]
        else:
            quotes_part1 = quote_text
            quote_part2 = ""
        labelText = f"{quotes_part1}\n{quote_part2}\n-{author_text}"
        # print(random_quote["q"], " - ", random_quote["a"])
        self.ui.labelQuote.setText(labelText)
