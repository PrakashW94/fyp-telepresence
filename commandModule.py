import naoModule
import leapModule
import time
import sys
from PyQt4 import QtCore, QtGui, uic

leapModule.connect()


def nao_stand():
    naoModule.posture_stand()


def nao_say(phrase_to_say):
    naoModule.say_phrase(phrase_to_say)


def nao_walk():
    direction = 0
    hands = 0
    while hands == 0:
        hands = leapModule.count_hands()

    while hands == 1:
        pitch = leapModule.get_pitch()
        print pitch
        if pitch > 0:
            naoModule.move_walk(0.1)
            if direction != 1:
                direction = 1
                naoModule.move_stop()
                naoModule.say_phrase("I'm walking forward!")
        else:
            naoModule.move_walk(-0.1)
            if direction != -1:
                direction = -1
                naoModule.move_stop()
                naoModule.say_phrase("I'm walking backwards!")
        hands = leapModule.count_hands()
    naoModule.move_stop()


def nao_turn():
    direction = 0
    hands = 0
    while hands == 0:
        hands = leapModule.count_hands()

    while hands == 1:
        yaw = leapModule.get_yaw()
        print yaw
        if yaw < 0:
            naoModule.move_turn(yaw)
            if direction != 1:
                direction = 1
                naoModule.move_stop()
                naoModule.say_phrase("I'm turning clockwise!")
        else:
            naoModule.move_turn(yaw)
            if direction != -1:
                direction = -1
                naoModule.move_stop()
                naoModule.say_phrase("I'm turning anticlockwise!")
        hands = leapModule.count_hands()
    naoModule.move_stop()


def nao_rotate_head_yaw():
    direction = 0
    hands = 0

    while hands == 0:
        hands = leapModule.count_hands()

    while hands == 1:
        yaw = leapModule.get_yaw()
        print yaw
        if yaw > 0:
            naoModule.move_head_yaw(0.25)
            if direction != 1:
                direction = 1
                naoModule.move_stop()
                naoModule.say_phrase("I'm turning my head clockwise!")
        else:
            naoModule.move_head_yaw(-0.25)
            if direction != -1:
                direction = -1
                naoModule.move_stop()
                naoModule.say_phrase("I'm turning my head anticlockwise!")
        hands = leapModule.count_hands()
    naoModule.move_stop()


def nao_rotate_head_pitch():
    direction = 0
    hands = 0

    while hands == 0:
        hands = leapModule.count_hands()

    while hands == 1:
        yaw = leapModule.get_pitch()
        print yaw
        if yaw > 0:
            naoModule.move_head_pitch(-0.25)
            if direction != 1:
                direction = 1
                naoModule.move_stop()
                naoModule.say_phrase("I'm turning my head up!")
        else:
            naoModule.move_head_pitch(0.25)
            if direction != -1:
                direction = -1
                naoModule.move_stop()
                naoModule.say_phrase("I'm turning my head down!")
        hands = leapModule.count_hands()
    naoModule.move_stop()


def scale(value, old_min, old_max, new_min, new_max):
    old_range = old_max - old_min
    new_range = new_max - new_min
    new_value = (((value - old_min) * new_range) / old_range) + new_min
    if new_value > new_max:
        new_value = new_max
    if new_value < new_min:
        new_value = new_min
    return new_value


def test_func():
    hands = 0
    while hands == 0:
        hands = leapModule.count_hands()

    while hands == 1:
        height = leapModule.get_height()
        scaled_height = scale(height, 100, 400, 50, 90)
        pitch = leapModule.get_pitch()
        scaled_pitch1 = scale(pitch, -20, 90, 0, scaled_height)
        output_str = "raw: " + str(pitch) \
              + ", scaled: " + str(scaled_pitch1) \
              + ", height: " + str(scaled_height)

        print output_str
        hands = leapModule.count_hands()

    print "Test function complete!"


def test_func2(window, app):
    hands = 0
    while hands == 0:
        hands = leapModule.count_hands()

    while hands == 1:
        height = leapModule.get_height()
        scaled_height = scale(height, 100, 400, 50, 90)
        pitch = leapModule.get_pitch()
        scaled_pitch1 = scale(pitch, -20, 90, 0, scaled_height)
        output_str = "raw: " + str(pitch) \
                     + ", scaled: " + str(scaled_pitch1) \
                     + ", height: " + str(scaled_height)

        print output_str
        window.label.setText(output_str)
        window.horizontalSlider.setValue(scaled_height)
        app.processEvents()
        hands = leapModule.count_hands()

    print "Test function complete!"


def update_status_window(window, app):
    service_status = leapModule.get_service_status()
    tracking_status = leapModule.get_tracking_status()

    if service_status:
        window.edit_leap_service.setText("CONNECTED")
        window.edit_leap_service.setStyleSheet("background-color:green")
    else:
        window.edit_leap_service.setText("NOT CONNECTED")
        window.edit_leap_service.setStyleSheet("background-color:red")

    if tracking_status:
        window.edit_leap_tracking.setText("CONNECTED")
        window.edit_leap_tracking.setStyleSheet("background-color:green")
    else:
        window.edit_leap_tracking.setText("NOT CONNECTED")
        window.edit_leap_tracking.setStyleSheet("background-color:red")

    while window.isVisible():
        bandwidth_status = leapModule.get_bandwidth_status()
        window.edit_leap_bandwidth.setText(str(bandwidth_status))
        if bandwidth_status > 100:
            window.edit_leap_bandwidth.setStyleSheet("background-color:green")
        elif 60 < bandwidth_status < 100:
            window.edit_leap_bandwidth.setStyleSheet("background-color:orange")
        else:
            window.edit_leap_bandwidth.setStyleSheet("background-color:red")
        app.processEvents()
        # time.sleep(0.5)
