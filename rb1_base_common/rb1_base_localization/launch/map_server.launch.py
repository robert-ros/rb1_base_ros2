#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    pkg_rb1_base_localization = get_package_share_directory('rb1_base_localization')
    map_name = 'demo_map/demo_map.yaml'
    map_file = os.path.join(pkg_rb1_base_localization, 'maps', map_name)

    start_map_server = Node(
        package='nav2_map_server',
        executable='map_server',
        name='map_server',
        output='screen',
        parameters=[{'use_sim_time': True},
                    {'topic_name': 'map'},
                    {'frame_id': 'robot_map'},
                    {'yaml_filename': map_file}]
    )

    nodes = [
        start_map_server,
    ]

    return LaunchDescription(nodes)
