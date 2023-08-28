# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calendar.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QListView, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Calendar(object):
    def setupUi(self, Calendar):
        if not Calendar.objectName():
            Calendar.setObjectName(u"Calendar")
        Calendar.resize(296, 401)
        self.verticalLayoutWidget = QWidget(Calendar)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 291, 401))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.calendarWidget = QCalendarWidget(self.verticalLayoutWidget)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.verticalLayout.addWidget(self.calendarWidget)

        self.listViewTask = QListView(self.verticalLayoutWidget)
        self.listViewTask.setObjectName(u"listViewTask")

        self.verticalLayout.addWidget(self.listViewTask)


        self.retranslateUi(Calendar)

        QMetaObject.connectSlotsByName(Calendar)
    # setupUi

    def retranslateUi(self, Calendar):
        Calendar.setWindowTitle(QCoreApplication.translate("Calendar", u"Calendar", None))
    # retranslateUi

