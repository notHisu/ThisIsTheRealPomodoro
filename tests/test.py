"""
import sys

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QProgressBar,
    QPushButton,
    QGridLayout,
    QApplication,
)

from PySide6.QtGui import QFont


class MainTimerView(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.timer_label = QLabel("25:00")
        self.timer_label.setFont(QFont("Arial", 48))

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMaximum(1500)  # 25 minutes in seconds
        self.progress_bar.setValue(1500)  # start with full time

        self.start_button = QPushButton("Start", clicked=self.start_timer)
        self.pause_button = QPushButton("Pause", clicked=self.pause_timer)
        self.stop_button = QPushButton("Stop", clicked=self.stop_timer)

        layout = QGridLayout()
        layout.addWidget(self.timer_label, 0, 0, 1, 3)
        layout.addWidget(self.progress_bar, 1, 0, 1, 3)
        layout.addWidget(self.start_button, 2, 0)
        layout.addWidget(self.pause_button, 2, 1)
        layout.addWidget(self.stop_button, 2, 2)

        self.setLayout(layout)
        self.show()

    def start_timer(self):
        # start timer logic
        pass

    def pause_timer(self):
        # pause timer logic
        pass

    def stop_timer(self):
        # stop timer logic
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainTimerView()
    widget.show()
    sys.exit(app.exec())
"""
import sys
from PySide6.QtWidgets import (
    QWidget,
    QTableView,
    QAbstractItemView,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QApplication,
)
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex

"""
class TaskSchedulerView(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.table = QTableView()
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.model = TaskTableModel()  # custom table model
        self.table.setModel(self.model)

        # buttons
        self.add_button = QPushButton("Add")
        self.edit_button = QPushButton("Edit")
        self.delete_button = QPushButton("Delete")

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.edit_button)
        self.button_layout.addWidget(self.delete_button)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(self.button_layout)

        self.setLayout(layout)


class TaskTableModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.tasks = []  # populated from db

    def rowCount(self, parent=QModelIndex()):
        return len(self.tasks)

    def columnCount(self, parent=QModelIndex()):
        return 3

    # other model methods


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TaskSchedulerView()
    widget.show()
    sys.exit(app.exec())
"""

from PySide6.QtWidgets import QWidget, QCalendarWidget, QListView, QVBoxLayout

from PySide6.QtCore import QDate


class CalendarView(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # calendar widget
        self.calendar = QCalendarWidget()
        self.calendar.selectionChanged.connect(self.update_schedule)

        # list view to show tasks on selected day
        self.task_list = QListView()

        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        layout.addWidget(self.task_list)

        self.setLayout(layout)

    def update_schedule(self, selectedDate):
        # get selected date
        date = self.calendar.selectedDate()

        # update task list with schedule for selected date
        self.task_list.clear()

        # query tasks from db for date and populate list


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = CalendarView()
    widget.show()
    sys.exit(app.exec())
