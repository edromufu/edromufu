// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from modularized_bhv_msgs:msg/StateMachineMsg.idl
// generated code does not contain a copyright notice

#ifndef MODULARIZED_BHV_MSGS__MSG__DETAIL__STATE_MACHINE_MSG__BUILDER_HPP_
#define MODULARIZED_BHV_MSGS__MSG__DETAIL__STATE_MACHINE_MSG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "modularized_bhv_msgs/msg/detail/state_machine_msg__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace modularized_bhv_msgs
{

namespace msg
{

namespace builder
{

class Init_StateMachineMsg_head_kick_check
{
public:
  explicit Init_StateMachineMsg_head_kick_check(::modularized_bhv_msgs::msg::StateMachineMsg & msg)
  : msg_(msg)
  {}
  ::modularized_bhv_msgs::msg::StateMachineMsg head_kick_check(::modularized_bhv_msgs::msg::StateMachineMsg::_head_kick_check_type arg)
  {
    msg_.head_kick_check = std::move(arg);
    return std::move(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::StateMachineMsg msg_;
};

class Init_StateMachineMsg_hor_motor_out_of_center
{
public:
  explicit Init_StateMachineMsg_hor_motor_out_of_center(::modularized_bhv_msgs::msg::StateMachineMsg & msg)
  : msg_(msg)
  {}
  Init_StateMachineMsg_head_kick_check hor_motor_out_of_center(::modularized_bhv_msgs::msg::StateMachineMsg::_hor_motor_out_of_center_type arg)
  {
    msg_.hor_motor_out_of_center = std::move(arg);
    return Init_StateMachineMsg_head_kick_check(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::StateMachineMsg msg_;
};

class Init_StateMachineMsg_fall_state
{
public:
  explicit Init_StateMachineMsg_fall_state(::modularized_bhv_msgs::msg::StateMachineMsg & msg)
  : msg_(msg)
  {}
  Init_StateMachineMsg_hor_motor_out_of_center fall_state(::modularized_bhv_msgs::msg::StateMachineMsg::_fall_state_type arg)
  {
    msg_.fall_state = std::move(arg);
    return Init_StateMachineMsg_hor_motor_out_of_center(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::StateMachineMsg msg_;
};

class Init_StateMachineMsg_ball_found
{
public:
  explicit Init_StateMachineMsg_ball_found(::modularized_bhv_msgs::msg::StateMachineMsg & msg)
  : msg_(msg)
  {}
  Init_StateMachineMsg_fall_state ball_found(::modularized_bhv_msgs::msg::StateMachineMsg::_ball_found_type arg)
  {
    msg_.ball_found = std::move(arg);
    return Init_StateMachineMsg_fall_state(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::StateMachineMsg msg_;
};

class Init_StateMachineMsg_ball_close
{
public:
  explicit Init_StateMachineMsg_ball_close(::modularized_bhv_msgs::msg::StateMachineMsg & msg)
  : msg_(msg)
  {}
  Init_StateMachineMsg_ball_found ball_close(::modularized_bhv_msgs::msg::StateMachineMsg::_ball_close_type arg)
  {
    msg_.ball_close = std::move(arg);
    return Init_StateMachineMsg_ball_found(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::StateMachineMsg msg_;
};

class Init_StateMachineMsg_ball_position
{
public:
  Init_StateMachineMsg_ball_position()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_StateMachineMsg_ball_close ball_position(::modularized_bhv_msgs::msg::StateMachineMsg::_ball_position_type arg)
  {
    msg_.ball_position = std::move(arg);
    return Init_StateMachineMsg_ball_close(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::StateMachineMsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::modularized_bhv_msgs::msg::StateMachineMsg>()
{
  return modularized_bhv_msgs::msg::builder::Init_StateMachineMsg_ball_position();
}

}  // namespace modularized_bhv_msgs

#endif  // MODULARIZED_BHV_MSGS__MSG__DETAIL__STATE_MACHINE_MSG__BUILDER_HPP_
