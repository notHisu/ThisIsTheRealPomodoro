# settings.py
from PySide6.QtWidgets import QDialog
from ui_settings import Ui_Settings


class SettingsForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.main_window = parent

        self.ui.buttonApply.clicked.connect(self.apply_settings)

    def apply_settings(self):
        session_length = int(self.ui.lineEditCustomSession.text())
        break_length = int(self.ui.lineEditCustomBreak.text())
        self.main_window.set_custom_length(session_length, break_length)
        self.close()
