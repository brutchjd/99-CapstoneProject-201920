"""
  Capstone Project.  Code to call functions for sprint 3.

  Authors:  Your professors (for the framework)
    and Jared Brutcher.
  Winter term, 2018-2019.
"""

import rosebot
import time

def clockwise_find_object(robot, speed, area):
    """
    :type robot:    rosebot.RoseBot

    """
    robot.drive_system.spin_clockwise_until_sees_object(speed, area)
    #moves robot to have the object in the center of the claw
    robot.drive_system.right_motor.turn_on(speed)
    while True:
        blob_x = robot.sensor_system.camera.get_biggest_blob().center.x
        if blob_x > 160 and blob_x < 190:
            robot.drive_system.right_motor.turn_off()
            break
    robot.drive_system.go_forward_until_distance_is_less_than(2, speed)
    robot.arm_and_claw.raise_arm()

def counterclockwise_find_object(robot, speed, area):
    """
    :type robot:    rosebot.RoseBot

    """
    robot.drive_system.spin_counterclockwise_until_sees_object(speed, area)
    #moves robot to have the object in the center of the claw
    robot.drive_system.left_motor.turn_on(speed)
    while True:
        blob_x = robot.sensor_system.camera.get_biggest_blob().center.x
        if blob_x > 160 and blob_x < 190:
            robot.drive_system.left_motor.turn_off()
            break
    robot.drive_system.go_forward_until_distance_is_less_than(2, speed)
    robot.arm_and_claw.raise_arm()









