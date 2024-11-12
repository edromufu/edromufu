// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from potmessage:msg/Potmsg.idl
// generated code does not contain a copyright notice

#ifndef POTMESSAGE__MSG__DETAIL__POTMSG__BUILDER_HPP_
#define POTMESSAGE__MSG__DETAIL__POTMSG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "potmessage/msg/detail/potmsg__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace potmessage
{

namespace msg
{

namespace builder
{

class Init_Potmsg_imu3
{
public:
  explicit Init_Potmsg_imu3(::potmessage::msg::Potmsg & msg)
  : msg_(msg)
  {}
  ::potmessage::msg::Potmsg imu3(::potmessage::msg::Potmsg::_imu3_type arg)
  {
    msg_.imu3 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::potmessage::msg::Potmsg msg_;
};

class Init_Potmsg_imu2
{
public:
  explicit Init_Potmsg_imu2(::potmessage::msg::Potmsg & msg)
  : msg_(msg)
  {}
  Init_Potmsg_imu3 imu2(::potmessage::msg::Potmsg::_imu2_type arg)
  {
    msg_.imu2 = std::move(arg);
    return Init_Potmsg_imu3(msg_);
  }

private:
  ::potmessage::msg::Potmsg msg_;
};

class Init_Potmsg_imu1
{
public:
  explicit Init_Potmsg_imu1(::potmessage::msg::Potmsg & msg)
  : msg_(msg)
  {}
  Init_Potmsg_imu2 imu1(::potmessage::msg::Potmsg::_imu1_type arg)
  {
    msg_.imu1 = std::move(arg);
    return Init_Potmsg_imu2(msg_);
  }

private:
  ::potmessage::msg::Potmsg msg_;
};

class Init_Potmsg_pot8
{
public:
  explicit Init_Potmsg_pot8(::potmessage::msg::Potmsg & msg)
  : msg_(msg)
  {}
  Init_Potmsg_imu1 pot8(::potmessage::msg::Potmsg::_pot8_type arg)
  {
    msg_.pot8 = std::move(arg);
    return Init_Potmsg_imu1(msg_);
  }

private:
  ::potmessage::msg::Potmsg msg_;
};

class Init_Potmsg_pot7
{
public:
  explicit Init_Potmsg_pot7(::potmessage::msg::Potmsg & msg)
  : msg_(msg)
  {}
  Init_Potmsg_pot8 pot7(::potmessage::msg::Potmsg::_pot7_type arg)
  {
    msg_.pot7 = std::move(arg);
    return Init_Potmsg_pot8(msg_);
  }

private:
  ::potmessage::msg::Potmsg msg_;
};

class Init_Potmsg_pot6
{
public:
  explicit Init_Potmsg_pot6(::potmessage::msg::Potmsg & msg)
  : msg_(msg)
  {}
  Init_Potmsg_pot7 pot6(::potmessage::msg::Potmsg::_pot6_type arg)
  {
    msg_.pot6 = std::move(arg);
    return Init_Potmsg_pot7(msg_);
  }

private:
  ::potmessage::msg::Potmsg msg_;
};

class Init_Potmsg_pot5
{
public:
  explicit Init_Potmsg_pot5(::potmessage::msg::Potmsg & msg)
  : msg_(msg)
  {}
  Init_Potmsg_pot6 pot5(::potmessage::msg::Potmsg::_pot5_type arg)
  {
    msg_.pot5 = std::move(arg);
    return Init_Potmsg_pot6(msg_);
  }

private:
  ::potmessage::msg::Potmsg msg_;
};

class Init_Potmsg_pot4
{
public:
  explicit Init_Potmsg_pot4(::potmessage::msg::Potmsg & msg)
  : msg_(msg)
  {}
  Init_Potmsg_pot5 pot4(::potmessage::msg::Potmsg::_pot4_type arg)
  {
    msg_.pot4 = std::move(arg);
    return Init_Potmsg_pot5(msg_);
  }

private:
  ::potmessage::msg::Potmsg msg_;
};

class Init_Potmsg_pot3
{
public:
  explicit Init_Potmsg_pot3(::potmessage::msg::Potmsg & msg)
  : msg_(msg)
  {}
  Init_Potmsg_pot4 pot3(::potmessage::msg::Potmsg::_pot3_type arg)
  {
    msg_.pot3 = std::move(arg);
    return Init_Potmsg_pot4(msg_);
  }

private:
  ::potmessage::msg::Potmsg msg_;
};

class Init_Potmsg_pot2
{
public:
  explicit Init_Potmsg_pot2(::potmessage::msg::Potmsg & msg)
  : msg_(msg)
  {}
  Init_Potmsg_pot3 pot2(::potmessage::msg::Potmsg::_pot2_type arg)
  {
    msg_.pot2 = std::move(arg);
    return Init_Potmsg_pot3(msg_);
  }

private:
  ::potmessage::msg::Potmsg msg_;
};

class Init_Potmsg_pot1
{
public:
  Init_Potmsg_pot1()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Potmsg_pot2 pot1(::potmessage::msg::Potmsg::_pot1_type arg)
  {
    msg_.pot1 = std::move(arg);
    return Init_Potmsg_pot2(msg_);
  }

private:
  ::potmessage::msg::Potmsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::potmessage::msg::Potmsg>()
{
  return potmessage::msg::builder::Init_Potmsg_pot1();
}

}  // namespace potmessage

#endif  // POTMESSAGE__MSG__DETAIL__POTMSG__BUILDER_HPP_
