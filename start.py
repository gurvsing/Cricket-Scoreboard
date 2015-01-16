# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created: Fri Jan 03 21:45:52 2014
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

class Ui_MainWindow001(object):
    def setupUi(self, MainWindow001):
        MainWindow001.setObjectName(_fromUtf8("MainWindow001"))
        MainWindow001.resize(800, 570)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/new/Users/Gurvinder/Desktop/indian-cricket-logo.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow001.setWindowIcon(icon)
        MainWindow001.setStatusTip(_fromUtf8(""))
        MainWindow001.setAutoFillBackground(False)
        MainWindow001.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow001)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.commandLinkButton001 = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton001.setGeometry(QtCore.QRect(40, 450, 501, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton001.setFont(font)
        self.commandLinkButton001.setAutoFillBackground(False)
        self.commandLinkButton001.setIcon(icon)
        self.commandLinkButton001.setObjectName(_fromUtf8("commandLinkButton001"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 30, 641, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Myriad Pro Cond"))
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("gridline-color: rgb(0, 0, 0);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 120, 321, 271))
        self.textBrowser.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(420, 250, 221, 201))
        self.frame.setStyleSheet(_fromUtf8("background-image: url(:/newPrefix/p2.jpg);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(520, 0, 221, 201))
        self.frame_2.setStyleSheet(_fromUtf8("background-image: url(:/newPrefix/p3.jpg);"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        MainWindow001.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow001)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuENTER_APP = QtGui.QMenu(self.menubar)
        self.menuENTER_APP.setObjectName(_fromUtf8("menuENTER_APP"))
        self.menuEXIT = QtGui.QMenu(self.menubar)
        self.menuEXIT.setObjectName(_fromUtf8("menuEXIT"))
        MainWindow001.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow001)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow001.setStatusBar(self.statusbar)
        self.menuEXIT.addSeparator()
        self.menubar.addAction(self.menuENTER_APP.menuAction())
        self.menubar.addAction(self.menuEXIT.menuAction())

        self.retranslateUi(MainWindow001)
        QtCore.QObject.connect(self.menubar, QtCore.SIGNAL(_fromUtf8("triggered(QAction*)")), self.commandLinkButton001.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow001)

    def retranslateUi(self, MainWindow001):
        MainWindow001.setWindowTitle(_translate("MainWindow001", "CRICKET APP", None))
        MainWindow001.setWhatsThis(_translate("MainWindow001", "<html><head/><body><p><img src=\":/new/Users/Gurvinder/Desktop/indian-cricket-logo.jpg\"/></p></body></html>", None))
        self.commandLinkButton001.setStatusTip(_translate("MainWindow001", "Click Here to Enter App", None))
        self.commandLinkButton001.setText(_translate("MainWindow001", "Click Here To Enter App......!!!", None))
        self.commandLinkButton001.setShortcut(_translate("MainWindow001", "Ctrl+S", None))
        self.label.setText(_translate("MainWindow001", "CRICKET       SCOREBORD", None))
        self.textBrowser.setHtml(_translate("MainWindow001", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Constantia\'; font-size:12pt; font-weight:600; color:#000000;\">WELCOME TO THE WORLD OF CRICKET………!!</span><span style=\" font-size:12pt; font-weight:600;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings 2\'; font-size:12pt; font-weight:600; color:#0bd0d9;\"></span><span style=\" font-family:\'Constantia\'; font-size:12pt; font-weight:600; color:#000000;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Constantia\'; font-size:12pt; font-weight:600; color:#000000;\">LEAVE BORING SCOREBOOK AND GET INTO ADVANCE TECHNOLOGY SCORING….</span><span style=\" font-size:12pt; font-weight:600;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Constantia\'; font-size:12pt; font-weight:600; color:#000000;\">THIS APP WILL HELP YOU TO CALCULATE </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Constantia\'; font-size:12pt; font-weight:600; color:#000000;\">SCORES,DISPLAY OF VARIETIES OF SCORECARD ND LOTS MORE</span><span style=\" font-size:12pt; font-weight:600;\"> </span></p></body></html>", None))
        self.menuENTER_APP.setTitle(_translate("MainWindow001", "ENTER APP", None))
        self.menuEXIT.setTitle(_translate("MainWindow001", "EXIT", None))

import pro
