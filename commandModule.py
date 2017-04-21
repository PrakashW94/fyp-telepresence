import naoModule
import leapModule
import time

command_list = []

# leapModule.connect()


# flag
def nao_stand():
    naoModule.posture_stand()
    local_command_list = [{"type": "stand", "parameters": [-1]}]
    record_command_list(local_command_list)


# flag
def nao_say(phrase_to_say):
    naoModule.say_phrase(phrase_to_say)
    local_command_list = [{"type": "say", "parameters": [phrase_to_say]}]
    record_command_list(local_command_list)


def nao_walk_ss():
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


# flag
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
    naoModule.move_walk(1)

    print "Test function complete!"


def test_func2(window, app):
    hands = 0
    while hands == 0:
        hands = leapModule.count_hands()

    while hands == 1:
        height = leapModule.get_height()
        scaled_height = scale(height, 100, 400, 50, 90)
        pitch = leapModule.get_pitch()
        scaled_pitch1 = scale(pitch, -20, 90, 0, scaled_height)
        output_str = "raw: " + str(pitch) \
                     + ", scaled: " + str(scaled_pitch1) \
                     + ", height: " + str(scaled_height)

        print output_str
        window.label.setText(output_str)
        window.horizontalSlider.setValue(scaled_height)
        app.processEvents()
        hands = leapModule.count_hands()

    print "Test function complete!"


# flag
def update_status_window(window, app):
    leap_service_status = leapModule.get_service_status()
    leap_tracking_status = leapModule.get_tracking_status()

    if leap_service_status:
        window.edit_leap_service.setText("CONNECTED")
        window.edit_leap_service.setStyleSheet("background-color:green")
    else:
        window.edit_leap_service.setText("NOT CONNECTED")
        window.edit_leap_service.setStyleSheet("background-color:red")

    if leap_tracking_status:
        window.edit_leap_tracking.setText("CONNECTED")
        window.edit_leap_tracking.setStyleSheet("background-color:green")
    else:
        window.edit_leap_tracking.setText("NOT CONNECTED")
        window.edit_leap_tracking.setStyleSheet("background-color:red")

    # Check connection to robot
    nao_connection_status = naoModule.get_connection_status()

    if nao_connection_status:
        window.edit_nao_connection.setText("CONNECTED")
        window.edit_nao_connection.setStyleSheet("background-color:green")
        # TODO uncomment when working with real robot or implement virtual robot check
        # nao_battery = naoModule.get_battery()
        # nao_volume = naoModule.get_volume()
        # window.pbar_battery.setValue(nao_battery)
        # window.sldr_volume.setValue(nao_volume)
    else:
        window.edit_nao_connection.setText("NOT CONNECTED")
        window.edit_nao_connection.setStyleSheet("background-color:red")
        window.pbar_battery.setValue(0)
        window.sldr_volume.setValue(0)

    while window.isVisible():
        bandwidth_status = leapModule.get_bandwidth_status()
        window.edit_leap_bandwidth.setText(str(bandwidth_status))
        if bandwidth_status > 100:
            window.edit_leap_bandwidth.setStyleSheet("background-color:green")
        elif 60 < bandwidth_status < 100:
            window.edit_leap_bandwidth.setStyleSheet("background-color:orange")
        else:
            window.edit_leap_bandwidth.setStyleSheet("background-color:red")
        app.processEvents()


# flag
def nao_set_volume(value):
    naoModule.set_volume(value)
    naoModule.say_phrase("My volume is now " + str(value))


