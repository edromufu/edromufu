// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from movement_utils:msg/BodyMotorsData.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__MSG__DETAIL__BODY_MOTORS_DATA__BUILDER_HPP_
#define MOVEMENT_UTILS__MSG__DETAIL__BODY_MOTORS_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "movement_utils/msg/detail/body_motors_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace movement_utils
{

namespace msg
{

namespace builder
{

class Init_BodyMotorsData_pos_vector
{
public:
  Init_BodyMotorsData_pos_vector()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::movement_utils::msg::BodyMotorsData pos_vector(::movement_utils::msg::BodyMotorsData::_pos_vector_type arg)
  {
    msg_.pos_vector = std::move(arg);
    return std::move(msg_);
  }

private:
  ::movement_utils::msg::BodyMotorsData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::movement_utils::msg::BodyMotorsData>()
{
  return movement_utils::msg::builder::Init_BodyMotorsData_pos_vector();
}

}  // namespace movement_utils

#endif  // MOVEMENT_UTILS__MSG__DETAIL__BODY_MOTORS_DATA__BUILDER_HPP_
