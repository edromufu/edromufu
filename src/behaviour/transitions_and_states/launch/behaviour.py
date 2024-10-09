from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([

        # Argumento para a conexão do IMU
        DeclareLaunchArgument(
            'imu_connected',
            default_value='true',
            description='Define se o IMU está conectado'
        ),

        # Argumento para a porta do IMU
        DeclareLaunchArgument(
            'imu_port',
            default_value='/dev/ttyIMU',
            description='Porta serial para o IMU'
        ),

        # Argumento para o estado inicial do GameController
        DeclareLaunchArgument(
            'game_controller_state',
            default_value='3',  # Estado "Playing" por padrão
            description='Estado inicial do GameController (0: Inicial, 1: Ready, 2: Set, 3: Playing, 4: Finished)'
        ),

        # Máquina de Estados
        Node(
            package='transitions_and_states',
            executable='state_machine_receiver.py',
            name='behaviour_node',
            output='screen',
        ),

        Node(
            package='states_routine',
            executable='walking_routine.py',
            name='walking',
            output='screen',
        ),
        Node(
            package='states_routine',
            executable='kick_routine.py',
            name='kick',
            output='screen',
        ),
        Node(
            package='states_routine',
            executable='stand_still_routine.py',
            name='stand_still',
            output='screen',
        ),
        Node(
            package='states_routine',
            executable='getting_up_routine.py',
            name='getting_up',
            output='screen',
        ),

        # Interpretação
        Node(
            package='sensor_observer',
            executable='ros_packer.py',
            name='ros_packer',
            output='screen',
        ),

        # Leitura do IMU (apenas se imu_connected for True)
        Node(
            package='imu_ros_arduino',
            executable='imu_read.py',
            name='imu_ros_arduino',
            output='screen',
            condition=LaunchConfiguration('imu_connected'),
            parameters=[{'port': LaunchConfiguration('imu_port')}],
        ),

        # Nó do GameController para controlar o estado do jogo
        Node(
            package='game_controller_pkg',  # Substitua pelo nome do pacote correto do GameController
            executable='game_controller_node.py',  # Substitua pelo nome correto do executável
            name='game_controller',
            output='screen',
            parameters=[{'initial_state': LaunchConfiguration('game_controller_state')}],  # Parâmetro para definir o estado inicial
        ),
    ])
