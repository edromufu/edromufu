from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Argumentos de lançamento
    world_arg = DeclareLaunchArgument(
        'world',
        default_value='',
        description='Path to the world to load'
    )
    
    mode_arg = DeclareLaunchArgument(
        'mode',
        default_value='realtime',
        description='Startup mode (realtime, fast, pause)'
    )
    
    no_gui_arg = DeclareLaunchArgument(
        'no_gui',
        default_value='false',
        description='Start Webots with minimal GUI'
    )
    
    # Nó do Webots (usando webots_ros2 oficial)
    webots_node = ExecuteProcess(
        cmd=[
            'ros2', 'launch', 'webots_ros2_core', 'robot_launch.py',
            'world:=', LaunchConfiguration('world'),
            'mode:=', LaunchConfiguration('mode'),
            'gui:=', PythonExpression(["'true' if ", LaunchConfiguration('no_gui'), " == 'false' else 'false'"])
        ],
        name='webots',
        output='screen'
    )
    
    return LaunchDescription([
        world_arg,
        mode_arg,
        no_gui_arg,
        webots_node
    ])