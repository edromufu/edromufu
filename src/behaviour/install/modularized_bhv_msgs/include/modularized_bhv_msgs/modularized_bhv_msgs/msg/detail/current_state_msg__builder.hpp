// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from modularized_bhv_msgs:msg/CurrentStateMsg.idl
// generated code does not contain a copyright notice

#ifndef MODULARIZED_BHV_MSGS__MSG__DETAIL__CURRENT_STATE_MSG__BUILDER_HPP_
#define MODULARIZED_BHV_MSGS__MSG__DETAIL__CURRENT_STATE_MSG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "modularized_bhv_msgs/msg/detail/current_state_msg__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace modularized_bhv_msgs
{

namespace msg
{

namespace builder
{

class Init_CurrentStateMsg_current_state
{
public:
  Init_CurrentStateMsg_current_state()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::modularized_bhv_msgs::msg::CurrentStateMsg current_state(::modularized_bhv_msgs::msg::CurrentStateMsg::_current_state_type arg)
  {
    msg_.current_state = std::move(arg);
    return std::move(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::CurrentStateMsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::modularized_bhv_msgs::msg::CurrentStateMsg>()
{
  return modularized_bhv_msgs::msg::builder::Init_CurrentStateMsg_current_state();
}

}  // namespace modularized_bhv_msgs

#endif  // MODULARIZED_BHV_MSGS__MSG__DETAIL__CURRENT_STATE_MSG__BUILDER_HPP_
