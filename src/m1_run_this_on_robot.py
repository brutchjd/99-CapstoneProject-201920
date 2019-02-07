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


def test_raise_arm():
    robot = rosebot.RoseBot()
    print('created robot')
    robot.arm_and_claw.raise_arm()
    print('Done!')

def test_calibrate_arm():
    robot = rosebot.RoseBot()
    print('created robot')
    robot.arm_and_claw.calibrate_arm()
    print('Done!')

def test_lower_arm():
    robot = rosebot.RoseBot()
    print("Robot Created")
    robot.arm_and_claw.lower_arm()
    print('Done!')


def real_demonstration():
    robot = rosebot.RoseBot()
    reciever = rec.Reciever(robot)
    mqtt_reciever = com.MqttClient(reciever)
    mqtt_reciever.connect_to_pc()

    while True:
        time.sleep(0.01)







# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()