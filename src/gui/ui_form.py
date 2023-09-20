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
        Main.resize(300, 384)
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
        self.actionSpotify = QAction(Main)
        self.actionSpotify.setObjectName(u"actionSpotify")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTime = QLabel(self.frame_2)
        self.labelTime.setObjectName(u"labelTime")
        font1 = QFont()
        font1.setPointSize(40)
        font1.setBold(True)
        self.labelTime.setFont(font1)
        self.labelTime.setFocusPolicy(Qt.ClickFocus)
        self.labelTime.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelTime, 0, Qt.AlignHCenter)

        self.labelCounter = QLabel(self.frame_2)
        self.labelCounter.setObjectName(u"labelCounter")
        self.labelCounter.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout.addWidget(self.labelCounter, 0, Qt.AlignHCenter)

        self.labelQuote = QLabel(self.frame_2)
        self.labelQuote.setObjectName(u"labelQuote")
        self.labelQuote.setMaximumSize(QSize(300, 300))
        font2 = QFont()
        font2.setBold(False)
        font2.setItalic(True)
        self.labelQuote.setFont(font2)
        self.labelQuote.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout.addWidget(self.labelQuote, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.buttonStart = QPushButton(self.frame)
        self.buttonStart.setObjectName(u"buttonStart")
        sizePolicy.setHeightForWidth(self.buttonStart.sizePolicy().hasHeightForWidth())
        self.buttonStart.setSizePolicy(sizePolicy)
        self.buttonStart.setMaximumSize(QSize(120, 32))
        self.buttonStart.setFocusPolicy(Qt.ClickFocus)
        self.buttonStart.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.buttonStart)

        self.buttonReset = QPushButton(self.frame)
        self.buttonReset.setObjectName(u"buttonReset")
        sizePolicy.setHeightForWidth(self.buttonReset.sizePolicy().hasHeightForWidth())
        self.buttonReset.setSizePolicy(sizePolicy)
        self.buttonReset.setMaximumSize(QSize(120, 32))
        self.buttonReset.setFocusPolicy(Qt.ClickFocus)
        self.buttonReset.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.buttonReset)

        self.buttonQuote = QPushButton(self.frame)
        self.buttonQuote.setObjectName(u"buttonQuote")
        sizePolicy.setHeightForWidth(self.buttonQuote.sizePolicy().hasHeightForWidth())
        self.buttonQuote.setSizePolicy(sizePolicy)
        self.buttonQuote.setMaximumSize(QSize(120, 32))
        self.buttonQuote.setFocusPolicy(Qt.ClickFocus)
        self.buttonQuote.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.buttonQuote)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.progressBar = QProgressBar(self.frame_4)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setFocusPolicy(Qt.ClickFocus)
        self.progressBar.setValue(1)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(False)

        self.verticalLayout_4.addWidget(self.progressBar)


        self.verticalLayout_2.addWidget(self.frame_4)

        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 300, 37))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionSpotify)
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
        self.actionSpotify.setText(QCoreApplication.translate("Main", u"Spotify", None))
        self.labelTime.setText(QCoreApplication.translate("Main", u"00:00", None))
        self.labelCounter.setText(QCoreApplication.translate("Main", u"Counter: 0", None))
        self.labelQuote.setText(QCoreApplication.translate("Main", u"Quote", None))
        self.buttonStart.setText(QCoreApplication.translate("Main", u"Start", None))
        self.buttonReset.setText(QCoreApplication.translate("Main", u"Reset", None))
        self.buttonQuote.setText(QCoreApplication.translate("Main", u"Random Quotes", None))
        self.menuFile.setTitle(QCoreApplication.translate("Main", u"File", None))
    # retranslateUi

