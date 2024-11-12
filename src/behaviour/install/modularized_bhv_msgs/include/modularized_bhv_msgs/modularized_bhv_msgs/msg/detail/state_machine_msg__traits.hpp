// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from modularized_bhv_msgs:msg/StateMachineMsg.idl
// generated code does not contain a copyright notice

#ifndef MODULARIZED_BHV_MSGS__MSG__DETAIL__STATE_MACHINE_MSG__TRAITS_HPP_
#define MODULARIZED_BHV_MSGS__MSG__DETAIL__STATE_MACHINE_MSG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "modularized_bhv_msgs/msg/detail/state_machine_msg__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace modularized_bhv_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const StateMachineMsg & msg,
  std::ostream & out)
{
  out << "{";
  // member: ball_position
  {
    out << "ball_position: ";
    rosidl_generator_traits::value_to_yaml(msg.ball_position, out);
    out << ", ";
  }

  // member: ball_close
  {
    out << "ball_close: ";
    rosidl_generator_traits::value_to_yaml(msg.ball_close, out);
    out << ", ";
  }

  // member: ball_found
  {
    out << "ball_found: ";
    rosidl_generator_traits::value_to_yaml(msg.ball_found, out);
    out << ", ";
  }

  // member: fall_state
  {
    out << "fall_state: ";
    rosidl_generator_traits::value_to_yaml(msg.fall_state, out);
    out << ", ";
  }

  // member: hor_motor_out_of_center
  {
    out << "hor_motor_out_of_center: ";
    rosidl_generator_traits::value_to_yaml(msg.hor_motor_out_of_center, out);
    out << ", ";
  }

  // member: head_kick_check
  {
    out << "head_kick_check: ";
    rosidl_generator_traits::value_to_yaml(msg.head_kick_check, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const StateMachineMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: ball_position
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ball_position: ";
    rosidl_generator_traits::value_to_yaml(msg.ball_position, out);
    out << "\n";
  }

  // member: ball_close
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ball_close: ";
    rosidl_generator_traits::value_to_yaml(msg.ball_close, out);
    out << "\n";
  }

  // member: ball_found
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ball_found: ";
    rosidl_generator_traits::value_to_yaml(msg.ball_found, out);
    out << "\n";
  }

  // member: fall_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "fall_state: ";
    rosidl_generator_traits::value_to_yaml(msg.fall_state, out);
    out << "\n";
  }

  // member: hor_motor_out_of_center
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "hor_motor_out_of_center: ";
    rosidl_generator_traits::value_to_yaml(msg.hor_motor_out_of_center, out);
    out << "\n";
  }

  // member: head_kick_check
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "head_kick_check: ";
    rosidl_generator_traits::value_to_yaml(msg.head_kick_check, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const StateMachineMsg & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace modularized_bhv_msgs

namespace rosidl_generator_traits
{

[[deprecated("use modularized_bhv_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const modularized_bhv_msgs::msg::StateMachineMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  modularized_bhv_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use modularized_bhv_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const modularized_bhv_msgs::msg::StateMachineMsg & msg)
{
  return modularized_bhv_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<modularized_bhv_msgs::msg::StateMachineMsg>()
{
  return "modularized_bhv_msgs::msg::StateMachineMsg";
}

template<>
inline const char * name<modularized_bhv_msgs::msg::StateMachineMsg>()
{
  return "modularized_bhv_msgs/msg/StateMachineMsg";
}

template<>
struct has_fixed_size<modularized_bhv_msgs::msg::StateMachineMsg>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<modularized_bhv_msgs::msg::StateMachineMsg>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<modularized_bhv_msgs::msg::StateMachineMsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MODULARIZED_BHV_MSGS__MSG__DETAIL__STATE_MACHINE_MSG__TRAITS_HPP_
