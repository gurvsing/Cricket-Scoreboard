# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Wed Feb 13 16:53:39 2013
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(799, 564)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton01 = QtGui.QPushButton(self.centralwidget)
        self.pushButton01.setGeometry(QtCore.QRect(210, 280, 75, 23))
        self.pushButton01.setObjectName(_fromUtf8("pushButton01"))
        self.label01 = QtGui.QLabel(self.centralwidget)
        self.label01.setGeometry(QtCore.QRect(100, 100, 46, 13))
        self.label01.setObjectName(_fromUtf8("label01"))
        self.lineEdit01 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit01.setGeometry(QtCore.QRect(100, 140, 113, 20))
        self.lineEdit01.setObjectName(_fromUtf8("lineEdit01"))
        self.radioButton01 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton01.setGeometry(QtCore.QRect(340, 180, 82, 17))
        self.radioButton01.setObjectName(_fromUtf8("radioButton01"))
        self.lineEdit002 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit002.setGeometry(QtCore.QRect(100, 170, 113, 20))
        self.lineEdit002.setObjectName(_fromUtf8("lineEdit002"))
        self.lineEdit03 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit03.setGeometry(QtCore.QRect(100, 210, 113, 20))
        self.lineEdit03.setObjectName(_fromUtf8("lineEdit03"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAa = QtGui.QAction(MainWindow)
        self.actionAa.setObjectName(_fromUtf8("actionAa"))

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.lineEdit01, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.label01.setText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton01.setText(_translate("MainWindow", "PushButton", None))
        self.label01.setText(_translate("MainWindow", "TextLabel", None))
        self.radioButton01.setText(_translate("MainWindow", "RadioButton", None))
        self.actionAa.setText(_translate("MainWindow", "aa", None))

