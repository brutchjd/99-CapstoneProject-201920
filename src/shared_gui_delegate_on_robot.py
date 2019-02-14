"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Jared Brutcher, Nathaniel Craan, Daniel Decker.
  Winter term, 2018-2019.
"""
import m2_extra
import m1_extra

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
        print("Got Speak", speak)
        self.robot.sound_system.speech_maker.speak(speak)

    def beep(self, beep):
        print('Got Beep', beep)
        for k in range(int(beep)):
            self.robot.sound_system.beeper.beep().wait()

    def frequency(self, frequency, duration):
        print('Got Frequency', frequency, duration)
        self.robot.sound_system.tone_maker.play_tone(int(frequency), int(duration))

    def lessthan(self, inches, speed):
        print('Got Less Than', inches, speed)
        self.robot.drive_system.go_forward_until_distance_is_less_than(int(inches), int(speed))

    def greaterthan(self, inches, speed):
        print('Got Greater Than', inches, speed)
        self.robot.drive_system.go_backward_until_distance_is_greater_than(int(inches), int(speed))

    def within(self, delta, inches, speed):
        print('Got Within', delta, inches, speed)
        self.robot.drive_system.go_until_distance_is_within(float(delta), int(inches), int(speed))

    def camera_data(self):
        print('Got Camera Data')
        self.robot.drive_system.display_camera_data()

    def camera_counterclockwise(self, area, speed):
        print('Got Camera Counterclockwise')
        self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), int(area))

    def camera_clockwise(self, area, speed):
        print('Got Camera Clockwise')
        self.robot.drive_system.spin_clockwise_until_sees_object(int(speed), int(area))

    def m2_pickup_tone(self):
        print('Got Pick Up With Tones')
        m2_extra.m2_pickup()

    def clockwise_find_object(self, speed, area):
        print('Got Clockwise Find Object')
        m1_extra.clockwise_find_object(self.robot, int(speed), int(area))


