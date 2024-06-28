// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from vision_msgs:msg/Robot.idl
// generated code does not contain a copyright notice

#ifndef VISION_MSGS__MSG__DETAIL__ROBOT__BUILDER_HPP_
#define VISION_MSGS__MSG__DETAIL__ROBOT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "vision_msgs/msg/detail/robot__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace vision_msgs
{

namespace msg
{

namespace builder
{

class Init_Robot_y
{
public:
  explicit Init_Robot_y(::vision_msgs::msg::Robot & msg)
  : msg_(msg)
  {}
  ::vision_msgs::msg::Robot y(::vision_msgs::msg::Robot::_y_type arg)
  {
    msg_.y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::vision_msgs::msg::Robot msg_;
};

class Init_Robot_x
{
public:
  Init_Robot_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Robot_y x(::vision_msgs::msg::Robot::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Robot_y(msg_);
  }

private:
  ::vision_msgs::msg::Robot msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::vision_msgs::msg::Robot>()
{
  return vision_msgs::msg::builder::Init_Robot_x();
}

}  // namespace vision_msgs

#endif  // VISION_MSGS__MSG__DETAIL__ROBOT__BUILDER_HPP_
