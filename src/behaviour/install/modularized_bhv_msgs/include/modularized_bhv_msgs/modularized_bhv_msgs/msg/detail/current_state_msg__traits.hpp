// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from modularized_bhv_msgs:msg/CurrentStateMsg.idl
// generated code does not contain a copyright notice

#ifndef MODULARIZED_BHV_MSGS__MSG__DETAIL__CURRENT_STATE_MSG__TRAITS_HPP_
#define MODULARIZED_BHV_MSGS__MSG__DETAIL__CURRENT_STATE_MSG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "modularized_bhv_msgs/msg/detail/current_state_msg__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace modularized_bhv_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const CurrentStateMsg & msg,
  std::ostream & out)
{
  out << "{";
  // member: current_state
  {
    out << "current_state: ";
    rosidl_generator_traits::value_to_yaml(msg.current_state, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CurrentStateMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: current_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "current_state: ";
    rosidl_generator_traits::value_to_yaml(msg.current_state, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CurrentStateMsg & msg, bool use_flow_style = false)
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
  const modularized_bhv_msgs::msg::CurrentStateMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  modularized_bhv_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use modularized_bhv_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const modularized_bhv_msgs::msg::CurrentStateMsg & msg)
{
  return modularized_bhv_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<modularized_bhv_msgs::msg::CurrentStateMsg>()
{
  return "modularized_bhv_msgs::msg::CurrentStateMsg";
}

template<>
inline const char * name<modularized_bhv_msgs::msg::CurrentStateMsg>()
{
  return "modularized_bhv_msgs/msg/CurrentStateMsg";
}

template<>
struct has_fixed_size<modularized_bhv_msgs::msg::CurrentStateMsg>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<modularized_bhv_msgs::msg::CurrentStateMsg>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<modularized_bhv_msgs::msg::CurrentStateMsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MODULARIZED_BHV_MSGS__MSG__DETAIL__CURRENT_STATE_MSG__TRAITS_HPP_
