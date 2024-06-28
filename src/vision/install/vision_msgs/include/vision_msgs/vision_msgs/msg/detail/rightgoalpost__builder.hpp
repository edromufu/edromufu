// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from vision_msgs:msg/Rightgoalpost.idl
// generated code does not contain a copyright notice

#ifndef VISION_MSGS__MSG__DETAIL__RIGHTGOALPOST__BUILDER_HPP_
#define VISION_MSGS__MSG__DETAIL__RIGHTGOALPOST__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "vision_msgs/msg/detail/rightgoalpost__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace vision_msgs
{

namespace msg
{

namespace builder
{

class Init_Rightgoalpost_roi_height
{
public:
  explicit Init_Rightgoalpost_roi_height(::vision_msgs::msg::Rightgoalpost & msg)
  : msg_(msg)
  {}
  ::vision_msgs::msg::Rightgoalpost roi_height(::vision_msgs::msg::Rightgoalpost::_roi_height_type arg)
  {
    msg_.roi_height = std::move(arg);
    return std::move(msg_);
  }

private:
  ::vision_msgs::msg::Rightgoalpost msg_;
};

class Init_Rightgoalpost_roi_width
{
public:
  explicit Init_Rightgoalpost_roi_width(::vision_msgs::msg::Rightgoalpost & msg)
  : msg_(msg)
  {}
  Init_Rightgoalpost_roi_height roi_width(::vision_msgs::msg::Rightgoalpost::_roi_width_type arg)
  {
    msg_.roi_width = std::move(arg);
    return Init_Rightgoalpost_roi_height(msg_);
  }

private:
  ::vision_msgs::msg::Rightgoalpost msg_;
};

class Init_Rightgoalpost_y
{
public:
  explicit Init_Rightgoalpost_y(::vision_msgs::msg::Rightgoalpost & msg)
  : msg_(msg)
  {}
  Init_Rightgoalpost_roi_width y(::vision_msgs::msg::Rightgoalpost::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_Rightgoalpost_roi_width(msg_);
  }

private:
  ::vision_msgs::msg::Rightgoalpost msg_;
};

class Init_Rightgoalpost_x
{
public:
  explicit Init_Rightgoalpost_x(::vision_msgs::msg::Rightgoalpost & msg)
  : msg_(msg)
  {}
  Init_Rightgoalpost_y x(::vision_msgs::msg::Rightgoalpost::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Rightgoalpost_y(msg_);
  }

private:
  ::vision_msgs::msg::Rightgoalpost msg_;
};

class Init_Rightgoalpost_found
{
public:
  Init_Rightgoalpost_found()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Rightgoalpost_x found(::vision_msgs::msg::Rightgoalpost::_found_type arg)
  {
    msg_.found = std::move(arg);
    return Init_Rightgoalpost_x(msg_);
  }

private:
  ::vision_msgs::msg::Rightgoalpost msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::vision_msgs::msg::Rightgoalpost>()
{
  return vision_msgs::msg::builder::Init_Rightgoalpost_found();
}

}  // namespace vision_msgs

#endif  // VISION_MSGS__MSG__DETAIL__RIGHTGOALPOST__BUILDER_HPP_
