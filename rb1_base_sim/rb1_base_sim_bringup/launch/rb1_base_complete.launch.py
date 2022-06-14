#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():

    pkg_rb1_base_gazebo = get_package_share_directory('rb1_base_gazebo')

    start_rb1_base_gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_rb1_base_gazebo, 'launch', 'rb1_base_gazebo.launch.py')
        )
    )

    nodes = [
        start_rb1_base_gazebo
    ]

    return LaunchDescription(nodes)