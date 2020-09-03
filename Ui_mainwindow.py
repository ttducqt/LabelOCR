# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(412, 283)
        self.horizontalLayoutWidget = QWidget(mainWindow)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 210, 391, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.backButton = QPushButton(self.horizontalLayoutWidget)
        self.backButton.setObjectName(u"backButton")

        self.horizontalLayout.addWidget(self.backButton)

        self.delButton = QPushButton(self.horizontalLayoutWidget)
        self.delButton.setObjectName(u"delButton")

        self.horizontalLayout.addWidget(self.delButton)

        self.nextButton = QPushButton(self.horizontalLayoutWidget)
        self.nextButton.setObjectName(u"nextButton")

        self.horizontalLayout.addWidget(self.nextButton)

        self.frame = QLabel(mainWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 371, 141))
        self.frame.setAlignment(Qt.AlignCenter)
        self.labelBox = QLineEdit(mainWindow)
        self.labelBox.setObjectName(u"labelBox")
        self.labelBox.setGeometry(QRect(10, 170, 391, 25))
        self.idxBox = QLineEdit(mainWindow)
        self.idxBox.setObjectName(u"idxBox")
        self.idxBox.setGeometry(QRect(10, 130, 41, 25))
        self.saveButton = QPushButton(mainWindow)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(10, 250, 391, 25))
        self.gotoButton = QPushButton(mainWindow)
        self.gotoButton.setObjectName(u"gotoButton")
        self.gotoButton.setGeometry(QRect(60, 130, 51, 25))

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"mainWindow", None))
        self.backButton.setText(QCoreApplication.translate("mainWindow", u"Back", None))
        self.delButton.setText(QCoreApplication.translate("mainWindow", u"Delete this image", None))
        self.nextButton.setText(QCoreApplication.translate("mainWindow", u"Next", None))
        self.frame.setText("")
        self.saveButton.setText(QCoreApplication.translate("mainWindow", u"Save", None))
        self.gotoButton.setText(QCoreApplication.translate("mainWindow", u"Goto", None))
    # retranslateUi

