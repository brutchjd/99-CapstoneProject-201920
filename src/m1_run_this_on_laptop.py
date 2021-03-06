"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Jared Brutcher.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------

    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------

    root = tkinter.Tk()
    root.title('CSSE 120 Capstone Project, Winter 2018-19')

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------

    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------

    #teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, color_frame = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    #find_object_frame = get_find_object_frame(main_frame, mqtt_sender)
    #pickup_led_frame = get_pickup_LED_frame(main_frame, mqtt_sender)

    #test_frame = get_sprint_3_test_frame(main_frame, mqtt_sender)
    sp3f = get_sprint_3_frame(main_frame, mqtt_sender)
    #control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------

    #grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, find_object_frame, color_frame, pickup_led_frame)

    #test_frame.grid(row=1, column=2)
    #control_frame.grid(row=0, column=0)
    sp3f.grid(row=0, column=0)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------

    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    drive_frame = shared_gui.get_drive_frame(main_frame, mqtt_sender)
    sound_frame = shared_gui.get_sound_frame(main_frame, mqtt_sender)
    color_frame = shared_gui.get_color_frame(main_frame, mqtt_sender)

    return teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, color_frame

def grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, find_object_frame, color_frame, pickup_led_frame):
    teleop_frame.grid(row=0,column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    drive_frame.grid(row=0, column=1)
    sound_frame.grid(row=1, column=1)
    find_object_frame.grid(row=3, column=0)
    color_frame.grid(row=2, column=1)
    pickup_led_frame.grid(row=3, column =1)

def get_find_object_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text='Find Object LED')
    clockwise_button = ttk.Button(frame, text='Turn Clockwise and Pick Up Object')
    counterclockwise_button = ttk.Button(frame, text='Turn Counterclockwise and Pick Up Object')

    speed_label = ttk.Label(frame, text='Enter Speed:')
    speed_entry = ttk.Entry(frame)

    area_label = ttk.Label(frame, text='Enter Min Area:')
    area_entry = ttk.Entry(frame)

    frame_label.grid(row=0, column=1)
    clockwise_button.grid(row=1, column=0)
    counterclockwise_button.grid(row=1, column=2)
    speed_label.grid(row=2, column=0)
    speed_entry.grid(row=2, column=1)
    area_label.grid(row=3, column=0)
    area_entry.grid(row=3, column=1)

    clockwise_button['command'] = lambda: handle_clockwise(speed_entry, area_entry, mqtt_sender)
    counterclockwise_button['command'] = lambda: handle_counterclockwise(speed_entry, area_entry, mqtt_sender)

    return frame

def get_pickup_LED_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text='Cycle LED')
    led_button = ttk.Button(frame, text='Cycle LED')
    intialrate_entry = ttk.Entry(frame)
    rateincrease_entry = ttk.Entry(frame)

    intialrate_label = ttk.Label(frame, text='Enter initial rate (cycle/sec):')
    rateincrease_label = ttk.Label(frame, text='Enter rate of increase (cycle*inches/sec):')

    frame_label.grid(row=0, column=0)
    led_button.grid(row=1, column=1)
    intialrate_label.grid(row=2, column=0)
    rateincrease_label.grid(row=3, column=0)
    intialrate_entry.grid(row=2, column=1)
    rateincrease_entry.grid(row=3, column=1)

    led_button['command'] = lambda: handle_led_button(rateincrease_entry, intialrate_entry, mqtt_sender)

    return frame


def handle_clockwise(speed_entry, area_entry, mqtt_sender):
    print('Turn Clockwise and find Object')
    mqtt_sender.send_message('m1_clockwise_find_object', [speed_entry.get(), area_entry.get()])

def handle_counterclockwise(speed_entry, area_entry, mqtt_sender):
    print('Turn Clockwise and find Object')
    mqtt_sender.send_message('m1_counterclockwise_find_object', [speed_entry.get(), area_entry.get()])

def handle_led_button(rateincrease_entry, intialrate_entry, mqtt_sender):
    print('Cycle Leds')
    mqtt_sender.send_message('m1_pickup_LED', [rateincrease_entry.get(), intialrate_entry.get()])

# Sprint 3 Gui Frames

def get_sprint_3_test_frame(window, mqtt_sender):
    """
    This function obtains the GUI frame for running tests on the
    individual functions and small groups of functions that are
    used in sprint 3.
    """
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text='Sprint 3 Tests')
    close_calibration_button = ttk.Button(frame, text='Run Test m1_calibrate_camera_close')
    far_calibration_button = ttk.Button(frame, text='Run Test m1_calibrate_camera_far')
    get_direction_button = ttk.Button(frame, text='Run Test m1_get_direction')
    dive_button = ttk.Button(frame, text='Run Test m1_dive_for_ball')

    frame_label.grid(row=0, column=1)
    close_calibration_button.grid(row=2, column=1)
    far_calibration_button.grid(row=2, column=0)
    get_direction_button.grid(row=3, column=1)
    dive_button.grid(row=4, column=1)

    far_calibration_button['command'] = lambda: handle_far_calibration(mqtt_sender)
    close_calibration_button['command'] = lambda: handle_close_calibration(mqtt_sender)
    get_direction_button['command'] = lambda: handle_get_direction(mqtt_sender)
    dive_button['command'] = lambda: handle_dive_button(mqtt_sender)

    return frame

