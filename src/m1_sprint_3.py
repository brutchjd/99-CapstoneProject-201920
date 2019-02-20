"""
  Capstone Project.  Code to call functions for sprint 3.

  Authors:  Your professors (for the framework)
    and Jared Brutcher.
  Winter term, 2018-2019.
"""

import rosebot
import time

class m1_data_storage(object):
    """
    This class is used to store data during the run all in one place.
    The functions called in the program will be able to mutate and
    obtain the data in an object called run_data that is of
    this class.
    This object is to be defined in m1_run_on_this_robot and passed
    to the functions via the delegate for the main run.
    For test functions it will be defined in the delegate.
    """
    def __init__(self):
        # camera calibration variables
        self.close_center_x = 0
        self.close_center_y = 0
        self.far_center_x = 0
        self.far_center_y = 0
        self.max_area = 0
        self.min_area = 0


def m1_calibrate_camera_close(robot, run_data):
    """
    This function obtains the camera's x, y, and area information when the ball is placed directly in front of the
    claw. This will obtain the y at which the ball is close to the claw, the x at which the ball will be directly
    in the center, and the area upper bound for which the robot will be tracking the ball in.

    Mutates the run_data variable

    :type robot: rosebot.RoseBot
    :type run_data: m1_data_storage
    """
    run_data.close_center_x = robot.sensor_system.camera.get_biggest_blob().center.x
    run_data.close_center_y = robot.sensor_system.camera.get_biggest_blob().center.y
    run_data.max_area = robot.sensor_system.camera.get_biggest_blob().height * robot.sensor_system.camera.get_biggest_blob().width


def m1_calibrate_camera_far(robot, run_data):
    """
    This function obtains the camera's x, y, and area information when the ball is placed directly in front of the
    claw at the far end of the court. This will obtain the y at which the ball is far from the claw, the x at
    which the ball will be directly in the center, and the area upper bound for which the robot will be
    tracking the ball in.

    Mutates the run_data object

    :type robot: rosebot.RoseBot
    :type run_data: m1_data_storage
    """

    run_data.far_center_x = robot.sensor_system.camera.get_biggest_blob().center.x
    run_data.far_center_y = robot.sensor_system.camera.get_biggest_blob().center.y
    run_data.min_area = robot.sensor_system.camera.get_biggest_blob().height * robot.sensor_system.camera.get_biggest_blob().width

def m1_predict_direction(robot, run_data):
    """
    Obtains three readings of the camera 1 milisecond apart in order
    to predict 1st if the ball is moving towards the goal (area
    getting bigger) and to see of the ball is moving to the left or
    right.

    Mutates the run_data direction instance variable to say if it
    is going 'left' or 'right'

    Only breaks the loop when the ball is coming towards the robot.

    Also checks to see if the ball is within the court by comparing
    with the camera calibration values.

    :type robot: rosebot.RoseBot
    :type run_data: m1_data_storage
    """

    while True:
        area1 = robot.sensor_system.camera.get_biggest_blob().height * robot.sensor_system.camera.get_biggest_blob().width
        x_pos1 = robot.sensor_system.camera.get_biggest_blob().center.x
        y_pos_original = robot.sensor_system.camera.get_biggest_blob().center.y
        time.sleep(0.001)
        area2 = robot.sensor_system.camera.get_biggest_blob().height * robot.sensor_system.camera.get_biggest_blob().width
        x_pos2 = robot.sensor_system.camera.get_biggest_blob().center.x
        time.sleep(0.001)
        area3 = robot.sensor_system.camera.get_biggest_blob().height * robot.sensor_system.camera.get_biggest_blob().width
        x_pos3 = robot.sensor_system.camera.get_biggest_blob().center.x

        #checks if ball is in court
        if area1 > run_data.min_area and area1 < run_data.max_area:
            # checks if ball is coming towards the goal
            