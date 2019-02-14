import rosebot
import time


def m2_pickup():
    robot = rosebot.RoseBot()
    robot.drive_system.go_until_distance_is_within(0.9, 1, 25)
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        robot.sound_system.tone_maker.play_tone(150, 1000)
        time.sleep(1 / distance)
        if distance >= 1 - 1 or distance <= 1 + 1 :
            break
    robot.arm_and_claw.raise_arm()
