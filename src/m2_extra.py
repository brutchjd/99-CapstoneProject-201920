import rosebot
import time


def m2_pickup(freq, rate):
    robot = rosebot.RoseBot()
    go_until_distance_is_within_tone(robot, 2, 0, 25, freq, rate)
    robot.arm_and_claw.raise_arm()
    # while True:
       # distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
       # robot.sound_system.tone_maker.play_tone(150, 1000)
       # time.sleep(1 / (distance + 0.00001))
       # if distance >= 1 - 1 or distance <= 1 + 1:
        #    break


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




def go_until_distance_is_within_tone(robot, delta, inches, speed, freq, rate):
    start = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    print(start)

    if start > inches + delta:
        robot.drive_system.go(speed, speed)
        while True:
            test = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            robot.sound_system.tone_maker.play_tone(freq * (1 / (distance + 0.01)), 500)
            time.sleep(1 / (rate * (distance + 0.00001)))
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
            robot.sound_system.tone_maker.play_tone(freq * (1 / (distance + 0.01)), 500)
            time.sleep(1 / (rate * (distance + 0.00001)))
            print(test)
            if test >= (inches - delta) and test <= (inches + delta):
                print(test)
                robot.drive_system.left_motor.turn_off()
                robot.drive_system.right_motor.turn_off()
                break


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