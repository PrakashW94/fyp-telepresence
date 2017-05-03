from naoqi import ALProxy

naoIP = "127.0.0.1"
naoPort = 55422
camera_quality = 0


# set stiffness
def set_stiffness():
    # required if working with the robot without autonomous mode
    motion = ALProxy("ALMotion", naoIP, naoPort)
    motion.stiffnessInterpolation("Body", 1.0, 1.0)


# nao say phrase
def say_phrase(phrase_to_say):
    tts = ALProxy("ALTextToSpeech", naoIP, naoPort)
    tts.say(phrase_to_say)


# nao walk turn
def move_walk_turn(dist, theta):
    motion = ALProxy("ALMotion", naoIP, naoPort)
    motion.move(dist, 0, theta)


# nao stop motion
def move_stop():
    motion = ALProxy("ALMotion", naoIP, naoPort)
    motion.stopMove()


# nao posture stand
def posture_stand():
    posture = ALProxy("ALRobotPosture", naoIP, naoPort)
    posture.goToPosture("StandInit", 0.5)


# nao get connection status, bool response
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


# nao get battery level
def get_battery():
    battery = ALProxy("ALBattery", naoIP, naoPort)
    return battery.getBatteryCharge()


# nao get volume level
def get_volume():
    audio = ALProxy("ALAudioDevice", naoIP, naoPort)
    return audio.getOutputVolume()


# nao set volume level
def set_volume(value):
    audio = ALProxy("ALAudioDevice", naoIP, naoPort)
    audio.setOutputVolume(value)


# nao rotate head
def rotate_head(angles):
    motion = ALProxy("ALMotion", naoIP, naoPort)
    joints = ["HeadPitch", "HeadYaw"]
    fraction_max_speed = 0.1
    motion.setAngles(joints, angles, fraction_max_speed)


# nao initialise video proxy
def initialise_video_proxy(widget):
    import vision_definitions
    widget._video_proxy = ALProxy("ALVideoDevice", naoIP, naoPort)

    # set camera quality based on user input
    if camera_quality == 0:
        resolution = vision_definitions.kQQQVGA  # really bad
    elif camera_quality == 1:
        resolution = vision_definitions.kQQVGA  # bad
    elif camera_quality == 2:
        resolution = vision_definitions.kQVGA  # good

    colour_space = vision_definitions.kRGBColorSpace
    fps = 30
    widget._img_client = widget._video_proxy.subscribe("_client", resolution, colour_space, fps)
    widget._video_proxy.setParam(vision_definitions.kCameraSelectID, 0)


# nao destroy video proxy
def destroy_video_proxy(widget):
    widget._video_proxy.unsubscribe(widget._img_client)


# nao move shoulder
def move_shoulder(angles, hand):
    motion = ALProxy("ALMotion", naoIP, naoPort)
    if hand == "left":
        joints = ["LShoulderPitch", "LShoulderRoll"]
    else:
        joints = ["RShoulderPitch", "RShoulderRoll"]
    fraction_max_speed = 0.3
    motion.setAngles(joints, angles, fraction_max_speed)


# nao move elbow
def move_elbow(angles, hand):
    motion = ALProxy("ALMotion", naoIP, naoPort)
    if hand == "left":
        joints = ["LElbowYaw", "LElbowRoll"]
    else:
        joints = ["RElbowYaw", "RElbowRoll"]
    fraction_max_speed = 0.3
    motion.setAngles(joints, angles, fraction_max_speed)


# nao move wrist
def move_wrist(angles, hand):
    motion = ALProxy("ALMotion", naoIP, naoPort)
    if hand == "left":
        joints = ["LWristYaw"]
    else:
        joints = ["RWristYaw"]
    fraction_max_speed = 0.3
    motion.setAngles(joints, angles, fraction_max_speed)


# nao return object containing joint limits
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
