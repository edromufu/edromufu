// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from vision_msgs:msg/Webotsmsg.idl
// generated code does not contain a copyright notice

#ifndef VISION_MSGS__MSG__DETAIL__WEBOTSMSG__TRAITS_HPP_
#define VISION_MSGS__MSG__DETAIL__WEBOTSMSG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "vision_msgs/msg/detail/webotsmsg__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'ball'
#include "vision_msgs/msg/detail/ball__traits.hpp"
// Member 'leftgoalpost'
#include "vision_msgs/msg/detail/leftgoalpost__traits.hpp"
// Member 'rightgoalpost'
#include "vision_msgs/msg/detail/rightgoalpost__traits.hpp"

namespace vision_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Webotsmsg & msg,
  std::ostream & out)
{
  out << "{";
  // member: searching
  {
    out << "searching: ";
    rosidl_generator_traits::value_to_yaml(msg.searching, out);
    out << ", ";
  }

  // member: fps
  {
    out << "fps: ";
    rosidl_generator_traits::value_to_yaml(msg.fps, out);
    out << ", ";
  }

  // member: ball
  {
    out << "ball: ";
    to_flow_style_yaml(msg.ball, out);
    out << ", ";
  }

  // member: leftgoalpost
  {
    out << "leftgoalpost: ";
    to_flow_style_yaml(msg.leftgoalpost, out);
    out << ", ";
  }

  // member: rightgoalpost
  {
    out << "rightgoalpost: ";
    to_flow_style_yaml(msg.rightgoalpost, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Webotsmsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: searching
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "searching: ";
    rosidl_generator_traits::value_to_yaml(msg.searching, out);
    out << "\n";
  }

  // member: fps
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "fps: ";
    rosidl_generator_traits::value_to_yaml(msg.fps, out);
    out << "\n";
  }

  // member: ball
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ball:\n";
    to_block_style_yaml(msg.ball, out, indentation + 2);
  }

  // member: leftgoalpost
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "leftgoalpost:\n";
    to_block_style_yaml(msg.leftgoalpost, out, indentation + 2);
  }

  // member: rightgoalpost
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rightgoalpost:\n";
    to_block_style_yaml(msg.rightgoalpost, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Webotsmsg & msg, bool use_flow_style = false)
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
  const vision_msgs::msg::Webotsmsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  vision_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use vision_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const vision_msgs::msg::Webotsmsg & msg)
{
  return vision_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<vision_msgs::msg::Webotsmsg>()
{
  return "vision_msgs::msg::Webotsmsg";
}

template<>
inline const char * name<vision_msgs::msg::Webotsmsg>()
{
  return "vision_msgs/msg/Webotsmsg";
}

template<>
struct has_fixed_size<vision_msgs::msg::Webotsmsg>
  : std::integral_constant<bool, has_fixed_size<vision_msgs::msg::Ball>::value && has_fixed_size<vision_msgs::msg::Leftgoalpost>::value && has_fixed_size<vision_msgs::msg::Rightgoalpost>::value> {};

template<>
struct has_bounded_size<vision_msgs::msg::Webotsmsg>
  : std::integral_constant<bool, has_bounded_size<vision_msgs::msg::Ball>::value && has_bounded_size<vision_msgs::msg::Leftgoalpost>::value && has_bounded_size<vision_msgs::msg::Rightgoalpost>::value> {};

template<>
struct is_message<vision_msgs::msg::Webotsmsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // VISION_MSGS__MSG__DETAIL__WEBOTSMSG__TRAITS_HPP_
