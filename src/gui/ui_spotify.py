# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spotify_player.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Spotify(object):
    def setupUi(self, Spotify):
        if not Spotify.objectName():
            Spotify.setObjectName(u"Spotify")
        Spotify.resize(800, 500)
        Spotify.setMinimumSize(QSize(800, 500))
        self.verticalLayout_2 = QVBoxLayout(Spotify)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Spotify)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.webEngineView = QWebEngineView(self.frame)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.verticalLayout.addWidget(self.webEngineView)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Spotify)

        QMetaObject.connectSlotsByName(Spotify)
    # setupUi

    def retranslateUi(self, Spotify):
        Spotify.setWindowTitle(QCoreApplication.translate("Spotify", u"Spotify Player", None))
    # retranslateUi

