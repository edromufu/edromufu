from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Inicia o ambiente de simulação do Webots
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('bhv_independent_simulator'),
                    'launch/start_sim_world.launch.py'
                ])
            ])
        ),
        
        # Inicia o supervisor da robô simulada
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('bhv_independent_simulator'),
                    'launch/start_sim_supervisor.launch.py'
                ])
            ])
        ),
        
       
    
    ])
       