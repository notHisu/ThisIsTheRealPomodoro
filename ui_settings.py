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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(312, 471)
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        Settings.setFont(font)
        self.layoutWidget = QWidget(Settings)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 291, 461))
        self.layoutWidget.setFocusPolicy(Qt.ClickFocus)
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameSetTimer = QFrame(self.layoutWidget)
        self.frameSetTimer.setObjectName(u"frameSetTimer")
        self.frameSetTimer.setFocusPolicy(Qt.ClickFocus)
        self.frameSetTimer.setFrameShape(QFrame.Box)
        self.lineEditCustomSession = QLineEdit(self.frameSetTimer)
        self.lineEditCustomSession.setObjectName(u"lineEditCustomSession")
        self.lineEditCustomSession.setGeometry(QRect(140, 30, 125, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditCustomSession.sizePolicy().hasHeightForWidth())
        self.lineEditCustomSession.setSizePolicy(sizePolicy)
        self.lineEditCustomSession.setFocusPolicy(Qt.ClickFocus)
        self.labeCustomSessionl = QLabel(self.frameSetTimer)
        self.labeCustomSessionl.setObjectName(u"labeCustomSessionl")
        self.labeCustomSessionl.setGeometry(QRect(11, 31, 128, 16))
        self.labeCustomSessionl.setFocusPolicy(Qt.ClickFocus)
        self.lineEditCustomBreak = QLineEdit(self.frameSetTimer)
        self.lineEditCustomBreak.setObjectName(u"lineEditCustomBreak")
        self.lineEditCustomBreak.setGeometry(QRect(140, 60, 125, 21))
        self.lineEditCustomBreak.setFocusPolicy(Qt.ClickFocus)
        self.labelCustomBreak = QLabel(self.frameSetTimer)
        self.labelCustomBreak.setObjectName(u"labelCustomBreak")
        self.labelCustomBreak.setGeometry(QRect(11, 61, 115, 16))
        self.labelCustomBreak.setFocusPolicy(Qt.ClickFocus)
        self.labelLongBreak = QLabel(self.frameSetTimer)
        self.labelLongBreak.setObjectName(u"labelLongBreak")
        self.labelLongBreak.setGeometry(QRect(10, 90, 121, 16))
        self.labelLongBreak.setFocusPolicy(Qt.ClickFocus)
        self.lineEditCustomLongBreak = QLineEdit(self.frameSetTimer)
        self.lineEditCustomLongBreak.setObjectName(u"lineEditCustomLongBreak")
        self.lineEditCustomLongBreak.setGeometry(QRect(139, 89, 125, 21))
        sizePolicy.setHeightForWidth(self.lineEditCustomLongBreak.sizePolicy().hasHeightForWidth())
        self.lineEditCustomLongBreak.setSizePolicy(sizePolicy)
        self.lineEditCustomLongBreak.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout_2.addWidget(self.frameSetTimer)

        self.framePresets = QFrame(self.layoutWidget)
        self.framePresets.setObjectName(u"framePresets")
        self.framePresets.setFocusPolicy(Qt.ClickFocus)
        self.framePresets.setFrameShape(QFrame.Box)
        self.verticalLayout_3 = QVBoxLayout(self.framePresets)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.buttonPreset15 = QPushButton(self.framePresets)
        self.buttonPreset15.setObjectName(u"buttonPreset15")
        self.buttonPreset15.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout_3.addWidget(self.buttonPreset15)

        self.buttonPreset30 = QPushButton(self.framePresets)
        self.buttonPreset30.setObjectName(u"buttonPreset30")
        self.buttonPreset30.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout_3.addWidget(self.buttonPreset30)

        self.buttonPreset45 = QPushButton(self.framePresets)
        self.buttonPreset45.setObjectName(u"buttonPreset45")
        self.buttonPreset45.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout_3.addWidget(self.buttonPreset45)


        self.verticalLayout_2.addWidget(self.framePresets)

        self.frameSettings = QFrame(self.layoutWidget)
        self.frameSettings.setObjectName(u"frameSettings")
        self.frameSettings.setFocusPolicy(Qt.ClickFocus)
        self.frameSettings.setFrameShape(QFrame.Box)
        self.checkBoxAutoStopSession = QCheckBox(self.frameSettings)
        self.checkBoxAutoStopSession.setObjectName(u"checkBoxAutoStopSession")
        self.checkBoxAutoStopSession.setGeometry(QRect(10, 30, 181, 22))
        self.checkBoxAutoStopSession.setFocusPolicy(Qt.ClickFocus)
        self.checkBoxAutoStopBreak = QCheckBox(self.frameSettings)
        self.checkBoxAutoStopBreak.setObjectName(u"checkBoxAutoStopBreak")
        self.checkBoxAutoStopBreak.setGeometry(QRect(10, 50, 181, 22))
        self.checkBoxAutoStopBreak.setFocusPolicy(Qt.ClickFocus)
        self.checkBoxSkipBreak = QCheckBox(self.frameSettings)
        self.checkBoxSkipBreak.setObjectName(u"checkBoxSkipBreak")
        self.checkBoxSkipBreak.setGeometry(QRect(10, 70, 211, 22))
        self.checkBoxSkipBreak.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout_2.addWidget(self.frameSettings)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Form", None))
        self.lineEditCustomSession.setText("")
        self.labeCustomSessionl.setText(QCoreApplication.translate("Settings", u"Session time (min)", None))
        self.lineEditCustomBreak.setText("")
        self.labelCustomBreak.setText(QCoreApplication.translate("Settings", u"Break time (min)", None))
        self.labelLongBreak.setText(QCoreApplication.translate("Settings", u"Long break time (min)", None))
        self.lineEditCustomLongBreak.setText("")
        self.buttonPreset15.setText(QCoreApplication.translate("Settings", u"15 minutes", None))
        self.buttonPreset30.setText(QCoreApplication.translate("Settings", u"30 minutes", None))
        self.buttonPreset45.setText(QCoreApplication.translate("Settings", u"45 minutes", None))
        self.checkBoxAutoStopSession.setText(QCoreApplication.translate("Settings", u"Auto stop session after break", None))
        self.checkBoxAutoStopBreak.setText(QCoreApplication.translate("Settings", u"Auto stop break after session", None))
        self.checkBoxSkipBreak.setText(QCoreApplication.translate("Settings", u"Skip break if you press stop button", None))
    # retranslateUi

