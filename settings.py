# settings.py
from PySide6.QtWidgets import QDialog, QLabel, QPushButton
from PySide6.QtGui import QFont
from ui_settings import Ui_Settings


class SettingsForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.main_window = parent

        self.ui.buttonPreset15.clicked.connect(lambda: self.set_preset_time(15))
        self.ui.buttonPreset30.clicked.connect(lambda: self.set_preset_time(30))
        self.ui.buttonPreset45.clicked.connect(lambda: self.set_preset_time(45))
        self.ui.lineEditCustomSession.returnPressed.connect(self.set_custom_session)
        self.ui.lineEditCustomBreak.returnPressed.connect(self.set_custom_break)
        self.ui.lineEditCustomLongBreak.returnPressed.connect(
            self.set_custom_long_break
        )

    def set_custom_session(self):
        session_length = (
            0
            if self.ui.lineEditCustomSession.text() == ""
            else int(self.ui.lineEditCustomSession.text()) * 60
        )
        self.main_window.set_custom_session(session_length)

    def set_custom_break(self):
        break_length = (
            0
            if self.ui.lineEditCustomBreak.text() == ""
            else int(self.ui.lineEditCustomBreak.text()) * 60
        )
        self.main_window.set_custom_break(break_length)

    def set_custom_long_break(self):
        long_break_length = (
            0
            if self.ui.lineEditCustomLongBreak.text() == ""
            else int(self.ui.lineEditCustomLongBreak.text()) * 60
        )
        self.main_window.set_custom_long_break(long_break_length)

    def set_preset_time(self, presetTime):
        session_length = presetTime * 60
        self.main_window.set_custom_session(session_length)
