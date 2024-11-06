// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from potmessage:msg/Potmsg.idl
// generated code does not contain a copyright notice

#ifndef POTMESSAGE__MSG__DETAIL__POTMSG__TRAITS_HPP_
#define POTMESSAGE__MSG__DETAIL__POTMSG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "potmessage/msg/detail/potmsg__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace potmessage
{

namespace msg
{

inline void to_flow_style_yaml(
  const Potmsg & msg,
  std::ostream & out)
{
  out << "{";
  // member: pot1
  {
    out << "pot1: ";
    rosidl_generator_traits::value_to_yaml(msg.pot1, out);
    out << ", ";
  }

  // member: pot2
  {
    out << "pot2: ";
    rosidl_generator_traits::value_to_yaml(msg.pot2, out);
    out << ", ";
  }

  // member: pot3
  {
    out << "pot3: ";
    rosidl_generator_traits::value_to_yaml(msg.pot3, out);
    out << ", ";
  }

  // member: pot4
  {
    out << "pot4: ";
    rosidl_generator_traits::value_to_yaml(msg.pot4, out);
    out << ", ";
  }

  // member: pot5
  {
    out << "pot5: ";
    rosidl_generator_traits::value_to_yaml(msg.pot5, out);
    out << ", ";
  }

  // member: pot6
  {
    out << "pot6: ";
    rosidl_generator_traits::value_to_yaml(msg.pot6, out);
    out << ", ";
  }

  // member: pot7
  {
    out << "pot7: ";
    rosidl_generator_traits::value_to_yaml(msg.pot7, out);
    out << ", ";
  }

  // member: pot8
  {
    out << "pot8: ";
    rosidl_generator_traits::value_to_yaml(msg.pot8, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Potmsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: pot1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pot1: ";
    rosidl_generator_traits::value_to_yaml(msg.pot1, out);
    out << "\n";
  }

  // member: pot2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pot2: ";
    rosidl_generator_traits::value_to_yaml(msg.pot2, out);
    out << "\n";
  }

  // member: pot3
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pot3: ";
    rosidl_generator_traits::value_to_yaml(msg.pot3, out);
    out << "\n";
  }

  // member: pot4
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pot4: ";
    rosidl_generator_traits::value_to_yaml(msg.pot4, out);
    out << "\n";
  }

  // member: pot5
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pot5: ";
    rosidl_generator_traits::value_to_yaml(msg.pot5, out);
    out << "\n";
  }

  // member: pot6
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pot6: ";
    rosidl_generator_traits::value_to_yaml(msg.pot6, out);
    out << "\n";
  }

  // member: pot7
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pot7: ";
    rosidl_generator_traits::value_to_yaml(msg.pot7, out);
    out << "\n";
  }

  // member: pot8
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pot8: ";
    rosidl_generator_traits::value_to_yaml(msg.pot8, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Potmsg & msg, bool use_flow_style = false)
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
  const potmessage::msg::Potmsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  potmessage::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use potmessage::msg::to_yaml() instead")]]
inline std::string to_yaml(const potmessage::msg::Potmsg & msg)
{
  return potmessage::msg::to_yaml(msg);
}

template<>
inline const char * data_type<potmessage::msg::Potmsg>()
{
  return "potmessage::msg::Potmsg";
}

template<>
inline const char * name<potmessage::msg::Potmsg>()
{
  return "potmessage/msg/Potmsg";
}

template<>
struct has_fixed_size<potmessage::msg::Potmsg>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<potmessage::msg::Potmsg>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<potmessage::msg::Potmsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // POTMESSAGE__MSG__DETAIL__POTMSG__TRAITS_HPP_
