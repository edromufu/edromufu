from launch import LaunchDescription
from launch_ros.actions import Node	
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    #Declaração dos argumentos que poderão ser passados na execução de ros2 launch
    camera = DeclareLaunchArgument('camera',default_value='0')
    output_img = DeclareLaunchArgument('img_output',default_value='False')
    ajuste = DeclareLaunchArgument('ajuste',default_value='False')
    bright = DeclareLaunchArgument('brilho',default_value='4')

    #Estrutura do launch
    return LaunchDescription([
       camera,
       output_img,
       ajuste,
       bright,
       
       #Visão
       Node(
           package='object_finder',
           namespace='EDROM',
           executable='finder',
           name='vision',
           output='screen',
           parameters=[
               {'vision/camera': LaunchConfiguration('camera')},
               {'vision/img_output': LaunchConfiguration('img_output')},
               {'vision/ajuste' : LaunchConfiguration('ajuste')},
               {'vision/brilho': LaunchConfiguration('brilho')},
            ],
            emulate_tty=True,   #Utililizado para os prints acontecerem em tempo real
        )
   ])
