// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from movement_utils:srv/WalkForward.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__SRV__DETAIL__WALK_FORWARD__BUILDER_HPP_
#define MOVEMENT_UTILS__SRV__DETAIL__WALK_FORWARD__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "movement_utils/srv/detail/walk_forward__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace movement_utils
{

namespace srv
{

namespace builder
{

class Init_WalkForward_Request_steps_number
{
public:
  explicit Init_WalkForward_Request_steps_number(::movement_utils::srv::WalkForward_Request & msg)
  : msg_(msg)
  {}
  ::movement_utils::srv::WalkForward_Request steps_number(::movement_utils::srv::WalkForward_Request::_steps_number_type arg)
  {
    msg_.steps_number = std::move(arg);
    return std::move(msg_);
  }

private:
  ::movement_utils::srv::WalkForward_Request msg_;
};

class Init_WalkForward_Request_support_foot
{
public:
  Init_WalkForward_Request_support_foot()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_WalkForward_Request_steps_number support_foot(::movement_utils::srv::WalkForward_Request::_support_foot_type arg)
  {
    msg_.support_foot = std::move(arg);
    return Init_WalkForward_Request_steps_number(msg_);
  }

private:
  ::movement_utils::srv::WalkForward_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::movement_utils::srv::WalkForward_Request>()
{
  return movement_utils::srv::builder::Init_WalkForward_Request_support_foot();
}

}  // namespace movement_utils


namespace movement_utils
{

namespace srv
{

namespace builder
{

class Init_WalkForward_Response_success
{
public:
  Init_WalkForward_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::movement_utils::srv::WalkForward_Response success(::movement_utils::srv::WalkForward_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::movement_utils::srv::WalkForward_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::movement_utils::srv::WalkForward_Response>()
{
  return movement_utils::srv::builder::Init_WalkForward_Response_success();
}

}  // namespace movement_utils

#endif  // MOVEMENT_UTILS__SRV__DETAIL__WALK_FORWARD__BUILDER_HPP_
