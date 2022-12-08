cmake_minimum_required(VERSION 2.8.3)

project(webots_natasha)

find_package(Protobuf REQUIRED)

find_package(catkin REQUIRED)

catkin_package()

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

protobuf_generate_python(PROTO_PY scripts/messages.proto)
add_custom_target(robocup_api_proto ALL DEPENDS ${PROTO_PY})
add_custom_command(
  TARGET robocup_api_proto POST_BUILD
  COMMAND ${CMAKE_COMMAND} -E copy ${PROTO_PY} ${CMAKE_SOURCE_DIR}/src/simulacao/webots_natasha
)
