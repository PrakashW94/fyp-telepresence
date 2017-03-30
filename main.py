import sys

sys.path.insert(0, "LeapSDK/lib")
sys.path.insert(0, "LeapSDK/lib/x86")

import Leap
import leapModule

controller = Leap.Controller();
while not controller.is_connected:
    print "waiting for connection..."
else:
    print "connected"

commands = ["1 - Head movement with Yaw", "2 - Head movement with Pitch", "3 - Three"]
while 1:
    print "Menu"
    for command in commands:
        print command

    input_command = input("Enter a command")

    if input_command == 1:
        while(1):
            print leapModule.getYaw()
    elif input_command == 2:
        while(1):
            print leapModule.getPitch()

