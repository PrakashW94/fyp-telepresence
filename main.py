import commandModule

commands = ["1 - Head movement with Yaw (LR)", "2 - Head movement with Pitch (UD)", "3 - Walk linear", "4 - Walk rotate", "5 - Reset Pose"]
while 1:
    print "Menu"
    for command in commands:
        print command

    input_command = input("Enter a command")

    if input_command == 1:
        commandModule.nao_rotate_head_yaw()
    elif input_command == 2:
        commandModule.nao_rotate_head_pitch()
    elif input_command == 3:
        commandModule.nao_walk()
    elif input_command == 4:
        commandModule.nao_turn()
    elif input_command == 5:
        commandModule.nao_stand()
    elif input_command == 6:
        commandModule.nao_say("Good morning Firat, welcome to my demo!")
    elif input_command == 7:
        commandModule.test_func()
    else:
        print "Command not recognised"
