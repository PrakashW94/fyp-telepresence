# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'command_list_window.ui'
#
# Created: Sat Apr 22 13:06:39 2017
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
        command_list_window.resize(325, 359)
        self.wgt_command_list = QtGui.QListWidget(command_list_window)
        self.wgt_command_list.setGeometry(QtCore.QRect(10, 70, 151, 271))
        self.wgt_command_list.setObjectName(_fromUtf8("wgt_command_list"))
        self.lbl_title = QtGui.QLabel(command_list_window)
        self.lbl_title.setGeometry(QtCore.QRect(10, 10, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName(_fromUtf8("lbl_title"))
        self.btn_play_single = QtGui.QPushButton(command_list_window)
        self.btn_play_single.setGeometry(QtCore.QRect(180, 70, 131, 31))
        self.btn_play_single.setObjectName(_fromUtf8("btn_play_single"))
        self.btn_play_all = QtGui.QPushButton(command_list_window)
        self.btn_play_all.setGeometry(QtCore.QRect(180, 110, 131, 31))
        self.btn_play_all.setObjectName(_fromUtf8("btn_play_all"))
        self.btn_move_up = QtGui.QPushButton(command_list_window)
        self.btn_move_up.setGeometry(QtCore.QRect(180, 150, 131, 31))
        self.btn_move_up.setObjectName(_fromUtf8("btn_move_up"))
        self.btn_move_down = QtGui.QPushButton(command_list_window)
        self.btn_move_down.setGeometry(QtCore.QRect(180, 190, 131, 31))
        self.btn_move_down.setObjectName(_fromUtf8("btn_move_down"))
        self.btn_deleve_action = QtGui.QPushButton(command_list_window)
        self.btn_deleve_action.setGeometry(QtCore.QRect(180, 230, 131, 31))
        self.btn_deleve_action.setObjectName(_fromUtf8("btn_deleve_action"))
        self.btn_save_actions = QtGui.QPushButton(command_list_window)
        self.btn_save_actions.setGeometry(QtCore.QRect(180, 270, 131, 31))
        self.btn_save_actions.setObjectName(_fromUtf8("btn_save_actions"))
        self.btn_load_actions = QtGui.QPushButton(command_list_window)
        self.btn_load_actions.setGeometry(QtCore.QRect(180, 310, 131, 31))
        self.btn_load_actions.setObjectName(_fromUtf8("btn_load_actions"))

        self.retranslateUi(command_list_window)
        QtCore.QMetaObject.connectSlotsByName(command_list_window)

    def retranslateUi(self, command_list_window):
        command_list_window.setWindowTitle(_translate("command_list_window", "Saved Actions", None))
        self.lbl_title.setText(_translate("command_list_window", "Saved Actions", None))
        self.btn_play_single.setText(_translate("command_list_window", "Play Selected Action", None))
        self.btn_play_all.setText(_translate("command_list_window", "Play All Actions", None))
        self.btn_move_up.setText(_translate("command_list_window", "Move Action Up", None))
        self.btn_move_down.setText(_translate("command_list_window", "Move Action Down", None))
        self.btn_deleve_action.setText(_translate("command_list_window", "Delete Action", None))
        self.btn_save_actions.setText(_translate("command_list_window", "Save Actions", None))
        self.btn_load_actions.setText(_translate("command_list_window", "Load Actions", None))

