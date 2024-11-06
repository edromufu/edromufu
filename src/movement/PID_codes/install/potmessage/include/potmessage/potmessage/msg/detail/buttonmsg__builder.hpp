// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from potmessage:msg/Buttonmsg.idl
// generated code does not contain a copyright notice

#ifndef POTMESSAGE__MSG__DETAIL__BUTTONMSG__BUILDER_HPP_
#define POTMESSAGE__MSG__DETAIL__BUTTONMSG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "potmessage/msg/detail/buttonmsg__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace potmessage
{

namespace msg
{

namespace builder
{

class Init_Buttonmsg_bot2
{
public:
  explicit Init_Buttonmsg_bot2(::potmessage::msg::Buttonmsg & msg)
  : msg_(msg)
  {}
  ::potmessage::msg::Buttonmsg bot2(::potmessage::msg::Buttonmsg::_bot2_type arg)
  {
    msg_.bot2 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::potmessage::msg::Buttonmsg msg_;
};

class Init_Buttonmsg_bot1
{
public:
  Init_Buttonmsg_bot1()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Buttonmsg_bot2 bot1(::potmessage::msg::Buttonmsg::_bot1_type arg)
  {
    msg_.bot1 = std::move(arg);
    return Init_Buttonmsg_bot2(msg_);
  }

private:
  ::potmessage::msg::Buttonmsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::potmessage::msg::Buttonmsg>()
{
  return potmessage::msg::builder::Init_Buttonmsg_bot1();
}

}  // namespace potmessage

#endif  // POTMESSAGE__MSG__DETAIL__BUTTONMSG__BUILDER_HPP_
