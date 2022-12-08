cmake_minimum_required(VERSION 3.0.2)
project(movement_msgs)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)


find_package(catkin REQUIRED COMPONENTS
  std_msgs
  message_generation
)

################################################
## Declare ROS messages, services and actions ##
################################################


## Generate messages in the 'msg' folder
add_message_files(
  FILES
  HeadParamsMsg.msg
  WalkingPositionsMsg.msg
  OpencmRequestMsg.msg
  OpencmResponseMsg.msg
  WebotsRequestMsg.msg
  ApprovedMovementMsg.msg
  WalkCreatorRequestMsg.msg
  )

## Generate services in the 'srv' folder
add_service_files(
  FILES
  BehRequestSrv.srv
  CommandToOpenCMSrv.srv
  WalkTestParametersSrv.srv
)

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs
)

################################################
## Declare ROS dynamic reconfigure parameters ##
################################################



###################################
## catkin specific configuration ##
###################################

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES movement_msgs
#  CATKIN_DEPENDS std_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


## Specify libraries to link a library or executable target against
# target_link_libraries(${PROJECT_NAME}_node
#   ${catkin_LIBRARIES}
# )

#############
## Install ##
#############


