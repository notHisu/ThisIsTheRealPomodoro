import json
import os

from PySide6.QtWidgets import (
    QPushButton,
    QTableWidget,
    QDialog,
    QLineEdit,
    QSpinBox,
    QTableWidgetItem,
    QMessageBox,
)
from PySide6.QtCore import QAbstractTableModel
from gui.ui_task_scheduler_view import Ui_TaskSchedularView


class TaskViewForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TaskSchedularView()
        self.ui.setupUi(self)
        self.main_window = parent
        self.tasks_file = os.path.join("utils", "tasks.json")
        self.load_tasks()

        self.setWindowTitle("Task View")
        self.ui.tableWidgetTask.setColumnWidth(0, self.ui.tableWidgetTask.width())

        self.ui.buttonAdd.clicked.connect(self.add_task)
        self.ui.buttonDelete.clicked.connect(self.delete_task)

        self.ui.tableWidgetTask.cellClicked.connect(self.update_selected_row)
        self.selected_row = None

    def add_task(self):
        name = self.ui.lineEditName.text()
        pomodoros = self.ui.spinBoxPomodoros.value()

        if name != "" and pomodoros > 0:
            # Get row count
            row_count = self.ui.tableWidgetTask.rowCount()

            # Insert new row at end
            self.ui.tableWidgetTask.insertRow(row_count)

            # Create items with input data
            name_item = QTableWidgetItem(name)
            pomodoro_item = QTableWidgetItem(str(pomodoros))

            # Set items for the new row
            self.ui.tableWidgetTask.setItem(row_count, 0, name_item)
            self.ui.tableWidgetTask.setItem(row_count, 1, pomodoro_item)

            # Clear input fields
            self.ui.lineEditName.clear()
            self.ui.spinBoxPomodoros.setValue(25)

    def delete_task(self):
        if self.selected_row is not None:
            self.ui.tableWidgetTask.removeRow(self.selected_row)

    def edit_task(self):
        if self.selected_row is not None:
            name = self.ui.lineEditName.text()
            pomodoros = self.ui.spinBoxPomodoros.value()

            if name != "" and pomodoros > 0:
                name_item = QTableWidgetItem(name)
                pomodoro_item = QTableWidgetItem(str(pomodoros))

                self.ui.tableWidgetTask.setItem(self.selected_row, 0, name_item)
                self.ui.tableWidgetTask.setItem(self.selected_row, 1, pomodoro_item)

                # Clear input fields after editing
                self.ui.lineEditName.clear()
                self.ui.spinBoxPomodoros.setValue(25)
                self.selected_row = None

    def update_selected_row(self, row, col):
        self.selected_row = row

        name_item = self.ui.tableWidgetTask.item(row, 0)
        pomodoro_item = self.ui.tableWidgetTask.item(row, 1)

        if name_item is not None and pomodoro_item is not None:
            name = name_item.text()
            pomodoros = int(pomodoro_item.text())

            self.ui.lineEditName.setText(name)
            self.ui.spinBoxPomodoros.setValue(pomodoros)

    def save_tasks(self):
        tasks = []
        for row in range(self.ui.tableWidgetTask.rowCount()):
            name = self.ui.tableWidgetTask.item(row, 0).text()
            pomodoros = int(self.ui.tableWidgetTask.item(row, 1).text())
            task = {"name": name, "pomodoros": pomodoros}
            tasks.append(task)

        with open(self.tasks_file, "w") as f:
            json.dump(tasks, f)

    def closeEvent(self, event):
        try:
            self.save_tasks()
            print("Done.")
        except:
            print("Can't save!")

    def load_tasks(self):
        try:
            with open(self.tasks_file) as f:
                tasks = json.load(f)
                # print(tasks)
                for task in tasks:
                    name = task["name"]
                    pomodoros = task["pomodoros"]
                    # Create items
                    name_item = QTableWidgetItem(name)
                    pomodoros_item = QTableWidgetItem(str(pomodoros))

                    # Get row count and insert new row
                    row = self.ui.tableWidgetTask.rowCount()
                    self.ui.tableWidgetTask.insertRow(row)

                    # Set row items
                    self.ui.tableWidgetTask.setItem(row, 0, name_item)
                    self.ui.tableWidgetTask.setItem(row, 1, pomodoros_item)
        except:
            print("File doesn't exist")
