// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from vision_msgs:msg/Leftgoalpost.idl
// generated code does not contain a copyright notice

#ifndef VISION_MSGS__MSG__DETAIL__LEFTGOALPOST__BUILDER_HPP_
#define VISION_MSGS__MSG__DETAIL__LEFTGOALPOST__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "vision_msgs/msg/detail/leftgoalpost__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace vision_msgs
{

namespace msg
{

namespace builder
{

class Init_Leftgoalpost_roi_height
{
public:
  explicit Init_Leftgoalpost_roi_height(::vision_msgs::msg::Leftgoalpost & msg)
  : msg_(msg)
  {}
  ::vision_msgs::msg::Leftgoalpost roi_height(::vision_msgs::msg::Leftgoalpost::_roi_height_type arg)
  {
    msg_.roi_height = std::move(arg);
    return std::move(msg_);
  }

private:
  ::vision_msgs::msg::Leftgoalpost msg_;
};

class Init_Leftgoalpost_roi_width
{
public:
  explicit Init_Leftgoalpost_roi_width(::vision_msgs::msg::Leftgoalpost & msg)
  : msg_(msg)
  {}
  Init_Leftgoalpost_roi_height roi_width(::vision_msgs::msg::Leftgoalpost::_roi_width_type arg)
  {
    msg_.roi_width = std::move(arg);
    return Init_Leftgoalpost_roi_height(msg_);
  }

private:
  ::vision_msgs::msg::Leftgoalpost msg_;
};

class Init_Leftgoalpost_y
{
public:
  explicit Init_Leftgoalpost_y(::vision_msgs::msg::Leftgoalpost & msg)
  : msg_(msg)
  {}
  Init_Leftgoalpost_roi_width y(::vision_msgs::msg::Leftgoalpost::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_Leftgoalpost_roi_width(msg_);
  }

private:
  ::vision_msgs::msg::Leftgoalpost msg_;
};

class Init_Leftgoalpost_x
{
public:
  explicit Init_Leftgoalpost_x(::vision_msgs::msg::Leftgoalpost & msg)
  : msg_(msg)
  {}
  Init_Leftgoalpost_y x(::vision_msgs::msg::Leftgoalpost::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Leftgoalpost_y(msg_);
  }

private:
  ::vision_msgs::msg::Leftgoalpost msg_;
};

class Init_Leftgoalpost_found
{
public:
  Init_Leftgoalpost_found()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Leftgoalpost_x found(::vision_msgs::msg::Leftgoalpost::_found_type arg)
  {
    msg_.found = std::move(arg);
    return Init_Leftgoalpost_x(msg_);
  }

private:
  ::vision_msgs::msg::Leftgoalpost msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::vision_msgs::msg::Leftgoalpost>()
{
  return vision_msgs::msg::builder::Init_Leftgoalpost_found();
}

}  // namespace vision_msgs

#endif  // VISION_MSGS__MSG__DETAIL__LEFTGOALPOST__BUILDER_HPP_
