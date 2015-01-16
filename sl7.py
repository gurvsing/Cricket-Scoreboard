# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sl7.ui'
#
# Created: Fri Jan 03 22:14:33 2014
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

class Ui_Form001(object):
    def setupUi(self, Form001):
        Form001.setObjectName(_fromUtf8("Form001"))
        Form001.setWindowModality(QtCore.Qt.NonModal)
        Form001.resize(733, 483)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/new/Users/Gurvinder/Desktop/indian-cricket-logo.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form001.setWindowIcon(icon)
        Form001.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label = QtGui.QLabel(Form001)
        self.label.setGeometry(QtCore.QRect(80, 10, 451, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Magneto"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form001)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form001)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form001)
        self.label_4.setGeometry(QtCore.QRect(20, 270, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(Form001)
        self.lineEdit.setGeometry(QtCore.QRect(190, 200, 133, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form001)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 270, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.frame = QtGui.QFrame(Form001)
        self.frame.setGeometry(QtCore.QRect(400, 120, 251, 191))
        self.frame.setStyleSheet(_fromUtf8("background-image: url(:/newPrefix/images.jpg);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton = QtGui.QPushButton(Form001)
        self.pushButton.setGeometry(QtCore.QRect(430, 420, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form001)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 420, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_5 = QtGui.QLabel(Form001)
        self.label_5.setGeometry(QtCore.QRect(10, 340, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_3 = QtGui.QLineEdit(Form001)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 350, 71, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_3.setInputMask(_fromUtf8(""))
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))

        self.retranslateUi(Form001)
        QtCore.QMetaObject.connectSlotsByName(Form001)

    def retranslateUi(self, Form001):
        Form001.setWindowTitle(_translate("Form001", "CRICKET APP", None))
        self.label.setText(_translate("Form001", "Welcome to CRICKET APP", None))
        self.label_2.setText(_translate("Form001", "Enter Team names", None))
        self.label_3.setText(_translate("Form001", "Team 1(Batting First)", None))
        self.label_4.setText(_translate("Form001", "Team 2(Fielding First)", None))
        self.pushButton.setStatusTip(_translate("Form001", "Click to go to next page", None))
        self.pushButton.setText(_translate("Form001", "Next", None))
        self.pushButton.setShortcut(_translate("Form001", "Ctrl+N", None))
        self.pushButton_2.setText(_translate("Form001", "Back", None))
        self.pushButton_2.setShortcut(_translate("Form001", "Ctrl+B", None))
        self.label_5.setText(_translate("Form001", "ENTER numbers of over in match", None))
        self.lineEdit_3.setToolTip(_translate("Form001", "ENTER IN No.s", None))
        self.lineEdit_3.setStatusTip(_translate("Form001", "ENTER IN No.s", None))
        self.lineEdit_3.setWhatsThis(_translate("Form001", "ENTER IN No.s", None))

import pro
