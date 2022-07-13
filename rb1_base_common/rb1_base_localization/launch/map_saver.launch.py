#!/usr/bin/python3
#-*- coding: utf-8 -*-

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    map_name = "my_test_map.yaml"

    start_map_saver = Node(
        package='nav2_map_server',
        executable='map_saver_cli',
        name='map_saver_cli',
        output='screen',
        arguments=['-f', 'my_test_map'],
        parameters=[{'topic_name': 'map'},
                    {'frame_id': 'robot_map'},
                    {'save_map_timeout': 5000},
                    {'occupied_thresh_default': 0.65},
                    {'free_thresh_default': 0.25}]
    )

    nodes = [
        start_map_saver
    ]

    return LaunchDescription(nodes)