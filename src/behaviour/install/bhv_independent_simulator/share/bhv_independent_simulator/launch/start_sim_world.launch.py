from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Argumento para modo sem GUI
    no_gui_arg = DeclareLaunchArgument(
        'no_gui',
        default_value='false',
        description='Start Webots with minimal GUI'
    )
    
    # Caminho para o arquivo world
    world_path = PathJoinSubstitution([
        FindPackageShare('bhv_independent_simulator'),
        'worlds',
        'bhv_sim_world.wbt'
    ])
    
    # Inclusão do launch do Webots ROS2
    webots_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('bhv_independent_simulator'),
                'launch',
                'webots.launch.py'
            ])
        ]),
        launch_arguments={
            'mode': 'realtime',
            'no_gui': LaunchConfiguration('no_gui'),
            'world': world_path
        }.items()
    )
    
    return LaunchDescription([
        no_gui_arg,
        webots_launch
    ])