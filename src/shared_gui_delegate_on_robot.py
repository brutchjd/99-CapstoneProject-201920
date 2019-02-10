"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Jared Brutcher, Nathaniel Craan, Daniel Decker.
  Winter term, 2018-2019.
"""


class Receiver(object):

    def __init__(self, robot):
        """ :type   robot:  rosebot.RoseBot"""
        self.robot = robot
        self.quit_bool = False

    def forward(self, lws, rws):
        print('Got Forward', lws, rws)
        self.robot.drive_system.go(int(lws), int(rws))

    def backward(self, lws, rws):
        rws_b = int(rws) * -1
        lws_b = int(lws) * -1
        print('Got Backward', lws_b, rws_b)
        self.robot.drive_system.go(lws_b, rws_b)

    def left(self, lws, rws):
        print('Got Left')
        self.robot.drive_system.go(-int(lws), int(rws))

    def right(self, lws, rws):
        print('Got Right')
        self.robot.drive_system.go(int(lws), -int(rws))

    def stop(self):
        print('Got Stop')
        self.robot.drive_system.stop()

    def raise_arm(self):
        print('Got Raise Arm')
        self.robot.arm_and_claw.raise_arm()

    def lower(self):
        print('Got Lower Arm')
        self.robot.arm_and_claw.lower_arm()

    def calibrate(self):
        print('Got Calibrate Arm')
        self.robot.arm_and_claw.calibrate_arm()

    def position(self, pos):
        print('Got Position: ', pos)
        self.robot.arm_and_claw.move_arm_to_position(int(pos))

    def quit(self):
        print('Got Quit')
        self.quit_bool = True

    def seconds(self, seconds, speed):
        print('Got Seconds', seconds)
        self.robot.drive_system.go_straight_for_seconds(int(seconds), int(speed))

    def inches(self, inches, speed):
        print('Got Inches', inches)
        self.robot.drive_system.go_straight_for_inches_using_time(int(inches), int(speed))

    def encoder(self, encoder, speed):
        print('Got Encoder', encoder)
        self.robot.drive_system.go_straight_for_inches_using_encoder(int(encoder), int(speed))

    def speak(self, speak):
        pass

    def beep(self, beep):
        pass

    def frequency(self, frequency):
        pass