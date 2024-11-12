// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from movement_utils:srv/EnableTorque.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__SRV__DETAIL__ENABLE_TORQUE__BUILDER_HPP_
#define MOVEMENT_UTILS__SRV__DETAIL__ENABLE_TORQUE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "movement_utils/srv/detail/enable_torque__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace movement_utils
{

namespace srv
{

namespace builder
{

class Init_EnableTorque_Request_motor_ids
{
public:
  explicit Init_EnableTorque_Request_motor_ids(::movement_utils::srv::EnableTorque_Request & msg)
  : msg_(msg)
  {}
  ::movement_utils::srv::EnableTorque_Request motor_ids(::movement_utils::srv::EnableTorque_Request::_motor_ids_type arg)
  {
    msg_.motor_ids = std::move(arg);
    return std::move(msg_);
  }

private:
  ::movement_utils::srv::EnableTorque_Request msg_;
};

class Init_EnableTorque_Request_data
{
public:
  Init_EnableTorque_Request_data()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_EnableTorque_Request_motor_ids data(::movement_utils::srv::EnableTorque_Request::_data_type arg)
  {
    msg_.data = std::move(arg);
    return Init_EnableTorque_Request_motor_ids(msg_);
  }

private:
  ::movement_utils::srv::EnableTorque_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::movement_utils::srv::EnableTorque_Request>()
{
  return movement_utils::srv::builder::Init_EnableTorque_Request_data();
}

}  // namespace movement_utils


namespace movement_utils
{

namespace srv
{

namespace builder
{

class Init_EnableTorque_Response_success
{
public:
  Init_EnableTorque_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::movement_utils::srv::EnableTorque_Response success(::movement_utils::srv::EnableTorque_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::movement_utils::srv::EnableTorque_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::movement_utils::srv::EnableTorque_Response>()
{
  return movement_utils::srv::builder::Init_EnableTorque_Response_success();
}

}  // namespace movement_utils

#endif  // MOVEMENT_UTILS__SRV__DETAIL__ENABLE_TORQUE__BUILDER_HPP_
