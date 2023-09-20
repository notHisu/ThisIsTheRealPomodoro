# settings.py
import ctypes
import os
import json
import PySide6.QtGui
from PySide6.QtWidgets import QDialog
from gui.ui_settings import Ui_Settings

settings = {
    "session_length": 25,
    "break_length": 5,
    "long_break": 15,
    "auto_skip_break": False,
    "auto_stop_session": False,
    "auto_stop_break": False,
    "focus_mode_win": False,
    "focus_mode_mac": False,
    "break_app": "/Applications/Spotify.app",
}


class SettingsForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.main_window = parent
        self.settings_file = os.path.join("utils", "settings.json")
        self.load_settings()

        self.setWindowTitle("Settings")
        self.ui.checkBoxAutoStopSession.toggled.connect(self.auto_stop_session)
        self.ui.checkBoxFocusMode.toggled.connect(self.set_focus_assist_win)
        self.ui.buttonPreset15.clicked.connect(lambda: self.set_preset_time(15))
        self.ui.buttonPreset30.clicked.connect(lambda: self.set_preset_time(30))
        self.ui.buttonPreset45.clicked.connect(lambda: self.set_preset_time(45))
        self.ui.lineEditCustomSession.returnPressed.connect(self.set_custom_session)
        self.ui.lineEditCustomBreak.returnPressed.connect(self.set_custom_break)
        self.ui.lineEditCustomLongBreak.returnPressed.connect(
            self.set_custom_long_break
        )
        self.ui.lineEditBreakAppPath.returnPressed.connect(self.set_break_app)

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

    def auto_stop_session(self):
        pass

    def set_focus_assist_win(enable):
        VK_WIN = 0x5B
        VK_N = 0x4E
        VK_RETURN = 0x0D

        ctypes.windll.user32.keybd_event(VK_WIN, 0, 0, 0)  # press the Windows key
        ctypes.windll.user32.keybd_event(VK_N, 0, 0, 0)  # press the 'N' key
        ctypes.windll.user32.keybd_event(VK_N, 0, 2, 0)  # release the 'N' key
        ctypes.windll.user32.keybd_event(VK_WIN, 0, 2, 0)  # release the Windows key
        ctypes.windll.user32.keybd_event(VK_RETURN, 0, 0, 0)  # press the Enter key
        ctypes.windll.user32.keybd_event(VK_RETURN, 0, 2, 0)  # release the Enter key

    def set_focus_assist_mac(enable):
        pass

    def set_break_app(self):
        path = self.ui.lineEditBreakAppPath.text()
        self.main_window.set_break_app(path)

    def load_settings(self):
        try:
            with open(self.settings_file) as f:
                settings = json.load(f)

            self.ui.checkBoxSkipBreak.setChecked(settings["auto_skip_break"])
            self.ui.checkBoxAutoStopBreak.setChecked(settings["auto_stop_break"])
            self.ui.checkBoxAutoStopSession.setChecked(settings["auto_stop_session"])
            self.ui.checkBoxFocusMode.setChecked(settings["focus_mode_win"])
            self.ui.checkBoxFocusModeMac.setChecked(settings["focus_mode_mac"])
            self.ui.lineEditBreakAppPath.setText(settings["break_app"])
            self.ui.lineEditCustomSession.setText(str(settings["session_length"]))
            self.ui.lineEditCustomBreak.setText(str(settings["break_length"]))
            self.ui.lineEditCustomLongBreak.setText(str(settings["long_break"]))

        except FileNotFoundError:
            print("No settings")

    def save_settings(self):
        settings["session_length"] = int(self.ui.lineEditCustomSession.text())
        settings["break_length"] = int(self.ui.lineEditCustomBreak.text())
        settings["long_break"] = int(self.ui.lineEditCustomLongBreak.text())
        settings["break_app"] = self.ui.lineEditBreakAppPath.text()
        settings["auto_skip_break"] = self.ui.checkBoxSkipBreak.isChecked()
        settings["auto_stop_break"] = self.ui.checkBoxAutoStopBreak.isChecked()
        settings["auto_stop_session"] = self.ui.checkBoxAutoStopSession.isChecked()
        settings["focus_mode_win"] = self.ui.checkBoxFocusMode.isChecked()
        settings["focus_mode_mac"] = self.ui.checkBoxFocusModeMac.isChecked()

    def closeEvent(self, event):
        self.save_settings()
        # settings["auto_skip_break"] = self.ui.checkBoxAutoStopBreak.isChecked()
        with open(self.settings_file, "w") as f:
            json.dump(settings, f)
        event.accept()
