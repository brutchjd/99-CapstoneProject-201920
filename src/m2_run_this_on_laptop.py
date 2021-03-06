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
    tabControl = ttk.Notebook(root)
    tab1 = ttk.Frame(tabControl)
    tabControl.add(tab1, text='Shared Gui')
    tabControl.pack(expand=1, fill='both')

    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab2, text='Individual')
    tabControl.pack(expand=1, fill='both')

    main_frame = ttk.Frame(tab1, padding=10, borderwidth=5, relief='groove')
    main_frame.pack()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, color_frame = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)
    proximity_frame, camera_frame = get_individual_frame(main_frame, mqtt_sender)
    shape_frame = get_shape_frame(tab2, mqtt_sender)
    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proximity_frame, color_frame, camera_frame,)
    shape_frame.pack()
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
    camera_frame = get_camera_frame(main_frame, mqtt_sender)

    return proximity_frame, camera_frame


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


def get_camera_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text='Find Object Camera')
    frame_label.grid(row=0, column=1)

    speed_label = ttk.Label(frame, text='Enter Speed:')
    area_label = ttk.Label(frame, text='Enter Area:')

    speed_entry = ttk.Entry(frame, width=12)
    area_entry = ttk.Entry(frame, width=12)

    clockwise_button = ttk.Button(frame, text='Spin Clockwise')
    counterclock_button = ttk.Button(frame, text='Spin Counterclockwise')

    speed_entry.grid(row=2, column=1)
    area_entry.grid(row=3, column=1)
    speed_label.grid(row=2, column=0)
    area_label.grid(row=3, column=0)

    clockwise_button.grid(row=1, column=0)
    counterclock_button.grid(row=1, column=2)

    clockwise_button["command"] = lambda: handle_camera_clockwise(speed_entry, area_entry, mqtt_sender)
    counterclock_button["command"] = lambda: handle_camera_counterclockwise(speed_entry, area_entry, mqtt_sender)

    return frame

def get_shape_frame(window, mqtt_sender):

    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text='Drive In Shape:')
    frame_label.grid(row=0, column=1)

    rectangle_button = ttk.Button(frame, text='Rectangle')
    rectangle_button.grid(row=1, column=0)

    triangle_button = ttk.Button(frame, text='Triangle')
    triangle_button.grid(row=1, column=1)

    circle_button = ttk.Button(frame, text='Circle')
    circle_button.grid(row=1, column=2)

    clear_button = ttk.Button(frame, text='Clear')
    clear_button.grid(row=3, column=1)

    speed_entry = ttk.Entry(frame, width=10)
    width_entry = ttk.Entry(frame, width=10)
    length_entry = ttk.Entry(frame, width=10)
    loops_entry = ttk.Entry(frame, width=10)
    duration_entry = ttk.Entry(frame, width=10)

    speed_label = ttk.Label(frame, text='Enter Speed:')
    width_label = ttk.Label(frame, text='Enter Width:')
    length_label = ttk.Label(frame, text='Enter Length/Inner Circle:')
    loops_label = ttk.Label(frame, text='Enter Loops:')
    duration_label = ttk.Label(frame, text='Enter Circle Duration:')

    speed_label.grid(row=4, column=0)
    speed_entry.grid(row=5, column=0)

    width_label.grid(row=6, column=0)
    width_entry.grid(row=7, column=0)

    length_label.grid(row=8, column=0)
    length_entry.grid(row=9, column=0)

    loops_label.grid(row=4, column=2)
    loops_entry.grid(row=5, column=2)

    duration_label.grid(row=6, column=2)
    duration_entry.grid(row=7, column=2)



    canvas = tkinter.Canvas(frame, width=750, height=500, bg='#a2a2a2')
    canvas.grid(row=2, column=1)

    rectangle_button["command"] = lambda: rectangle_functions(canvas, speed_entry, length_entry, width_entry, loops_entry, mqtt_sender)
    circle_button["command"] = lambda: circle_functions(canvas, speed_entry, length_entry, loops_entry, duration_entry, mqtt_sender)
    triangle_button["command"] = lambda: triangle_functions(canvas, speed_entry, length_entry, loops_entry, mqtt_sender)
    clear_button["command"] = lambda: canvas.delete('all')
    return frame

def handle_pickup_led(mqtt_sender):
    print('Pickup')
    mqtt_sender.send_message('m1_pickup_LED')


def handle_pickup(freq_entry, rate_entry, mqtt_sender):
    print('Pickup', freq_entry.get(), rate_entry.get())
    mqtt_sender.send_message('m3_pickup_tone', [freq_entry.get(), rate_entry.get()])


def handle_pickup_beep(rate_entry, mqtt_sender):
    print('Pickup', rate_entry.get())
    mqtt_sender.send_message('m2_pickup_beep', [rate_entry.get()])


def handle_camera_clockwise(speed_entry, area_entry, mqtt_sender):
    print('Find and Pickup', speed_entry.get(), area_entry.get())
    mqtt_sender.send_message('m2_camera_clockwise', [speed_entry.get(), area_entry.get()])


def handle_camera_counterclockwise(speed_entry, area_entry, mqtt_sender):
    print('Find and Pickup', speed_entry.get(), area_entry.get())
    mqtt_sender.send_message('m2_camera_counterclockwise', [speed_entry.get(), area_entry.get()])


def handle_rectangle(speed_entry, length_entry, width_entry, loops_entry, mqtt_sender):
    print('Drive Rectangle', speed_entry.get(), length_entry.get(), width_entry.get(), loops_entry.get())
    mqtt_sender.send_message('m2_rectangle', [speed_entry.get(), length_entry.get(), width_entry.get(), loops_entry.get()])


def handle_triangle(speed_entry, length_entry, loops_entry, mqtt_sender):
    print('Drive Triangle', speed_entry.get(), length_entry.get(), loops_entry.get())
    mqtt_sender.send_message('m2_triangle', [speed_entry.get(), length_entry.get(), loops_entry.get()])


def handle_circle(speed_entry, length_entry, loops_entry, duration_entry, mqtt_sender):
    print('Drive Circle', speed_entry.get(), length_entry.get(), loops_entry.get(), duration_entry.get())
    mqtt_sender.send_message('m2_circle', [speed_entry.get(), length_entry.get(), loops_entry.get(), duration_entry.get()])


def grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, proximity_frame, color_frame, camera_frame):
    teleop_frame.grid(row=3, column=2)
    arm_frame.grid(row=0, column=2)
    control_frame.grid(row=4, column=1)
    drive_frame.grid(row=1, column=1)
    sound_frame.grid(row=0, column=1)
    proximity_frame.grid(row=3, column=1)
    color_frame.grid(row=3, column=0)
    camera_frame.grid(row=0, column=0)

def rectangle_functions(canvas, speed_entry, length_entry, width_entry, loops_entry,  mqtt_sender):
    canvas.create_rectangle(150, 100, 600, 400, fill='#9a0000')
    handle_rectangle(speed_entry, length_entry, width_entry, loops_entry, mqtt_sender)

def triangle_functions(canvas, speed_entry, length_entry, loops_entry, mqtt_sender):
    canvas.create_polygon(150, 75, 600, 75, 375, 450, fill='#cc76e5')
    handle_triangle(speed_entry, length_entry, loops_entry, mqtt_sender)

def circle_functions(canvas, speed_entry, length_entry, loops_entry, duration_entry, mqtt_sender):
    canvas.create_oval(250, 150, 500, 400, fill='#0a8043')
    handle_circle(speed_entry, length_entry, loops_entry, duration_entry, mqtt_sender)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()