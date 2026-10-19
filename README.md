# study1_pkg
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class EvenPublisher(Node):

    def __init__(self):
        super().__init__('even_pub')

        self.number_pub = self.create_publisher(
            Int32, 'even_numbers', 10
        )

        self.overflow_pub = self.create_publisher(
            Int32, 'overflow', 10
        )

        self.counter = 0

        self.timer = self.create_timer(
            0.1, self.timer_callback
        )

    def timer_callback(self):
        msg = Int32()
        msg.data = self.counter

        self.number_pub.publish(msg)

        self.get_logger().info(
            f'Число: {msg.data}'
        )

        self.counter += 2

        if self.counter >= 100:
            overflow_msg = Int32()
            overflow_msg.data = self.counter

            self.overflow_pub.publish(overflow_msg)

            self.get_logger().warning(
                'Счётчик достиг 100'
            )

            self.counter = 0


def main(args=None):
    rclpy.init(args=args)
    node = EvenPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if name == '__main__':
    main()
