import naoModule
import leapModule
import time

action_list = []


# make nao stand
def nao_stand():
    naoModule.set_stiffness()
    naoModule.posture_stand()
    local_action_list = [{"type": "stand", "parameters": [-1]}]
    record_action_list(local_action_list)


# make nao say phrase
def nao_say(phrase_to_say):
    naoModule.say_phrase(phrase_to_say)
    local_action_list = [{"type": "say", "parameters": [phrase_to_say]}]
    record_action_list(local_action_list)


# scale value to new range
def scale(value, old_min, old_max, new_min, new_max):
    old_range = old_max - old_min
    new_range = new_max - new_min
    new_value = (((value - old_min) * new_range) / old_range) + new_min
    if new_value > new_max:
        new_value = new_max
    if new_value < new_min:
        new_value = new_min
    return new_value


# test function
def test_func():
    print "Test function complete!"


# update the status window ui elements
def update_status_window(window, app):
    leap_service_status = leapModule.get_service_status()

    if leap_service_status:
        window.edit_leap_service.setText("CONNECTED")
        window.edit_leap_service.setStyleSheet("background-color:green")

        leap_tracking_status = leapModule.get_tracking_status()

        if leap_tracking_status:
            window.edit_leap_tracking.setText("CONNECTED")
            window.edit_leap_tracking.setStyleSheet("background-color:green")

            # if tracking, check tracking quality
            leap_lighting_status = leapModule.get_lighting_status()
            leap_smudge_status = leapModule.get_smudge_status()

            if leap_lighting_status:
                window.edit_leap_lighting.setText("GOOD")
                window.edit_leap_lighting.setStyleSheet("background-color:green")
            else:
                window.edit_leap_lighting.setText("BAD")
                window.edit_leap_lighting.setStyleSheet("background-color:red")

            if leap_smudge_status:
                window.edit_leap_smudge.setText("GOOD")
                window.edit_leap_smudge.setStyleSheet("background-color:green")
            else:
                window.edit_leap_smudge.setText("BAD")
                window.edit_leap_smudge.setStyleSheet("background-color:red")
        else:
            window.edit_leap_tracking.setText("NOT CONNECTED")
            window.edit_leap_tracking.setStyleSheet("background-color:red")
            window.edit_leap_lighting.setText("NOT CONNECTED")
            window.edit_leap_lighting.setStyleSheet("background-color:red")
            window.edit_leap_smudge.setText("NOT CONNECTED")
            window.edit_leap_smudge.setStyleSheet("background-color:red")
    else:
        window.edit_leap_service.setText("NOT CONNECTED")
        window.edit_leap_service.setStyleSheet("background-color:red")
        window.edit_leap_tracking.setText("NOT CONNECTED")
        window.edit_leap_tracking.setStyleSheet("background-color:red")
        window.edit_leap_lighting.setText("NOT CONNECTED")
        window.edit_leap_lighting.setStyleSheet("background-color:red")
        window.edit_leap_smudge.setText("NOT CONNECTED")
        window.edit_leap_smudge.setStyleSheet("background-color:red")

    # Check connection to robot
    nao_connection_status = naoModule.get_connection_status()

    if nao_connection_status:
        window.edit_nao_connection.setText("CONNECTED")
        window.edit_nao_connection.setStyleSheet("background-color:green")
        if naoModule.naoIP != "127.0.0.1":  # not virtual robot
            window.pbar_battery.setEnabled(True)
            window.sldr_volume.setEnabled(True)
            nao_battery = naoModule.get_battery()
            nao_volume = naoModule.get_volume()
            window.pbar_battery.setValue(nao_battery)
            window.sldr_volume.setValue(nao_volume)
            window.cbo_nao_camera.setEnabled(True)
            window.cbo_nao_camera.setCurrentIndex(naoModule.camera_quality)
        else:  # functionality not available on virtual robot
            window.pbar_battery.setValue(0)
            window.sldr_volume.setValue(0)
            window.pbar_battery.setEnabled(False)
            window.sldr_volume.setEnabled(False)
            window.cbo_nao_camera.setEnabled(False)
    else:
        window.edit_nao_connection.setText("NOT CONNECTED")
        window.edit_nao_connection.setStyleSheet("background-color:red")
        window.pbar_battery.setEnabled(False)
        window.sldr_volume.setEnabled(False)
        window.cbo_nao_camera.setEnabled(False)

        window.pbar_battery.setValue(0)
        window.sldr_volume.setValue(0)

    window.edit_nao_ip.setText(naoModule.naoIP)
    window.edit_nao_port.setText(str(naoModule.naoPort))

    if leap_tracking_status:  # update leap motion bandwidth
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
            # process ui update events
    else:
        window.edit_leap_bandwidth.setStyleSheet("background-color:red")
        window.edit_leap_bandwidth.setText("N/A")


