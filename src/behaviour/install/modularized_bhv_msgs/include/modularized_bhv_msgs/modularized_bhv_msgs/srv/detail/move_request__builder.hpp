// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from modularized_bhv_msgs:srv/MoveRequest.idl
// generated code does not contain a copyright notice

#ifndef MODULARIZED_BHV_MSGS__SRV__DETAIL__MOVE_REQUEST__BUILDER_HPP_
#define MODULARIZED_BHV_MSGS__SRV__DETAIL__MOVE_REQUEST__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "modularized_bhv_msgs/srv/detail/move_request__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace modularized_bhv_msgs
{

namespace srv
{

namespace builder
{

class Init_MoveRequest_Request_move_request
{
public:
  Init_MoveRequest_Request_move_request()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::modularized_bhv_msgs::srv::MoveRequest_Request move_request(::modularized_bhv_msgs::srv::MoveRequest_Request::_move_request_type arg)
  {
    msg_.move_request = std::move(arg);
    return std::move(msg_);
  }

private:
  ::modularized_bhv_msgs::srv::MoveRequest_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::modularized_bhv_msgs::srv::MoveRequest_Request>()
{
  return modularized_bhv_msgs::srv::builder::Init_MoveRequest_Request_move_request();
}

}  // namespace modularized_bhv_msgs


namespace modularized_bhv_msgs
{

namespace srv
{

namespace builder
{

class Init_MoveRequest_Response_success
{
public:
  Init_MoveRequest_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::modularized_bhv_msgs::srv::MoveRequest_Response success(::modularized_bhv_msgs::srv::MoveRequest_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::modularized_bhv_msgs::srv::MoveRequest_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::modularized_bhv_msgs::srv::MoveRequest_Response>()
{
  return modularized_bhv_msgs::srv::builder::Init_MoveRequest_Response_success();
}

}  // namespace modularized_bhv_msgs

#endif  // MODULARIZED_BHV_MSGS__SRV__DETAIL__MOVE_REQUEST__BUILDER_HPP_
