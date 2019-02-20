"""
Code for sprint 3
Authors: Professors for framework and Daniel Decker
"""
import rosebot
import time
import m3_extra as cam

def go_forward_until_scared(speed, intensity):
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_until_intensity_is_less_than(intensity, speed)
    robot.sound_system.speech_maker.speak('Ruh roh, Raggy')
    robot.drive_system.go((speed/2), (-speed/2))
    time.sleep(2*(100/speed))
    robot.drive_system.stop()
    time.sleep(1.0)
    robot.drive_system.go_straight_for_seconds(5, speed)
    robot.drive_system.stop()


def scooby_snack(speed, area):
    robot = rosebot.RoseBot()
    cam.m3_camera_clockwise(speed, area)

    robot.sound_system.speech_maker.speak('Ooh, a Scooby Snack')


