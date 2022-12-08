################################################################################
# CMake
################################################################################
cmake_minimum_required(VERSION 2.8.3)
project(behaviour_msgs)

################################################################################
# Packages
################################################################################
find_package(catkin REQUIRED COMPONENTS
  message_generation
  std_msgs 
  geometry_msgs
  dynamic_reconfigure
)  

################################################################################
# Declare ROS messages, services and actions
################################################################################
# Generate dynamic parameters
generate_dynamic_reconfigure_options()


add_message_files(
  FILES
  simMovMsg.msg
)

add_service_files(
  FILES
  GameControllerSrv.srv
  ActionPanelSrv.srv
  service_page.srv
  yamlTransitionSrv.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
)

################################################################################
# Declare ROS dynamic reconfigure parameters
################################################################################

################################################################################
# Catkin specific configuration
################################################################################
catkin_package(
  INCLUDE_DIRS include
  CATKIN_DEPENDS message_generation std_msgs geometry_msgs dynamic_reconfigure
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
