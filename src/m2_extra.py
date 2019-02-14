import rosebot
import time


def m2_pickup():
    robot = rosebot.RoseBot()
    go_until_distance_is_within_tone(robot, 1, 0, 25)
    robot.arm_and_claw.raise_arm()
    # while True:
       # distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
       # robot.sound_system.tone_maker.play_tone(150, 1000)
       # time.sleep(1 / (distance + 0.00001))
       # if distance >= 1 - 1 or distance <= 1 + 1:
        #    break

def m2_pickup_beep():
    robot = rosebot.RoseBot()
    go_until_distance_is_within_beep(robot, 1, 0, 25)
    robot.arm_and_claw.raise_arm()


def go_until_distance_is_within_tone(robot, delta, inches, speed):
    start = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    print(start)

    if start > inches + delta:
        robot.drive_system.go(speed, speed)
        while True:
            test = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            robot.sound_system.tone_maker.play_tone(270 * (1 / (distance + 0.01)), 500)
            time.sleep(1 / (distance + 0.00001))
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
            robot.sound_system.tone_maker.play_tone(270 * (1 / (distance + 0.01)), 500)
            time.sleep(1 / (distance + 0.00001))
            print(test)
            if test >= (inches - delta) and test <= (inches + delta):
                print(test)
                robot.drive_system.left_motor.turn_off()
                robot.drive_system.right_motor.turn_off()
                break


def go_until_distance_is_within_beep(robot, delta, inches, speed):
    start = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    print(start)

    if start > inches + delta:
        robot.drive_system.go(speed, speed)
        while True:
            test = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            robot.sound_system.beeper.beep()
            time.sleep(1 / (distance + 0.00001))
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
            time.sleep(1 / (distance + 0.00001))
            print(test)
            if test >= (inches - delta) and test <= (inches + delta):
                print(test)
                robot.drive_system.left_motor.turn_off()
                robot.drive_system.right_motor.turn_off()
                break