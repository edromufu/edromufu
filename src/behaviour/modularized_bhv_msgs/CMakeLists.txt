################################################################################
# CMake
################################################################################
cmake_minimum_required(VERSION 3.8)
project(modularized_bhv_msgs)

################################################################################
# Packages
################################################################################
# Encontra o Ament (sistema de build do ROS2) e os pacotes necessários.
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

################################################################################
# Declare ROS messages, services and actions
################################################################################
# Macro unificada do ROS2 para gerar mensagens e serviços
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/StateMachineMsg.msg"
  "msg/CurrentStateMsg.msg"
  "srv/MoveRequest.srv"
  DEPENDENCIES std_msgs geometry_msgs
)

################################################################################
# Catkin specific configuration
################################################################################
# Macro que finaliza o empacotamento no Ament
ament_package()