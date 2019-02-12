# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot as rec


def main():
    robot = rosebot.RoseBot()
    robot.drive_system.go_forward_until_distance_is_less_than(5, 100)
    robot.drive_system.go_backward_until_distance_is_greater_than(12, 100)
    robot.drive_system.go_until_distance_is_within(3, 24, 100)





main()