"""
  Capstone Project.  Code to call functions for sprint 3.

  Authors:  Your professors (for the framework)
    and Nathaniel Craan
  Winter term, 2018-2019.
"""




import rosebot
import time
#import tkinter
#from tkinter import ttk
#import m2_run_this_on_laptop as m2L


def m2_pickup_beep(rate):
    robot = rosebot.RoseBot()
    go_until_distance_is_within_beep(robot, 2, 0, 25, rate)
    robot.arm_and_claw.raise_arm()


def m2_camera_clockwise(speed, area):
    robot = rosebot.RoseBot()
    robot.drive_system.spin_clockwise_until_sees_object(speed, area)

    robot.drive_system.right_motor.turn_on(speed)
    while True:
        object_x = robot.sensor_system.camera.get_biggest_blob().center.x
        if object_x > 150 and object_x < 200:
            robot.drive_system.right_motor.turn_off()
            break
    m2_pickup_beep(10)


def m2_camera_counterclockwise(speed, area):
    robot = rosebot.RoseBot()
    robot.drive_system.spin_counterclockwise_until_sees_object(speed, area)

    robot.drive_system.left_motor.turn_on(speed)
    while True:
        object_x = robot.sensor_system.camera.get_biggest_blob().center.x
        if object_x > 150 and object_x < 200:
            robot.drive_system.left_motor.turn_off()
            break
    m2_pickup_beep(10)


def go_until_distance_is_within_beep(robot, delta, inches, speed, rate):
    start = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    print(start)

    if start > inches + delta:
        robot.drive_system.go(speed, speed)
        while True:
            test = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            robot.sound_system.beeper.beep()
            time.sleep(1 / (rate *(distance + 0.00001)))
            print(test)
            if test >= (inches - delta) and test <= (inches + delta):
                print(test)
                robot.drive_system.left_motor.turn_off()
                robot.drive_system.right_motor.turn_off()
                break

    if start < inches + delta:
        robot.drive_system.go(-1 * speed, -1 * speed)
        while True:
            test = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            robot.sound_system.beeper.beep()
            time.sleep(1 / (rate *(distance + 0.00001)))
            print(test)
            if test >= (inches - delta) and test <= (inches + delta):
                print(test)
                robot.drive_system.left_motor.turn_off()
                robot.drive_system.right_motor.turn_off()
                break


def map_rectangle(speed, width, length, loops):
    robot = rosebot.RoseBot()

    while True:
        if robot.sensor_system.color_sensor.get_color_as_name() == 'Blue' or robot.sensor_system.color_sensor.get_color() == 2:
            robot.drive_system.go_until_distance_is_within(2, 0, 25)
            robot.arm_and_claw.raise_arm()
            for k in range(loops):
                for _ in range(2):
                    robot.drive_system.go_straight_for_inches_using_encoder(length, speed)
                    robot.drive_system.left_motor.turn_on(speed)
                    start = time.time()
                    while True:
                        current = time.time()
                        if current - start >= 1:
                            break
                    robot.drive_system.left_motor.turn_off()
                    robot.drive_system.go_straight_for_inches_using_encoder(width, speed)
                    robot.drive_system.left_motor.turn_on(speed)
                    start = time.time()
                    while True:
                        current = time.time()
                        if current - start >= 1:
                            break
                    robot.drive_system.left_motor.turn_off()
                    break


def map_triangle(speed, length, loops):
    robot = rosebot.RoseBot()
    while True:
        if robot.sensor_system.color_sensor.get_color_as_name() == 'Blue' or robot.sensor_system.color_sensor.get_color() == 2:
            robot.drive_system.go_until_distance_is_within(2, 0, 25)
            robot.arm_and_claw.raise_arm()
            for k in range(loops):
                for _ in range(2):
                    robot.drive_system.go_straight_for_inches_using_encoder(length, speed)
                    robot.drive_system.left_motor.turn_on(speed)
                    start = time.time()
                    while True:
                        current = time.time()
                        if current - start >= 1:
                            break
                    robot.drive_system.left_motor.turn_off()
                    break


def map_circle(speed, length, loops, duration):
    robot = rosebot.RoseBot()
    while True:
        if robot.sensor_system.color_sensor.get_color_as_name() == 'Blue' or robot.sensor_system.color_sensor.get_color() == 2:
            robot.drive_system.go_until_distance_is_within(2, 0, 25)
            robot.arm_and_claw.raise_arm()
            for _ in range(loops):
                robot.drive_system.right_motor.turn_on(speed)
                robot.drive_system.left_motor.turn_on(length)
                start = time.time()
                while True:
                    current = time.time()
                    if current - start >= duration:
                        break
                    robot.drive_system.right_motor.turn_off()
                    robot.drive_system.left_motor.turn_off()
                    break



