import sys

# import nao sdk path, relative
sys.path.insert(0, "LeapSDK/lib")
sys.path.insert(0, "LeapSDK/lib/x86")

import Leap

controller = Leap.Controller()
last_frame = 0
# last frame to prevent duplicate frames being processed


# return users hand rotation data
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


# return users hand height
def get_height():
    frame = controller.frame()
    while frame.id < 0:
        frame = controller.frame()
    hand = frame.hands[0]
    height = hand.palm_position[1]
    return height


# return 1 if hands detected
def count_hands():
    frame = controller.frame()
    while frame.id < 0:
        frame = controller.frame()
    if frame.hands.is_empty:
        return 0
    else:
        return 1


# leap get service status
def get_service_status():
    return controller.is_service_connected()


# leap get tracking status
def get_tracking_status():
    return not controller.is_paused()


# leap get lighting status
def get_lighting_status():
    device = controller.devices[0]
    return not device.is_lighting_bad


# leap get smudge status
def get_smudge_status():
    device = controller.devices[0]
    return not device.is_smudged


# leap get bandwidth status (fps)
def get_bandwidth_status():
    frame = controller.frame()
    return frame.current_frames_per_second


# leap get extended fingers
def get_extended_fingers():
    frame = controller.frame()
    return len(frame.pointables.extended())


# Leap get hand gesture
def get_hand_gesture():
    frame = controller.frame()
    pointables_list = frame.hands[0].pointables
    gesture = ""
    # build string describing hand gesture in terms of fingers extended
    for pointable in pointables_list:
        if pointable.is_extended and pointable.is_valid:
            gesture += "T"  # extended
        else:
            gesture += "F"  # not extended
    if gesture == "TTTTT":  # fingers fully extended
        return 0
    elif gesture == "FTTTF":  # middle three fingers extended
        return 1
    elif gesture == "TFFFT":  # outer two fingers extended
        return 2
    elif gesture == "FFFFF":  # no fingers extended
        return 3
    else:
        return -1  # other

