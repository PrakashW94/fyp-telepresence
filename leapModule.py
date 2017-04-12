import sys

sys.path.insert(0, "LeapSDK/lib")
sys.path.insert(0, "LeapSDK/lib/x86")

import Leap

controller = Leap.Controller()
last_frame = 0


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
    global last_frame
    frame = controller.frame()
    while last_frame == frame.id:
        frame = controller.frame()
    last_frame = frame.id
    hand = frame.hands[0]
    return int(hand.direction.pitch * Leap.RAD_TO_DEG)


def get_yaw():
    frame = controller.frame()
    while frame.id < 0:
        frame = controller.frame()
    hand = frame.hands[0]
    return hand.direction.yaw


def get_pitch_yaw_roll():
    global last_frame
    frame = controller.frame()
    while last_frame == frame.id:
        frame = controller.frame()
    last_frame = frame.id
    hand = frame.hands[0]
    pitch = int(hand.direction.pitch * Leap.RAD_TO_DEG)
    yaw = int(hand.direction.yaw * Leap.RAD_TO_DEG)
    roll = int(hand.palm_normal.roll * Leap.RAD_TO_DEG)
    return [pitch, yaw, roll]


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


def get_service_status():
    return controller.is_connected


def get_tracking_status():
    device = controller.devices[0]
    return device.is_streaming


def get_bandwidth_status():
    frame = controller.frame()
    return frame.current_frames_per_second


def get_extended_fingers():
    frame = controller.frame()
    return len(frame.pointables.extended())
