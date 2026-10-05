printenv ROS_DISTRO ROS_DOMAIN_ID

jazzy
16

# Got ROS-2 version and Domain-ID


ros2 pkg prefix turtlesim

/opt/ros/jazzy


ros2 pkg create --build-type ament_python --license MIT turtle_bringup --dependencies launch launch_ros turtlesim

(!) creating ./turtle_bringup/package.xml
(!) creating ./turtle_bringup/setup.py
# package.xml and setup.py describe package, used later
# Create new package (Python lang; Depends on: (launch, launch_ros, turtlesim))


ls src/turtle_bringup/

LICENSE      resource   setup.py  turtle_bringup
package.xml  setup.cfg  test


set -o pipefail
colcon build --symlink-install --packages-select turtle_bringup 2>&1 | tee evidence/pr02/build-empty.txt
# Build package using 'colcon'; log output to 'build-empty.txt'; 'pipefail' needed to return error linked with pipe
*Same for non-empty package, 'build.txt' for log*


ros2 pkg prefix turtle_bringup

/home/ubuntu/install/turtle_bringup


ls "$(ros2 pkg prefix turtle_bringup)/share/turtle_bringup/launch"

sim.launch.py


ros2 launch turtle_bringup sim.launch.py

[INFO] [launch]: All log files can be found below /root/.ros/log/2026-10-05-08-59-29-333877-dd444d1349bc-435
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [turtlesim_node-1]: process started with pid [438]
[turtlesim_node-1] QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
[turtlesim_node-1] [INFO] [1791190769.607620873] [turtlesim]: Starting turtlesim with node name /turtlesim
[turtlesim_node-1] [INFO] [1791190769.629447903] [turtlesim]: Spawning turtle [turtle1] at x=[5.544445], y=[5.544445], theta=[0.000000]
[turtlesim_node-1] MESA: error: Failed to query drm device.
[turtlesim_node-1] glx: failed to create dri3 screen
[turtlesim_node-1] failed to load driver: iris
^C[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[turtlesim_node-1] [INFO] [1791190838.748208711] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[INFO] [turtlesim_node-1]: process has finished cleanly [pid 438]


ros2 node list --no-daemon --spin-time 2

/turtlesim


ros2 node list --no-daemon --spin-time 2


ros2 interface show geometry_msgs/msg/Twist

# This expresses velocity in free space broken into its linear and angular parts.

Vector3  linear
	float64 x
	float64 y
	float64 z
Vector3  angular
	float64 x
	float64 y
	float64 z


ros2 topic type /turtle1/pose

turtlesim/msg/Pose


ros2 topic echo /turtle1/pose --once

x: 5.544444561004639
y: 5.544444561004639
theta: 0.0
linear_velocity: 0.0
angular_velocity: 0.0
---


ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist \

  '{linear: {x: 1.0}, angular: {z: 0.5}}'
publisher: beginning loop
publishing #1: geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(x=1.0, y=0.0, z=0.0), angular=geometry_msgs.msg.Vector3(x=0.0, y=0.0, z=0.5))


ros2 topic echo /turtle1/pose --once

x: 6.509308815002441
y: 5.796990871429443
theta: 0.5040000081062317
linear_velocity: 0.0
angular_velocity: 0.0
---


ros2 topic pub --rate 1 --wait-matching-subscriptions 0 \

  /cmd_vel geometry_msgs/msg/Twist \
  '{linear: {x: 1.0}, angular: {z: 0.5}}'
publisher: beginning loop
publishing #1: geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(x=1.0, y=0.0, z=0.0), angular=geometry_msgs.msg.Vector3(x=0.0, y=0.0, z=0.5))

publishing #2: geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(x=1.0, y=0.0, z=0.0), angular=geometry_msgs.msg.Vector3(x=0.0, y=0.0, z=0.5))

publishing #3: geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(x=1.0, y=0.0, z=0.0), angular=geometry_msgs.msg.Vector3(x=0.0, y=0.0, z=0.5))

publishing #4: geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(x=1.0, y=0.0, z=0.0), angular=geometry_msgs.msg.Vector3(x=0.0, y=0.0, z=0.5))

publishing #5: geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(x=1.0, y=0.0, z=0.0), angular=geometry_msgs.msg.Vector3(x=0.0, y=0.0, z=0.5))


ros2 topic info /cmd_vel --verbose

Type: geometry_msgs/msg/Twist

Publisher count: 1

Node name: _ros2cli_628
Node namespace: /
Topic type: geometry_msgs/msg/Twist
Topic type hash: RIHS01_9c45bf16fe0983d80e3cfe750d6835843d265a9a6c46bd2e609fcddde6fb8d2a
Endpoint type: PUBLISHER
GID: 01.0f.eb.7d.74.02.01.06.00.00.00.00.00.00.07.03
QoS profile:
  Reliability: RELIABLE
  History (Depth): UNKNOWN
  Durability: VOLATILE
  Lifespan: Infinite
  Deadline: Infinite
  Liveliness: AUTOMATIC
  Liveliness lease duration: Infinite

Subscription count: 0


ros2 topic info /turtle1/cmd_vel --verbose

Type: geometry_msgs/msg/Twist

Publisher count: 0

Subscription count: 1

Node name: turtlesim
Node namespace: /
Topic type: geometry_msgs/msg/Twist
Topic type hash: RIHS01_9c45bf16fe0983d80e3cfe750d6835843d265a9a6c46bd2e609fcddde6fb8d2a
Endpoint type: SUBSCRIPTION
GID: 01.0f.eb.7d.ec.01.c0.19.00.00.00.00.00.00.1d.04
QoS profile:
  Reliability: RELIABLE
  History (Depth): UNKNOWN
  Durability: VOLATILE
  Lifespan: Infinite
  Deadline: Infinite
  Liveliness: AUTOMATIC
  Liveliness lease duration: Infinite

  
ros2 topic info /cmd_vel --verbose

Unknown topic '/cmd_vel'


ros2 topic info /turtle1/cmd_vel --verbose

Type: geometry_msgs/msg/Twist

Publisher count: 1

Node name: _ros2cli_681
Node namespace: /
Topic type: geometry_msgs/msg/Twist
Topic type hash: RIHS01_9c45bf16fe0983d80e3cfe750d6835843d265a9a6c46bd2e609fcddde6fb8d2a
Endpoint type: PUBLISHER
GID: 01.0f.eb.7d.a9.02.27.b9.00.00.00.00.00.00.07.03
QoS profile:
  Reliability: RELIABLE
  History (Depth): UNKNOWN
  Durability: VOLATILE
  Lifespan: Infinite
  Deadline: Infinite
  Liveliness: AUTOMATIC
  Liveliness lease duration: Infinite

Subscription count: 1

Node name: turtlesim
Node namespace: /
Topic type: geometry_msgs/msg/Twist
Topic type hash: RIHS01_9c45bf16fe0983d80e3cfe750d6835843d265a9a6c46bd2e609fcddde6fb8d2a
Endpoint type: SUBSCRIPTION
GID: 01.0f.eb.7d.ec.01.c0.19.00.00.00.00.00.00.1d.04
QoS profile:
  Reliability: RELIABLE
  History (Depth): UNKNOWN
  Durability: VOLATILE
  Lifespan: Infinite
  Deadline: Infinite
  Liveliness: AUTOMATIC
  Liveliness lease duration: Infinite


ros2 topic info /cmd_vel --verbose

Unknown topic '/cmd_vel'


ros2 topic info /turtle1/cmd_vel --verbose
Type: geometry_msgs/msg/Twist

Publisher count: 0

Subscription count: 1

Node name: turtlesim
Node namespace: /
Topic type: geometry_msgs/msg/Twist
Topic type hash: RIHS01_9c45bf16fe0983d80e3cfe750d6835843d265a9a6c46bd2e609fcddde6fb8d2a
Endpoint type: SUBSCRIPTION
GID: 01.0f.eb.7d.ec.01.c0.19.00.00.00.00.00.00.1d.04
QoS profile:
  Reliability: RELIABLE
  History (Depth): UNKNOWN
  Durability: VOLATILE
  Lifespan: Infinite
  Deadline: Infinite
  Liveliness: AUTOMATIC
  Liveliness lease duration: Infinite
  

# Strict matching of Topic name and Type hash required