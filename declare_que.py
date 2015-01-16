# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'declare_que.ui'
#
# Created: Fri Jan 03 15:30:41 2014
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

class Ui_Dialogdec(object):
    def setupUi(self, Dialogdec):
        Dialogdec.setObjectName(_fromUtf8("Dialogdec"))
        Dialogdec.resize(471, 167)
        self.pushButton = QtGui.QPushButton(Dialogdec)
        self.pushButton.setGeometry(QtCore.QRect(260, 130, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialogdec)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 130, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(Dialogdec)
        self.label.setGeometry(QtCore.QRect(20, 30, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialogdec)
        QtCore.QMetaObject.connectSlotsByName(Dialogdec)

    def retranslateUi(self, Dialogdec):
        Dialogdec.setWindowTitle(_translate("Dialogdec", "Dialog", None))
        self.pushButton.setText(_translate("Dialogdec", "Yes", None))
        self.pushButton_2.setText(_translate("Dialogdec", "No", None))
        self.label.setText(_translate("Dialogdec", "Are you sure you want to declare............?????", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialogdec = QtGui.QDialog()
    ui = Ui_Dialogdec()
    ui.setupUi(Dialogdec)
    Dialogdec.show()
    sys.exit(app.exec_())

