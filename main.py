from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QImage, QPainter, QWidget, QFileDialog

from gui.main_window import Ui_main_window
from gui.status_window import Ui_status_window
from gui.movement_window import Ui_movement_window
from gui.camera_window import Ui_camera_window
from gui.command_list_window import Ui_command_list_window

import commandModule
import sys


class StatusWindow(QtGui.QMainWindow, Ui_status_window):
    def __init__(self, parent=None):
        super(StatusWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.sldr_volume.sliderReleased.connect(self.sldr_volume_changed)
        self.btn_ip.clicked.connect(self.btn_ip_clicked)
        self.btn_port.clicked.connect(self.btn_port_clicked)
        self.cbo_nao_camera.currentIndexChanged.connect(self.cbo_nao_camera_changed)

    def sldr_volume_changed(self):
        value = self.sldr_volume.value()
        commandModule.nao_set_volume(value)

    def btn_ip_clicked(self):
        commandModule.nao_set_ip(self.edit_nao_ip.text())

    def btn_port_clicked(self):
        commandModule.nao_set_port(self.edit_nao_port.text())

    def cbo_nao_camera_changed(self):
        commandModule.nao_set_camera_quality(self.cbo_nao_camera.currentIndex())


class MovementWindow(QtGui.QMainWindow, Ui_movement_window):
    def __init__(self, parent=None):
        super(MovementWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)


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

    def btn_play_action_single_click(self):
        try:
            selected_index = self.wgt_command_list.selectedIndexes()[0].row()
        except IndexError, e:
            selected_index = -1
        if selected_index != -1:
            commandModule.play_single_action(selected_index, app)

    def btn_play_action_all_click(self):
        commandModule.play_all_actions(app)

    def btn_move_up_click(self):
        try:
            selected_index = self.wgt_command_list.selectedIndexes()[0].row()
        except IndexError, e:
            selected_index = -1
        if selected_index != -1:
            commandModule.move_action_up(selected_index)
            commandModule.print_action_list(self.window())

    def btn_move_down_click(self):
        try:
            selected_index = self.wgt_command_list.selectedIndexes()[0].row()
        except IndexError, e:
            selected_index = -1
        if selected_index != -1:
            commandModule.move_action_down(selected_index)
            commandModule.print_action_list(self.window())

    def btn_delete_action_click(self):
        try:
            selected_index = self.wgt_command_list.selectedIndexes()[0].row()
        except IndexError, e:
            selected_index = -1
        if selected_index != -1:
            commandModule.delete_action(selected_index)
            commandModule.print_action_list(self.window())

    def btn_load_actions_click(self):
        file_name = QFileDialog.getOpenFileName(self, "Load Actions", "actions/", "JSON (*.json)")
        if file_name != "":
            actions_file = open(file_name, 'r')
            data = actions_file.read()
            actions_file.close()
            commandModule.load_actions(data)
            commandModule.print_action_list(self.window())

    def btn_save_actions_click(self):
        file_name = QFileDialog.getSaveFileName(self, "Save Actions", "", "JSON (*.json)")
        if file_name != "":
            actions_file = open(file_name, 'w')
            content = commandModule.json_encode_actions()
            actions_file.write(content)
            actions_file.close()


class CameraWindow(QtGui.QMainWindow, Ui_camera_window):
    def __init__(self, parent=None):
        super(CameraWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)


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

    def __del__(self):
        self._unregister_image_client()


class MainWindow(QtGui.QMainWindow, Ui_main_window):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.btn_status.clicked.connect(self.btn_status_click)
        self.btn_nao_head.clicked.connect(self.btn_head_click)
        self.btn_nao_camera.clicked.connect(self.btn_camera_click)
        self.btn_nao_walk.clicked.connect(self.btn_nao_walk_click)
        self.btn_nao_say.clicked.connect(self.btn_nao_say_click)
        self.btn_nao_larm.clicked.connect(self.btn_nao_larm_click)
        self.btn_nao_rarm.clicked.connect(self.btn_nao_rarm_click)
        self.btn_command_list.clicked.connect(self.btn_command_list_click)

    def btn_status_click(self):
        status_window = StatusWindow(self)
        status_window.show()
        commandModule.update_status_window(status_window, app)

    def btn_head_click(self):
        movement_window = MovementWindow(self)
        movement_window.show()
        app.processEvents()
        commandModule.nao_rotate_head(movement_window, app)
        movement_window.close()

    def btn_camera_click(self):
        camera_widget = ImageWidget(self)
        camera_window = CameraWindow(self)
        camera_window.setCentralWidget(camera_widget)
        camera_window.show()

    def btn_nao_walk_click(self):
        movement_window = MovementWindow(self)
        movement_window.show()
        app.processEvents()
        commandModule.nao_stand()
        commandModule.nao_walk(movement_window, app)
        movement_window.close()

    def btn_nao_say_click(self):
        phrase_to_say = self.text_nao_say.toPlainText()
        commandModule.nao_say(str(phrase_to_say))

    def btn_nao_larm_click(self):
        movement_window = MovementWindow(self)
        movement_window.show()
        app.processEvents()
        commandModule.nao_arm(movement_window, app, "left")
        movement_window.close()

    def btn_nao_rarm_click(self):
        movement_window = MovementWindow(self)
        movement_window.show()
        app.processEvents()
        commandModule.nao_arm(movement_window, app, "right")
        movement_window.close()

    def btn_command_list_click(self):
        command_list_window = CommandListWindow(self)
        commandModule.print_action_list(command_list_window)
        command_list_window.show()

    def btn_nao_test_click(self):
        print "Test button"

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
