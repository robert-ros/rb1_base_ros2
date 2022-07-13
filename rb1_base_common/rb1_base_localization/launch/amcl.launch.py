#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    pkg_rb1_base_localization = get_package_share_directory('rb1_base_localization')

    map_name = 'demo_map/demo_map.yaml'
    map_file = os.path.join(pkg_rb1_base_localization,'maps',map_name)

    nav2_yaml = os.path.join(pkg_rb1_base_localization,'config/amcl.yaml')

    start_amcl = Node(
        package='nav2_amcl',
        executable='amcl',
        name='amcl',
        output='screen',
        parameters=[nav2_yaml, {'use_sim_time': True}],
        remappings=[
            ('/scan', 'front_laser/scan'),
            ('/map', 'map')
        ]
    )

    nodes = [
        start_amcl,
    ]

    return LaunchDescription(nodes)
