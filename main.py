from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QImage, QPainter, QWidget, QFileDialog, QMessageBox

from gui.main_window import Ui_main_window
from gui.status_window import Ui_status_window
from gui.movement_window import Ui_movement_window
from gui.camera_window import Ui_camera_window
from gui.command_list_window import Ui_command_list_window

import commandModule
import sys


# status window, code to handle UI events in status window
class StatusWindow(QtGui.QMainWindow, Ui_status_window):
    def __init__(self, parent=None):
        super(StatusWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)

        # UI element events
        self.sldr_volume.sliderReleased.connect(self.sldr_volume_changed)
        self.btn_ip.clicked.connect(self.btn_ip_clicked)
        self.btn_port.clicked.connect(self.btn_port_clicked)
        self.cbo_nao_camera.currentIndexChanged.connect(self.cbo_nao_camera_changed)

    # volume slider change
    def sldr_volume_changed(self):
        value = self.sldr_volume.value()
        commandModule.nao_set_volume(value)

    # save nao ip
    def btn_ip_clicked(self):
        commandModule.nao_set_ip(self.edit_nao_ip.text())
        # show confirmation
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Nao IP address has been updated.")
        msg.setWindowTitle("Nao IP Address")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    # save nao port
    def btn_port_clicked(self):
        commandModule.nao_set_port(self.edit_nao_port.text())
        # show confirmation
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Nao port has been updated.")
        msg.setWindowTitle("Nao Port")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    # nao camera quality changed
    def cbo_nao_camera_changed(self):
        commandModule.nao_set_camera_quality(self.cbo_nao_camera.currentIndex())


# movement window
class MovementWindow(QtGui.QMainWindow, Ui_movement_window):
    def __init__(self, parent=None):
        super(MovementWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)


