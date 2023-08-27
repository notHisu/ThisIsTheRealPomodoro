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

        self.ui.buttonApply.clicked.connect(self.apply_settings)
        self.ui.radioBold.toggled.connect(self.toggle_bold_text)
        self.ui.radioItalic.toggled.connect(self.toggle_italic_text)

    def apply_settings(self):
        session_length = int(self.ui.lineEditCustomSession.text())
        break_length = int(self.ui.lineEditCustomBreak.text())
        self.main_window.set_custom_length(session_length, break_length)
        self.close()

    def toggle_bold_text(self, toggled):
        bold_font = QFont()
        bold_font.setBold(toggled)
        self.apply_font_to_widgets(self.main_window, bold_font)

    def toggle_italic_text(self, toggled):
        italic_font = QFont()
        italic_font.setItalic(toggled)
        self.apply_font_to_widgets(self.main_window, italic_font)

    def apply_font_to_widgets(self, widget, font):
        for child in widget.findChildren(QLabel):
            child.setFont(font)
        for child in widget.findChildren(QPushButton):
            child.setFont(font)

        # Apply font to main window as well
        widget.setFont(font)
