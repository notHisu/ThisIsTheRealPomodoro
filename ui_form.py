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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(283, 299)
        font = QFont()
        font.setBold(False)
        Main.setFont(font)
        self.actionQuit = QAction(Main)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(Main)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionSettings = QAction(Main)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionTask = QAction(Main)
        self.actionTask.setObjectName(u"actionTask")
        self.actionCalendar = QAction(Main)
        self.actionCalendar.setObjectName(u"actionCalendar")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 261, 251))
        self.verticalLayoutWidget.setFocusPolicy(Qt.ClickFocus)
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFocusPolicy(Qt.ClickFocus)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 40, 136, 156))
        self.layoutWidget.setFocusPolicy(Qt.ClickFocus)
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelTime = QLabel(self.layoutWidget)
        self.labelTime.setObjectName(u"labelTime")
        font1 = QFont()
        font1.setPointSize(40)
        font1.setBold(True)
        self.labelTime.setFont(font1)
        self.labelTime.setFocusPolicy(Qt.ClickFocus)
        self.labelTime.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelTime)

        self.labelCounter = QLabel(self.layoutWidget)
        self.labelCounter.setObjectName(u"labelCounter")
        self.labelCounter.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout.addWidget(self.labelCounter)

        self.buttonStart = QPushButton(self.layoutWidget)
        self.buttonStart.setObjectName(u"buttonStart")
        self.buttonStart.setFocusPolicy(Qt.ClickFocus)
        self.buttonStart.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.buttonStart)

        self.buttonReset = QPushButton(self.layoutWidget)
        self.buttonReset.setObjectName(u"buttonReset")
        self.buttonReset.setFocusPolicy(Qt.ClickFocus)
        self.buttonReset.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.buttonReset)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 0, 100, 32))

        self.verticalLayout_2.addWidget(self.frame)

        self.progressBar = QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setFocusPolicy(Qt.ClickFocus)
        self.progressBar.setValue(1)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(False)

        self.verticalLayout_2.addWidget(self.progressBar)

        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 283, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionTask)
        self.menuFile.addAction(self.actionCalendar)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"It is working time!", None))
        self.actionQuit.setText(QCoreApplication.translate("Main", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("Main", u"About", None))
        self.actionSettings.setText(QCoreApplication.translate("Main", u"Settings", None))
        self.actionTask.setText(QCoreApplication.translate("Main", u"Task", None))
        self.actionCalendar.setText(QCoreApplication.translate("Main", u"Calendar", None))
        self.labelTime.setText(QCoreApplication.translate("Main", u"00:00", None))
        self.labelCounter.setText(QCoreApplication.translate("Main", u"Counter: 0", None))
        self.buttonStart.setText(QCoreApplication.translate("Main", u"Start", None))
        self.buttonReset.setText(QCoreApplication.translate("Main", u"Reset", None))
        self.pushButton.setText(QCoreApplication.translate("Main", u"PushButton", None))
        self.menuFile.setTitle(QCoreApplication.translate("Main", u"File", None))
    # retranslateUi

