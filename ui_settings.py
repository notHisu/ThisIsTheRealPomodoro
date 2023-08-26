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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGroupBox,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(419, 716)
        Settings.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(Settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.minutes = QGroupBox(Settings)
        self.minutes.setObjectName(u"minutes")
        self.formLayout = QFormLayout(self.minutes)
        self.formLayout.setObjectName(u"formLayout")
        self.stateTomatoLabel = QLabel(self.minutes)
        self.stateTomatoLabel.setObjectName(u"stateTomatoLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.stateTomatoLabel)

        self.stateTomato = QSpinBox(self.minutes)
        self.stateTomato.setObjectName(u"stateTomato")
        self.stateTomato.setMinimum(1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.stateTomato)

        self.stateBreakLabel = QLabel(self.minutes)
        self.stateBreakLabel.setObjectName(u"stateBreakLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.stateBreakLabel)

        self.stateBreak = QSpinBox(self.minutes)
        self.stateBreak.setObjectName(u"stateBreak")
        self.stateBreak.setMinimum(1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.stateBreak)

        self.stateLongBreakLabel = QLabel(self.minutes)
        self.stateLongBreakLabel.setObjectName(u"stateLongBreakLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.stateLongBreakLabel)

        self.stateLongBreak = QSpinBox(self.minutes)
        self.stateLongBreak.setObjectName(u"stateLongBreak")
        self.stateLongBreak.setMinimum(1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.stateLongBreak)

        self.repeatLabel = QLabel(self.minutes)
        self.repeatLabel.setObjectName(u"repeatLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.repeatLabel)

        self.repeat = QSpinBox(self.minutes)
        self.repeat.setObjectName(u"repeat")
        self.repeat.setMinimum(1)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.repeat)


        self.verticalLayout.addWidget(self.minutes)

        self.checkboxes = QGroupBox(Settings)
        self.checkboxes.setObjectName(u"checkboxes")
        self.formLayout_2 = QFormLayout(self.checkboxes)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.useSystemFont = QCheckBox(self.checkboxes)
        self.useSystemFont.setObjectName(u"useSystemFont")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.useSystemFont)

        self.notification = QCheckBox(self.checkboxes)
        self.notification.setObjectName(u"notification")
        self.notification.setLayoutDirection(Qt.LeftToRight)
        self.notification.setAutoRepeat(False)
        self.notification.setAutoExclusive(False)
        self.notification.setTristate(False)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.notification)

        self.interrupt = QCheckBox(self.checkboxes)
        self.interrupt.setObjectName(u"interrupt")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.interrupt.sizePolicy().hasHeightForWidth())
        self.interrupt.setSizePolicy(sizePolicy)
        self.interrupt.setLayoutDirection(Qt.LeftToRight)
        self.interrupt.setAutoFillBackground(False)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.interrupt)

        self.autoStopTomato = QCheckBox(self.checkboxes)
        self.autoStopTomato.setObjectName(u"autoStopTomato")
        self.autoStopTomato.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.autoStopTomato)

        self.autoStopBreak = QCheckBox(self.checkboxes)
        self.autoStopBreak.setObjectName(u"autoStopBreak")
        self.autoStopBreak.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.autoStopBreak)

        self.switchToTomatoOnAbort = QCheckBox(self.checkboxes)
        self.switchToTomatoOnAbort.setObjectName(u"switchToTomatoOnAbort")
        self.switchToTomatoOnAbort.setMinimumSize(QSize(0, 0))
        self.switchToTomatoOnAbort.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.switchToTomatoOnAbort)

        self.label = QLabel(self.checkboxes)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(7, QFormLayout.FieldRole, self.verticalSpacer)

        self.showTrayIcon = QCheckBox(self.checkboxes)
        self.showTrayIcon.setObjectName(u"showTrayIcon")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.showTrayIcon)


        self.verticalLayout.addWidget(self.checkboxes)

        self.commands = QGroupBox(Settings)
        self.commands.setObjectName(u"commands")
        self.formLayout_3 = QFormLayout(self.commands)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.afterStartLabel = QLabel(self.commands)
        self.afterStartLabel.setObjectName(u"afterStartLabel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.afterStartLabel)

        self.afterStartCommand = QLineEdit(self.commands)
        self.afterStartCommand.setObjectName(u"afterStartCommand")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.afterStartCommand)

        self.afterStopLabel = QLabel(self.commands)
        self.afterStopLabel.setObjectName(u"afterStopLabel")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.afterStopLabel)

        self.afterStopCommand = QLineEdit(self.commands)
        self.afterStopCommand.setObjectName(u"afterStopCommand")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.afterStopCommand)

        self.macrosHelp1 = QLabel(self.commands)
        self.macrosHelp1.setObjectName(u"macrosHelp1")

        self.formLayout_3.setWidget(4, QFormLayout.SpanningRole, self.macrosHelp1)

        self.macrosHelp2 = QLabel(self.commands)
        self.macrosHelp2.setObjectName(u"macrosHelp2")

        self.formLayout_3.setWidget(5, QFormLayout.SpanningRole, self.macrosHelp2)

        self.macrosHelp3 = QLabel(self.commands)
        self.macrosHelp3.setObjectName(u"macrosHelp3")

        self.formLayout_3.setWidget(6, QFormLayout.SpanningRole, self.macrosHelp3)

        self.onTomatoLabel = QLabel(self.commands)
        self.onTomatoLabel.setObjectName(u"onTomatoLabel")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.onTomatoLabel)

        self.onBreakLabel = QLabel(self.commands)
        self.onBreakLabel.setObjectName(u"onBreakLabel")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.onBreakLabel)

        self.onTomatoCommand = QLineEdit(self.commands)
        self.onTomatoCommand.setObjectName(u"onTomatoCommand")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.onTomatoCommand)

        self.onBreakCommand = QLineEdit(self.commands)
        self.onBreakCommand.setObjectName(u"onBreakCommand")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.onBreakCommand)


        self.verticalLayout.addWidget(self.commands)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.minutes.setTitle("")
        self.stateTomatoLabel.setText(QCoreApplication.translate("Settings", u"Tomato time (min)", None))
        self.stateBreakLabel.setText(QCoreApplication.translate("Settings", u"Break time (min)", None))
        self.stateLongBreakLabel.setText(QCoreApplication.translate("Settings", u"Long break time (min)", None))
        self.repeatLabel.setText(QCoreApplication.translate("Settings", u"Long break after (tomatoes)", None))
        self.checkboxes.setTitle("")
        self.useSystemFont.setText(QCoreApplication.translate("Settings", u"Use system font*", None))
        self.notification.setText(QCoreApplication.translate("Settings", u"Sound notification", None))
        self.interrupt.setText(QCoreApplication.translate("Settings", u"Interrupt me", None))
        self.autoStopTomato.setText(QCoreApplication.translate("Settings", u"Auto stop tomato after break", None))
        self.autoStopBreak.setText(QCoreApplication.translate("Settings", u"Auto stop break after tomato", None))
        self.switchToTomatoOnAbort.setText(QCoreApplication.translate("Settings", u"Skip break if you press stop button", None))
        self.label.setText(QCoreApplication.translate("Settings", u"* Need restart", None))
        self.showTrayIcon.setText(QCoreApplication.translate("Settings", u"Show tray icon*", None))
        self.commands.setTitle(QCoreApplication.translate("Settings", u"Execute custom commands:", None))
        self.afterStartLabel.setText(QCoreApplication.translate("Settings", u"On start", None))
        self.afterStopLabel.setText(QCoreApplication.translate("Settings", u"On stop", None))
        self.macrosHelp1.setText(QCoreApplication.translate("Settings", u"You can use macros to pass information to the command:", None))
        self.macrosHelp2.setText(QCoreApplication.translate("Settings", u"{tomatoes} - number of completed tomatoes", None))
        self.macrosHelp3.setText(QCoreApplication.translate("Settings", u"{state} - current state (\"tomato\", \"break\", \"long_break\")", None))
        self.onTomatoLabel.setText(QCoreApplication.translate("Settings", u"On tomato", None))
        self.onBreakLabel.setText(QCoreApplication.translate("Settings", u"On break", None))
    # retranslateUi

