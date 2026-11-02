topic_arg = DeclareLaunchArgument(
        'numbers_topic',
        default_value=PythonExpression([
            "'/even_numbers_fast' if '", mode,
            "' == 'fast' else '/even_numbers_slow'"
        ])
    )



# study1_pkg

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class OverflowListener(Node):

    def __init__(self):
        super().__init__('overflow_listener')

        self.subscription = self.create_subscription(
            Int32,
            'overflow',
            self.overflow_callback,
            10
        )

        self.get_logger().info(
            'Ожидание переполнения счётчика'
        )

    def overflow_callback(self, msg):
        self.get_logger().warning(
            f'!!! ПЕРЕПОЛНЕНИЕ !!! '
            f'Получено значение: {msg.data}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = OverflowListener()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if name == '__main__':
    main()
