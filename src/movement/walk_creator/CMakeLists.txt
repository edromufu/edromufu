cmake_minimum_required(VERSION 3.0.2)
project(walk_creator)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  movement_msgs
  std_msgs
)

find_package(PkgConfig REQUIRED)
pkg_check_modules(JSONCPP jsoncpp)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES walk_creator
  CATKIN_DEPENDS roscpp
#  DEPENDS system_lib
)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
  ${JSONCPP_INCLUDE_DIRS}
)

#Sources files
set(SOURCES_FILES_WALK
    include/CubicSpline.cpp
    include/HumanoidModel.cpp
    include/IKWalk.cpp
    include/LegIK.cpp
    include/Polynom.cpp
    include/Spline.cpp
)
set(SOURCES_FILES_EXAMPLE
    src/walk_creator.cpp
)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/..)

#Eigen library dependency
find_package(Eigen3 REQUIRED)
include_directories(${EIGEN3_INCLUDE_DIR})

#Enable C++11
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
#Enable compiler Warning
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -W -Wall")

#Build example application
add_executable(walk_creator 
    ${SOURCES_FILES_WALK} ${SOURCES_FILES_EXAMPLE})
target_link_libraries(walk_creator ${catkin_LIBRARIES} ${JSONCPP_LIBRARIES})
