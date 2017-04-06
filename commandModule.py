import naoModule
import leapModule

leapModule.connect()


def nao_stand():
    naoModule.posture_stand()


def nao_say(phrase_to_say):
    naoModule.say_phrase(phrase_to_say)


def nao_walk():
    direction = 0
    hands = 0
    while hands == 0:
        hands = leapModule.count_hands()

    while hands == 1:
        pitch = leapModule.get_pitch()
        print pitch
        if pitch > 0:
            naoModule.move_walk(0.1)
            if direction != 1:
                direction = 1
                naoModule.move_stop()
                naoModule.say_phrase("I'm walking forward!")
        else:
            naoModule.move_walk(-0.1)
            if direction != -1:
                direction = -1
                naoModule.move_stop()
                naoModule.say_phrase("I'm walking backwards!")
        hands = leapModule.count_hands()
    naoModule.move_stop()


def nao_turn():
    direction = 0
    hands = 0
    while hands == 0:
        hands = leapModule.count_hands()

    while hands == 1:
        yaw = leapModule.get_yaw()
        print yaw
        if yaw < 0:
            naoModule.move_turn(yaw)
            if direction != 1:
                direction = 1
                naoModule.move_stop()
                naoModule.say_phrase("I'm turning clockwise!")
        else:
            naoModule.move_turn(yaw)
            if direction != -1:
                direction = -1
                naoModule.move_stop()
                naoModule.say_phrase("I'm turning anticlockwise!")
        hands = leapModule.count_hands()
    naoModule.move_stop()


def nao_rotate_head_yaw():
    direction = 0
    hands = 0

    while hands == 0:
        hands = leapModule.count_hands()

    while hands == 1:
        yaw = leapModule.get_yaw()
        print yaw
        if yaw > 0:
            naoModule.move_head_yaw(0.25)
            if direction != 1:
                direction = 1
                naoModule.move_stop()
                naoModule.say_phrase("I'm turning my head clockwise!")
        else:
            naoModule.move_head_yaw(-0.25)
            if direction != -1:
                direction = -1
                naoModule.move_stop()
                naoModule.say_phrase("I'm turning my head anticlockwise!")
        hands = leapModule.count_hands()
    naoModule.move_stop()


def nao_rotate_head_pitch():
    direction = 0
    hands = 0

    while hands == 0:
        hands = leapModule.count_hands()

    while hands == 1:
        yaw = leapModule.get_pitch()
        print yaw
        if yaw > 0:
            naoModule.move_head_pitch(-0.25)
            if direction != 1:
                direction = 1
                naoModule.move_stop()
                naoModule.say_phrase("I'm turning my head up!")
        else:
            naoModule.move_head_pitch(0.25)
            if direction != -1:
                direction = -1
                naoModule.move_stop()
                naoModule.say_phrase("I'm turning my head down!")
        hands = leapModule.count_hands()
    naoModule.move_stop()


def scale(value, old_min, old_max, new_min, new_max):
    old_range = old_max - old_min
    new_range = new_max - new_min
    new_value = (((value - old_min) * new_range) / old_range) + new_min
    if new_value > new_max:
        new_value = new_max
    if new_value < new_min:
        new_value = new_min
    return new_value


def test_func():
    hands = 0
    while hands == 0:
        hands = leapModule.count_hands()

    while hands == 1:
        height = leapModule.get_height()
        scaled_height = scale(height, 100, 400, 50, 90)
        # print "raw: " + str(height) + ", scaled: " + str(scaled_height)

        pitch = leapModule.get_pitch()
        scaled_pitch1 = scale(pitch, -20, 90, 0, scaled_height)
        print "raw: " + str(pitch) \
              + ", scaled: " + str(scaled_pitch1) \
              + ", height: " + str(scaled_height)

        hands = leapModule.count_hands()

    print "Test function complete!"


