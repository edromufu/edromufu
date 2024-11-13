// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from movement_utils:srv/Rotate.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__SRV__DETAIL__ROTATE__BUILDER_HPP_
#define MOVEMENT_UTILS__SRV__DETAIL__ROTATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "movement_utils/srv/detail/rotate__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace movement_utils
{

namespace srv
{

namespace builder
{

class Init_Rotate_Request_steps_number
{
public:
  explicit Init_Rotate_Request_steps_number(::movement_utils::srv::Rotate_Request & msg)
  : msg_(msg)
  {}
  ::movement_utils::srv::Rotate_Request steps_number(::movement_utils::srv::Rotate_Request::_steps_number_type arg)
  {
    msg_.steps_number = std::move(arg);
    return std::move(msg_);
  }

private:
  ::movement_utils::srv::Rotate_Request msg_;
};

class Init_Rotate_Request_direction
{
public:
  Init_Rotate_Request_direction()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Rotate_Request_steps_number direction(::movement_utils::srv::Rotate_Request::_direction_type arg)
  {
    msg_.direction = std::move(arg);
    return Init_Rotate_Request_steps_number(msg_);
  }

private:
  ::movement_utils::srv::Rotate_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::movement_utils::srv::Rotate_Request>()
{
  return movement_utils::srv::builder::Init_Rotate_Request_direction();
}

}  // namespace movement_utils


namespace movement_utils
{

namespace srv
{

namespace builder
{

class Init_Rotate_Response_success
{
public:
  Init_Rotate_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::movement_utils::srv::Rotate_Response success(::movement_utils::srv::Rotate_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::movement_utils::srv::Rotate_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::movement_utils::srv::Rotate_Response>()
{
  return movement_utils::srv::builder::Init_Rotate_Response_success();
}

}  // namespace movement_utils

#endif  // MOVEMENT_UTILS__SRV__DETAIL__ROTATE__BUILDER_HPP_
