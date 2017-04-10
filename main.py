import commandModule

import sys
from PyQt4 import QtGui, QtCore
from gui.main_window import Ui_main_window
from gui.status_window import Ui_status_window
from gui.movement_window import Ui_movement_window


class StatusWindow(QtGui.QMainWindow, Ui_status_window):
    def __init__(self, parent=None):
        super(StatusWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.sldr_volume.sliderReleased.connect(self.sldr_volume_changed)

    def sldr_volume_changed(self):
        value = self.sldr_volume.value()
        commandModule.nao_set_volume(value)


class MovementWindow(QtGui.QMainWindow, Ui_movement_window):
    def __init__(self, parent=None):
        super(MovementWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)


class MainWindow(QtGui.QMainWindow, Ui_main_window):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.btn_status.clicked.connect(self.btn_status_click)
        self.btn_nao_head.clicked.connect(self.btn_head_click)

    def btn_status_click(self):
        status_window = StatusWindow(self)
        status_window.show()
        commandModule.update_status_window(status_window, app)

    def btn_head_click(self):
        movement_window = MovementWindow(self)
        movement_window.show()
        commandModule.nao_rotate_head(movement_window, app)
        movement_window.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

"""
commands = ["1 - Head movement with Yaw (LR)", "2 - Head movement with Pitch (UD)", "3 - Walk linear", "4 - Walk rotate", "5 - Reset Pose"]
while 1:
    print "Menu"
    for command in commands:
        print command

    input_command = input("Enter a command")

    if input_command == 1:
        commandModule.nao_rotate_head_yaw()
    elif input_command == 2:
        commandModule.nao_rotate_head_pitch()
    elif input_command == 3:
        commandModule.nao_walk()
    elif input_command == 4:
        commandModule.nao_turn()
    elif input_command == 5:
        commandModule.nao_stand()
    elif input_command == 6:
        commandModule.nao_say("Good morning Firat, welcome to my demo!")
    elif input_command == 7:
        commandModule.test_func()
    else:
        print "Command not recognised"
"""