# update up address
def nao_set_ip(new_ip):
    naoModule.naoIP = str(new_ip)


# update port
def nao_set_port(new_port):
    naoModule.naoPort = int(new_port)


# update camera quality
def nao_set_camera_quality(quality):
    naoModule.camera_quality = quality


# update volume
def nao_set_volume(value):
    naoModule.set_volume(value)
    naoModule.say_phrase("My volume is now " + str(value))


# nao rotate head
def nao_rotate_head(window, app):
    hands = 0

    while hands == 0:
        hands = leapModule.count_hands()

    window.lbl_wait.hide()
    window.lbl_sldr_vertical.setText("Yaw")
    window.lbl_sldr_horiz.setText("Pitch")
    app.processEvents()
    # setup ui for motion

    extended_fingers = leapModule.get_extended_fingers()
    close_counter = 0
    local_action_list = []

    naoModule.set_stiffness()
    while close_counter < 300:
        if extended_fingers == 0:
            close_counter += 1
            # if fist gesture, close window
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

            # calculate pitch limitations based on yaw
            x = scale(scaled_angles1[1], -90, 90, -120, 120)
            pitch_max = \
                (2 * 10 ** -7) * (x ** 4) \
                + (2 * 10 ** -17) * (x ** 3) \
                - 0.0039 * (x ** 2) \
                + (7 * 10 ** -14) * x \
                + 27.918 \
                - 1

            pitch_min = \
                - (3 * 10 ** -7) * (x ** 4) \
                - (9 * 10 ** -18) * (x ** 3) \
                + 0.005 * (x ** 2) \
                + (6 * 10 ** -13) * x \
                + 42.134 \
                * -1

            # scale angles according to nao head limits
            scaled_angles2 = \
                [
                    scale(scaled_angles1[0], -90, 90, pitch_min, pitch_max),
                    scale(scaled_angles1[1], -90, 90, -120, 120)
                ]

            # scale angles and height according to output limits and update ui
            output_pitch = scale(scaled_angles2[0], pitch_min, pitch_max, 0, 99)
            output_yaw = scale(scaled_angles2[1], -120, 120, 0, 99)
            window.sldr_vertical.setValue(output_pitch)
            window.sldr_horiz.setValue(output_yaw)
            output_height = scale(scaled_height, 30, 90, 0, 99)
            window.sldr_height.setValue(output_height)
            app.processEvents()

            # convert angles to radian and send to nao
            rad_scaled_angles = [scaled_angles2[0] * -0.0174533, scaled_angles2[1] * -0.0174533]
            naoModule.rotate_head(rad_scaled_angles)

            # record action
            local_action_list.append({"type": "head", "parameters": rad_scaled_angles})
        extended_fingers = leapModule.get_extended_fingers()
    if len(local_action_list) > 0:
        record_action_list(local_action_list)


# nao walk
def nao_walk(window, app):
    hands = 0

    while hands == 0:
        hands = leapModule.count_hands()

    window.lbl_wait.hide()
    window.lbl_sldr_vertical.setText("Yaw")
    window.lbl_sldr_horiz.setText("Pitch")
    app.processEvents()
    # prepare ui for motion

    extended_fingers = leapModule.get_extended_fingers()
    close_counter = 0
    local_action_list = []

    naoModule.set_stiffness()
    while close_counter < 300:
        if extended_fingers == 0:
            close_counter += 1
            # close window on fist gesture
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

            # scale angles and height to output limits and output
            output_pitch = scaled_angles2[0]
            output_yaw = scaled_angles2[1]
            window.sldr_vertical.setValue(output_pitch)
            window.sldr_horiz.setValue(output_yaw)
            output_height = scale(scaled_height, 30, 90, 0, 99)
            window.sldr_height.setValue(output_height)
            app.processEvents()

            # check whether pitch is outside of movement threshold (outside of -30 - 30 range)
            scaled_pitch = scale(scaled_angles2[0], 0, 99, -0.1, 0.1)
            if -0.03 < scaled_pitch < 0.03:
                scaled_pitch = 0

            # check whether yaw is outside of movement threshold
            if scaled_angles2[1] < 33:
                rad_yaw = 20
            elif scaled_angles2[1] > 66:
                rad_yaw = -20
            else:
                rad_yaw = 0

            # convert yaw to radians and send to nao
            rad_yaw *= 0.0174533
            naoModule.move_walk_turn(scaled_pitch, rad_yaw)
            # record action
            local_action_list.append({"type": "walk", "parameters": [scaled_pitch, rad_yaw]})

        extended_fingers = leapModule.get_extended_fingers()
    naoModule.move_stop()
    # stop nao moving when out of motion loop
    if len(local_action_list) > 0:
        record_action_list(local_action_list)


