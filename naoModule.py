from naoqi import ALProxy

# naoIP = "169.254.108.110"  # wired
naoIP = "158.125.103.28"
naoPort = 9559


def say_phrase(phrase_to_say):
    tts = ALProxy("ALTextToSpeech", naoIP, naoPort)
    tts.say(phrase_to_say)


def move_walk(dist):
    motion = ALProxy("ALMotion", naoIP, naoPort)
    motion.moveInit()
    motion.post.moveTo(dist, 0, 0)


def move_turn(theta):
    motion = ALProxy("ALMotion", naoIP, naoPort)
    motion.moveInit()
    motion.post.moveTo(0.1, 0, theta)


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

