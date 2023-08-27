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
    QSizePolicy, QStatusBar, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(300, 276)
        font = QFont()
        font.setBold(False)
        Main.setFont(font)
        self.actionQuit = QAction(Main)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(Main)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionSettings = QAction(Main)
        self.actionSettings.setObjectName(u"actionSettings")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 230, 301, 20))
        self.progressBar.setValue(1)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 261, 195))
        self.labelTime = QLabel(self.groupBox)
        self.labelTime.setObjectName(u"labelTime")
        self.labelTime.setGeometry(QRect(60, 32, 134, 70))
        font1 = QFont()
        font1.setPointSize(40)
        font1.setBold(True)
        self.labelTime.setFont(font1)
        self.labelTime.setAlignment(Qt.AlignCenter)
        self.labelCounter = QLabel(self.groupBox)
        self.labelCounter.setObjectName(u"labelCounter")
        self.labelCounter.setGeometry(QRect(100, 110, 55, 16))
        self.buttonReset = QPushButton(self.groupBox)
        self.buttonReset.setObjectName(u"buttonReset")
        self.buttonReset.setGeometry(QRect(90, 160, 80, 24))
        self.buttonStart = QPushButton(self.groupBox)
        self.buttonStart.setObjectName(u"buttonStart")
        self.buttonStart.setGeometry(QRect(90, 130, 80, 24))
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 300, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"It is working time!", None))
        self.actionQuit.setText(QCoreApplication.translate("Main", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("Main", u"About", None))
        self.actionSettings.setText(QCoreApplication.translate("Main", u"Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("Main", u"Timer", None))
        self.labelTime.setText(QCoreApplication.translate("Main", u"00:00", None))
        self.labelCounter.setText(QCoreApplication.translate("Main", u"Counter: 0", None))
        self.buttonReset.setText(QCoreApplication.translate("Main", u"Reset", None))
        self.buttonStart.setText(QCoreApplication.translate("Main", u"Start", None))
        self.menuFile.setTitle(QCoreApplication.translate("Main", u"File", None))
    # retranslateUi

