import commandModule

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QImage, QPainter, QWidget
from gui.main_window import Ui_main_window
from gui.status_window import Ui_status_window
from gui.movement_window import Ui_movement_window
from gui.camera_window import Ui_camera_window


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


class CameraWindow(QtGui.QMainWindow, Ui_camera_window):
    def __init__(self, parent=None):
        super(CameraWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)


class ImageWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        from naoModule import naoIP
        from naoModule import naoPort

        self._image = QImage()

        self._img_width = 320
        self._img_length = 240
        self.resize(self._img_width, self._img_length)

        self._camera_id = 0
        self._video_proxy = None
        self._al_image = None
        self._img_client = ""

        self._register_image_client(naoIP, naoPort)
        self.startTimer(100)

    def _register_image_client(self, nao_ip, nao_port):
        from naoqi import ALProxy
        import vision_definitions
        self._video_proxy = ALProxy("ALVideoDevice", nao_ip, nao_port)

        resolution = vision_definitions.kQVGA
        colour_space = vision_definitions.kRGBColorSpace
        fps = 30

        self._img_client = self._video_proxy.subscribe("_client", resolution, colour_space, fps)
        self._video_proxy.setParam(vision_definitions.kCameraSelectID, self._camera_id)

    def _unregister_image_client(self):
        self._video_proxy.unsubscribe(self._img_client)

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
        self.btn_nao_turn.clicked.connect(self.btn_nao_turn_click)

    def btn_status_click(self):
        status_window = StatusWindow(self)
        status_window.show()
        commandModule.update_status_window(status_window, app)

    def btn_head_click(self):
        movement_window = MovementWindow(self)
        movement_window.show()
        commandModule.nao_rotate_head(movement_window, app)
        movement_window.close()

    def btn_camera_click(self):
        camera_widget = ImageWidget(self)
        camera_window = CameraWindow(self)
        camera_window.setCentralWidget(camera_widget)
        camera_window.show()
        # commandModule.nao_camera(camera_window, app)

    def btn_nao_walk_click(self):
        movement_window = MovementWindow(self)
        movement_window.show()
        commandModule.nao_stand()
        commandModule.nao_walk2(movement_window, app)
        movement_window.close()

    def btn_nao_turn_click(self):
        print "Turn button"
        # movement_window = MovementWindow(self)
        # movement_window.show()
        # commandModule.nao_stand()
        # commandModule.nao_turn()

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
