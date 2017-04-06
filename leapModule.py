import sys

sys.path.insert(0, "LeapSDK/lib")
sys.path.insert(0, "LeapSDK/lib/x86")

import Leap

controller = Leap.Controller()


def connect():
    if not controller.is_connected:
        print "waiting for connection..."
    else:
        while not controller.is_connected:
            pass
        else:
            print "connected"


def get_roll():
    frame = controller.frame()
    while frame.id < 0:
        frame = controller.frame()
    hand = frame.hands[0]
    return int(hand.palm_normal.roll * Leap.RAD_TO_DEG)


def get_pitch():
    frame = controller.frame()
    while frame.id < 0:
        frame = controller.frame()
    hand = frame.hands[0]
    return int(hand.direction.pitch * Leap.RAD_TO_DEG)


def get_yaw():
    frame = controller.frame()
    while frame.id < 0:
        frame = controller.frame()
    hand = frame.hands[0]
    return hand.direction.yaw


def get_height():
    frame = controller.frame()
    while frame.id < 0:
        frame = controller.frame()
    hand = frame.hands[0]
    height = hand.palm_position[1]
    return height


def count_hands():
    frame = controller.frame()
    while frame.id < 0:
        frame = controller.frame()
    if frame.hands.is_empty:
        return 0
    else:
        return 1
