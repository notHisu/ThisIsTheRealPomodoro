# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QSizePolicy, QWidget


class Ui_Settings(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(400, 300)
        self.labeCustomSessionl = QLabel(Form)
        self.labeCustomSessionl.setObjectName("labeCustomSessionl")
        self.labeCustomSessionl.setGeometry(QRect(41, 31, 128, 16))
        self.labelCustomBreak = QLabel(Form)
        self.labelCustomBreak.setObjectName("labelCustomBreak")
        self.labelCustomBreak.setGeometry(QRect(41, 61, 115, 16))
        self.lineEditCustomSession = QLineEdit(Form)
        self.lineEditCustomSession.setObjectName("lineEditCustomSession")
        self.lineEditCustomSession.setGeometry(QRect(170, 30, 125, 21))
        self.lineEditCustomBreak = QLineEdit(Form)
        self.lineEditCustomBreak.setObjectName("lineEditCustomBreak")
        self.lineEditCustomBreak.setGeometry(QRect(170, 60, 125, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.labeCustomSessionl.setText(
            QCoreApplication.translate("Form", "Set Custom Session: ", None)
        )
        self.labelCustomBreak.setText(
            QCoreApplication.translate("Form", "Set Custom Break: ", None)
        )

    # retranslateUi
