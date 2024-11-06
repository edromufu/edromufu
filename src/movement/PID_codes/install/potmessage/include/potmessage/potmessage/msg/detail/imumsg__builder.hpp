// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from potmessage:msg/Imumsg.idl
// generated code does not contain a copyright notice

#ifndef POTMESSAGE__MSG__DETAIL__IMUMSG__BUILDER_HPP_
#define POTMESSAGE__MSG__DETAIL__IMUMSG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "potmessage/msg/detail/imumsg__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace potmessage
{

namespace msg
{

namespace builder
{

class Init_Imumsg_imu
{
public:
  Init_Imumsg_imu()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::potmessage::msg::Imumsg imu(::potmessage::msg::Imumsg::_imu_type arg)
  {
    msg_.imu = std::move(arg);
    return std::move(msg_);
  }

private:
  ::potmessage::msg::Imumsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::potmessage::msg::Imumsg>()
{
  return potmessage::msg::builder::Init_Imumsg_imu();
}

}  // namespace potmessage

#endif  // POTMESSAGE__MSG__DETAIL__IMUMSG__BUILDER_HPP_
