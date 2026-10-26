# Sam Lunev. 2026. MIT
from typing import Optional

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


class PatrolNode(Node):
    def __init__(self):
        super().__init__('patrol')
        self.last_pose: Optional[Pose] = None
        self.declare_parameter('lin_spd', 0.5)
        self.declare_parameter('ang_spd', 0.5)
        self.declare_parameter('frq_hz', 10.0)

        self.pose_subscription = self.create_subscription(
                                    Pose,
                                    '/turtle1/pose',
                                    self.pose_callback,
                                    10
                                )
        self.cmd_vel_publisher = self.create_publisher(
                                    Twist,
                                    '/cmd_vel',
                                    10
                                )
        # self.timer = self.create_timer(0.1, self.timer_callback)
        self.timer = None
        self.timer_freq = None
        self.update_timer()
        self.timer_call_count = 0
        self.get_logger().info('Patrol node initialized')

    def update_timer(self):
        freq = self.get_parameter('frq_hz').get_parameter_value().double_value
        if freq <= 0:
            return

        if freq != self.timer_freq:
            if self.timer is not None:
                self.destroy_timer(self.timer)

            self.timer = self.create_timer(1.0 / freq, self.timer_callback)
            self.timer_freq = freq

            self.get_logger().info(f'Frequency set to :{freq}')

    def pose_callback(self, msg: Pose) -> None:
        self.last_pose = msg

    def timer_callback(self) -> None:
        self.update_timer()

        lx = self.get_parameter('lin_spd').get_parameter_value().double_value
        lz = self.get_parameter('ang_spd').get_parameter_value().double_value

        self.timer_call_count += 1
        twist = self.get_command_from_pose(self.last_pose, lx, lz)
        self.cmd_vel_publisher.publish(twist)

    @staticmethod
    def get_command_from_pose(pose: Optional[Pose], lx: float = 0.00, lz: float = 0.00) -> Twist:
        twist = Twist()
        if pose is not None:
            twist.linear.x = lx
            twist.angular.z = lz

        return twist


def main(args=None):
    rclpy.init(args=args)
    node = PatrolNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