# command/action list window, code to handle UI events in action list window
class CommandListWindow(QtGui.QMainWindow, Ui_command_list_window):
    def __init__(self, parent=None):
        super(CommandListWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.btn_play_single.clicked.connect(self.btn_play_action_single_click)
        self.btn_play_all.clicked.connect(self.btn_play_action_all_click)
        self.btn_move_up.clicked.connect(self.btn_move_up_click)
        self.btn_move_down.clicked.connect(self.btn_move_down_click)
        self.btn_delete_action.clicked.connect(self.btn_delete_action_click)
        self.btn_load_actions.clicked.connect(self.btn_load_actions_click)
        self.btn_save_actions.clicked.connect(self.btn_save_actions_click)

    # play action if selected
    def btn_play_action_single_click(self):
        try:
            selected_index = self.wgt_command_list.selectedIndexes()[0].row()
        except IndexError, e:
            selected_index = -1
        if selected_index != -1:
            commandModule.play_single_action(selected_index, app)

    # play all actions
    def btn_play_action_all_click(self):
        commandModule.play_all_actions(app)

    # move action up in list if any selected
    def btn_move_up_click(self):
        try:
            selected_index = self.wgt_command_list.selectedIndexes()[0].row()
        except IndexError, e:
            selected_index = -1
        if selected_index != -1:
            commandModule.move_action_up(selected_index)
            commandModule.print_action_list(self.window())

    # move action down in list if any selected
    def btn_move_down_click(self):
        try:
            selected_index = self.wgt_command_list.selectedIndexes()[0].row()
        except IndexError, e:
            selected_index = -1
        if selected_index != -1:
            commandModule.move_action_down(selected_index)
            commandModule.print_action_list(self.window())

    # delete action
    def btn_delete_action_click(self):
        try:
            selected_index = self.wgt_command_list.selectedIndexes()[0].row()
        except IndexError, e:
            selected_index = -1
        if selected_index != -1:
            commandModule.delete_action(selected_index)
            commandModule.print_action_list(self.window())

    # load actions from file
    def btn_load_actions_click(self):
        file_name = QFileDialog.getOpenFileName(self, "Load Actions", "actions/", "JSON (*.json)")
        if file_name != "":
            actions_file = open(file_name, 'r')
            data = actions_file.read()
            actions_file.close()
            loaded = commandModule.load_actions(data)
            if loaded:
                pass
            else:
                # show confirmation
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Error in selected file.")
                msg.setWindowTitle("Load Actions Error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
            commandModule.print_action_list(self.window())

    # save actions to file
    def btn_save_actions_click(self):
        file_name = QFileDialog.getSaveFileName(self, "Save Actions", "", "JSON (*.json)")
        if file_name != "":
            actions_file = open(file_name, 'w')
            content = commandModule.json_encode_actions()
            actions_file.write(content)
            actions_file.close()


# camera window, stores image widget
class CameraWindow(QtGui.QMainWindow, Ui_camera_window):
    def __init__(self, parent=None):
        super(CameraWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)


# image widget, stores nao camera feed
class ImageWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self._image = QImage()

        self._img_width = 640
        self._img_length = 480
        self.resize(self._img_width, self._img_length)

        self._camera_id = 0
        self._video_proxy = None
        self._al_image = None
        self._img_client = ""

        commandModule.nao_camera_register(self)
        # startTimer runs timerEvent every 100ms
        self.startTimer(100)

    def _unregister_image_client(self):
        commandModule.nao_camera_unregister(self)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(painter.viewport(), self._image)

    def _update_image(self):
        self._al_image = self._video_proxy.getImageRemote(self._img_client)
        self._image = QImage\
            (
                self._al_image[6],
                self._al_image[0],
                self._al_image[1],
                QImage.Format_RGB888
            )

    def timerEvent(self, event):
        self._update_image()
        self.update()
        # update runs paintEvent

    def __del__(self):
        self._unregister_image_client()


# main window, code to handle UI events in main window
class MainWindow(QtGui.QMainWindow, Ui_main_window):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # ui elements events
        self.btn_status.clicked.connect(self.btn_status_click)
        self.btn_nao_head.clicked.connect(self.btn_head_click)
        self.btn_nao_camera.clicked.connect(self.btn_camera_click)
        self.btn_nao_walk.clicked.connect(self.btn_nao_walk_click)
        self.btn_nao_say.clicked.connect(self.btn_nao_say_click)
        self.btn_nao_larm.clicked.connect(self.btn_nao_larm_click)
        self.btn_nao_rarm.clicked.connect(self.btn_nao_rarm_click)
        self.btn_command_list.clicked.connect(self.btn_command_list_click)
        # self.btn_test.clicked.connect(self.btn_nao_test_click)

    # open status window
    def btn_status_click(self):
        status_window = StatusWindow(self)
        status_window.show()
        commandModule.update_status_window(status_window, app)

    # open movement window and rotate head
    def btn_head_click(self):
        movement_window = MovementWindow(self)
        movement_window.show()
        app.processEvents()
        commandModule.nao_rotate_head(movement_window, app)
        movement_window.close()

    # open camera window and start camera
    def btn_camera_click(self):
        camera_widget = ImageWidget(self)
        camera_window = CameraWindow(self)
        camera_window.setCentralWidget(camera_widget)
        camera_window.show()

    # open movement window and start stand + walk
    def btn_nao_walk_click(self):
        movement_window = MovementWindow(self)
        movement_window.show()
        app.processEvents()
        commandModule.nao_stand()
        commandModule.nao_walk(movement_window, app)
        movement_window.close()

    # pass phrase to say to robot
    def btn_nao_say_click(self):
        phrase_to_say = self.text_nao_say.toPlainText()
        commandModule.nao_say(str(phrase_to_say))

    # open movement window and move left arm
    def btn_nao_larm_click(self):
        movement_window = MovementWindow(self)
        movement_window.show()
        app.processEvents()
        commandModule.nao_arm(movement_window, app, "left")
        movement_window.close()

    # open movement window and move right arm
    def btn_nao_rarm_click(self):
        movement_window = MovementWindow(self)
        movement_window.show()
        app.processEvents()
        commandModule.nao_arm(movement_window, app, "right")
        movement_window.close()

    # open command list window
    def btn_command_list_click(self):
        command_list_window = CommandListWindow(self)
        commandModule.print_action_list(command_list_window)
        command_list_window.show()

    # test button
    def btn_nao_test_click(self):
        commandModule.test_func()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