# register camera
def nao_camera_register(widget):
    naoModule.initialise_video_proxy(widget)


# unregister camera
def nao_camera_unregister(widget):
    naoModule.destroy_video_proxy(widget)


# move naos arm, hand is left or right
def nao_arm(window, app, hand):
    hands = 0

    while hands == 0:
        hands = leapModule.count_hands()

    window.lbl_wait.hide()
    window.lbl_sldr_vertical.setText("Pitch")
    window.lbl_sldr_horiz.setText("Roll")
    window.lbl_title.setText("Movement Status - Shoulder")
    app.processEvents()
    # prepare window for motion

    joint_limits = naoModule.get_arm_joint_limits(hand)
    gesture = leapModule.get_hand_gesture()
    # get joint movement limits and current hand gesture
    close_counter = 0
    local_action_list = []

    naoModule.set_stiffness()
    while close_counter < 300:
        if gesture == 3:
            close_counter += 1
            # close window when hand gesture is fist
        else:
            height = leapModule.get_height()
            scaled_height = scale(height, 100, 500, 30, 90)

            angles = leapModule.get_pitch_yaw_roll()
            angles[2] *= -1  # invert roll
            # scale angles according to height for sensitivity
            angles_scaled_height = \
                [
                    scale(angles[0], -scaled_height, scaled_height, -90, 90),  # pitch
                    scale(angles[1], -scaled_height, scaled_height, -90, 90),  # yaw
                    scale(angles[2], -scaled_height, scaled_height, -90, 90)   # roll
                ]

            if gesture == 0:  # hand extended
                # move shoulder
                # scale angles according to nao arm limits
                scaled_limits = \
                    [
                        scale(angles_scaled_height[0],  # pitch
                              -90, 90,
                              joint_limits["shoulder_pitch_min"], joint_limits["shoulder_pitch_max"]),
                        scale(angles_scaled_height[2],  # roll
                              -90, 90,
                              joint_limits["shoulder_roll_min"], joint_limits["shoulder_roll_max"])
                    ]

                output_pitch = scale(scaled_limits[0],
                                     joint_limits["shoulder_pitch_min"], joint_limits["shoulder_pitch_max"],
                                     0, 99)
                output_roll = scale(scaled_limits[1],
                                    joint_limits["shoulder_roll_min"], joint_limits["shoulder_roll_max"],
                                    0, 99)

                window.sldr_vertical.setValue(output_pitch)
                window.sldr_horiz.setValue(output_roll)
                window.lbl_sldr_vertical.setText("Pitch")
                window.lbl_sldr_horiz.setText("Roll")
                window.lbl_title.setText("Movement Status - Shoulder")
                app.processEvents()

                scaled_radians = \
                    [
                        scaled_limits[0] * -0.0174533,
                        scaled_limits[1] * 0.0174533
                    ]

                naoModule.move_shoulder(scaled_radians, hand)
                local_action_list.append({"type": hand + "_shoulder", "parameters": scaled_radians})
            elif gesture == 1:  # middle three fingers extended
                # move elbow
                # scale angles according to nao arm limits
                scaled_limits = \
                    [
                        scale(angles_scaled_height[1],  # yaw
                              -90, 90,
                              joint_limits["elbow_yaw_min"], joint_limits["elbow_yaw_max"]),
                        scale(angles_scaled_height[2],  # roll
                              -90, 90,
                              joint_limits["elbow_roll_min"], joint_limits["elbow_roll_max"])
                    ]

                output_yaw = scale(scaled_limits[0],
                                   joint_limits["elbow_yaw_min"], joint_limits["elbow_yaw_max"],
                                   0, 99)
                output_roll = scale(scaled_limits[1],
                                    joint_limits["elbow_roll_min"], joint_limits["elbow_roll_max"],
                                    0, 99)

                window.sldr_vertical.setValue(output_roll)
                window.sldr_horiz.setValue(output_yaw)
                window.lbl_sldr_vertical.setText("Roll")
                window.lbl_sldr_horiz.setText("Yaw")
                window.lbl_title.setText("Movement Status - Elbow")

                app.processEvents()

                scaled_radians = \
                    [
                        scaled_limits[0] * -0.0174533,
                        scaled_limits[1] * 0.0174533
                    ]

                naoModule.move_elbow(scaled_radians, hand)
                local_action_list.append({"type": hand + "_elbow", "parameters": scaled_radians})
            elif gesture == 2: # outer two fingers extended
                # move wrist
                # scale angles according to nao arm limits
                scaled_limits = \
                    [
                        scale(angles_scaled_height[2],  # roll
                              -90, 90,
                              joint_limits["wrist_roll_min"], joint_limits["wrist_roll_max"])
                    ]

                output_roll = scale(scaled_limits[0],
                                    joint_limits["wrist_roll_min"], joint_limits["wrist_roll_max"],
                                    0, 99)

                window.sldr_vertical.setValue(50)
                window.sldr_horiz.setValue(output_roll)
                window.lbl_sldr_vertical.setText("N/A")
                window.lbl_sldr_horiz.setText("Roll")
                window.lbl_title.setText("Movement Status - Wrist")


                app.processEvents()

                scaled_radians = \
                    [
                        scaled_limits[0] * 0.0174533
                    ]

                naoModule.move_wrist(scaled_radians, hand)
                local_action_list.append({"type": hand + "_wrist", "parameters": scaled_radians})
            output_height = scale(scaled_height, 30, 90, 0, 99)
            window.sldr_height.setValue(output_height)

            app.processEvents()
        gesture = leapModule.get_hand_gesture()
    if len(local_action_list) > 0:
        record_action_list(local_action_list)


