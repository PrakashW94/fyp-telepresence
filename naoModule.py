from naoqi import ALProxy

# naoIP = "169.254.108.110"  # wired blue
# naoIP = "169.254.254.250" # wired red
# naoIP = "158.125.103.28"  # wireless blue
# naoPort = 9559 # real robot
naoIP = "127.0.0.1"
naoPort = 55218


# flag
def say_phrase(phrase_to_say):
    tts = ALProxy("ALTextToSpeech", naoIP, naoPort)
    tts.say(phrase_to_say)


# flag
def move_walk_turn(dist, theta):
    motion = ALProxy("ALMotion", naoIP, naoPort)
    motion.move(dist, 0, theta)


# flag
def move_stop():
    motion = ALProxy("ALMotion", naoIP, naoPort)
    motion.stopMove()


# flag
def posture_stand():
    posture = ALProxy("ALRobotPosture", naoIP, naoPort)
    posture.goToPosture("StandInit", 0.5)


# flag
def get_connection_status():
    if naoPort == 9559:  # real robot
        proxy = "ALSystem"
    else:
        proxy = "ALTextToSpeech"  # virtual robot
    try:
        system = ALProxy(proxy, naoIP, naoPort)
        return True
    except Exception, e:
        print "Could not create proxy."
        print "Error :", e
    return False


# flag
def get_battery():
    battery = ALProxy("ALBattery", naoIP, naoPort)
    return battery.getBatteryCharge()


# flag
def get_volume():
    audio = ALProxy("ALAudioDevice", naoIP, naoPort)
    return audio.getOutputVolume()


# flag
def set_volume(value):
    audio = ALProxy("ALAudioDevice", naoIP, naoPort)
    audio.setOutputVolume(value)


# flag
def rotate_head(angles):
    motion = ALProxy("ALMotion", naoIP, naoPort)
    joints = ["HeadPitch", "HeadYaw"]
    # angles = [0.2, -0.2]
    fraction_max_speed = 0.1
    motion.setAngles(joints, angles, fraction_max_speed)


# flag
def initialise_video_proxy(widget):
    import vision_definitions
    widget._video_proxy = ALProxy("ALVideoDevice", naoIP, naoPort)
    resolution = vision_definitions.kVGA
    colour_space = vision_definitions.kRGBColorSpace
    fps = 30
    widget._img_client = widget._video_proxy.subscribe("_client", resolution, colour_space, fps)
    widget._video_proxy.setParam(vision_definitions.kCameraSelectID, 0)


# flag
def destroy_video_proxy(widget):
    widget._video_proxy.unsubscribe(widget._img_client)


# flag
def move_shoulder(angles, hand):
    motion = ALProxy("ALMotion", naoIP, naoPort)
    if hand == "left":
        joints = ["LShoulderPitch", "LShoulderRoll"]
    else:
        joints = ["RShoulderPitch", "RShoulderRoll"]
    fraction_max_speed = 0.3
    motion.setAngles(joints, angles, fraction_max_speed)


# flag
def move_elbow(angles, hand):
    motion = ALProxy("ALMotion", naoIP, naoPort)
    if hand == "left":
        joints = ["LElbowYaw", "LElbowRoll"]
    else:
        joints = ["RElbowYaw", "RElbowRoll"]
    fraction_max_speed = 0.3
    motion.setAngles(joints, angles, fraction_max_speed)


# flag
def move_wrist(angles, hand):
    motion = ALProxy("ALMotion", naoIP, naoPort)
    if hand == "left":
        joints = ["LWristYaw"]
    else:
        joints = ["RWristYaw"]
    fraction_max_speed = 0.3
    motion.setAngles(joints, angles, fraction_max_speed)


# flag
def get_arm_joint_limits(hand):
    joint_limits = {}
    if hand == "left":
        joint_limits["shoulder_pitch_min"] = -120
        joint_limits["shoulder_pitch_max"] = 120
        joint_limits["shoulder_roll_min"] = -18
        joint_limits["shoulder_roll_max"] = 76
        joint_limits["elbow_yaw_min"] = -120
        joint_limits["elbow_yaw_max"] = 120
        joint_limits["elbow_roll_min"] = -89
        joint_limits["elbow_roll_max"] = -2
        joint_limits["wrist_roll_min"] = -105
        joint_limits["wrist_roll_max"] = 105
    else:
        joint_limits["shoulder_pitch_min"] = -120
        joint_limits["shoulder_pitch_max"] = 120
        joint_limits["shoulder_roll_min"] = -76
        joint_limits["shoulder_roll_max"] = 18
        joint_limits["elbow_yaw_min"] = -120
        joint_limits["elbow_yaw_max"] = 120
        joint_limits["elbow_roll_min"] = 2
        joint_limits["elbow_roll_max"] = 89
        joint_limits["wrist_roll_min"] = -105
        joint_limits["wrist_roll_max"] = 105
    return joint_limits
