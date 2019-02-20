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

    :type robot: rosebot.RoseBot
    :type run_data: m1_data_storage
    """
    camera_data_center = robot.sensor_system.camera.get_biggest_blob().center
    run_data.close_center_x = camera_data_center.x

def m1_calibrate_camera_far(robot, run_data):
    """
    This function obtains the camera's x, y, and area information when the ball is placed directly in front of the
    claw at the far end of the court. This will obtain the y at which the ball is far from the claw, the x at
    which the ball will be directly in the center, and the area upper bound for which the robot will be
    tracking the ball in.

    :type robot: rosebot.RoseBot
    :type run_data: m1_data_storage
    """



