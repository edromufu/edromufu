// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from movement_utils:msg/HeadMotorsData.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__MSG__DETAIL__HEAD_MOTORS_DATA__BUILDER_HPP_
#define MOVEMENT_UTILS__MSG__DETAIL__HEAD_MOTORS_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "movement_utils/msg/detail/head_motors_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace movement_utils
{

namespace msg
{

namespace builder
{

class Init_HeadMotorsData_pos_vector
{
public:
  Init_HeadMotorsData_pos_vector()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::movement_utils::msg::HeadMotorsData pos_vector(::movement_utils::msg::HeadMotorsData::_pos_vector_type arg)
  {
    msg_.pos_vector = std::move(arg);
    return std::move(msg_);
  }

private:
  ::movement_utils::msg::HeadMotorsData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::movement_utils::msg::HeadMotorsData>()
{
  return movement_utils::msg::builder::Init_HeadMotorsData_pos_vector();
}

}  // namespace movement_utils

#endif  // MOVEMENT_UTILS__MSG__DETAIL__HEAD_MOTORS_DATA__BUILDER_HPP_
