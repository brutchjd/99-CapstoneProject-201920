"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Daniel Decker.
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
    root.title('Ultra Project')

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, drive_frame, sound_frame = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    proximity_frame = get_individual_frame(main_frame, mqtt_sender)
    color_frame = get_second_individual_frame(main_frame, mqtt_sender)
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

    return teleop_frame, arm_frame, control_frame, drive_frame, sound_frame


def get_individual_frame(main_frame, mqtt_sender):
    proximity_frame = get_proximity_frame(main_frame, mqtt_sender)
    return proximity_frame


def get_second_individual_frame(main_frame, mqtt_sender):
    color_frame = get_color_frame(main_frame, mqtt_sender)
    return color_frame


def get_proximity_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text='Pick Up with Tones')

    pickup_button = ttk.Button(frame, text='Pick Up')

    frame_label.grid(row=0, column=1)
    pickup_button.grid(row=1, column=1)

    pickup_button["command"] = lambda: handle_pickup(mqtt_sender)

    return frame


def get_color_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='ridge')
    frame.grid()
    frame_label = ttk.Label(frame, text='Color')

    color_button = ttk.Button(frame, text='Choose Color')

    frame_label.grid(row=0, column=1)
    color_button.grid(row=1, column=1)

    color_button["command"] = lambda: handle_color(mqtt_sender)

    return frame


def intensity_button1(intensity_entry, speed_entry, mqtt_sender):
    print('Drive Straight Until Intensity Less Than', intensity_entry.get(), speed_entry.get())
    mqtt_sender.send_message('intensity', [intensity_entry.get(), speed_entry.get()])


def intensity_button2(intensity_entry, speed_entry, mqtt_sender):
    print('Drive Straight Until Intensity Graeter Than', intensity_entry.get(), speed_entry.get())
    mqtt_sender.send_message('intensity', [intensity_entry.get(), speed_entry.get()])


def color_button1(color_entry, speed_entry, mqtt_sender):
    print('Straight Until Color Is', color_entry.get(), speed_entry.get())
    mqtt_sender.send_message('color', [color_entry.get(), speed_entry.get()])


def color_button2(color_entry, speed_entry, mqtt_sender):
    print('Straight Until Color Is Not', color_entry.get(), speed_entry.get())
    mqtt_sender.send_message('color', [color_entry.get(), color_entry.get()])



def handle_pickup(mqtt_sender):
    print('Pickup')
    mqtt_sender.send_message('m2_pickup_tone')


def handle_color(mqtt_sender):
    print('Color')
    mqtt_sender.send_message('m3_color')


def grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proximity_frame, color_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    drive_frame.grid(row=0, column=1)
    sound_frame.grid(row=1, column=1)
    proximity_frame.grid(row=2, column=1)
    color_frame.grid(row=2, column=2)
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()