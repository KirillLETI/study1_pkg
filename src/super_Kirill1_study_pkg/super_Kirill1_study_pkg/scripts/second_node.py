
import rclpy

from datetime import datetime
from rclpy.node import Node

def timer_log(node):
    cur_time = datetime.now()
    time2str = cur_time.strftime('%H: %M: %S')
    node.get_logger().info(f"Current time: {time2str}")

def main(args=None):
    rclpy.init(args=args)                   # инициализация ROS 2
    node = Node('time_node')               # создаём узел с именем hello_node
    node.create_timer(5.0, lambda: timer_log(node))
    
    rclpy.spin(node)                        # запускаем цикл обработки
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()