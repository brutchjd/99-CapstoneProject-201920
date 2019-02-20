"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Jared Brutcher, Nathaniel Craan, Daniel Decker.
  Winter term, 2018-2019.
"""
import m2_extra
import m1_extra
import m3_extra
import m1_sprint_3
import rosebot
import m3_sprint_3

class Receiver(object):

    def __init__(self, robot):
        """ :type   robot:  rosebot.RoseBot"""
        self.robot = robot
        self.quit_bool = False
        self.m1_run_data = m1_sprint_3.m1_data_storage

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

    def m3_pickup_tone(self, freq, rate):
        print('Got Pick Up With Tones')
        m3_extra.m3_pickup(int(freq), int(rate))

    def m2_pickup_beep(self, rate):
        print('Got Pick Up with Beeps')
        m2_extra.m2_pickup_beep(int(rate))

    def m1_clockwise_find_object(self, speed, area):
        print('Got Clockwise Find Object')
        m1_extra.clockwise_find_object(self.robot, int(speed), int(area))

    def m1_counterclockwise_find_object(self, speed, area):
        print('Got Clockwise Find Object')
        m1_extra.counterclockwise_find_object(self.robot, int(speed), int(area))

    def m1_pickup_LED(self, rateincrease, intitialrate):
        print('Got Pick Up with LEDs')
        m1_extra.m1_pick_up_LED(self.robot, 80, float(rateincrease), float(intitialrate))

    def m2_camera_clockwise(self, speed, area):
        print('Got Find and Pick Up')
        m2_extra.m2_camera_clockwise(int(speed), int(area))

    def m2_camera_counterclockwise(self, speed, area):
        print('Got Find and Pick Up')
        m2_extra.m2_camera_counterclockwise(int(speed), int(area))

    def intensity_less(self, intensity, speed):
        print('Got Intensity Less')
        self.robot.drive_system.go_straight_until_intensity_is_less_than(int(intensity), int(speed))

    def intensity_more(self, intensity, speed):
        print('Got Intensity More')
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(int(intensity), int(speed))

    def color_equal(self, color, speed):
        print('Got Color Equal')
        self.robot.drive_system.go_straight_until_color_is(color, int(speed))

    def color_different(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is_not(color, int(speed))

    def m3_camera_clockwise(self, speed, area):
        print('Got Find and Pick Up Tone')
        m3_extra.m3_camera_clockwise(int(speed), int(area))

    def m3_camera_counterclockwise(self, speed, area):
        print('Got Find and Pick Up Tone')
        m3_extra.m3_camera_counterclockwise(int(speed), int(area))

    def m2_rectangle(self, speed, width, length, loops):
        print('Driving Retangle')
        m2_extra.map_rectangle(int(speed), int(width), int(length), int(loops))

    def m2_triangle(self, speed, length, loops):
        print('Driving Triangle')
        m2_extra.map_triangle(int(speed), int(length), int(loops))

    def m2_circle(self, speed, length, loops, duration):
        print('Driving Circle')
        m2_extra.map_circle(int(speed), int(length), int(loops), int(duration))

    def m1_test_far_calibration(self):
        print('Got Test Far Calibration')
        run_data = m1_sprint_3.m1_data_storage
        m1_sprint_3.m1_calibrate_camera_far(self.robot, run_data)
        run_data

    def m1_test_close_calibration(self):
        print('Got Test Close Calibration')
        run_data = m1_sprint_3.m1_data_storage
        m1_sprint_3.m1_calibrate_camera_close(self.robot, run_data)

    def go_forward_until_scared(self, speed, intensity):
        print('Scooby Running')
        m3_sprint_3.go_forward_until_scared(int(speed), int(intensity))

    def m1_test_get_direction(self):
        print('Got Test Get Direction')
        run_data = m1_sprint_3.m1_data_storage
        run_data.max_area = 1000
        run_data.min_area = 10
        m1_sprint_3.m1_get_direction(self.robot, run_data)

    def m1_test_dive(self):
        print('Got Test Dive')
        run_data = m1_sprint_3.m1_data_storage
        run_data.turn_time_threshold = 0.0
        run_data.ball_direction = 'left'
        run_data.speed = 60
        m1_sprint_3.m1_dive_for_ball(self.robot, run_data)
        run_data.ball_direction = 'right'
        m1_sprint_3.m1_dive_for_ball(self.robot, run_data)