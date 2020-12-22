from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

import os

def generate_launch_description():
    urdf_file = FindPackageShare('j2_controller').find('j2_controller') + "/urdf/j2.urdf"
    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()


    return LaunchDescription([
        Node(package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[
                {'robot_description': robot_desc}, 
                #{"use_tf_static": False}
            ]
        ),
        Node(
            package='joy_linux',
            executable='joy_linux_node',
            name='joy'
        ),
        #Node(
        #    package='teleop_twist_joy',
        #    executable='teleop_node',
        #    name='teleop',
        #    parameters=[
        #        {"axis_linear.x": 1},
        #        {"axis_angular.yaw": 3},
        #        {"require_enable_button": False},
        #        {"scale_linear.x": 0.5},
        #        {"scale_angular.yaw": 1.5}
        #    ]
        #),
        Node(
            package='j2_controller',
            executable='controller',
            output="screen",
            name='j2controller'
        )
    ])