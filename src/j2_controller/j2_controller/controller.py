import rclpy
from rclpy.node import Node

import serial
import struct

from geometry_msgs.msg import Twist

class J2Controller(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.ser = serial.Serial('/dev/ttyUSB0', 115200)  # open serial port1

    def listener_callback(self, msg):
        print(msg.linear)
        print(msg.angular)
        cmd = struct.pack("ff", msg.linear.x, -msg.angular.z)
        self.ser.write(cmd)

def main(args=None):
    rclpy.init(args=args)

    j2controller = J2Controller()

    rclpy.spin(j2controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    j2controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()