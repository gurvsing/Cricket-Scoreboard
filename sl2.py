# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sl2.ui'
#
# Created: Fri Jan 03 21:42:59 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow02(object):
    def setupUi(self, MainWindow02):
        MainWindow02.setObjectName(_fromUtf8("MainWindow02"))
        MainWindow02.resize(801, 579)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/new/Users/Gurvinder/Desktop/indian-cricket-logo.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow02.setWindowIcon(icon)
        MainWindow02.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(MainWindow02)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(290, 180, 20, 231))
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(300, 180, 251, 231))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.line_5 = QtGui.QFrame(self.layoutWidget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout.addWidget(self.line_5)
        self.commandLinkButton01 = QtGui.QCommandLinkButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton01.setFont(font)
        self.commandLinkButton01.setObjectName(_fromUtf8("commandLinkButton01"))
        self.verticalLayout.addWidget(self.commandLinkButton01)
        self.line_3 = QtGui.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.commandLinkButton02 = QtGui.QCommandLinkButton(self.layoutWidget)
        self.commandLinkButton02.setObjectName(_fromUtf8("commandLinkButton02"))
        self.verticalLayout.addWidget(self.commandLinkButton02)
        self.line_2 = QtGui.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.commandLinkButton03 = QtGui.QCommandLinkButton(self.layoutWidget)
        self.commandLinkButton03.setObjectName(_fromUtf8("commandLinkButton03"))
        self.verticalLayout.addWidget(self.commandLinkButton03)
        self.line_4 = QtGui.QFrame(self.layoutWidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout.addWidget(self.line_4)
        self.commandLinkButton04 = QtGui.QCommandLinkButton(self.layoutWidget)
        self.commandLinkButton04.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));"))
        self.commandLinkButton04.setObjectName(_fromUtf8("commandLinkButton04"))
        self.verticalLayout.addWidget(self.commandLinkButton04)
        self.line_6 = QtGui.QFrame(self.layoutWidget)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout.addWidget(self.line_6)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 40, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));"))
        self.label.setObjectName(_fromUtf8("label"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 110, 291, 381))
        self.frame.setStyleSheet(_fromUtf8("\n"
"background-image: url(:/newPrefix/144048.2.jpg);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(570, 170, 221, 231))
        self.frame_2.setStyleSheet(_fromUtf8("background-image: url(:/newPrefix/images (2).jpg);"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.line_8 = QtGui.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(540, 180, 20, 231))
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(633, 50, 91, 51))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        MainWindow02.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow02)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow02.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow02)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow02.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow02)
        QtCore.QMetaObject.connectSlotsByName(MainWindow02)

    def retranslateUi(self, MainWindow02):
        MainWindow02.setWindowTitle(_translate("MainWindow02", "CRICKET APP", None))
        self.commandLinkButton01.setText(_translate("MainWindow02", "Start   Game", None))
        self.commandLinkButton02.setText(_translate("MainWindow02", "About Developers", None))
        self.commandLinkButton03.setText(_translate("MainWindow02", "About Application", None))
        self.commandLinkButton04.setText(_translate("MainWindow02", "EXIT", None))
        self.label.setText(_translate("MainWindow02", "Welcome to World of Cricket", None))

import pro
