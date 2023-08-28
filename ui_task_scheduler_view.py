# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_scheduler_view.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_TaskSchedularView(object):
    def setupUi(self, TaskSchedularView):
        if not TaskSchedularView.objectName():
            TaskSchedularView.setObjectName(u"TaskSchedularView")
        TaskSchedularView.resize(393, 314)
        self.horizontalLayoutWidget = QWidget(TaskSchedularView)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 270, 371, 31))
        self.horizontalLayoutWidget.setFocusPolicy(Qt.ClickFocus)
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonAdd = QPushButton(self.horizontalLayoutWidget)
        self.buttonAdd.setObjectName(u"buttonAdd")
        self.buttonAdd.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.buttonAdd)

        self.buttonEdit = QPushButton(self.horizontalLayoutWidget)
        self.buttonEdit.setObjectName(u"buttonEdit")
        self.buttonEdit.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.buttonEdit)

        self.buttonDelete = QPushButton(self.horizontalLayoutWidget)
        self.buttonDelete.setObjectName(u"buttonDelete")
        self.buttonDelete.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.buttonDelete)

        self.verticalLayoutWidget = QWidget(TaskSchedularView)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 371, 271))
        self.verticalLayoutWidget.setFocusPolicy(Qt.ClickFocus)
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidgetTask = QTableWidget(self.verticalLayoutWidget)
        if (self.tableWidgetTask.columnCount() < 2):
            self.tableWidgetTask.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetTask.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetTask.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidgetTask.setObjectName(u"tableWidgetTask")
        self.tableWidgetTask.setFocusPolicy(Qt.ClickFocus)
        self.tableWidgetTask.setRowCount(0)
        self.tableWidgetTask.horizontalHeader().setVisible(True)
        self.tableWidgetTask.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetTask.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidgetTask.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidgetTask.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidgetTask.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tableWidgetTask)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEditName = QLineEdit(self.verticalLayoutWidget)
        self.lineEditName.setObjectName(u"lineEditName")
        self.lineEditName.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_2.addWidget(self.lineEditName)

        self.spinBoxPomodoros = QSpinBox(self.verticalLayoutWidget)
        self.spinBoxPomodoros.setObjectName(u"spinBoxPomodoros")
        self.spinBoxPomodoros.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_2.addWidget(self.spinBoxPomodoros)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(TaskSchedularView)

        QMetaObject.connectSlotsByName(TaskSchedularView)
    # setupUi

    def retranslateUi(self, TaskSchedularView):
        TaskSchedularView.setWindowTitle(QCoreApplication.translate("TaskSchedularView", u"Task View", None))
        self.buttonAdd.setText(QCoreApplication.translate("TaskSchedularView", u"Add", None))
        self.buttonEdit.setText(QCoreApplication.translate("TaskSchedularView", u"Edit", None))
        self.buttonDelete.setText(QCoreApplication.translate("TaskSchedularView", u"Delete", None))
        ___qtablewidgetitem = self.tableWidgetTask.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TaskSchedularView", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidgetTask.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TaskSchedularView", u"Pomodoros", None));
    # retranslateUi

