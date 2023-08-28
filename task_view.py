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
from ui_task_scheduler_view import Ui_TaskSchedularView


class TaskViewForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TaskSchedularView()
        self.ui.setupUi(self)
        self.main_window = parent

        self.setWindowTitle("Task View")
        self.ui.tableWidgetTask.setColumnWidth(0, self.ui.tableWidgetTask.width())
        # self.ui.tableWidgetTask.setColumnWidth(
        #     1, self.ui.tableWidgetTask.width()
        # )

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
