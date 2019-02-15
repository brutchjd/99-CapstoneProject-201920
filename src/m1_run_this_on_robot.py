"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Jared Brutcher.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot as rec
import m1_extra

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    #test_raise_arm()
    #test_calibrate_arm()
    #test_lower_arm()
    real_demonstration()
    #test_move_arm_to_position()
    #test_go_straight_for_inches_using_time()
    #test_go_straight_for_inches_using_encoder()
    #test_display_camera_data()
    #test_cycle_LEDs()


def test_raise_arm():
    print('test_raise_arm():')
    print('creating robot')
    robot = rosebot.RoseBot()
    print('created robot')
    robot.arm_and_claw.raise_arm()
    print('Done!')

def test_calibrate_arm():
    print('test_calibrate_arm():')
    print('creating robot')
    robot = rosebot.RoseBot()
    print('calibrating arm')
    robot.arm_and_claw.calibrate_arm()
    print('Done!')

def test_lower_arm():
    print('test_lower_arm():')
    print('creating robot')
    robot = rosebot.RoseBot()
    print("Robot Created")
    print("Moving to a position above 0")
    robot.arm_and_claw.move_arm_to_position(2000)
    print('Testing Lower arm')
    robot.arm_and_claw.lower_arm()
    print('Done!')

def test_move_arm_to_position():
    print('test_move_arm_to_position():')
    print('creating robot')
    robot = rosebot.RoseBot()
    print('calibrating arm')
    robot.arm_and_claw.calibrate_arm()
    print('testing move arm to position 3000 degrees')
    robot.arm_and_claw.move_arm_to_position(3000)
    time.sleep(5.0)
    print('500 degrees')
    robot.arm_and_claw.move_arm_to_position(500)
    print('Done!')

def real_demonstration():
    print('creating robot')
    robot = rosebot.RoseBot()
    receiver = rec.Receiver(robot)
    mqtt_receiver = com.MqttClient(receiver)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
        if receiver.quit_bool:
            break

def test_go_straight_for_inches_using_time():
    print('Creating robot')
    robot = rosebot.RoseBot()
    print('Go forward for 3 inches, half speed')
    robot.drive_system.go_straight_for_inches_using_time(3, 50)
    print('Go forward for 6 inches, full speed')
    robot.drive_system.go_straight_for_inches_using_time(6, 100)
    print('Done!')

def test_go_straight_for_inches_using_encoder():
    print('Creating robot')
    robot = rosebot.RoseBot()
    print('Go forward for 3 inches, half speed')
    robot.drive_system.go_straight_for_inches_using_encoder(3, 50)
    print('Go forward for 6 inches, full speed')
    robot.drive_system.go_straight_for_inches_using_encoder(6, 100)
    print('Done!')

def test_display_camera_data():
    print('Creating robot')
    robot = rosebot.RoseBot()
    print('Testing display camera data:')
    robot.drive_system.display_camera_data()

def test_cycle_LEDs():
    robot = rosebot.RoseBot()
    for k in range(20):
        m1_extra.cycle_LEDs(robot, 0.5, 5, 20-k)





# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()