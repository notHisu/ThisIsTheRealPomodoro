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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QHBoxLayout,
    QListView, QSizePolicy, QWidget)

class Ui_Calendar(object):
    def setupUi(self, Calendar):
        if not Calendar.objectName():
            Calendar.setObjectName(u"Calendar")
        Calendar.resize(658, 288)
        self.horizontalLayout_2 = QHBoxLayout(Calendar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(Calendar)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 0))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.calendarWidget = QCalendarWidget(self.frame)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setMinimumSize(QSize(300, 250))
        self.calendarWidget.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.calendarWidget)

        self.listViewTask = QListView(self.frame)
        self.listViewTask.setObjectName(u"listViewTask")
        self.listViewTask.setMinimumSize(QSize(300, 250))
        self.listViewTask.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.listViewTask)


        self.horizontalLayout_2.addWidget(self.frame)


        self.retranslateUi(Calendar)

        QMetaObject.connectSlotsByName(Calendar)
    # setupUi

    def retranslateUi(self, Calendar):
        Calendar.setWindowTitle(QCoreApplication.translate("Calendar", u"Calendar", None))
    # retranslateUi

