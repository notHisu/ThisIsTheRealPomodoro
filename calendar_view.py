from PySide6.QtWidgets import QDialog
from ui_calendar import Ui_Calendar


class CalendarForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Calendar()
        self.ui.setupUi(self)
        self.main_window = parent

        self.setWindowTitle("Calendar")
