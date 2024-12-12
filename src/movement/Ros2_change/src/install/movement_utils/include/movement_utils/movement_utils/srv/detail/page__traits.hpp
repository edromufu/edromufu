// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from movement_utils:srv/Page.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__SRV__DETAIL__PAGE__TRAITS_HPP_
#define MOVEMENT_UTILS__SRV__DETAIL__PAGE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "movement_utils/srv/detail/page__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace movement_utils
{

namespace srv
{

inline void to_flow_style_yaml(
  const Page_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: page_name
  {
    out << "page_name: ";
    rosidl_generator_traits::value_to_yaml(msg.page_name, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Page_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: page_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "page_name: ";
    rosidl_generator_traits::value_to_yaml(msg.page_name, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Page_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace movement_utils

namespace rosidl_generator_traits
{

[[deprecated("use movement_utils::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const movement_utils::srv::Page_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  movement_utils::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use movement_utils::srv::to_yaml() instead")]]
inline std::string to_yaml(const movement_utils::srv::Page_Request & msg)
{
  return movement_utils::srv::to_yaml(msg);
}

template<>
inline const char * data_type<movement_utils::srv::Page_Request>()
{
  return "movement_utils::srv::Page_Request";
}

template<>
inline const char * name<movement_utils::srv::Page_Request>()
{
  return "movement_utils/srv/Page_Request";
}

template<>
struct has_fixed_size<movement_utils::srv::Page_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<movement_utils::srv::Page_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<movement_utils::srv::Page_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace movement_utils
{

namespace srv
{

inline void to_flow_style_yaml(
  const Page_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Page_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Page_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace movement_utils

namespace rosidl_generator_traits
{

[[deprecated("use movement_utils::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const movement_utils::srv::Page_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  movement_utils::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use movement_utils::srv::to_yaml() instead")]]
inline std::string to_yaml(const movement_utils::srv::Page_Response & msg)
{
  return movement_utils::srv::to_yaml(msg);
}

template<>
inline const char * data_type<movement_utils::srv::Page_Response>()
{
  return "movement_utils::srv::Page_Response";
}

template<>
inline const char * name<movement_utils::srv::Page_Response>()
{
  return "movement_utils/srv/Page_Response";
}

template<>
struct has_fixed_size<movement_utils::srv::Page_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<movement_utils::srv::Page_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<movement_utils::srv::Page_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<movement_utils::srv::Page>()
{
  return "movement_utils::srv::Page";
}

template<>
inline const char * name<movement_utils::srv::Page>()
{
  return "movement_utils/srv/Page";
}

template<>
struct has_fixed_size<movement_utils::srv::Page>
  : std::integral_constant<
    bool,
    has_fixed_size<movement_utils::srv::Page_Request>::value &&
    has_fixed_size<movement_utils::srv::Page_Response>::value
  >
{
};

template<>
struct has_bounded_size<movement_utils::srv::Page>
  : std::integral_constant<
    bool,
    has_bounded_size<movement_utils::srv::Page_Request>::value &&
    has_bounded_size<movement_utils::srv::Page_Response>::value
  >
{
};

template<>
struct is_service<movement_utils::srv::Page>
  : std::true_type
{
};

template<>
struct is_service_request<movement_utils::srv::Page_Request>
  : std::true_type
{
};

template<>
struct is_service_response<movement_utils::srv::Page_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // MOVEMENT_UTILS__SRV__DETAIL__PAGE__TRAITS_HPP_
