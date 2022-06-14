# rb1_base_ros2

rb1 simulation for ROS2

## 1. Installation


Create workspace
```bash
cd && mkdir ros2_ws && cd ros2_ws && mkdir src
```

Clone this repository:

```bash
git clone https://github.com/robert-ros/rb1_base_ros2.git
```

Install dependencies:

```bash
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -y
sudo apt-get install ros-foxy-teleop-twist-keyboard 
```

Build and source

```bash
colcon build --symlink-install
source install/setup.bash
```

## 2. Usage

Launch the simulation

```bash
ros2 launch rb1_base_sim_bringup rb1_base_complete.launch.py
```

Use teleop twist keyboard node to control the robot:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard cmd_vel:=/robot/robotnik_base_control/cmd_vel_unstamped
```
