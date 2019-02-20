"""
Code for sprint 3
Authors: Professors for framework and Daniel Decker
"""
import rosebot
import time

def go_forward_until_scared(intensity, speed):
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_until_intensity_is_less_than(intensity, speed)
    robot.sound_system.speech_maker.speak('Ruh roh, Raggy')
    robot.drive_system.go(speed, -speed)
    time.sleep(2*(100/speed))
    robot.drive_system.stop()
    time.sleep(1.0)
    robot.drive_system.go_straight_for_seconds(5, speed)
    robot.drive_system.stop()


def second_placeholder(x, y):
    robot = rosebot.RoseBot()

