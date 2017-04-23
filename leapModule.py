import sys

sys.path.insert(0, "LeapSDK/lib")
sys.path.insert(0, "LeapSDK/lib/x86")

import Leap

controller = Leap.Controller()
last_frame = 0


# flag
def connect():
    print "Connecting..."
    while not controller.is_connected:
        pass
    else:
        print "Connected"


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


# flag
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


# flag
def get_height():
    frame = controller.frame()
    while frame.id < 0:
        frame = controller.frame()
    hand = frame.hands[0]
    height = hand.palm_position[1]
    return height


# flag
def count_hands():
    frame = controller.frame()
    while frame.id < 0:
        frame = controller.frame()
    if frame.hands.is_empty:
        return 0
    else:
        return 1


# flag
def get_service_status():
    return controller.is_service_connected()


# flag
def get_tracking_status():
    return not controller.is_paused()


# flag
def get_lighting_status():
    device = controller.devices[0]
    return not device.is_lighting_bad


# flag
def get_smudge_status():
    device = controller.devices[0]
    return not device.is_smudged


# flag
def get_bandwidth_status():
    frame = controller.frame()
    return frame.current_frames_per_second


# flag
def get_extended_fingers():
    # global last_frame
    # while last_frame == frame.id:
        # frame = controller.frame()
    # last_frame = frame.id
    frame = controller.frame()
    return len(frame.pointables.extended())


# flag
def get_hand_gesture():
    frame = controller.frame()
    pointables_list = frame.hands[0].pointables
    gesture = ""
    for pointable in pointables_list:
        if pointable.is_extended and pointable.is_valid:
            gesture += "T"
        else:
            gesture += "F"
    if gesture == "TTTTT":
        return 0
    elif gesture == "FTTTF":
        return 1
    elif gesture == "TFFFT":
        return 2
    elif gesture == "FFFFF":
        return 3
    else:
        return -1

