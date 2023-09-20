# settings.py
import ctypes
import time
from PySide6.QtWidgets import QDialog
from gui.ui_settings import Ui_Settings


class SettingsForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.main_window = parent

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
        print("something")

    def set_focus_assist_win(enable):
        VK_WIN = 0x5B
        VK_N = 0x4E
        VK_RETURN = 0x0D

        ctypes.windll.user32.keybd_event(VK_WIN, 0, 0, 0)  # press the Windows key
        ctypes.windll.user32.keybd_event(VK_N, 0, 0, 0)  # press the 'N' key
        ctypes.windll.user32.keybd_event(VK_N, 0, 2, 0)  # release the 'N' key
        ctypes.windll.user32.keybd_event(VK_WIN, 0, 2, 0)  # release the Windows key
        ctypes.windll.user32.keybd_event(VK_RETURN, 0, 0, 0)  # press the Enter key

    def set_focus_assist_mac(enable):
        pass

    def set_break_app(self):
        path = self.ui.lineEditBreakAppPath.text()
        self.main_window.set_break_app(path)
