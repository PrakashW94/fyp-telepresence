import sys

sys.path.insert(0, "LeapSDK/lib")
sys.path.insert(0, "LeapSDK/lib/x86")

import Leap

""""
controller = Leap.Controller();
while not controller.is_connected:
    print "waiting for connection..."
else:
    print "connected"
"""


def getYaw():
    controller = Leap.Controller()
    frame = controller.frame()
    hand = frame.hands[0]
    return hand.palm_normal.roll * Leap.RAD_TO_DEG

def getPitch():
    controller = Leap.Controller()
    frame = controller.frame()
    hand = frame.hands[0]
    return hand.direction.pitch * Leap.RAD_TO_DEG
