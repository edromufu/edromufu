// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from movement_utils:srv/Gait.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__SRV__DETAIL__GAIT__BUILDER_HPP_
#define MOVEMENT_UTILS__SRV__DETAIL__GAIT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "movement_utils/srv/detail/gait__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace movement_utils
{

namespace srv
{

namespace builder
{

class Init_Gait_Request_step_height
{
public:
  explicit Init_Gait_Request_step_height(::movement_utils::srv::Gait_Request & msg)
  : msg_(msg)
  {}
  ::movement_utils::srv::Gait_Request step_height(::movement_utils::srv::Gait_Request::_step_height_type arg)
  {
    msg_.step_height = std::move(arg);
    return std::move(msg_);
  }

private:
  ::movement_utils::srv::Gait_Request msg_;
};

class Init_Gait_Request_steps_number
{
public:
  Init_Gait_Request_steps_number()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Gait_Request_step_height steps_number(::movement_utils::srv::Gait_Request::_steps_number_type arg)
  {
    msg_.steps_number = std::move(arg);
    return Init_Gait_Request_step_height(msg_);
  }

private:
  ::movement_utils::srv::Gait_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::movement_utils::srv::Gait_Request>()
{
  return movement_utils::srv::builder::Init_Gait_Request_steps_number();
}

}  // namespace movement_utils


namespace movement_utils
{

namespace srv
{

namespace builder
{

class Init_Gait_Response_success
{
public:
  Init_Gait_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::movement_utils::srv::Gait_Response success(::movement_utils::srv::Gait_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::movement_utils::srv::Gait_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::movement_utils::srv::Gait_Response>()
{
  return movement_utils::srv::builder::Init_Gait_Response_success();
}

}  // namespace movement_utils

#endif  // MOVEMENT_UTILS__SRV__DETAIL__GAIT__BUILDER_HPP_
