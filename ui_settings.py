# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(400, 300)
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        Settings.setFont(font)
        self.labeCustomSessionl = QLabel(Settings)
        self.labeCustomSessionl.setObjectName(u"labeCustomSessionl")
        self.labeCustomSessionl.setGeometry(QRect(41, 31, 128, 16))
        self.labelCustomBreak = QLabel(Settings)
        self.labelCustomBreak.setObjectName(u"labelCustomBreak")
        self.labelCustomBreak.setGeometry(QRect(41, 61, 115, 16))
        self.lineEditCustomSession = QLineEdit(Settings)
        self.lineEditCustomSession.setObjectName(u"lineEditCustomSession")
        self.lineEditCustomSession.setGeometry(QRect(170, 30, 125, 21))
        self.lineEditCustomBreak = QLineEdit(Settings)
        self.lineEditCustomBreak.setObjectName(u"lineEditCustomBreak")
        self.lineEditCustomBreak.setGeometry(QRect(170, 60, 125, 21))
        self.buttonApply = QPushButton(Settings)
        self.buttonApply.setObjectName(u"buttonApply")
        self.buttonApply.setGeometry(QRect(180, 90, 100, 32))
        self.radioBold = QRadioButton(Settings)
        self.radioBold.setObjectName(u"radioBold")
        self.radioBold.setGeometry(QRect(40, 150, 71, 20))
        self.radioItalic = QRadioButton(Settings)
        self.radioItalic.setObjectName(u"radioItalic")
        self.radioItalic.setGeometry(QRect(40, 170, 71, 20))

        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Form", None))
        self.labeCustomSessionl.setText(QCoreApplication.translate("Settings", u"Set Custom Session: ", None))
        self.labelCustomBreak.setText(QCoreApplication.translate("Settings", u"Set Custom Break: ", None))
        self.buttonApply.setText(QCoreApplication.translate("Settings", u"Apply", None))
        self.radioBold.setText(QCoreApplication.translate("Settings", u"Bold", None))
        self.radioItalic.setText(QCoreApplication.translate("Settings", u"Italic", None))
    # retranslateUi

