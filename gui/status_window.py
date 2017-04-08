# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'status_window.ui'
#
# Created: Sat Apr 08 13:17:24 2017
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

class Ui_status_window(object):
    def setupUi(self, status_window):
        status_window.setObjectName(_fromUtf8("status_window"))
        status_window.resize(458, 193)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(status_window.sizePolicy().hasHeightForWidth())
        status_window.setSizePolicy(sizePolicy)
        status_window.setMinimumSize(QtCore.QSize(458, 193))
        status_window.setMaximumSize(QtCore.QSize(458, 193))
        self.lbl_title = QtGui.QLabel(status_window)
        self.lbl_title.setGeometry(QtCore.QRect(10, 10, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName(_fromUtf8("lbl_title"))
        self.group_leapmotion = QtGui.QGroupBox(status_window)
        self.group_leapmotion.setGeometry(QtCore.QRect(20, 50, 201, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.group_leapmotion.setFont(font)
        self.group_leapmotion.setObjectName(_fromUtf8("group_leapmotion"))
        self.lbl_service = QtGui.QLabel(self.group_leapmotion)
        self.lbl_service.setGeometry(QtCore.QRect(10, 30, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_service.setFont(font)
        self.lbl_service.setObjectName(_fromUtf8("lbl_service"))
        self.edit_leap_service = QtGui.QLineEdit(self.group_leapmotion)
        self.edit_leap_service.setGeometry(QtCore.QRect(80, 30, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_leap_service.setFont(font)
        self.edit_leap_service.setStyleSheet(_fromUtf8("background-color:red"))
        self.edit_leap_service.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_leap_service.setReadOnly(True)
        self.edit_leap_service.setObjectName(_fromUtf8("edit_leap_service"))
        self.lbl_tracking = QtGui.QLabel(self.group_leapmotion)
        self.lbl_tracking.setGeometry(QtCore.QRect(10, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_tracking.setFont(font)
        self.lbl_tracking.setObjectName(_fromUtf8("lbl_tracking"))
        self.edit_leap_tracking = QtGui.QLineEdit(self.group_leapmotion)
        self.edit_leap_tracking.setGeometry(QtCore.QRect(80, 60, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_leap_tracking.setFont(font)
        self.edit_leap_tracking.setStyleSheet(_fromUtf8("background-color:red"))
        self.edit_leap_tracking.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_leap_tracking.setReadOnly(True)
        self.edit_leap_tracking.setObjectName(_fromUtf8("edit_leap_tracking"))
        self.edit_leap_bandwidth = QtGui.QLineEdit(self.group_leapmotion)
        self.edit_leap_bandwidth.setGeometry(QtCore.QRect(80, 90, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_leap_bandwidth.setFont(font)
        self.edit_leap_bandwidth.setStyleSheet(_fromUtf8("background-color:red"))
        self.edit_leap_bandwidth.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_leap_bandwidth.setReadOnly(True)
        self.edit_leap_bandwidth.setObjectName(_fromUtf8("edit_leap_bandwidth"))
        self.lbl_bandwidth = QtGui.QLabel(self.group_leapmotion)
        self.lbl_bandwidth.setGeometry(QtCore.QRect(10, 90, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_bandwidth.setFont(font)
        self.lbl_bandwidth.setObjectName(_fromUtf8("lbl_bandwidth"))
        self.group_nao = QtGui.QGroupBox(status_window)
        self.group_nao.setGeometry(QtCore.QRect(240, 50, 201, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.group_nao.setFont(font)
        self.group_nao.setObjectName(_fromUtf8("group_nao"))
        self.lbl_connected = QtGui.QLabel(self.group_nao)
        self.lbl_connected.setGeometry(QtCore.QRect(10, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_connected.setFont(font)
        self.lbl_connected.setObjectName(_fromUtf8("lbl_connected"))
        self.editNaoConnected = QtGui.QLineEdit(self.group_nao)
        self.editNaoConnected.setGeometry(QtCore.QRect(80, 30, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.editNaoConnected.setFont(font)
        self.editNaoConnected.setStyleSheet(_fromUtf8("background-color:red"))
        self.editNaoConnected.setAlignment(QtCore.Qt.AlignCenter)
        self.editNaoConnected.setReadOnly(True)
        self.editNaoConnected.setObjectName(_fromUtf8("editNaoConnected"))
        self.lbl_battery = QtGui.QLabel(self.group_nao)
        self.lbl_battery.setGeometry(QtCore.QRect(10, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_battery.setFont(font)
        self.lbl_battery.setObjectName(_fromUtf8("lbl_battery"))
        self.lbl_volume = QtGui.QLabel(self.group_nao)
        self.lbl_volume.setGeometry(QtCore.QRect(10, 90, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_volume.setFont(font)
        self.lbl_volume.setObjectName(_fromUtf8("lbl_volume"))
        self.sldr_volume = QtGui.QSlider(self.group_nao)
        self.sldr_volume.setGeometry(QtCore.QRect(80, 90, 111, 22))
        self.sldr_volume.setOrientation(QtCore.Qt.Horizontal)
        self.sldr_volume.setObjectName(_fromUtf8("sldr_volume"))
        self.pbar_battery = QtGui.QProgressBar(self.group_nao)
        self.pbar_battery.setGeometry(QtCore.QRect(80, 60, 111, 23))
        self.pbar_battery.setProperty("value", 50)
        self.pbar_battery.setObjectName(_fromUtf8("pbar_battery"))

        self.retranslateUi(status_window)
        QtCore.QMetaObject.connectSlotsByName(status_window)

    def retranslateUi(self, status_window):
        status_window.setWindowTitle(_translate("status_window", "Status", None))
        self.lbl_title.setText(_translate("status_window", "Status", None))
        self.group_leapmotion.setTitle(_translate("status_window", "Leap Motion", None))
        self.lbl_service.setText(_translate("status_window", "Service: ", None))
        self.edit_leap_service.setText(_translate("status_window", "NOT CONNECTED", None))
        self.lbl_tracking.setText(_translate("status_window", "Tracking: ", None))
        self.edit_leap_tracking.setText(_translate("status_window", "NOT CONNECTED", None))
        self.edit_leap_bandwidth.setText(_translate("status_window", "NOT CONNECTED", None))
        self.lbl_bandwidth.setText(_translate("status_window", "Bandwidth: ", None))
        self.group_nao.setTitle(_translate("status_window", "Nao Robot", None))
        self.lbl_connected.setText(_translate("status_window", "Connected: ", None))
        self.editNaoConnected.setText(_translate("status_window", "NOT CONNECTED", None))
        self.lbl_battery.setText(_translate("status_window", "Battery: ", None))
        self.lbl_volume.setText(_translate("status_window", "Volume", None))

