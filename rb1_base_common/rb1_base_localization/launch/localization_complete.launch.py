#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    pkg_rb1_base_localization = get_package_share_directory('rb1_base_localization')

    start_map_server = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_rb1_base_localization, 'launch', 'map_server.launch.py')
        )
    )

    start_amcl = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_rb1_base_localization, 'launch', 'amcl.launch.py')
        )
    )

    start_lifecycle_manager = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_rb1_base_localization, 'launch', 'lifecycle_manager.launch.py')
        )
    )

    nodes = [
        start_map_server,
        start_amcl,
        start_lifecycle_manager
    ]

    return LaunchDescription(nodes)