"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Nathaniel Craan, Daniel Decker and Jared Brutcher.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)


    return frame


def get_drive_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Drive System")
    speed_label = ttk.Label(frame, text="Enter speed:")
    inches_label = ttk.Label(frame, text="Enter Inches:")
    delta_label = ttk.Label(frame, text="Enter Delta:")
    seconds_button = ttk.Button(frame, text='Straight Using Seconds')
    inches_button = ttk.Button(frame, text='Straight Using Inches')
    encoder_button = ttk.Button(frame, text='Straight Using Encoder')
    greaterthan_button = ttk.Button(frame, text='Straight Until Greater Than')
    lessthan_button = ttk.Button(frame, text='Straight Until Less Than')
    within_button = ttk.Button(frame, text='Straight Until Within')
    display_camera_data_button = ttk.Button(frame, text='Print Camera Data')
    camera_clockwise = ttk.Button(frame, text='Spin Clockwise Till Object Seen')
    camera_counterclockwise = ttk.Button(frame, text='Spin Counterclockwise Till Object Seen')
    area_label = ttk.Label(frame, text='Enter Smallest Area of object to detect:')


    seconds_entry = ttk.Entry(frame, width=12)
    inches_entry = ttk.Entry(frame, width=12)
    encoder_entry = ttk.Entry(frame, width=12)
    speed_entry = ttk.Entry(frame, width=12)
    inches_entry = ttk.Entry(frame, width=12)
    inches2_entry = ttk.Entry(frame, width=12)
    delta_entry = ttk.Entry(frame, width=12)
    camera_area_entry = ttk.Entry(frame, width=12)


    frame_label.grid(row=0, column=1)
    speed_label.grid(row=8, column=0)
    inches_label.grid(row=6, column=0)
    delta_label.grid(row=7, column=0)

    speed_entry.grid(row=8, column=1)
    seconds_button.grid(row=1, column=0)
    inches_button.grid(row=2, column=0)
    encoder_button.grid(row=3, column=0)
    greaterthan_button.grid(row=5, column=0)
    lessthan_button.grid(row=5, column=1)
    within_button.grid(row=5, column=2)

    seconds_entry.grid(row=1, column=1)
    inches_entry.grid(row=2, column=1)
    encoder_entry.grid(row=3, column=1)
    inches2_entry.grid(row=6, column=1)
    delta_entry.grid(row=7, column=2)

    display_camera_data_button.grid(row=9, column=0)
    camera_clockwise.grid(row=9, column=1)
    camera_counterclockwise.grid(row=9, column=2)
    camera_area_entry.grid(row=10, column=1)
    area_label.grid(row=10, column=0)


    seconds_button["command"] = lambda: handle_seconds(seconds_entry, speed_entry, mqtt_sender)
    inches_button["command"] = lambda: handle_inches(inches_entry, speed_entry, mqtt_sender)
    encoder_button["command"] = lambda: handle_encoder(encoder_entry, speed_entry, mqtt_sender)
    greaterthan_button["command"] = lambda: handle_greaterthan(inches2_entry, speed_entry, mqtt_sender)
    lessthan_button["command"] = lambda: handle_lessthan(inches2_entry, speed_entry, mqtt_sender)
    within_button["command"] = lambda: handle_within(delta_entry, inches2_entry, speed_entry, mqtt_sender)
    display_camera_data_button['command'] = lambda: handle_camera_data(mqtt_sender)
    camera_counterclockwise['command'] = lambda: handle_camera_counterclockwise(camera_area_entry, speed_entry, mqtt_sender)
    camera_clockwise['command'] = lambda: handle_camera_clockwise(camera_area_entry, speed_entry, mqtt_sender)

    return frame


def get_sound_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Sound System")
    beep_button = ttk.Button(frame, text='Beep')
    frequency_button = ttk.Button(frame, text='Tone')
    speak_button = ttk.Button(frame, text='Speak')

    beep_entry = ttk.Entry(frame, width=12)
    frequency_entry = ttk.Entry(frame, width=12)
    duration_entry = ttk.Entry(frame, width=12)
    speak_entry = ttk.Entry(frame, width=12)

    frame_label.grid(row=0, column=1)
    beep_entry.grid(row=1, column=1)
    beep_button.grid(row=1, column=0)
    frequency_button.grid(row=2, column=0)
    frequency_entry.grid(row=2, column=1)
    duration_entry.grid(row=2, column=2)
    speak_button.grid(row=4, column=0)
    speak_entry.grid(row=4, column=1)

    speak_button["command"] = lambda: handle_speak(speak_entry, mqtt_sender)
    frequency_button["command"] = lambda: handle_frequency(frequency_entry, duration_entry, mqtt_sender)
    beep_button["command"] = lambda: handle_beep(beep_entry, mqtt_sender)

    return frame

def get_color_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='ridge')
    frame.grid()

    frame_label = ttk.Label(frame, text='Color Stuff')
    less_intensity_button = ttk.Button(frame, text='less_intensity')
    more_intensity_button = ttk.Button(frame, text='more_intensity')
    is_color_button = ttk.Button(frame, text='same_color')
    different_color = ttk.Button(frame, text='different_color')

    intensity_label = ttk.Label(frame, text='insert_intensity')
    intensity_entry = ttk.Entry(frame)

    color_label = ttk.Label(frame, text='insert_color')
    color_entry = ttk.Entry(frame)

    speed_label = ttk.Label(frame, text='insert_speed')
    speed_entry = ttk.Entry(frame)

    frame_label.grid(row=0, column=0)
    less_intensity_button.grid(row=1, column=1)
    more_intensity_button.grid(row=2, column=1)
    is_color_button.grid(row=3, column=1)
    different_color.grid(row=4, column=1)
    intensity_label.grid(row=1, column=2)
    color_label.grid(row=3, column=2)
    intensity_entry.grid(row=1, column=3)
    color_entry.grid(row=3, column=3)
    speed_label.grid(row=4, column=2)
    speed_entry.grid(row=4, column=3)

    less_intensity_button["command"] = lambda: handle_intensity_button1(intensity_entry, speed_entry, mqtt_sender)
    more_intensity_button["command"] = lambda: handle_intensity_button2(intensity_entry, speed_entry, mqtt_sender)
    is_color_button["command"] = lambda: handle_color_button1(color_entry, speed_entry, mqtt_sender)
    different_color["command"] = lambda: handle_color_button2(color_entry, speed_entry, mqtt_sender)

    return frame

