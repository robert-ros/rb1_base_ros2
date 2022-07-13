#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node

import xacro

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.actions import ExecuteProcess
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution


# this is the function launch  system will look for
def generate_launch_description():

    pkg_rb1_base_control = get_package_share_directory('rb1_base_control')

    # TO DO: recieve from rb1_base_one_robot
    xacro_file = 'rb1_base_std.urdf.xacro'
    pkg_rb1_description = "rb1_base_description"
    xacro_path = os.path.join(get_package_share_directory(pkg_rb1_description), "robots", xacro_file)
    robot_description = {"robot_description": xacro.process_file(xacro_path).toxml()}


    robot_controllers = PathJoinSubstitution(
        [
            pkg_rb1_base_control,
            "config",
            "rb1_base_control.yaml",
        ]
    )


    control_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[robot_description, robot_controllers, {'use_sim_time': True}],
        output="both",
    )

    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
    )

    robot_controller_spawner = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["robotnik_base_control", "-c", "/controller_manager"],
    )

    # Delay start of robot_controller after `joint_state_broadcaster`
    delay_robot_controller_spawner_after_joint_state_broadcaster_spawner = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=joint_state_broadcaster_spawner,
            on_exit=[robot_controller_spawner],
        )
    )


    nodes = [
        control_node,
        joint_state_broadcaster_spawner,
        delay_robot_controller_spawner_after_joint_state_broadcaster_spawner
    ]

    return LaunchDescription(nodes)