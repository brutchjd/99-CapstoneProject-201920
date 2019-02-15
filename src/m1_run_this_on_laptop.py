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

    teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, color_frame = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    find_object_frame = get_find_object_frame(main_frame, mqtt_sender)
    pickup_led_frame = get_pickup_LED_frame(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------

    grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, find_object_frame, color_frame, pickup_led_frame)

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
    rateincrease_label = ttk.Label(frame, text='Enter rate of increase (cycle/sec/inch):')

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
    mqtt_sender.send_message('clockwise_find_object', [speed_entry.get(), area_entry.get()])

def handle_counterclockwise(speed_entry, area_entry, mqtt_sender):
    print('Turn Clockwise and find Object')
    mqtt_sender.send_message('clockwise_find_object', [speed_entry.get(), area_entry.get()])

def handle_led_button(rateincrease_entry, intialrate_entry, mqtt_sender):
    print('Cycle Leds')
    mqtt_sender.send_message('m1_pickup_LED', [rateincrease_entry.get(), intialrate_entry.get()])

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()