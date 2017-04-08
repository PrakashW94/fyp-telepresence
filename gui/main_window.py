# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Fri Apr 07 18:56:42 2017
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

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName(_fromUtf8("main_window"))
        main_window.resize(529, 368)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setMinimumSize(QtCore.QSize(529, 368))
        main_window.setMaximumSize(QtCore.QSize(529, 368))
        self.lbl_title = QtGui.QLabel(main_window)
        self.lbl_title.setGeometry(QtCore.QRect(20, 10, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName(_fromUtf8("lbl_title"))
        self.group_movement = QtGui.QGroupBox(main_window)
        self.group_movement.setGeometry(QtCore.QRect(20, 200, 151, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.group_movement.setFont(font)
        self.group_movement.setObjectName(_fromUtf8("group_movement"))
        self.btn_nao_walk = QtGui.QPushButton(self.group_movement)
        self.btn_nao_walk.setGeometry(QtCore.QRect(10, 30, 131, 31))
        self.btn_nao_walk.setObjectName(_fromUtf8("btn_nao_walk"))
        self.btn_nao_turn = QtGui.QPushButton(self.group_movement)
        self.btn_nao_turn.setGeometry(QtCore.QRect(10, 70, 131, 31))
        self.btn_nao_turn.setObjectName(_fromUtf8("btn_nao_turn"))
        self.group_control = QtGui.QGroupBox(main_window)
        self.group_control.setGeometry(QtCore.QRect(190, 200, 151, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.group_control.setFont(font)
        self.group_control.setObjectName(_fromUtf8("group_control"))
        self.btn_nao_head = QtGui.QPushButton(self.group_control)
        self.btn_nao_head.setGeometry(QtCore.QRect(10, 30, 131, 31))
        self.btn_nao_head.setObjectName(_fromUtf8("btn_nao_head"))
        self.btn_nao_larm = QtGui.QPushButton(self.group_control)
        self.btn_nao_larm.setGeometry(QtCore.QRect(10, 70, 131, 31))
        self.btn_nao_larm.setObjectName(_fromUtf8("btn_nao_larm"))
        self.btn_nao_rarm = QtGui.QPushButton(self.group_control)
        self.btn_nao_rarm.setGeometry(QtCore.QRect(10, 110, 131, 31))
        self.btn_nao_rarm.setObjectName(_fromUtf8("btn_nao_rarm"))
        self.group_speech = QtGui.QGroupBox(main_window)
        self.group_speech.setGeometry(QtCore.QRect(20, 50, 491, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.group_speech.setFont(font)
        self.group_speech.setObjectName(_fromUtf8("group_speech"))
        self.text_nao_say = QtGui.QPlainTextEdit(self.group_speech)
        self.text_nao_say.setGeometry(QtCore.QRect(10, 30, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_nao_say.setFont(font)
        self.text_nao_say.setPlainText(_fromUtf8(""))
        self.text_nao_say.setObjectName(_fromUtf8("text_nao_say"))
        self.btn_nao_say = QtGui.QPushButton(self.group_speech)
        self.btn_nao_say.setGeometry(QtCore.QRect(10, 90, 131, 31))
        self.btn_nao_say.setObjectName(_fromUtf8("btn_nao_say"))
        self.group_misc = QtGui.QGroupBox(main_window)
        self.group_misc.setGeometry(QtCore.QRect(360, 200, 151, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.group_misc.setFont(font)
        self.group_misc.setObjectName(_fromUtf8("group_misc"))
        self.btn_nao_camera = QtGui.QPushButton(self.group_misc)
        self.btn_nao_camera.setGeometry(QtCore.QRect(10, 30, 131, 31))
        self.btn_nao_camera.setObjectName(_fromUtf8("btn_nao_camera"))
        self.btn_status = QtGui.QPushButton(self.group_misc)
        self.btn_status.setGeometry(QtCore.QRect(10, 70, 131, 31))
        self.btn_status.setObjectName(_fromUtf8("btn_status"))

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(_translate("main_window", "Nao Telepresence System - V1", None))
        self.lbl_title.setText(_translate("main_window", "Nao Telepresence System - V1", None))
        self.group_movement.setTitle(_translate("main_window", "Movement", None))
        self.btn_nao_walk.setText(_translate("main_window", "Make Nao Walk", None))
        self.btn_nao_turn.setText(_translate("main_window", "Make Nao Turn", None))
        self.group_control.setTitle(_translate("main_window", "Joint Control", None))
        self.btn_nao_head.setText(_translate("main_window", "Head", None))
        self.btn_nao_larm.setText(_translate("main_window", "Left Arm", None))
        self.btn_nao_rarm.setText(_translate("main_window", "Right Arm", None))
        self.group_speech.setTitle(_translate("main_window", "Speech", None))
        self.btn_nao_say.setText(_translate("main_window", "Say", None))
        self.group_misc.setTitle(_translate("main_window", "Misc", None))
        self.btn_nao_camera.setText(_translate("main_window", "Toggle Camera", None))
        self.btn_status.setText(_translate("main_window", "Status", None))

