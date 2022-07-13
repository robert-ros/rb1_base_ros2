#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

import xacro

def generate_launch_description():

    pkg_rb1_base_control = get_package_share_directory('rb1_base_control')

    entity_name = "rb1"
    position = [0.0, 0.0, 0.2]
    orientation = [0.0, 0.0, 0.0]

    xacro_file = 'rb1_base_std.urdf.xacro'
    pkg_rb1_description = "rb1_base_description"


    # Load urdf model
    xacro_path = os.path.join(get_package_share_directory(pkg_rb1_description), "robots", xacro_file)
    xacro_file =  xacro.process_file(xacro_path).toxml()

    # Robot State Publisher
    start_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output="both",
        parameters=[{
            'use_sim_time': True,
            'robot_description': xacro_file
        }],
    )

    # Spawn robot
    start_spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='spawn_entity',
        output='screen',
        arguments=['-entity',
                   entity_name,
                   '-x', str(position[0]), '-y', str(position[1]), '-z', str(position[2]),
                   '-R', str(orientation[0]), '-P', str(orientation[1]), '-Y', str(orientation[2]),
                   '-topic', '/robot_description'
                   ]
    )

    # ROS controller
    start_rb1_base_control = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_rb1_base_control, 'launch', 'rb1_base_control.launch.py')
        )
    )


    nodes = [
        start_robot_state_publisher,
        start_spawn_robot,
        #start_rb1_base_control
    ]

    return LaunchDescription(nodes)