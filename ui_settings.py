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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(429, 300)
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        Settings.setFont(font)
        self.groupBoxPresets = QGroupBox(Settings)
        self.groupBoxPresets.setObjectName(u"groupBoxPresets")
        self.groupBoxPresets.setGeometry(QRect(310, 0, 104, 127))
        self.verticalLayout_3 = QVBoxLayout(self.groupBoxPresets)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.buttonPreset15 = QPushButton(self.groupBoxPresets)
        self.buttonPreset15.setObjectName(u"buttonPreset15")
        self.buttonPreset15.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_3.addWidget(self.buttonPreset15)

        self.buttonPreset30 = QPushButton(self.groupBoxPresets)
        self.buttonPreset30.setObjectName(u"buttonPreset30")
        self.buttonPreset30.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_3.addWidget(self.buttonPreset30)

        self.buttonPreset45 = QPushButton(self.groupBoxPresets)
        self.buttonPreset45.setObjectName(u"buttonPreset45")
        self.buttonPreset45.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_3.addWidget(self.buttonPreset45)

        self.groupBoxSetTimer = QGroupBox(Settings)
        self.groupBoxSetTimer.setObjectName(u"groupBoxSetTimer")
        self.groupBoxSetTimer.setGeometry(QRect(11, 1, 291, 127))
        self.lineEditCustomSession = QLineEdit(self.groupBoxSetTimer)
        self.lineEditCustomSession.setObjectName(u"lineEditCustomSession")
        self.lineEditCustomSession.setGeometry(QRect(140, 30, 125, 21))
        self.lineEditCustomSession.setFocusPolicy(Qt.ClickFocus)
        self.labeCustomSessionl = QLabel(self.groupBoxSetTimer)
        self.labeCustomSessionl.setObjectName(u"labeCustomSessionl")
        self.labeCustomSessionl.setGeometry(QRect(11, 31, 128, 16))
        self.lineEditCustomBreak = QLineEdit(self.groupBoxSetTimer)
        self.lineEditCustomBreak.setObjectName(u"lineEditCustomBreak")
        self.lineEditCustomBreak.setGeometry(QRect(140, 60, 125, 21))
        self.lineEditCustomBreak.setFocusPolicy(Qt.ClickFocus)
        self.labelCustomBreak = QLabel(self.groupBoxSetTimer)
        self.labelCustomBreak.setObjectName(u"labelCustomBreak")
        self.labelCustomBreak.setGeometry(QRect(11, 61, 115, 16))
        self.labelLongBreak = QLabel(self.groupBoxSetTimer)
        self.labelLongBreak.setObjectName(u"labelLongBreak")
        self.labelLongBreak.setGeometry(QRect(10, 90, 121, 16))
        self.lineEditCustomLongBreak = QLineEdit(self.groupBoxSetTimer)
        self.lineEditCustomLongBreak.setObjectName(u"lineEditCustomLongBreak")
        self.lineEditCustomLongBreak.setGeometry(QRect(139, 89, 125, 21))
        self.lineEditCustomLongBreak.setFocusPolicy(Qt.ClickFocus)
        self.groupBoxSettings = QGroupBox(Settings)
        self.groupBoxSettings.setObjectName(u"groupBoxSettings")
        self.groupBoxSettings.setGeometry(QRect(10, 130, 401, 151))
        self.checkBoxAutoStopSession = QCheckBox(self.groupBoxSettings)
        self.checkBoxAutoStopSession.setObjectName(u"checkBoxAutoStopSession")
        self.checkBoxAutoStopSession.setGeometry(QRect(10, 30, 181, 22))
        self.checkBoxAutoStopSession.setFocusPolicy(Qt.NoFocus)
        self.checkBoxAutoStopBreak = QCheckBox(self.groupBoxSettings)
        self.checkBoxAutoStopBreak.setObjectName(u"checkBoxAutoStopBreak")
        self.checkBoxAutoStopBreak.setGeometry(QRect(10, 50, 181, 22))
        self.checkBoxAutoStopBreak.setFocusPolicy(Qt.NoFocus)
        self.checkBoxSkipBreak = QCheckBox(self.groupBoxSettings)
        self.checkBoxSkipBreak.setObjectName(u"checkBoxSkipBreak")
        self.checkBoxSkipBreak.setGeometry(QRect(10, 70, 211, 22))
        self.checkBoxSkipBreak.setFocusPolicy(Qt.NoFocus)

        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Form", None))
        self.groupBoxPresets.setTitle(QCoreApplication.translate("Settings", u"Presets", None))
        self.buttonPreset15.setText(QCoreApplication.translate("Settings", u"15 minutes", None))
        self.buttonPreset30.setText(QCoreApplication.translate("Settings", u"30 minutes", None))
        self.buttonPreset45.setText(QCoreApplication.translate("Settings", u"45 minutes", None))
        self.groupBoxSetTimer.setTitle(QCoreApplication.translate("Settings", u"Set timer", None))
        self.lineEditCustomSession.setText("")
        self.labeCustomSessionl.setText(QCoreApplication.translate("Settings", u"Session time (min)", None))
        self.lineEditCustomBreak.setText("")
        self.labelCustomBreak.setText(QCoreApplication.translate("Settings", u"Break time (min)", None))
        self.labelLongBreak.setText(QCoreApplication.translate("Settings", u"Long break time (min)", None))
        self.lineEditCustomLongBreak.setText("")
        self.groupBoxSettings.setTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.checkBoxAutoStopSession.setText(QCoreApplication.translate("Settings", u"Auto stop session after break", None))
        self.checkBoxAutoStopBreak.setText(QCoreApplication.translate("Settings", u"Auto stop break after session", None))
        self.checkBoxSkipBreak.setText(QCoreApplication.translate("Settings", u"Skip break if you press stop button", None))
    # retranslateUi

