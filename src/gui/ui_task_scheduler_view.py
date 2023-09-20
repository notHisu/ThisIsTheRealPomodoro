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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_TaskSchedularView(object):
    def setupUi(self, TaskSchedularView):
        if not TaskSchedularView.objectName():
            TaskSchedularView.setObjectName(u"TaskSchedularView")
        TaskSchedularView.resize(338, 305)
        self.verticalLayout = QVBoxLayout(TaskSchedularView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(TaskSchedularView)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidgetTask = QTableWidget(self.frame_2)
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
        self.tableWidgetTask.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableWidgetTask)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(TaskSchedularView)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEditName = QLineEdit(self.frame)
        self.lineEditName.setObjectName(u"lineEditName")
        self.lineEditName.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_3.addWidget(self.lineEditName)

        self.spinBoxPomodoros = QSpinBox(self.frame)
        self.spinBoxPomodoros.setObjectName(u"spinBoxPomodoros")
        self.spinBoxPomodoros.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_3.addWidget(self.spinBoxPomodoros)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(TaskSchedularView)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.buttonAdd = QPushButton(self.frame_3)
        self.buttonAdd.setObjectName(u"buttonAdd")
        self.buttonAdd.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_4.addWidget(self.buttonAdd)

        self.buttonDelete = QPushButton(self.frame_3)
        self.buttonDelete.setObjectName(u"buttonDelete")
        self.buttonDelete.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_4.addWidget(self.buttonDelete)

        self.buttonEdit = QPushButton(self.frame_3)
        self.buttonEdit.setObjectName(u"buttonEdit")
        self.buttonEdit.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_4.addWidget(self.buttonEdit)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(TaskSchedularView)

        QMetaObject.connectSlotsByName(TaskSchedularView)
    # setupUi

    def retranslateUi(self, TaskSchedularView):
        TaskSchedularView.setWindowTitle(QCoreApplication.translate("TaskSchedularView", u"Task View", None))
        ___qtablewidgetitem = self.tableWidgetTask.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TaskSchedularView", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidgetTask.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TaskSchedularView", u"Pomodoros", None));
        self.buttonAdd.setText(QCoreApplication.translate("TaskSchedularView", u"Add", None))
        self.buttonDelete.setText(QCoreApplication.translate("TaskSchedularView", u"Delete", None))
        self.buttonEdit.setText(QCoreApplication.translate("TaskSchedularView", u"Edit", None))
    # retranslateUi

