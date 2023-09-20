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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(400, 402)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Settings.sizePolicy().hasHeightForWidth())
        Settings.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        Settings.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(Settings)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(Settings)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labeCustomSessionl = QLabel(self.frame)
        self.labeCustomSessionl.setObjectName(u"labeCustomSessionl")
        sizePolicy.setHeightForWidth(self.labeCustomSessionl.sizePolicy().hasHeightForWidth())
        self.labeCustomSessionl.setSizePolicy(sizePolicy)
        self.labeCustomSessionl.setMinimumSize(QSize(0, 0))
        self.labeCustomSessionl.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout.addWidget(self.labeCustomSessionl)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer = QSpacerItem(20, 0, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lineEditCustomSession = QLineEdit(self.frame)
        self.lineEditCustomSession.setObjectName(u"lineEditCustomSession")
        self.lineEditCustomSession.setMinimumSize(QSize(200, 0))
        self.lineEditCustomSession.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.lineEditCustomSession)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelCustomBreak = QLabel(self.frame)
        self.labelCustomBreak.setObjectName(u"labelCustomBreak")
        self.labelCustomBreak.setMinimumSize(QSize(100, 0))
        self.labelCustomBreak.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.labelCustomBreak)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.lineEditCustomBreak = QLineEdit(self.frame)
        self.lineEditCustomBreak.setObjectName(u"lineEditCustomBreak")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEditCustomBreak.sizePolicy().hasHeightForWidth())
        self.lineEditCustomBreak.setSizePolicy(sizePolicy1)
        self.lineEditCustomBreak.setMinimumSize(QSize(200, 0))
        self.lineEditCustomBreak.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_2.addWidget(self.lineEditCustomBreak)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelBreakAppPath = QLabel(self.frame)
        self.labelBreakAppPath.setObjectName(u"labelBreakAppPath")
        self.labelBreakAppPath.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_4.addWidget(self.labelBreakAppPath)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.lineEditBreakAppPath = QLineEdit(self.frame)
        self.lineEditBreakAppPath.setObjectName(u"lineEditBreakAppPath")
        sizePolicy1.setHeightForWidth(self.lineEditBreakAppPath.sizePolicy().hasHeightForWidth())
        self.lineEditBreakAppPath.setSizePolicy(sizePolicy1)
        self.lineEditBreakAppPath.setMinimumSize(QSize(200, 0))
        self.lineEditBreakAppPath.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_4.addWidget(self.lineEditBreakAppPath)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelLongBreak = QLabel(self.frame)
        self.labelLongBreak.setObjectName(u"labelLongBreak")
        self.labelLongBreak.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.labelLongBreak)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.lineEditCustomLongBreak = QLineEdit(self.frame)
        self.lineEditCustomLongBreak.setObjectName(u"lineEditCustomLongBreak")
        sizePolicy1.setHeightForWidth(self.lineEditCustomLongBreak.sizePolicy().hasHeightForWidth())
        self.lineEditCustomLongBreak.setSizePolicy(sizePolicy1)
        self.lineEditCustomLongBreak.setMinimumSize(QSize(200, 0))
        self.lineEditCustomLongBreak.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_3.addWidget(self.lineEditCustomLongBreak)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(Settings)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBoxSkipBreak = QCheckBox(self.frame_2)
        self.checkBoxSkipBreak.setObjectName(u"checkBoxSkipBreak")
        self.checkBoxSkipBreak.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout.addWidget(self.checkBoxSkipBreak)

        self.checkBoxAutoStopSession = QCheckBox(self.frame_2)
        self.checkBoxAutoStopSession.setObjectName(u"checkBoxAutoStopSession")
        self.checkBoxAutoStopSession.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout.addWidget(self.checkBoxAutoStopSession)

        self.checkBoxAutoStopBreak = QCheckBox(self.frame_2)
        self.checkBoxAutoStopBreak.setObjectName(u"checkBoxAutoStopBreak")
        self.checkBoxAutoStopBreak.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout.addWidget(self.checkBoxAutoStopBreak)

        self.checkBoxFocusMode = QCheckBox(self.frame_2)
        self.checkBoxFocusMode.setObjectName(u"checkBoxFocusMode")
        self.checkBoxFocusMode.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout.addWidget(self.checkBoxFocusMode)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(Settings)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.buttonPreset15 = QPushButton(self.frame_3)
        self.buttonPreset15.setObjectName(u"buttonPreset15")
        self.buttonPreset15.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_2.addWidget(self.buttonPreset15)

        self.buttonPreset30 = QPushButton(self.frame_3)
        self.buttonPreset30.setObjectName(u"buttonPreset30")
        self.buttonPreset30.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_2.addWidget(self.buttonPreset30)

        self.buttonPreset45 = QPushButton(self.frame_3)
        self.buttonPreset45.setObjectName(u"buttonPreset45")
        self.buttonPreset45.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_2.addWidget(self.buttonPreset45)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Form", None))
        self.labeCustomSessionl.setText(QCoreApplication.translate("Settings", u"Session time (min)", None))
        self.lineEditCustomSession.setText("")
        self.labelCustomBreak.setText(QCoreApplication.translate("Settings", u"Break time (min)", None))
        self.lineEditCustomBreak.setText("")
        self.labelBreakAppPath.setText(QCoreApplication.translate("Settings", u"Break app path", None))
        self.lineEditBreakAppPath.setText("")
        self.labelLongBreak.setText(QCoreApplication.translate("Settings", u"Long break time (min)", None))
        self.lineEditCustomLongBreak.setText("")
        self.checkBoxSkipBreak.setText(QCoreApplication.translate("Settings", u"Skip break if you press stop button", None))
        self.checkBoxAutoStopSession.setText(QCoreApplication.translate("Settings", u"Auto stop session after break", None))
        self.checkBoxAutoStopBreak.setText(QCoreApplication.translate("Settings", u"Auto stop break after session", None))
        self.checkBoxFocusMode.setText(QCoreApplication.translate("Settings", u"Focus mode", None))
        self.buttonPreset15.setText(QCoreApplication.translate("Settings", u"15 minutes", None))
        self.buttonPreset30.setText(QCoreApplication.translate("Settings", u"30 minutes", None))
        self.buttonPreset45.setText(QCoreApplication.translate("Settings", u"45 minutes", None))
    # retranslateUi

