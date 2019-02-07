"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Jared Brutcher, Nathaniel Craan, Daniel Decker.
  Winter term, 2018-2019.
"""

class Reciever(object):

    def __init__(self, robot):
        """ :type   robot:  rosebot.RoseBot"""
        self.robot = robot

    def forward(self, lws, rws):

        print('Got Forward', lws, rws)
        self.robot.drive_system.go(int(lws), int(rws))