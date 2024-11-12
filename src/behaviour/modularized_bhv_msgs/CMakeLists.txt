################################################################################
# CMake
################################################################################
cmake_minimum_required(VERSION 2.8.3)
project(modularized_bhv_msgs)

################################################################################
# Packages
################################################################################
find_package(catkin REQUIRED COMPONENTS
  message_generation
  message_runtime
  std_msgs 
  geometry_msgs
  dynamic_reconfigure
)  

################################################################################
# Declare ROS messages, services and actions
################################################################################

add_message_files(
  FILES
  stateMachineMsg.msg
  currentStateMsg.msg
  gameControllerMsg.msg
)

add_service_files(
  FILES
  moveRequest.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
)

################################################################################
# Catkin specific configuration
################################################################################
catkin_package(
  CATKIN_DEPENDS message_runtime std_msgs geometry_msgs dynamic_reconfigure
)

################################################################################
# Build
################################################################################
include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

################################################################################
# Install
################################################################################

################################################################################
# Test
################################################################################