# flag
def nao_rotate_head(window, app):
    hands = 0

    while hands == 0:
        hands = leapModule.count_hands()

    # naoModule.say_phrase("My head is now under your control!")
    extended_fingers = leapModule.get_extended_fingers()
    close_counter = 0
    local_command_list = []
    while close_counter < 300:
        if extended_fingers == 0:
            close_counter += 1
        else:
            height = leapModule.get_height()
            scaled_height = scale(height, 100, 400, 30, 90)

            angles = leapModule.get_pitch_yaw_roll()
            # scale angles according to height for sensitivity
            scaled_angles1 = \
                [
                    scale(angles[0], -scaled_height, scaled_height, -90, 90),
                    scale(angles[1], -scaled_height, scaled_height, -90, 90)
                ]

            # scale angles according to nao head limits
            scaled_angles2 = \
                [
                    scale(scaled_angles1[0], -90, 90, -39, 30),
                    scale(scaled_angles1[1], -90, 90, -120, 120)
                ]

            output_pitch = scale(scaled_angles2[0], -39, 30, 0, 99)
            output_yaw = scale(scaled_angles2[1], -120, 120, 0, 99)
            window.sldr_pitch.setValue(output_pitch)
            window.sldr_yaw.setValue(output_yaw)

            output_height = scale(scaled_height, 30, 90, 0, 99)
            window.sldr_height.setValue(output_height)

            app.processEvents()
            # print "input, " + str(angles[0]) + ", output, " + str(scaled_angles2[0])
            # print "pitch: " + str(scaled_angles[1]) + ", yaw: " + str(scaled_angles[0])
            rad_scaled_angles = [scaled_angles2[0] * -0.0174533, scaled_angles2[1] * 0.0174533]
            naoModule.rotate_head(rad_scaled_angles)
            local_command_list.append({"type": "head", "parameters": [scaled_angles2[0] * -0.0174533, scaled_angles2[1] * 0.0174533]})
        extended_fingers = leapModule.get_extended_fingers()
    record_command_list(local_command_list)


# flag
def nao_walk(window, app):
    hands = 0

    while hands == 0:
        hands = leapModule.count_hands()

    extended_fingers = leapModule.get_extended_fingers()
    close_counter = 0
    local_command_list = []
    test_list = []
    while close_counter < 300:
        if extended_fingers == 0:
            close_counter += 1
        else:
            height = leapModule.get_height()
            scaled_height = scale(height, 100, 400, 30, 90)

            angles = leapModule.get_pitch_yaw_roll()
            # scale angles according to height for sensitivity
            scaled_angles1 = \
                [
                    scale(angles[0], -scaled_height, scaled_height, -90, 90),
                    scale(angles[1], -scaled_height, scaled_height, -90, 90)
                ]

            # scale angles according to output scale
            scaled_angles2 = \
                [
                    scale(scaled_angles1[0], -90, 90, 0, 99),
                    scale(scaled_angles1[1], -90, 90, 0, 99)
                ]

            output_pitch = scaled_angles2[0]
            output_yaw = scaled_angles2[1]

            window.sldr_pitch.setValue(output_pitch)
            window.sldr_yaw.setValue(output_yaw)

            output_height = scale(scaled_height, 30, 90, 0, 99)
            window.sldr_height.setValue(output_height)

            app.processEvents()

            scaled_pitch = scale(scaled_angles2[0], 0, 99, -0.1, 0.1)
            if -0.03 < scaled_pitch < 0.03:
                scaled_pitch = 0

            if scaled_angles2[1] < 33:
                rad_yaw = 20
            elif scaled_angles2[1] > 66:
                rad_yaw = -20
            else:
                rad_yaw = 0

            rad_yaw *= 0.0174533

            # print "x, " + str(scaled_pitch) + ", theta: " + str(rad_yaw)
            naoModule.move_walk_turn(scaled_pitch, rad_yaw)
            local_command_list.append({"type": "walk", "parameters": [scaled_pitch, rad_yaw]})

        extended_fingers = leapModule.get_extended_fingers()
    naoModule.move_stop()
    record_command_list(local_command_list)


# flag
def nao_camera_register(widget):
    naoModule.initialise_video_proxy(widget)


# flag
def nao_camera_unregister(widget):
    naoModule.destroy_video_proxy(widget)


