from naoqi import ALProxy

naoIP = "169.254.179.156"  # wired blue
# naoIP = "169.254.254.250" # wired red
# naoIP = "158.125.103.28"  # wireless blue
naoPort = 9559


def say_phrase(phrase_to_say):
    tts = ALProxy("ALTextToSpeech", naoIP, naoPort)
    tts.say(phrase_to_say)


def move_walk(dist):
    motion = ALProxy("ALMotion", naoIP, naoPort)
    # motion.moveInit()
    motion.post.moveTo(dist, 0, 0)


def move_turn(theta):
    motion = ALProxy("ALMotion", naoIP, naoPort)
    # motion.moveInit()
    motion.post.moveTo(0.1, 0, theta)


def move_walk_turn(dist, theta):
    motion = ALProxy("ALMotion", naoIP, naoPort)
    motion.move(dist, 0, theta)


def move_stop():
    motion = ALProxy("ALMotion", naoIP, naoPort)
    motion.stopMove()


def posture_stand():
    posture = ALProxy("ALRobotPosture", naoIP, naoPort)
    posture.goToPosture("StandInit", 0.5)


def move_head_yaw(angle):
    motion = ALProxy("ALMotion", naoIP, naoPort)
    motion.changeAngles("HeadYaw", angle, 0.05)


def move_head_pitch(angle):
    motion = ALProxy("ALMotion", naoIP, naoPort)
    motion.changeAngles("HeadPitch", angle, 0.05)


def get_connection_status():
    try:
        system = ALProxy("ALSystem", naoIP, naoPort)
        return True
    except Exception, e:
        print "Could not create proxy."
        print "Error :", e
    return False


def get_battery():
    battery = ALProxy("ALBattery", naoIP, naoPort)
    return battery.getBatteryCharge()


def get_volume():
    audio = ALProxy("ALAudioDevice", naoIP, naoPort)
    return audio.getOutputVolume()


def set_volume(value):
    audio = ALProxy("ALAudioDevice", naoIP, naoPort)
    audio.setOutputVolume(value)


def rotate_head(angles):
    motion = ALProxy("ALMotion", naoIP, naoPort)
    joints = ["HeadPitch", "HeadYaw"]
    # angles = [0.2, -0.2]
    fraction_max_speed = 0.1
    motion.setAngles(joints, angles, fraction_max_speed)


def get_video_proxy(display):
    import vision_definitions
    camera = ALProxy("ALVideoDevice", naoIP, naoPort)

    camera_id = 0
    resolution = vision_definitions.kQQVGA
    colour_space = vision_definitions.kYuvColorSpace
    fps = 30

    display._imgClient = camera.subscribe("_client", resolution, colour_space, fps)
    camera.setParam(vision_definitions.kCameraSelectID, camera_id)
    display._videoProxy = camera

