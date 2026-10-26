colcon build --symlink-install --packages-select patrol
Starting >>> patrol  
Finished <<< patrol [3.38s]          

Summary: 1 package finished [3.63s]


source install/setup.bash


ros2 topic echo /turtle1/pose --once
x: 4.545897006988525
y: 6.44012975692749
theta: -1.47029709815979
linear_velocity: 0.0
angular_velocity: 0.0
---


ros2 run patrol patrol
[INFO] [1793005358.676597014] [patrol]: Frequency set to :10.0
[INFO] [1793005358.677370327] [patrol]: Patrol node initialized


ros2 topic echo /turtle1/pose --once
x: 4.545897006988525
y: 6.44012975692749
theta: -1.47029709815979
linear_velocity: 0.0
angular_velocity: 0.0
---


ros2 run patrol patrol -r cmd_vel:=/turtle1/cmd_vel


ros2 topic echo /turtle1/pose --once
x: 6.534738063812256
y: 6.651142597198486
theta: 1.6737029552459717
linear_velocity: 0.5
angular_velocity: 0.5
---


ros2 topic hz /turtle1/cmd_vel
average rate: 10.001
	min: 0.099s max: 0.101s std dev: 0.00036s window: 11
average rate: 10.001
	min: 0.099s max: 0.101s std dev: 0.00032s window: 22
average rate: 10.000
	min: 0.099s max: 0.101s std dev: 0.00029s window: 32
average rate: 10.000
	min: 0.099s max: 0.101s std dev: 0.00028s window: 43



rclpy.init() and rclpy.spin() handle different parts of a ROS 2 Python program:
    rclpy.init() initializes the ROS 2 client library and its context. Call it before creating nodes or using ROS functionality.
    rclpy.spin(node) runs the node’s executor, which waits for work and runs callbacks. It usually blocks until ROS shuts down or the node is otherwise stopped. Read the Docs

Callbacks are functions ROS runs in response to events—for example, receiving a message, a service request, or an action event. You register them when creating a subscription, service, timer, and so on. The executor runs them when their work is ready.
Timers schedule a callback to run repeatedly at a chosen interval. For example, create_timer(0.5, self.timer_callback) schedules it about every 0.5 seconds. The timer doesn’t run the callback by itself: the executor must be spinning for it to be serviced.

When you press Ctrl+C in the terminal, Python receives an interrupt (KeyboardInterrupt) and ROS 2’s signal handling starts shutdown. spin() stops, and the program can clean up—such as destroying the node and shutting down rclpy.