# flag, TODO recording arm movement
def nao_arm(window, app, hand):
    hands = 0

    while hands == 0:
        hands = leapModule.count_hands()

    gesture = leapModule.get_hand_gesture()
    close_counter = 0
    while close_counter < 120:
        if gesture == 3:
            close_counter += 1
        else:
            height = leapModule.get_height()
            scaled_height = scale(height, 100, 400, 30, 90)

            angles = leapModule.get_pitch_yaw_roll()
            angles[2] *= -1  # invert roll
            # scale angles according to height for sensitivity
            scaled_angles1 = \
                [
                    scale(angles[0], -scaled_height, scaled_height, -90, 90),
                    scale(angles[1], -scaled_height, scaled_height, -90, 90),
                    scale(angles[2], -scaled_height, scaled_height, -90, 90)
                ]

            if gesture == 0:
                # move shoulder
                # scale angles according to nao arm limits
                scaled_angles2 = \
                    [
                        scale(scaled_angles1[0], -90, 90, -120, 120),
                        scale(scaled_angles1[1], -90, 90, -1, 1),
                        scale(scaled_angles1[2], -90, 90, -18, 76)
                    ]

                output_pitch = scale(scaled_angles2[0], -120, 120, 0, 99)
                # output_yaw = scale(scaled_angles2[1], -120, 120, -1, 1)
                output_roll = scale(scaled_angles2[2], -18, 76, 0, 99)
                window.sldr_pitch.setValue(output_pitch)
                window.sldr_yaw.setValue(output_roll)

                app.processEvents()

                rad_scaled_angles = \
                    [
                        scaled_angles2[0] * -0.0174533,
                        #scaled_angles2[1] * 0.0174533,
                        scaled_angles2[2] * 0.0174533
                    ]

                naoModule.move_shoulder(rad_scaled_angles, hand)
            elif gesture == 1:
                # move elbow
                # scale angles according to nao arm limits
                scaled_angles2 = \
                    [
                        scale(scaled_angles1[0], -90, 90, -1, 1),
                        scale(scaled_angles1[1], -90, 90, -120, 120),
                        scale(scaled_angles1[2], -90, 90, -88.5, -2)
                    ]

                # output_pitch = scale(scaled_angles2[0], -120, 120, 0, 99)
                output_yaw = scale(scaled_angles2[1], -120, 120, 0, 99)
                output_roll = scale(scaled_angles2[2], -88.5, -2, 0, 99)
                window.sldr_pitch.setValue(output_roll)
                window.sldr_yaw.setValue(output_yaw)

                app.processEvents()

                rad_scaled_angles = \
                    [
                        scaled_angles2[0] * -0.0174533,
                        # scaled_angles2[1] * 0.0174533,
                        scaled_angles2[2] * 0.0174533
                    ]

                naoModule.move_elbow(rad_scaled_angles, hand)
            elif gesture == 2:
                # move wrist
                # scale angles according to nao arm limits
                scaled_angles2 = \
                    [
                        scale(scaled_angles1[0], -90, 90, -1, 1),
                        scale(scaled_angles1[1], -90, 90, -1, 1),
                        scale(scaled_angles1[2], -90, 90, -105, 105)
                    ]

                # output_pitch = scale(scaled_angles2[0], -120, 120, 0, 99)
                # output_yaw = scale(scaled_angles2[1], -105, 105, 0, 99)
                output_roll = scale(scaled_angles2[2], -18, 76, 0, 99)
                window.sldr_pitch.setValue(50)
                window.sldr_yaw.setValue(output_roll)

                app.processEvents()

                rad_scaled_angles = \
                    [
                        # scaled_angles2[0] * -0.0174533,
                        # scaled_angles2[1] * 0.0174533,
                        scaled_angles2[2] * 0.0174533
                    ]

                naoModule.move_wrist(rad_scaled_angles, hand)
            output_height = scale(scaled_height, 30, 90, 0, 99)
            window.sldr_height.setValue(output_height)

            app.processEvents()
        gesture = leapModule.get_hand_gesture()


# flag
def record_command_list(local_command_list):
    global command_list
    command_list.append(local_command_list)


# flag
def print_command_list(window, app):
    list_view = window.wgt_command_list
    for local_command_list in command_list:
        output_string = local_command_list[0]["type"] + " - " + str(len(local_command_list))
        list_view.addItem(output_string)
    # app.processEvents()


# flag
def parse_command_list():
    frame_rate = 1 / leapModule.get_bandwidth_status()

    for local_command_list in command_list:
        for command in local_command_list:
            time.sleep(frame_rate)
            if command["type"] == "head":
                naoModule.rotate_head(command["parameters"])
            elif command["type"] == "walk":
                naoModule.move_walk_turn(command["parameters"][0], command["parameters"][1])
            elif command["type"] == "say":
                naoModule.say_phrase(command["parameters"][0])
            elif command["type"] == "stand":
                naoModule.posture_stand()
            else:
                print "WIP: " + command["type"]