###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('Forward', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("forward", [left_entry_box.get(), right_entry_box.get()])


def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('Backward', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("backward", [left_entry_box.get(), right_entry_box.get()])


def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('left', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("left", [left_entry_box.get(), right_entry_box.get()])


def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('right', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("right", [left_entry_box.get(), right_entry_box.get()])


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Stop')
    mqtt_sender.send_message("stop")

###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print("Raise Arm")
    mqtt_sender.send_message('raise_arm')

def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print("Lower Arm")
    mqtt_sender.send_message('lower')

def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Calibrating Arm')
    mqtt_sender.send_message('calibrate')

def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print('Move To Position', arm_position_entry.get())
    mqtt_sender.send_message('position', [arm_position_entry.get()])


###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print('Quit')
    mqtt_sender.send_message('quit')


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print('Exit')
    handle_quit(mqtt_sender)
    exit()


##############################################################################
# Handlers for Buttons in the Drive System frame.
##############################################################################
def handle_seconds(seconds_entry, speed_entry, mqtt_sender):
    print('Drive Straight (Seconds)', seconds_entry.get(), speed_entry.get())
    mqtt_sender.send_message('seconds',[seconds_entry.get(), speed_entry.get()])


def handle_inches(inches_entry, speed_entry, mqtt_sender):
    print('Drive Straight (Inches)', inches_entry.get(), speed_entry.get())
    mqtt_sender.send_message('inches', [inches_entry.get(), speed_entry.get()])


def handle_encoder(encoder_entry, speed_entry, mqtt_sender):
    print('Drive Straight (Encoder)', encoder_entry.get(), speed_entry.get())
    mqtt_sender.send_message('encoder', [encoder_entry.get(), speed_entry.get()])


def handle_greaterthan(inches2_entry, speed_entry, mqtt_sender):
    print('Drive Backward Until Greater Than', inches2_entry.get(), speed_entry.get())
    mqtt_sender.send_message('greaterthan', [inches2_entry.get(), speed_entry.get()])


def handle_lessthan(inches2_entry, speed_entry, mqtt_sender):
    print('Drive Forward Until Less Than', inches2_entry.get(), speed_entry.get())
    mqtt_sender.send_message('lessthan', [inches2_entry.get(), speed_entry.get()])


def handle_within(delta_entry, inches2_entry, speed_entry, mqtt_sender):
    print('Drive Straight Until Within', delta_entry.get(), inches2_entry.get(), speed_entry.get())
    mqtt_sender.send_message('within', [delta_entry.get(), inches2_entry.get(), speed_entry.get()])

def handle_camera_data(mqtt_sender):
    print('Print Camera Data')
    mqtt_sender.send_message('camera_data')

def handle_camera_counterclockwise(area_entry, speed_entry, mqtt_sender):
    print('Turn counter clockwise till object detected', area_entry.get(), speed_entry.get())
    mqtt_sender.send_message('camera_counterclockwise', [area_entry.get(), speed_entry.get()])

def handle_camera_clockwise(area_entry, speed_entry, mqtt_sender):
    print('Turn clockwise till object detected', area_entry.get(), speed_entry.get())
    mqtt_sender.send_message('camera_clockwise', [area_entry.get(), speed_entry.get()])


##############################################################################
# Handlers for Buttons in the Sound System frame.
##############################################################################
def handle_beep(beep_entry, mqtt_sender):
    print('Beeping', beep_entry.get(), 'times')
    mqtt_sender.send_message('beep', [beep_entry.get()])


def handle_frequency(frequency_entry, duration_entry, mqtt_sender):
    print('Frequency:', frequency_entry.get())
    mqtt_sender.send_message('frequency', [frequency_entry.get(), duration_entry.get()])


def handle_speak(speak_entry, mqtt_sender):
    print('Saying:', speak_entry.get())
    mqtt_sender.send_message('speak', [speak_entry.get()])

##############################################################################
# Handlers for Buttons in the color sensor frame.
##############################################################################

def handle_intensity_button1(intensity_entry, speed_entry, mqtt_sender):
    print('Drive Straight Until Intensity Less Than', intensity_entry.get(), speed_entry.get())
    mqtt_sender.send_message('intensity_less', [intensity_entry.get(), speed_entry.get()])


def handle_intensity_button2(intensity_entry, speed_entry, mqtt_sender):
    print('Drive Straight Until Intensity Greater Than', intensity_entry.get(), speed_entry.get())
    mqtt_sender.send_message('intensity_more', [intensity_entry.get(), speed_entry.get()])


def handle_color_button1(color_entry, speed_entry, mqtt_sender):
    print('Straight Until Color Is', color_entry.get(), speed_entry.get())
    mqtt_sender.send_message('color_equal', [color_entry.get(), speed_entry.get()])


def handle_color_button2(color_entry, speed_entry, mqtt_sender):
    print('Straight Until Color Is Not', color_entry.get(), speed_entry.get())
    mqtt_sender.send_message('color_different', [color_entry.get(), speed_entry.get()])