def get_sprint_3_frame(window, mqtt_sender):
    """
    This function obtains the GUI frame for the actual run of the
    program.
    """
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    camera_cal_label = ttk.Label(frame, text='Camera Calibration')
    close_calibration_button = ttk.Button(frame, text='Close Ball Calibration')
    far_calibration_button = ttk.Button(frame, text='Far Ball Calibration')
    help_label = ttk.Label(frame, text='Click here to find out how to play!')
    help_button = ttk.Button(frame, text='Instructions')

    game_label = ttk.Label(frame, text='Game Controls')
    score_entry_label = ttk.Label(frame, text='Enter Score to Play to: ')
    difficulty_label = ttk.Label(frame, text='Enter Difficulty (1-5): ')
    difficulty_entry = ttk.Entry(frame)
    score_entry = ttk.Entry(frame)
    game_start = ttk.Button(frame, text='Start Game')
    round_button = ttk.Button(frame, text='Next Round')

    #scoreboard_label = ttk.Label(frame, text='Scoreboard')
    #player_label = ttk.Label(frame, text='Player')
    #robot_label = ttk.Label(frame, text='Robot')
    #goal_label = ttk.Label(frame, text='Goal')

    #player_score = ttk.Label(frame, text='0')
    #robot_score = ttk.Label(frame, text='0')
    #goal_score = ttk.Label(frame, text=score_entry.get())

    #grids
    help_label.grid(row=0, column=0)
    help_button.grid(row=0, column=1)
    camera_cal_label.grid(row=1, column=0)
    close_calibration_button.grid(row=2, column=0)
    far_calibration_button.grid(row=2, column=1)
    game_label.grid(row=3, column=0)
    score_entry.grid(row=4, column=1)
    score_entry_label.grid(row=4, column=0)
    difficulty_label.grid(row=5, column=0)
    difficulty_entry.grid(row=5, column=1)
    game_start.grid(row=6, column=0)
    round_button.grid(row=6, column=1)
    #scoreboard_label.grid(row=7, column=0)
    #player_label.grid(row=8, column=0)
    #robot_label.grid(row=8, column=1)
    #goal_label.grid(row=8, column=2)
    #player_score.grid(row=9, column=0)
    #robot_score.grid(row=9, column=1)
    #goal_score.grid(row=9, column=2)

    #shared frames
    teleop_frame = shared_gui.get_teleoperation_frame(window, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(window, mqtt_sender)
    control_frame = shared_gui.get_control_frame(window, mqtt_sender)

    #shared frames grid
    teleop_frame.grid(row=7, column=0)
    arm_frame.grid(row=8, column=0)
    control_frame.grid(row=9, column=0)

    far_calibration_button['command'] = lambda: handle_far_cal(mqtt_sender)
    close_calibration_button['command'] = lambda: handle_close_cal(mqtt_sender)
    help_button['command'] = lambda: handle_help()

    game_start['command'] = lambda: handle_game_start(mqtt_sender, score_entry.get(), difficulty_entry.get())
    round_button['command'] = lambda: handle_round_button(mqtt_sender)

    return frame

# Handles for run time buttons

def handle_help():
    file = open('m1_instructions.txt', 'r')
    for k in file:
        print(k)

def handle_far_cal(mqtt_sender):
    print('Sending Far Calibration')
    mqtt_sender.send_message('m1_far_calibration', [])

def handle_close_cal(mqtt_sender):
    print('Sending Close Calibration')
    mqtt_sender.send_message('m1_close_calibration', [])

def handle_game_start(mqtt_sender, score, difficulty):
    print('Starting Game')
    mqtt_sender.send_message('m1_start_game', [int(score), int(difficulty)])

def handle_round_button(mqtt_sender):
    print('Next Round')
    mqtt_sender.send_message('m1_round', [])

# Handles for test buttons

def handle_far_calibration(mqtt_sender):
    print('Sending Test Far Calibration')
    mqtt_sender.send_message('m1_test_far_calibration', [])

def handle_close_calibration(mqtt_sender):
    print('Sending Test Close Calibration')
    mqtt_sender.send_message('m1_test_close_calibration', [])

def handle_get_direction(mqtt_sender):
    print('Sending Test Get Direction')
    mqtt_sender.send_message('m1_test_get_direction', [])

def handle_dive_button(mqtt_sender):
    print('Sending Test Dive')
    mqtt_sender.send_message('m1_test_dive', [])

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()