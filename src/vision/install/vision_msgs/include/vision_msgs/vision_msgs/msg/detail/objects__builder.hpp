// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from vision_msgs:msg/Objects.idl
// generated code does not contain a copyright notice

#ifndef VISION_MSGS__MSG__DETAIL__OBJECTS__BUILDER_HPP_
#define VISION_MSGS__MSG__DETAIL__OBJECTS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "vision_msgs/msg/detail/objects__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace vision_msgs
{

namespace msg
{

namespace builder
{

class Init_Objects_image
{
public:
  explicit Init_Objects_image(::vision_msgs::msg::Objects & msg)
  : msg_(msg)
  {}
  ::vision_msgs::msg::Objects image(::vision_msgs::msg::Objects::_image_type arg)
  {
    msg_.image = std::move(arg);
    return std::move(msg_);
  }

private:
  ::vision_msgs::msg::Objects msg_;
};

class Init_Objects_robots
{
public:
  explicit Init_Objects_robots(::vision_msgs::msg::Objects & msg)
  : msg_(msg)
  {}
  Init_Objects_image robots(::vision_msgs::msg::Objects::_robots_type arg)
  {
    msg_.robots = std::move(arg);
    return Init_Objects_image(msg_);
  }

private:
  ::vision_msgs::msg::Objects msg_;
};

class Init_Objects_goal
{
public:
  explicit Init_Objects_goal(::vision_msgs::msg::Objects & msg)
  : msg_(msg)
  {}
  Init_Objects_robots goal(::vision_msgs::msg::Objects::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return Init_Objects_robots(msg_);
  }

private:
  ::vision_msgs::msg::Objects msg_;
};

class Init_Objects_ball
{
public:
  Init_Objects_ball()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Objects_goal ball(::vision_msgs::msg::Objects::_ball_type arg)
  {
    msg_.ball = std::move(arg);
    return Init_Objects_goal(msg_);
  }

private:
  ::vision_msgs::msg::Objects msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::vision_msgs::msg::Objects>()
{
  return vision_msgs::msg::builder::Init_Objects_ball();
}

}  // namespace vision_msgs

#endif  // VISION_MSGS__MSG__DETAIL__OBJECTS__BUILDER_HPP_
