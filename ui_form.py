# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(478, 436)
        self.actionQuit = QAction(Main)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(Main)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(100, 220, 251, 20))
        self.progressBar.setValue(1)
        self.groupBoxPresets = QGroupBox(self.centralwidget)
        self.groupBoxPresets.setObjectName(u"groupBoxPresets")
        self.groupBoxPresets.setGeometry(QRect(230, 70, 127, 137))
        self.verticalLayout_3 = QVBoxLayout(self.groupBoxPresets)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.buttonPreset15 = QPushButton(self.groupBoxPresets)
        self.buttonPreset15.setObjectName(u"buttonPreset15")

        self.verticalLayout_3.addWidget(self.buttonPreset15)

        self.buttonPreset30 = QPushButton(self.groupBoxPresets)
        self.buttonPreset30.setObjectName(u"buttonPreset30")

        self.verticalLayout_3.addWidget(self.buttonPreset30)

        self.buttonPreset45 = QPushButton(self.groupBoxPresets)
        self.buttonPreset45.setObjectName(u"buttonPreset45")

        self.verticalLayout_3.addWidget(self.buttonPreset45)

        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 80, 101, 131))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelCounter = QLabel(self.layoutWidget)
        self.labelCounter.setObjectName(u"labelCounter")

        self.verticalLayout_2.addWidget(self.labelCounter)

        self.labelTime = QLabel(self.layoutWidget)
        self.labelTime.setObjectName(u"labelTime")

        self.verticalLayout_2.addWidget(self.labelTime)

        self.buttonStart = QPushButton(self.layoutWidget)
        self.buttonStart.setObjectName(u"buttonStart")

        self.verticalLayout_2.addWidget(self.buttonStart)

        self.buttonReset = QPushButton(self.layoutWidget)
        self.buttonReset.setObjectName(u"buttonReset")

        self.verticalLayout_2.addWidget(self.buttonReset)

        self.buttonSetting = QPushButton(self.centralwidget)
        self.buttonSetting.setObjectName(u"buttonSetting")
        self.buttonSetting.setGeometry(QRect(370, 0, 100, 32))
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 478, 37))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Main", None))
        self.actionQuit.setText(QCoreApplication.translate("Main", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("Main", u"About", None))
        self.groupBoxPresets.setTitle(QCoreApplication.translate("Main", u"Presets", None))
        self.buttonPreset15.setText(QCoreApplication.translate("Main", u"15 minutes", None))
        self.buttonPreset30.setText(QCoreApplication.translate("Main", u"30 minutes", None))
        self.buttonPreset45.setText(QCoreApplication.translate("Main", u"45 minutes", None))
        self.labelCounter.setText(QCoreApplication.translate("Main", u"Counter: 0", None))
        self.labelTime.setText(QCoreApplication.translate("Main", u"00:00", None))
        self.buttonStart.setText(QCoreApplication.translate("Main", u"Start", None))
        self.buttonReset.setText(QCoreApplication.translate("Main", u"Reset", None))
        self.buttonSetting.setText(QCoreApplication.translate("Main", u"Settings", None))
        self.menuFile.setTitle(QCoreApplication.translate("Main", u"File", None))
    # retranslateUi

