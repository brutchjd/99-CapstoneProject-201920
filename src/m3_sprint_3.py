"""
Code for sprint 3
Authors: Professors for framework and Daniel Decker
"""
import rosebot
import time
import m3_run_this_on_laptop

def go_forward_until_scared(intensity, speed):
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_until_intensity_is_less_than(intensity, speed)
    robot.sound_system.speech_maker('Ruh roh, Raggy')
    robot.drive_system.go(speed, 0)
    """Need a way to turn it 180 degrees"""



