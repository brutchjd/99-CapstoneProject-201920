# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot as rec


def main():
    robot = rosebot.RoseBot()
    robot.drive_system.go_forward_until_distance_is_less_than(24, 50)
    robot.drive_system.go_backward_until_distance_is_greater_than(36, 50)
    robot.drive_system.go_until_distance_is_within(4, 24, 50)


def test():
    robot = rosebot.RoseBot()
    while True:
        test = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        time.sleep(5)
        print(test)



#test()
main()