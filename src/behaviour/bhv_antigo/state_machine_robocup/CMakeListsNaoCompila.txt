cmake_minimum_required(VERSION 2.8.3)
project(state_machine)

find_package(catkin REQUIRED COMPONENTS
  behaviour_msgs
  vision_msgs
  movement_msgs
  rospy
  sensor_msgs
  std_msgs
)


catkin_package(
)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

catkin_python_setup()




