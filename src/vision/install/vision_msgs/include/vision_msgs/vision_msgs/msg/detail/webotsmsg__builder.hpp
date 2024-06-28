// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from vision_msgs:msg/Webotsmsg.idl
// generated code does not contain a copyright notice

#ifndef VISION_MSGS__MSG__DETAIL__WEBOTSMSG__BUILDER_HPP_
#define VISION_MSGS__MSG__DETAIL__WEBOTSMSG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "vision_msgs/msg/detail/webotsmsg__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace vision_msgs
{

namespace msg
{

namespace builder
{

class Init_Webotsmsg_rightgoalpost
{
public:
  explicit Init_Webotsmsg_rightgoalpost(::vision_msgs::msg::Webotsmsg & msg)
  : msg_(msg)
  {}
  ::vision_msgs::msg::Webotsmsg rightgoalpost(::vision_msgs::msg::Webotsmsg::_rightgoalpost_type arg)
  {
    msg_.rightgoalpost = std::move(arg);
    return std::move(msg_);
  }

private:
  ::vision_msgs::msg::Webotsmsg msg_;
};

class Init_Webotsmsg_leftgoalpost
{
public:
  explicit Init_Webotsmsg_leftgoalpost(::vision_msgs::msg::Webotsmsg & msg)
  : msg_(msg)
  {}
  Init_Webotsmsg_rightgoalpost leftgoalpost(::vision_msgs::msg::Webotsmsg::_leftgoalpost_type arg)
  {
    msg_.leftgoalpost = std::move(arg);
    return Init_Webotsmsg_rightgoalpost(msg_);
  }

private:
  ::vision_msgs::msg::Webotsmsg msg_;
};

class Init_Webotsmsg_ball
{
public:
  explicit Init_Webotsmsg_ball(::vision_msgs::msg::Webotsmsg & msg)
  : msg_(msg)
  {}
  Init_Webotsmsg_leftgoalpost ball(::vision_msgs::msg::Webotsmsg::_ball_type arg)
  {
    msg_.ball = std::move(arg);
    return Init_Webotsmsg_leftgoalpost(msg_);
  }

private:
  ::vision_msgs::msg::Webotsmsg msg_;
};

class Init_Webotsmsg_fps
{
public:
  explicit Init_Webotsmsg_fps(::vision_msgs::msg::Webotsmsg & msg)
  : msg_(msg)
  {}
  Init_Webotsmsg_ball fps(::vision_msgs::msg::Webotsmsg::_fps_type arg)
  {
    msg_.fps = std::move(arg);
    return Init_Webotsmsg_ball(msg_);
  }

private:
  ::vision_msgs::msg::Webotsmsg msg_;
};

class Init_Webotsmsg_searching
{
public:
  Init_Webotsmsg_searching()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Webotsmsg_fps searching(::vision_msgs::msg::Webotsmsg::_searching_type arg)
  {
    msg_.searching = std::move(arg);
    return Init_Webotsmsg_fps(msg_);
  }

private:
  ::vision_msgs::msg::Webotsmsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::vision_msgs::msg::Webotsmsg>()
{
  return vision_msgs::msg::builder::Init_Webotsmsg_searching();
}

}  // namespace vision_msgs

#endif  // VISION_MSGS__MSG__DETAIL__WEBOTSMSG__BUILDER_HPP_
