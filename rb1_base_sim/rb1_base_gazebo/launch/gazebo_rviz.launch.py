#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
# from ament_index_python.packages import get_package_prefix

def generate_launch_description():

    pkg_rb1_base_gazebo = get_package_share_directory('rb1_base_gazebo')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    gazebo_world = os.path.join(
        pkg_rb1_base_gazebo,
        'worlds',
        'demo.world'
    )

    # Gazebo
    start_gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py'),
        ),
        #launch_arguments={'world': gazebo_world}.items()
        launch_arguments={"verbose": "true"}.items()
    )    


    return LaunchDescription([
        start_gazebo
    ])
