// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from vision_msgs:msg/Objects.idl
// generated code does not contain a copyright notice

#ifndef VISION_MSGS__MSG__DETAIL__OBJECTS__TRAITS_HPP_
#define VISION_MSGS__MSG__DETAIL__OBJECTS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "vision_msgs/msg/detail/objects__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'ball'
#include "vision_msgs/msg/detail/ball__traits.hpp"
// Member 'goal'
#include "vision_msgs/msg/detail/goal__traits.hpp"
// Member 'robots'
#include "vision_msgs/msg/detail/robot__traits.hpp"
// Member 'image'
#include "sensor_msgs/msg/detail/image__traits.hpp"

namespace vision_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Objects & msg,
  std::ostream & out)
{
  out << "{";
  // member: ball
  {
    out << "ball: ";
    to_flow_style_yaml(msg.ball, out);
    out << ", ";
  }

  // member: goal
  {
    out << "goal: ";
    to_flow_style_yaml(msg.goal, out);
    out << ", ";
  }

  // member: robots
  {
    if (msg.robots.size() == 0) {
      out << "robots: []";
    } else {
      out << "robots: [";
      size_t pending_items = msg.robots.size();
      for (auto item : msg.robots) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: image
  {
    out << "image: ";
    to_flow_style_yaml(msg.image, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Objects & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: ball
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ball:\n";
    to_block_style_yaml(msg.ball, out, indentation + 2);
  }

  // member: goal
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal:\n";
    to_block_style_yaml(msg.goal, out, indentation + 2);
  }

  // member: robots
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.robots.size() == 0) {
      out << "robots: []\n";
    } else {
      out << "robots:\n";
      for (auto item : msg.robots) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: image
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "image:\n";
    to_block_style_yaml(msg.image, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Objects & msg, bool use_flow_style = false)
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
  const vision_msgs::msg::Objects & msg,
  std::ostream & out, size_t indentation = 0)
{
  vision_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use vision_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const vision_msgs::msg::Objects & msg)
{
  return vision_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<vision_msgs::msg::Objects>()
{
  return "vision_msgs::msg::Objects";
}

template<>
inline const char * name<vision_msgs::msg::Objects>()
{
  return "vision_msgs/msg/Objects";
}

template<>
struct has_fixed_size<vision_msgs::msg::Objects>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<vision_msgs::msg::Objects>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<vision_msgs::msg::Objects>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // VISION_MSGS__MSG__DETAIL__OBJECTS__TRAITS_HPP_
