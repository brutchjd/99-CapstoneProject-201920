"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Nathaniel Craan.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui
import shared_gui_delegate_on_robot


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
    root.title('Capstone Project')

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
    proximity_frame = get_individual_frame(main_frame, mqtt_sender)
    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proximity_frame, color_frame)

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


def get_individual_frame(main_frame, mqtt_sender):
    proximity_frame = get_proximity_frame(main_frame, mqtt_sender)
    return proximity_frame


def get_proximity_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text='Pick Up')
    freq_label = ttk.Label(frame, text='Frequency:')
    rate_label = ttk.Label(frame, text='Rate:')

    rate_entry = ttk.Entry(frame, width=12)
    freq_entry = ttk.Entry(frame, width=12)

    pickup_button = ttk.Button(frame, text='Pick Up Tone')
    pickup2_button = ttk.Button(frame, text='Pick Up Beep')
    pickup3_button = ttk.Button(frame, text='Pick UP LED')

    frame_label.grid(row=0, column=1)
    freq_label.grid(row=0, column=2)
    rate_label.grid(row=0, column=3)
    rate_entry.grid(row=1, column=3)
    freq_entry.grid(row=1, column=2)

    pickup_button.grid(row=1, column=1)
    pickup2_button.grid(row=2, column=1)
    pickup3_button.grid(row=3, column=1)

    pickup_button["command"] = lambda: handle_pickup(freq_entry, rate_entry, mqtt_sender)
    pickup2_button["command"] = lambda: handle_pickup_beep(rate_entry, mqtt_sender)
    pickup3_button["command"] = lambda: handle_pickup_led(mqtt_sender)

    return frame


def handle_pickup_led(mqtt_sender):
    print('Pickup')
    mqtt_sender.send_message('m1_pickup_LED')


def handle_pickup(freq_entry, rate_entry, mqtt_sender):
    print('Pickup', freq_entry.get(), rate_entry.get())
    mqtt_sender.send_message('m2_pickup_tone', [freq_entry.get(), rate_entry.get()])


def handle_pickup_beep(rate_entry, mqtt_sender):
    print('Pickup', rate_entry.get())
    mqtt_sender.send_message('m2_pickup_beep', [rate_entry.get()])


def grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proximity_frame, color_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    drive_frame.grid(row=0, column=1)
    sound_frame.grid(row=1, column=1)
    proximity_frame.grid(row=2, column=1)
    color_frame.grid(row=3, column=1)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()