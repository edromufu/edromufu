// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from vision_msgs:msg/Goal.idl
// generated code does not contain a copyright notice

#ifndef VISION_MSGS__MSG__DETAIL__GOAL__BUILDER_HPP_
#define VISION_MSGS__MSG__DETAIL__GOAL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "vision_msgs/msg/detail/goal__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace vision_msgs
{

namespace msg
{

namespace builder
{

class Init_Goal_y
{
public:
  explicit Init_Goal_y(::vision_msgs::msg::Goal & msg)
  : msg_(msg)
  {}
  ::vision_msgs::msg::Goal y(::vision_msgs::msg::Goal::_y_type arg)
  {
    msg_.y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::vision_msgs::msg::Goal msg_;
};

class Init_Goal_x
{
public:
  explicit Init_Goal_x(::vision_msgs::msg::Goal & msg)
  : msg_(msg)
  {}
  Init_Goal_y x(::vision_msgs::msg::Goal::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Goal_y(msg_);
  }

private:
  ::vision_msgs::msg::Goal msg_;
};

class Init_Goal_found
{
public:
  Init_Goal_found()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Goal_x found(::vision_msgs::msg::Goal::_found_type arg)
  {
    msg_.found = std::move(arg);
    return Init_Goal_x(msg_);
  }

private:
  ::vision_msgs::msg::Goal msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::vision_msgs::msg::Goal>()
{
  return vision_msgs::msg::builder::Init_Goal_found();
}

}  // namespace vision_msgs

#endif  // VISION_MSGS__MSG__DETAIL__GOAL__BUILDER_HPP_
