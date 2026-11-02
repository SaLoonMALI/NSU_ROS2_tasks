ros2 param set /patrol frq_hz 10.0
Set parameter successful


ros2 param set /patrol frq_hz 5.0
Set parameter successful

ros2 param get /patrol frq_hz
Double value is: 5.0

ros2 topic hz /turtle1/cmd_vel
average rate: 5.000
	min: 0.200s max: 0.200s std dev: 0.00025s window: 7
average rate: 5.000
	min: 0.200s max: 0.200s std dev: 0.00023s window: 13
average rate: 5.000
	min: 0.200s max: 0.200s std dev: 0.00020s window: 18
average rate: 5.000


ros2 param set /patrol frq_hz nam
Setting parameter failed: Wrong parameter type, expected 'Type.DOUBLE' got 'Type.STRING'

ros2 param get /patrol frq_hz
Double value is: 5.0

ros2 topic hz /turtle1/cmd_vel
average rate: 5.000
	min: 0.200s max: 0.200s std dev: 0.00025s window: 7
average rate: 5.000
	min: 0.200s max: 0.200s std dev: 0.00023s window: 13
average rate: 5.000
	min: 0.200s max: 0.200s std dev: 0.00020s window: 18
average rate: 5.000


ros2 param set /patrol frq_hz 
usage: ros2 param set [-h] [--spin-time SPIN_TIME] [-s] [--no-daemon]
                      [--include-hidden-nodes] [--timeout N]
                      node_name parameter_name value
ros2 param set: error: the following arguments are required: value


# checking is disabled
ros2 param set /patrol frq_hz -5.0
Set parameter successful

ros2 param get /patrol frq_hz
Double value is: -5.0

ros2 topic hz /turtle1/cmd_vel
saverage rate: 4.999
	min: 0.200s max: 0.200s std dev: 0.00021s window: 6
average rate: 4.999
	min: 0.199s max: 0.200s std dev: 0.00027s window: 12
average rate: 5.000
	min: 0.199s max: 0.200s std dev: 0.00023s window: 17


ros2 param set /patrol frq_hz 0.0

ros2 param get /patrol frq_hz
Node not found


# after fix
ros2 param set /patrol frq_hz 1.0
Set parameter successful


ros2 param get /patrol frq_hz
Double value is: 1.0


ros2 param set /patrol frq_hz 0.0
Set parameter successful


ros2 param get /patrol frq_hz
Double value is: 0.0

# patrol-node terminal
'frq_hz' must be at 1 - 30; got 0.0
'frq_hz' must be at 1 - 30; got 0.0
'frq_hz' must be at 1 - 30; got 0.0
'frq_hz' must be at 1 - 30; got 0.0


os2 topic hz /turtle1/cmd_vel
average rate: 1.000
	min: 1.000s max: 1.000s std dev: 0.00031s window: 2
average rate: 1.000
	min: 1.000s max: 1.000s std dev: 0.00037s window: 4
average rate: 1.000
	min: 1.000s max: 1.000s std dev: 0.00033s window: 6


ros2 param set /patrol frq_hz 1.0
Set parameter successful
