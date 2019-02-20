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
        # camera prediction variables
        self.ball_direction = ''
        # robot movement/difficulty variables
        self.speed = 0
        self.turn_time = 0.4 #preset based on tests
        self.turn_time_threshold = 0.0

    def set_difficulty(self, diff):
        # sets the difficulty based on the presets 1 through 5
        self.speed = diff * 20
        self.turn_time_threshold = diff * 0.05



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

def m1_get_direction(robot, run_data):
    """
    Obtains three readings of the camera 1 milisecond apart in order
    to predict 1st if the ball is moving towards the goal (area
    getting bigger) and to see of the ball is moving to the left or
    right.

    Mutates the run_data direction instance variable to say if it
    is going 'left' or 'right' based on the predict position function

    Only breaks the loop when the ball is coming towards the robot.

    Also checks to see if the ball is within the court by comparing
    with the camera calibration values.

    Once loop is broken the robot moving function is called.

    :type robot: rosebot.RoseBot
    :type run_data: m1_data_storage
    """

    while True:
        area1 = robot.sensor_system.camera.get_biggest_blob().height * robot.sensor_system.camera.get_biggest_blob().width
        x_pos1 = robot.sensor_system.camera.get_biggest_blob().center.x
        time.sleep(0.001)
        area2 = robot.sensor_system.camera.get_biggest_blob().height * robot.sensor_system.camera.get_biggest_blob().width
        x_pos2 = robot.sensor_system.camera.get_biggest_blob().center.x
        time.sleep(0.001)
        area3 = robot.sensor_system.camera.get_biggest_blob().height * robot.sensor_system.camera.get_biggest_blob().width
        x_pos3 = robot.sensor_system.camera.get_biggest_blob().center.x

        # checks if ball is in court
        if area1 > run_data.min_area and area1 < run_data.max_area:
            # checks if ball is moving toward the goal
            if area3 > area2 and area2 > area1:
                # sends the positional information to the function
                # that will determine the balls direction
                print('Ball is coming')
                run_data.ball_direction = m1_predict_direction(x_pos1, x_pos2, x_pos3)
                break
    #makes the robot goalie dive in the predicted direction
    m1_dive_for_ball(robot, run_data)

def m1_predict_direction(x1, x2, x3):
    """
    Returns the prediction of the balls velocity direction to
    the get position function based off of positional data over
    time.
    """

    #checks if ball is moving left or right
    if x1 < x2 < x3:
        print('Ball is moving right')
        return 'right'
    else:
        print('Ball is moving left')
        return 'left'

def m1_dive_for_ball(robot, run_data):
    """
    Makes the robot goalie "dive" for the ball in the predicted
    direction. The directional information is stored in the
    run_data object.

    The robot goalie will only be able to move within the colored
    section of the court (The goalie box).

    The amount the robot turns will be a random time within a
    threshold to make it more like a realistic goalie that makes
    errors. It will also go at the speed found in run_data object
    based on the chosen difficulty setting.

    :type robot: rosebot.RoseBot
    :type run_data: m1_data_storage
    """

    if run_data.ball_direction == 'left':
        l = -1
        r = 1
    if run_data.ball_direction == 'right':
        l = 1
        r = -1

    robot.drive_system.left_motor.turn_on(l * run_data.speed)
    robot.drive_system.right_motor.turn_on(r * run_data.speed)
    time.sleep()