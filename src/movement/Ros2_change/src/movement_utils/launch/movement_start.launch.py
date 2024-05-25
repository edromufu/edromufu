from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, TextSubstitution


def generate_launch_description():
    return LaunchDescription([
        # Declare launch arguments
        DeclareLaunchArgument('u2d2_connected', default_value='true'),
        DeclareLaunchArgument('u2d2_port', default_value='/dev/ttyU2D2'),
        DeclareLaunchArgument('robot_name', default_value='aurea'),
        DeclareLaunchArgument('page_creation', default_value='false'),
        DeclareLaunchArgument('queue_time', default_value='0.05'),
        DeclareLaunchArgument('visualization', default_value='false'),
        DeclareLaunchArgument('head_plugged', default_value='true'),
        DeclareLaunchArgument('behaviour', default_value='true'),
        DeclareLaunchArgument('img_output', default_value='false'),

        # Node: movement_core
        Node(
            package='movement_core',
            executable='core',
            name='movement_central',
            output='screen',
            parameters=[{
                'name': LaunchConfiguration('robot_name'),
                'queue_time': LaunchConfiguration('queue_time'),
                'pub2vis': LaunchConfiguration('visualization'),
            }]
        ),

        # Node: u2d2
        Node(
            package='u2d2_comm',
            executable='dynamixel_sdk_comm',
            name='u2d2',
            output='screen',
            condition=IfCondition(LaunchConfiguration('u2d2_connected')), 
            parameters=[{
                'port': LaunchConfiguration('u2d2_port'),
                'robot_name': LaunchConfiguration('robot_name'),
            }]
        ),

        # Node: u2d2_false
        Node(
            package='u2d2_comm',
            executable='dynamixel_sdk_test',
            name='u2d2_false',
            output='screen',
            condition=UnlessCondition(LaunchConfiguration('u2d2_connected')),  
            parameters=[{
                'robot_name': LaunchConfiguration('robot_name'),
            }]
        ),

        # Node: head_core
        Node(
            package='movement_core',
            executable='core_head',
            name='head_core',
            output='screen',
            condition=IfCondition(LaunchConfiguration('head_plugged')),
        ),

        # Include: vision.launch
        #IncludeLaunchDescription(
        #    PythonLaunchDescriptionSource([
        #        PathJoinSubstitution([
        #            FindPackageShare('object_finder'),
        #            'launch',
        #            'vision.launch.py'
        #        ])
        #    ]),
        #    condition=IfCondition(LaunchConfiguration('head_plugged')),
        #    launch_arguments={
        #        'img_output': LaunchConfiguration('img_output'),
        #        'ajuste': 'false',
        #        'brilho': '4',
        #        'camera': '0',
        #    }.items(),
        #),

        # Node: page_creator
        Node(
            package='movement_pages',
            executable='page_interface',
            name='page_creator',
            output='screen',
            condition=IfCondition(LaunchConfiguration('page_creation')),
        ),

        # Include: display.launch
        #IncludeLaunchDescription(
        #    PythonLaunchDescriptionSource([
        #            PathJoinSubstitution([
        #                FindPackageShare('humanoid_visualization'),
        #                'launch',
        #                'display.launch.py'
        #            ])
        #    ]),
        #    condition=IfCondition(LaunchConfiguration('visualization')),
        #    launch_arguments={
        #        'model': PathJoinSubstitution([
        #                FindPackageShare('humanoid_visualization'),
        #                    'urdf',
        #                    LaunchConfiguration('robot_name'),
        #                    TextSubstitution(text='.urdf')
        #        ]),
        #       'rvizconfig': PathJoinSubstitution([
        #                FindPackageShare('humanoid_visualization'),
        #                    'urdf',
        #                    'movement.rviz'
        #        ]),
        #    }.items(),
        #),

        # Include: behaviour.launch
        #IncludeLaunchDescription(
        #    PythonLaunchDescriptionSource([
        #        PathJoinSubstitution([
        #            FindPackageShare('transitions_and_states'),
        #                'launch',
        #                'behaviour.launch.py'
        #        ])
        #    ]),
        #    condition=IfCondition(LaunchConfiguration('behaviour')),
        #),
    ])