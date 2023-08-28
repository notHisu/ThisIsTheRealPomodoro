from PySide6.QtWidgets import QPushButton, QTableView, QDialog
from ui_task_scheduler_view import Ui_TaskSchedularView


class TaskViewForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TaskSchedularView()
        self.ui.setupUi(self)
        self.main_window = parent

        self.setWindowTitle("Task View")
