cmake_minimum_required(VERSION 2.8.3)
project(vision_msgs)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
	rospy		 	
	std_msgs
	sensor_msgs
	message_generation
)


## Generate messages in the 'msg' folder
add_message_files(
   FILES
   Objects.msg
   Ball.msg
   Goal.msg
   Robot.msg
   Leftgoalpost.msg
   Rightgoalpost.msg
   Webotsmsg.msg
)


## Generate added messages and services with any dependencies listed here
generate_messages(
   DEPENDENCIES
   std_msgs
   sensor_msgs
)

catkin_package(
#  INCLUDE_DIRS include

 CATKIN_DEPENDS message_runtime std_msgs sensor_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
${catkin_INCLUDE_DIRS}
)
