import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy

from course_bringup.pose_types import Pose


class PoseSubscriber(Node):
    def __init__(self):
        super().__init__('pose_subscriber')

        self.declare_parameter('reliability', 'best_effort')
        reliability = self.get_parameter('reliability').get_parameter_value().string_value

        policies = {
            'reliable': QoSReliabilityPolicy.RELIABLE,
            'best_effort': QoSReliabilityPolicy.BEST_EFFORT,
        }
        if reliability not in policies:
            raise ValueError(
                f"'reliability' must be 'reliable' or 'best_effort', got '{reliability}'")

        qos = QoSProfile(depth=10, reliability=policies[reliability])

        self.sub = self.create_subscription(
            Pose, 'sensor_pose', self.pose_callback, qos)

        self.get_logger().info(f'pose_subscriber listening on sensor_pose, QoS={reliability}')

    def pose_callback(self, msg: Pose) -> None:
        self.get_logger().debug(f'x={msg.x:.2f} y={msg.y:.2f} theta={msg.theta:.2f}')


def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

