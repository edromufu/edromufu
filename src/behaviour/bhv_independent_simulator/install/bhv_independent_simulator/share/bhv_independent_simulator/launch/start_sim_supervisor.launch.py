from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable, ExecuteProcess
from launch.substitutions import LaunchConfiguration, EnvironmentVariable
from launch_ros.actions import Node
from launch.conditions import UnlessCondition, IfCondition
from launch.substitutions import PythonExpression

def generate_launch_description():
    # Argumento de lançamento
    auto_close_arg = DeclareLaunchArgument(
        'auto_close',
        default_value='false',
        description='Startup mode'
    )
    
    # Configuração de variáveis de ambiente
    ld_library_path = SetEnvironmentVariable(
        'LD_LIBRARY_PATH',
        [EnvironmentVariable('LD_LIBRARY_PATH'), ':', EnvironmentVariable('WEBOTS_HOME'), '/lib/controller']
    )
    
    # Configuração condicional do PYTHONPATH
    python_path_py27 = SetEnvironmentVariable(
        'PYTHONPATH',
        [EnvironmentVariable('PYTHONPATH'), ':', EnvironmentVariable('WEBOTS_HOME'), '/lib/controller/python27'],
        condition=UnlessCondition(
            PythonExpression(["'", EnvironmentVariable('ROS_DISTRO'), "' == 'noetic'"])  
        )  
    )
    
    python_path_py38 = SetEnvironmentVariable(
        'PYTHONPATH',
        [EnvironmentVariable('PYTHONPATH'), ':', EnvironmentVariable('WEBOTS_HOME'), '/lib/controller/python38'],
        condition=IfCondition(
            PythonExpression(["'", EnvironmentVariable('ROS_DISTRO'), "' == 'noetic'"])  
        )  
    )
    
    # Nó do supervisor
    bhv_simulator_node = Node(
        package='bhv_independent_simulator',
        executable='bhv_sim.py',
        name='bhv_simulator',
        output='screen',
        on_exit=ExecuteProcess(
            cmd=['ros2', 'launch', 'webots_ros2_core', 'webots_launcher.py'],
            condition=IfCondition(LaunchConfiguration('auto_close'))
        if LaunchConfiguration('auto_close') == 'true' else None
        )
    )
    
    return LaunchDescription([
        auto_close_arg,
        ld_library_path,
        python_path_py27,
        python_path_py38,
        bhv_simulator_node
    ])