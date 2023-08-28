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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_TaskSchedularView(object):
    def setupUi(self, TaskSchedularView):
        if not TaskSchedularView.objectName():
            TaskSchedularView.setObjectName(u"TaskSchedularView")
        TaskSchedularView.resize(395, 302)
        self.horizontalLayoutWidget = QWidget(TaskSchedularView)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 270, 391, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonAdd = QPushButton(self.horizontalLayoutWidget)
        self.buttonAdd.setObjectName(u"buttonAdd")

        self.horizontalLayout.addWidget(self.buttonAdd)

        self.buttonEdit = QPushButton(self.horizontalLayoutWidget)
        self.buttonEdit.setObjectName(u"buttonEdit")

        self.horizontalLayout.addWidget(self.buttonEdit)

        self.buttonDelete = QPushButton(self.horizontalLayoutWidget)
        self.buttonDelete.setObjectName(u"buttonDelete")

        self.horizontalLayout.addWidget(self.buttonDelete)

        self.verticalLayoutWidget = QWidget(TaskSchedularView)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 391, 271))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableViewTask = QTableView(self.verticalLayoutWidget)
        self.tableViewTask.setObjectName(u"tableViewTask")

        self.verticalLayout.addWidget(self.tableViewTask)


        self.retranslateUi(TaskSchedularView)

        QMetaObject.connectSlotsByName(TaskSchedularView)
    # setupUi

    def retranslateUi(self, TaskSchedularView):
        TaskSchedularView.setWindowTitle(QCoreApplication.translate("TaskSchedularView", u"Task View", None))
        self.buttonAdd.setText(QCoreApplication.translate("TaskSchedularView", u"Add", None))
        self.buttonEdit.setText(QCoreApplication.translate("TaskSchedularView", u"Edit", None))
        self.buttonDelete.setText(QCoreApplication.translate("TaskSchedularView", u"Delete", None))
    # retranslateUi

