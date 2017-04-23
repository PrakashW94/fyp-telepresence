# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movement_window.ui'
#
# Created: Sun Apr 23 17:08:54 2017
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

class Ui_movement_window(object):
    def setupUi(self, movement_window):
        movement_window.setObjectName(_fromUtf8("movement_window"))
        movement_window.resize(420, 285)
        self.lbl_title = QtGui.QLabel(movement_window)
        self.lbl_title.setGeometry(QtCore.QRect(10, 10, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName(_fromUtf8("lbl_title"))
        self.sldr_horiz = QtGui.QSlider(movement_window)
        self.sldr_horiz.setGeometry(QtCore.QRect(90, 150, 160, 22))
        self.sldr_horiz.setOrientation(QtCore.Qt.Horizontal)
        self.sldr_horiz.setObjectName(_fromUtf8("sldr_horiz"))
        self.sldr_vertical = QtGui.QSlider(movement_window)
        self.sldr_vertical.setGeometry(QtCore.QRect(160, 80, 22, 160))
        self.sldr_vertical.setOrientation(QtCore.Qt.Vertical)
        self.sldr_vertical.setObjectName(_fromUtf8("sldr_vertical"))
        self.sldr_height = QtGui.QSlider(movement_window)
        self.sldr_height.setGeometry(QtCore.QRect(350, 80, 22, 160))
        self.sldr_height.setOrientation(QtCore.Qt.Vertical)
        self.sldr_height.setObjectName(_fromUtf8("sldr_height"))
        self.lbl_x_sliders = QtGui.QLabel(movement_window)
        self.lbl_x_sliders.setGeometry(QtCore.QRect(30, 60, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_x_sliders.setFont(font)
        self.lbl_x_sliders.setObjectName(_fromUtf8("lbl_x_sliders"))
        self.lbl_height_slider = QtGui.QLabel(movement_window)
        self.lbl_height_slider.setGeometry(QtCore.QRect(240, 60, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_height_slider.setFont(font)
        self.lbl_height_slider.setObjectName(_fromUtf8("lbl_height_slider"))
        self.lbl_sldr_vertical = QtGui.QLabel(movement_window)
        self.lbl_sldr_vertical.setGeometry(QtCore.QRect(130, 60, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_sldr_vertical.setFont(font)
        self.lbl_sldr_vertical.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sldr_vertical.setObjectName(_fromUtf8("lbl_sldr_vertical"))
        self.lbl_sldr_horiz = QtGui.QLabel(movement_window)
        self.lbl_sldr_horiz.setGeometry(QtCore.QRect(15, 150, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_sldr_horiz.setFont(font)
        self.lbl_sldr_horiz.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_sldr_horiz.setObjectName(_fromUtf8("lbl_sldr_horiz"))
        self.lbl_wait = QtGui.QLabel(movement_window)
        self.lbl_wait.setEnabled(True)
        self.lbl_wait.setGeometry(QtCore.QRect(0, 52, 421, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_wait.setFont(font)
        self.lbl_wait.setAutoFillBackground(True)
        self.lbl_wait.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_wait.setObjectName(_fromUtf8("lbl_wait"))

        self.retranslateUi(movement_window)
        QtCore.QMetaObject.connectSlotsByName(movement_window)

    def retranslateUi(self, movement_window):
        movement_window.setWindowTitle(_translate("movement_window", "Movement", None))
        self.lbl_title.setText(_translate("movement_window", "Movement Status", None))
        self.lbl_x_sliders.setText(_translate("movement_window", "Hand Rotation", None))
        self.lbl_height_slider.setText(_translate("movement_window", "Hand Height", None))
        self.lbl_sldr_vertical.setText(_translate("movement_window", "lbl_sldr_vert", None))
        self.lbl_sldr_horiz.setText(_translate("movement_window", "lbl_sldr_horiz", None))
        self.lbl_wait.setText(_translate("movement_window", "Waiting for hand...", None))

