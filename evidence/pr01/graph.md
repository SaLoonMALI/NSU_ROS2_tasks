default: term_C

ros2 node list --no-daemon --spin-time 2

/teleop_turtle
/turtlesim


ros2 topic list -t

/parameter_events [rcl_interfaces/msg/ParameterEvent]
/rosout [rcl_interfaces/msg/Log]
/turtle1/cmd_vel [geometry_msgs/msg/Twist]
/turtle1/color_sensor [turtlesim/msg/Color]
/turtle1/pose [turtlesim/msg/Pose]


ros2 node info /turtlesim

/turtlesim
  Subscribers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /turtle1/cmd_vel: geometry_msgs/msg/Twist
  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
    /turtle1/color_sensor: turtlesim/msg/Color
    /turtle1/pose: turtlesim/msg/Pose
  Service Servers:
    /clear: std_srvs/srv/Empty
    /kill: turtlesim/srv/Kill
    /reset: std_srvs/srv/Empty
    /spawn: turtlesim/srv/Spawn
    /turtle1/set_pen: turtlesim/srv/SetPen
    /turtle1/teleport_absolute: turtlesim/srv/TeleportAbsolute
    /turtle1/teleport_relative: turtlesim/srv/TeleportRelative
    /turtlesim/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /turtlesim/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /turtlesim/get_parameters: rcl_interfaces/srv/GetParameters
    /turtlesim/get_type_description: type_description_interfaces/srv/GetTypeDescription
    /turtlesim/list_parameters: rcl_interfaces/srv/ListParameters
    /turtlesim/set_parameters: rcl_interfaces/srv/SetParameters
    /turtlesim/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
  Service Clients:

  Action Servers:
    /turtle1/rotate_absolute: turtlesim/action/RotateAbsolute
  Action Clients:


ros2 topic type /turtle/pose

turtlesim/msg/Pose


POSE_TYPE=$(ros2 topic type /turtle1/pose)


ros2 topic echo /turtle1/pose --once

x: 2.133466958999634
y: 1.6493611335754395
theta: 0.136073499917984
linear_velocity: 0.0
angular_velocity: 0.0
---


ros2 topic hz /turtle1/pose

average rate: 62.588
	min: 0.015s max: 0.017s std dev: 0.00052s window: 64
average rate: 62.517
	min: 0.015s max: 0.017s std dev: 0.00052s window: 127
average rate: 62.505
	min: 0.015s max: 0.017s std dev: 0.00051s window: 190
average rate: 62.501
	min: 0.014s max: 0.017s std dev: 0.00052s window: 253
average rate: 62.500
	min: 0.014s max: 0.017s std dev: 0.00052s window: 316
average rate: 62.500
	min: 0.014s max: 0.017s std dev: 0.00051s window: 379
average rate: 62.499
	min: 0.014s max: 0.017s std dev: 0.00049s window: 442
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00049s window: 505
average rate: 62.499
	min: 0.014s max: 0.018s std dev: 0.00049s window: 568
average rate: 62.506
	min: 0.014s max: 0.018s std dev: 0.00049s window: 631
average rate: 62.502
	min: 0.014s max: 0.018s std dev: 0.00048s window: 694
average rate: 62.503
	min: 0.014s max: 0.018s std dev: 0.00049s window: 757
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00049s window: 820
average rate: 62.503
	min: 0.014s max: 0.018s std dev: 0.00049s window: 883
average rate: 62.503
	min: 0.014s max: 0.018s std dev: 0.00049s window: 946
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00050s window: 1009
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00049s window: 1072
average rate: 62.503
	min: 0.014s max: 0.018s std dev: 0.00049s window: 1135
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00049s window: 1198
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00049s window: 1261
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00050s window: 1324
average rate: 62.502
	min: 0.014s max: 0.018s std dev: 0.00050s window: 1387
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00050s window: 1450
average rate: 62.502
	min: 0.014s max: 0.018s std dev: 0.00050s window: 1513
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00050s window: 1576
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00050s window: 1639
average rate: 62.502
	min: 0.014s max: 0.018s std dev: 0.00050s window: 1702
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00050s window: 1765
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00050s window: 1828
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00050s window: 1891
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00050s window: 1954
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00049s window: 2017
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00049s window: 2080
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00049s window: 2143
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00049s window: 2206
average rate: 62.502
	min: 0.014s max: 0.018s std dev: 0.00049s window: 2269
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00048s window: 2332
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00048s window: 2395
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00049s window: 2458
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00048s window: 2521
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00048s window: 2584
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00048s window: 2647
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00048s window: 2710
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00048s window: 2773
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00048s window: 2836
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00048s window: 2899
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00048s window: 2962
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00048s window: 3025
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00048s window: 3088
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00047s window: 3151
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00048s window: 3214
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00048s window: 3277
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00048s window: 3340
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00047s window: 3403
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 3466
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 3529
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 3592
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 3655
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 3718
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00047s window: 3781
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 3844
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 3907
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 3970
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 4033
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 4096
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00047s window: 4159
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 4222
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 4285
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 4348
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 4411
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00047s window: 4474
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00047s window: 4537
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00047s window: 4600
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 4663
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 4726
average rate: 62.501
	min: 0.014s max: 0.018s std dev: 0.00047s window: 4789
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 4852
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 4915
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 4978
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 5041
average rate: 62.500
	min: 0.014s max: 0.018s std dev: 0.00047s window: 5104

(term_B)
export ROS_DOMAIN_ID=17
ros2 run turtlesim turtle_teleop_key


export ROS_DOMAIN_ID=17
ros2 node list --no-daemon --spin-time 2

/teleop_turtle


timeout 5s ros2 topic echo /turtle1/pose "$POSE_TYPE" --once > temp_rep_file
printf 'exit=%s\n' "$?"

exit=124


(term_B)
export ROS_DOMAIN_ID=16
ros2 run turtlesim turtle_teleop_key


export ROS_DOMAIN_ID=16
ros2 node list --no-daemon --spin-time 2

/teleop_turtle
/turtlesim


timeout 5s ros2 topic echo /turtle1/pose "$POSE_TYPE" --once > temp_rep_file
printf 'exit=%s\n' "$?"

exit=0


