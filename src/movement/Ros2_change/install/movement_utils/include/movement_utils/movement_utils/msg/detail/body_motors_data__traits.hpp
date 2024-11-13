// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from movement_utils:msg/BodyMotorsData.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__MSG__DETAIL__BODY_MOTORS_DATA__TRAITS_HPP_
#define MOVEMENT_UTILS__MSG__DETAIL__BODY_MOTORS_DATA__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "movement_utils/msg/detail/body_motors_data__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace movement_utils
{

namespace msg
{

inline void to_flow_style_yaml(
  const BodyMotorsData & msg,
  std::ostream & out)
{
  out << "{";
  // member: pos_vector
  {
    if (msg.pos_vector.size() == 0) {
      out << "pos_vector: []";
    } else {
      out << "pos_vector: [";
      size_t pending_items = msg.pos_vector.size();
      for (auto item : msg.pos_vector) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const BodyMotorsData & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: pos_vector
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.pos_vector.size() == 0) {
      out << "pos_vector: []\n";
    } else {
      out << "pos_vector:\n";
      for (auto item : msg.pos_vector) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const BodyMotorsData & msg, bool use_flow_style = false)
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

}  // namespace movement_utils

namespace rosidl_generator_traits
{

[[deprecated("use movement_utils::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const movement_utils::msg::BodyMotorsData & msg,
  std::ostream & out, size_t indentation = 0)
{
  movement_utils::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use movement_utils::msg::to_yaml() instead")]]
inline std::string to_yaml(const movement_utils::msg::BodyMotorsData & msg)
{
  return movement_utils::msg::to_yaml(msg);
}

template<>
inline const char * data_type<movement_utils::msg::BodyMotorsData>()
{
  return "movement_utils::msg::BodyMotorsData";
}

template<>
inline const char * name<movement_utils::msg::BodyMotorsData>()
{
  return "movement_utils/msg/BodyMotorsData";
}

template<>
struct has_fixed_size<movement_utils::msg::BodyMotorsData>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<movement_utils::msg::BodyMotorsData>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<movement_utils::msg::BodyMotorsData>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MOVEMENT_UTILS__MSG__DETAIL__BODY_MOTORS_DATA__TRAITS_HPP_
