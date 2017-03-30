import leapModule
import naoModule

leapModule.connect()

commands = ["1 - Head movement with Yaw (LR)", "2 - Head movement with Pitch (UD)", "3 - Walk linear", "4 - Walk rotate", "5 - Reset Pose"]
while 1:
    print "Menu"
    for command in commands:
        print command

    input_command = input("Enter a command")

    if input_command == 5:
        naoModule.posture_stand()
    elif input_command == 6:
        naoModule.say_phrase("Good morning Firat, welcome to my demo!")
    elif input_command == 3:
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
    elif input_command == 4:
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
    elif input_command == 1:
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
    elif input_command == 2:
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
    else:
        print "Command not recognised"
