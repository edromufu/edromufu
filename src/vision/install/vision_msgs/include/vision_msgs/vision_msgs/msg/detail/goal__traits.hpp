// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from vision_msgs:msg/Goal.idl
// generated code does not contain a copyright notice

#ifndef VISION_MSGS__MSG__DETAIL__GOAL__TRAITS_HPP_
#define VISION_MSGS__MSG__DETAIL__GOAL__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "vision_msgs/msg/detail/goal__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace vision_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Goal & msg,
  std::ostream & out)
{
  out << "{";
  // member: found
  {
    out << "found: ";
    rosidl_generator_traits::value_to_yaml(msg.found, out);
    out << ", ";
  }

  // member: x
  {
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << ", ";
  }

  // member: y
  {
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Goal & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: found
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "found: ";
    rosidl_generator_traits::value_to_yaml(msg.found, out);
    out << "\n";
  }

  // member: x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << "\n";
  }

  // member: y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Goal & msg, bool use_flow_style = false)
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

}  // namespace vision_msgs

namespace rosidl_generator_traits
{

[[deprecated("use vision_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const vision_msgs::msg::Goal & msg,
  std::ostream & out, size_t indentation = 0)
{
  vision_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use vision_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const vision_msgs::msg::Goal & msg)
{
  return vision_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<vision_msgs::msg::Goal>()
{
  return "vision_msgs::msg::Goal";
}

template<>
inline const char * name<vision_msgs::msg::Goal>()
{
  return "vision_msgs/msg/Goal";
}

template<>
struct has_fixed_size<vision_msgs::msg::Goal>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<vision_msgs::msg::Goal>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<vision_msgs::msg::Goal>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // VISION_MSGS__MSG__DETAIL__GOAL__TRAITS_HPP_
