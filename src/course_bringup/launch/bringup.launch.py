from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, GroupAction, LogInfo
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node, PushRosNamespace


def generate_launch_description():
    args = [
        DeclareLaunchArgument('namespace', default_value='robot_a',
                              description='Namespace for course nodes'),
        DeclareLaunchArgument('record', default_value='false',
                              description='Record sensor_pose to MCAP'),
        DeclareLaunchArgument('bag_dir', default_value='bags',
                              description='Directory for the bag'),
        DeclareLaunchArgument('subscriber_reliability', default_value='best_effort',
                              description='pose_subscriber QoS: reliable or best_effort'),
    ]

    # Глобальный turtlesim: топики остаются /turtle1/...
    turtlesim = Node(
        package='turtlesim', executable='turtlesim_node',
        name='turtlesim', output='screen',
    )

    course = GroupAction([
        PushRosNamespace(LaunchConfiguration('namespace')),
        LogInfo(msg=['Starting course nodes in namespace: ',
                     LaunchConfiguration('namespace')]),
        Node(package='course_bringup', executable='pose_relay',
             name='pose_relay', output='screen',
             remappings=[('turtle1/pose', '/turtle1/pose')]),
        Node(package='course_bringup', executable='pose_subscriber',
             name='pose_subscriber', output='screen',
             parameters=[{'reliability': LaunchConfiguration('subscriber_reliability')}]),
        Node(package='patrol', executable='patrol',
             name='patrol', output='screen',
             remappings=[('turtle1/pose', '/turtle1/pose'),
                         ('cmd_vel', '/turtle1/cmd_vel')]),
    ])

    recorder = ExecuteProcess(
        condition=IfCondition(LaunchConfiguration('record')),
        cmd=[
            'ros2', 'bag', 'record',
            '--storage', 'mcap',
            '-o', [LaunchConfiguration('bag_dir'), '/sensor_pose_bag'],
            '--topics', ['/', LaunchConfiguration('namespace'), '/sensor_pose'],
        ],
        output='screen',
    )

    return LaunchDescription(args + [turtlesim, course, recorder])

