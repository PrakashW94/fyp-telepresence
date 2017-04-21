# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'command_list_window.ui'
#
# Created: Fri Apr 21 14:45:30 2017
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_command_list_window(object):
    def setupUi(self, command_list_window):
        command_list_window.setObjectName(_fromUtf8("command_list_window"))
        command_list_window.resize(441, 282)
        self.wgt_command_list = QtGui.QListWidget(command_list_window)
        self.wgt_command_list.setGeometry(QtCore.QRect(10, 10, 421, 261))
        self.wgt_command_list.setObjectName(_fromUtf8("wgt_command_list"))

        self.retranslateUi(command_list_window)
        QtCore.QMetaObject.connectSlotsByName(command_list_window)

    def retranslateUi(self, command_list_window):
        command_list_window.setWindowTitle(_translate("command_list_window", "Dialog", None))

