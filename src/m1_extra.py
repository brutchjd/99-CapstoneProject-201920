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
    m1_pick_up_LED(robot, speed)


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
    m1_pick_up_LED(robot, speed)


def m1_pick_up_LED(robot, speed, rate, rate_increase):
    go_until_distance_is_within_LED(robot, 0, speed, rate, rate_increase)
    robot.arm_and_claw.raise_arm()


def go_until_distance_is_within_LED(robot, inches, speed, rate, rate_increase):
    """
    :type robot:    rosebot.RoseBot
    """
    start = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    print(start)

    if start > inches:
        k=1
    else:
        k=-1
    robot.drive_system.go(k * speed, k * speed)
    while True:
        test = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        cycle_LEDs(robot, rate, rate_increase, distance)
        print(test)
        if test >= (inches - 2) and test <= (inches + 2):
            print(test)
            robot.drive_system.left_motor.turn_off()
            robot.drive_system.right_motor.turn_off()
            break



def cycle_LEDs(robot, rate, rate_increase, distance):
    """
    :type robot:    rosebot.RoseBot
    """
    robot.led_system.left_led.turn_on()
    time.sleep((1/(rate + rate_increase/distance))/4)
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_on()
    time.sleep((1/(rate + rate_increase/distance))/4)
    robot.led_system.left_led.turn_on()
    time.sleep((1/(rate + rate_increase/distance))/4)
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_off()
    time.sleep((1/(rate + rate_increase/distance))/4)








