import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy

from course_bringup.pose_types import Pose


class PoseRelay(Node):
    def __init__(self):
        super().__init__('pose_relay')

        qos = QoSProfile(
            depth=10,
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
        )

        self.pub = self.create_publisher(Pose, 'sensor_pose', qos)
        self.sub = self.create_subscription(
            Pose, 'turtle1/pose', self.pose_callback, 10)

        self.get_logger().info('pose_relay started: turtle1/pose -> sensor_pose')

    def pose_callback(self, msg: Pose) -> None:
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = PoseRelay()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

