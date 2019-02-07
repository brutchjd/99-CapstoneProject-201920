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

    def forward(self, lws, rws):
        print('Got Forward', lws, rws)
        self.robot.drive_system.go(int(lws), int(rws))

    def backward(self, lws, rws):
        rws_b = int(rws) * -1
        lws_b = int(lws) * -1
        print('Got Backward', lws_b, rws_b)
        self.robot.drive_system.go(lws_b, rws_b)

    def left(self):
        print('Left')

    def right(self):
        print('Right')

    def stop(self):
        print('Stop')
        self.robot.drive_system.stop()