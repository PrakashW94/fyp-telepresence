# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movement_window.ui'
#
# Created: Mon Apr 10 21:04:40 2017
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
        self.sldr_pitch = QtGui.QSlider(movement_window)
        self.sldr_pitch.setGeometry(QtCore.QRect(90, 150, 160, 22))
        self.sldr_pitch.setOrientation(QtCore.Qt.Horizontal)
        self.sldr_pitch.setObjectName(_fromUtf8("sldr_pitch"))
        self.sldr_yaw = QtGui.QSlider(movement_window)
        self.sldr_yaw.setGeometry(QtCore.QRect(160, 80, 22, 160))
        self.sldr_yaw.setOrientation(QtCore.Qt.Vertical)
        self.sldr_yaw.setObjectName(_fromUtf8("sldr_yaw"))
        self.sldr_height = QtGui.QSlider(movement_window)
        self.sldr_height.setGeometry(QtCore.QRect(350, 80, 22, 160))
        self.sldr_height.setOrientation(QtCore.Qt.Vertical)
        self.sldr_height.setObjectName(_fromUtf8("sldr_height"))
        self.lbl_x_sliders = QtGui.QLabel(movement_window)
        self.lbl_x_sliders.setGeometry(QtCore.QRect(50, 60, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_x_sliders.setFont(font)
        self.lbl_x_sliders.setObjectName(_fromUtf8("lbl_x_sliders"))
        self.lbl_height_slider = QtGui.QLabel(movement_window)
        self.lbl_height_slider.setGeometry(QtCore.QRect(270, 60, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_height_slider.setFont(font)
        self.lbl_height_slider.setObjectName(_fromUtf8("lbl_height_slider"))
        self.lbl_yaw_max = QtGui.QLabel(movement_window)
        self.lbl_yaw_max.setGeometry(QtCore.QRect(150, 60, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_yaw_max.setFont(font)
        self.lbl_yaw_max.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_yaw_max.setObjectName(_fromUtf8("lbl_yaw_max"))
        self.lbl_yaw_min = QtGui.QLabel(movement_window)
        self.lbl_yaw_min.setGeometry(QtCore.QRect(150, 240, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_yaw_min.setFont(font)
        self.lbl_yaw_min.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_yaw_min.setObjectName(_fromUtf8("lbl_yaw_min"))
        self.lbl_pitch_min = QtGui.QLabel(movement_window)
        self.lbl_pitch_min.setGeometry(QtCore.QRect(30, 150, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_pitch_min.setFont(font)
        self.lbl_pitch_min.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_pitch_min.setObjectName(_fromUtf8("lbl_pitch_min"))
        self.lbl_pitch_max = QtGui.QLabel(movement_window)
        self.lbl_pitch_max.setGeometry(QtCore.QRect(260, 150, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_pitch_max.setFont(font)
        self.lbl_pitch_max.setObjectName(_fromUtf8("lbl_pitch_max"))
        self.lbl_height_max = QtGui.QLabel(movement_window)
        self.lbl_height_max.setGeometry(QtCore.QRect(350, 60, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_height_max.setFont(font)
        self.lbl_height_max.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_height_max.setObjectName(_fromUtf8("lbl_height_max"))
        self.lbl_height_min = QtGui.QLabel(movement_window)
        self.lbl_height_min.setGeometry(QtCore.QRect(350, 240, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_height_min.setFont(font)
        self.lbl_height_min.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_height_min.setObjectName(_fromUtf8("lbl_height_min"))

        self.retranslateUi(movement_window)
        QtCore.QMetaObject.connectSlotsByName(movement_window)

    def retranslateUi(self, movement_window):
        movement_window.setWindowTitle(_translate("movement_window", "Dialog", None))
        self.lbl_title.setText(_translate("movement_window", "Movement Status", None))
        self.lbl_x_sliders.setText(_translate("movement_window", "Pitch / Yaw", None))
        self.lbl_height_slider.setText(_translate("movement_window", "Height", None))
        self.lbl_yaw_max.setText(_translate("movement_window", "30", None))
        self.lbl_yaw_min.setText(_translate("movement_window", "-39", None))
        self.lbl_pitch_min.setText(_translate("movement_window", "-120", None))
        self.lbl_pitch_max.setText(_translate("movement_window", "120", None))
        self.lbl_height_max.setText(_translate("movement_window", "100", None))
        self.lbl_height_min.setText(_translate("movement_window", "1", None))

