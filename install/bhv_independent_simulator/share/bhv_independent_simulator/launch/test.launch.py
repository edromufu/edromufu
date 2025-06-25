from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='bhv_independent_simulator',
            executable='bhv_sim',
            name='test_node',
            output='screen'
        )
    ])
