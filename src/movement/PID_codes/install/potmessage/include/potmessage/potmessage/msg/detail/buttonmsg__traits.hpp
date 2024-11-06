// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from potmessage:msg/Buttonmsg.idl
// generated code does not contain a copyright notice

#ifndef POTMESSAGE__MSG__DETAIL__BUTTONMSG__TRAITS_HPP_
#define POTMESSAGE__MSG__DETAIL__BUTTONMSG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "potmessage/msg/detail/buttonmsg__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace potmessage
{

namespace msg
{

inline void to_flow_style_yaml(
  const Buttonmsg & msg,
  std::ostream & out)
{
  out << "{";
  // member: bot1
  {
    out << "bot1: ";
    rosidl_generator_traits::value_to_yaml(msg.bot1, out);
    out << ", ";
  }

  // member: bot2
  {
    out << "bot2: ";
    rosidl_generator_traits::value_to_yaml(msg.bot2, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Buttonmsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: bot1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "bot1: ";
    rosidl_generator_traits::value_to_yaml(msg.bot1, out);
    out << "\n";
  }

  // member: bot2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "bot2: ";
    rosidl_generator_traits::value_to_yaml(msg.bot2, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Buttonmsg & msg, bool use_flow_style = false)
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
  const potmessage::msg::Buttonmsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  potmessage::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use potmessage::msg::to_yaml() instead")]]
inline std::string to_yaml(const potmessage::msg::Buttonmsg & msg)
{
  return potmessage::msg::to_yaml(msg);
}

template<>
inline const char * data_type<potmessage::msg::Buttonmsg>()
{
  return "potmessage::msg::Buttonmsg";
}

template<>
inline const char * name<potmessage::msg::Buttonmsg>()
{
  return "potmessage/msg/Buttonmsg";
}

template<>
struct has_fixed_size<potmessage::msg::Buttonmsg>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<potmessage::msg::Buttonmsg>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<potmessage::msg::Buttonmsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // POTMESSAGE__MSG__DETAIL__BUTTONMSG__TRAITS_HPP_
