// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from potmessage:msg/Imumsg.idl
// generated code does not contain a copyright notice

#ifndef POTMESSAGE__MSG__DETAIL__IMUMSG__TRAITS_HPP_
#define POTMESSAGE__MSG__DETAIL__IMUMSG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "potmessage/msg/detail/imumsg__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace potmessage
{

namespace msg
{

inline void to_flow_style_yaml(
  const Imumsg & msg,
  std::ostream & out)
{
  out << "{";
  // member: imu
  {
    if (msg.imu.size() == 0) {
      out << "imu: []";
    } else {
      out << "imu: [";
      size_t pending_items = msg.imu.size();
      for (auto item : msg.imu) {
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
  const Imumsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: imu
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.imu.size() == 0) {
      out << "imu: []\n";
    } else {
      out << "imu:\n";
      for (auto item : msg.imu) {
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

inline std::string to_yaml(const Imumsg & msg, bool use_flow_style = false)
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

}  // namespace potmessage

namespace rosidl_generator_traits
{

[[deprecated("use potmessage::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const potmessage::msg::Imumsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  potmessage::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use potmessage::msg::to_yaml() instead")]]
inline std::string to_yaml(const potmessage::msg::Imumsg & msg)
{
  return potmessage::msg::to_yaml(msg);
}

template<>
inline const char * data_type<potmessage::msg::Imumsg>()
{
  return "potmessage::msg::Imumsg";
}

template<>
inline const char * name<potmessage::msg::Imumsg>()
{
  return "potmessage/msg/Imumsg";
}

template<>
struct has_fixed_size<potmessage::msg::Imumsg>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<potmessage::msg::Imumsg>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<potmessage::msg::Imumsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // POTMESSAGE__MSG__DETAIL__IMUMSG__TRAITS_HPP_