# add local action list to global action list
def record_action_list(local_action_list):
    global action_list
    action_list.append(local_action_list)


# print action list to list widget
def print_action_list(window):
    list_view = window.wgt_command_list
    list_view.clear()
    fps = leapModule.get_bandwidth_status()
    for local_action_list in action_list:
        # output format - "movement type - duration"
        # duration is estimated as number of actions recorded/leap motion fps
        if local_action_list[0]["type"] in ("left_shoulder", "left_elbow", "left_wrist"):
            output_string = "left arm - " + "{:.2f}".format(len(local_action_list)/fps) + "s"
        elif local_action_list[0]["type"] in ("right_shoulder", "right_elbow", "right_wrist"):
            output_string = "right arm - " + "{:.2f}".format(len(local_action_list)/fps) + "s"
        else:
            output_string = local_action_list[0]["type"] + " - " + "{:.2f}".format(len(local_action_list)/fps) + "s"
        list_view.addItem(output_string)


# parse individual action
def parse_action(action, frame_rate):
    if action["type"] == "head":
        naoModule.rotate_head(action["parameters"])
    elif action["type"] == "walk":
        naoModule.move_walk_turn(action["parameters"][0], action["parameters"][1])
    elif action["type"] == "say":
        naoModule.say_phrase(action["parameters"][0])
    elif action["type"] == "stand":
        naoModule.posture_stand()
    elif action["type"] == "left_shoulder":
        naoModule.move_shoulder(action["parameters"], "left")
    elif action["type"] == "left_elbow":
        naoModule.move_elbow(action["parameters"], "left")
    elif action["type"] == "left_wrist":
        naoModule.move_wrist(action["parameters"], "left")
    elif action["type"] == "right_shoulder":
        naoModule.move_shoulder(action["parameters"], "right")
    elif action["type"] == "right_elbow":
        naoModule.move_elbow(action["parameters"], "right")
    elif action["type"] == "right_wrist":
        naoModule.move_wrist(action["parameters"], "right")
    else:
        print "WIP: " + action["type"]
    time.sleep(frame_rate)
    # sleep required to force a delay in input being sent to nao


# play all actions
def play_all_actions(app):
    frame_rate = 1 / leapModule.get_bandwidth_status()
    naoModule.set_stiffness()
    for local_action_list in action_list:
        for action in local_action_list:
            parse_action(action, frame_rate)
            app.processEvents()


# play single action
def play_single_action(selected_index, app):
    frame_rate = 1 / leapModule.get_bandwidth_status()
    naoModule.set_stiffness()
    for action in action_list[selected_index]:
        parse_action(action, frame_rate)
        app.processEvents()


# move action up list
def move_action_up(selected_index):
    action_list.insert(selected_index - 1, action_list.pop(selected_index))


# move action down list
def move_action_down(selected_index):
    action_list.insert(selected_index + 1, action_list.pop(selected_index))


# delete action
def delete_action(selected_index):
    action_list.pop(selected_index)


# load actions from json file
def load_actions(data):
    import json
    try:
        loaded_data = json.loads(data)
        for local_action_list in loaded_data:
            record_action_list(local_action_list)
        return True
    except Exception, e:
        return False


# convert action list to json format

def json_encode_actions():
    import json
    return json.JSONEncoder().encode(action_list)
