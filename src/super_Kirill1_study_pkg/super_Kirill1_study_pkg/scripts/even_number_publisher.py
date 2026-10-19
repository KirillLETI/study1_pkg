#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node 
from std_msgs.msg import Int32

class Even_pub(Node):

    def __init__(self):
        super().__init__('even_pub')

        self.publisher = self.create_publisher(
            Int32, 'even_numbers', 10)

        self.overflow_pub = self.create_publisher(
        Int32, 'overflow', 10)

        self.counter = 0

        self.timer = self.create_timer(
            0.1, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = self.counter

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Число: {msg.data}')

        self.counter += 2

        if self.counter >= 100:
            overflow_msg = Int32()
            overflow_msg.data = self.counter

            self.overflow_pub.publish(overflow_msg)

            self.get_logger().warning('Счётчик достиг 100')

            self.counter = 0
    
def main(): 
    rclpy.init()
    node = Even_pub()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()

if __name__ == 'main': main()

