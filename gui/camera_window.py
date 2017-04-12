# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera_window.ui'
#
# Created: Wed Apr 12 13:07:37 2017
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

class Ui_camera_window(object):
    def setupUi(self, camera_window):
        camera_window.setObjectName(_fromUtf8("camera_window"))
        camera_window.resize(400, 300)
        camera_window.setMinimumSize(QtCore.QSize(400, 300))
        camera_window.setMaximumSize(QtCore.QSize(400, 300))

        self.retranslateUi(camera_window)
        QtCore.QMetaObject.connectSlotsByName(camera_window)

    def retranslateUi(self, camera_window):
        camera_window.setWindowTitle(_translate("camera_window", "Nao Camera Feed", None))

