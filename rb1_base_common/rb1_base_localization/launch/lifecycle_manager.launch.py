#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    start_lifecycle_manager = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager_localization',
        output='screen',
        parameters=[{'use_sim_time': True},
                    {'autostart': True},
                    {'node_names': ['map_server', 'amcl']}]
    )

    nodes = [
        start_lifecycle_manager
    ]

    return LaunchDescription(nodes)
