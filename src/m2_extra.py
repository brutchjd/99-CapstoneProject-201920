import rosebot
import time


def m2_pickup():
    robot = rosebot.RoseBot()
    robot.drive_system.go_until_distance_is_within(2, 4, 50)
    robot.arm_and_claw.raise_arm()
