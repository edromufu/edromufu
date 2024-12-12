// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from movement_utils:srv/WalkForward.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__SRV__DETAIL__WALK_FORWARD__TRAITS_HPP_
#define MOVEMENT_UTILS__SRV__DETAIL__WALK_FORWARD__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "movement_utils/srv/detail/walk_forward__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace movement_utils
{

namespace srv
{

inline void to_flow_style_yaml(
  const WalkForward_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: support_foot
  {
    out << "support_foot: ";
    rosidl_generator_traits::value_to_yaml(msg.support_foot, out);
    out << ", ";
  }

  // member: steps_number
  {
    out << "steps_number: ";
    rosidl_generator_traits::value_to_yaml(msg.steps_number, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const WalkForward_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: support_foot
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "support_foot: ";
    rosidl_generator_traits::value_to_yaml(msg.support_foot, out);
    out << "\n";
  }

  // member: steps_number
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "steps_number: ";
    rosidl_generator_traits::value_to_yaml(msg.steps_number, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const WalkForward_Request & msg, bool use_flow_style = false)
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
  const movement_utils::srv::WalkForward_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  movement_utils::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use movement_utils::srv::to_yaml() instead")]]
inline std::string to_yaml(const movement_utils::srv::WalkForward_Request & msg)
{
  return movement_utils::srv::to_yaml(msg);
}

template<>
inline const char * data_type<movement_utils::srv::WalkForward_Request>()
{
  return "movement_utils::srv::WalkForward_Request";
}

template<>
inline const char * name<movement_utils::srv::WalkForward_Request>()
{
  return "movement_utils/srv/WalkForward_Request";
}

template<>
struct has_fixed_size<movement_utils::srv::WalkForward_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<movement_utils::srv::WalkForward_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<movement_utils::srv::WalkForward_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace movement_utils
{

namespace srv
{

inline void to_flow_style_yaml(
  const WalkForward_Response & msg,
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
  const WalkForward_Response & msg,
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

inline std::string to_yaml(const WalkForward_Response & msg, bool use_flow_style = false)
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
  const movement_utils::srv::WalkForward_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  movement_utils::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use movement_utils::srv::to_yaml() instead")]]
inline std::string to_yaml(const movement_utils::srv::WalkForward_Response & msg)
{
  return movement_utils::srv::to_yaml(msg);
}

template<>
inline const char * data_type<movement_utils::srv::WalkForward_Response>()
{
  return "movement_utils::srv::WalkForward_Response";
}

template<>
inline const char * name<movement_utils::srv::WalkForward_Response>()
{
  return "movement_utils/srv/WalkForward_Response";
}

template<>
struct has_fixed_size<movement_utils::srv::WalkForward_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<movement_utils::srv::WalkForward_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<movement_utils::srv::WalkForward_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<movement_utils::srv::WalkForward>()
{
  return "movement_utils::srv::WalkForward";
}

template<>
inline const char * name<movement_utils::srv::WalkForward>()
{
  return "movement_utils/srv/WalkForward";
}

template<>
struct has_fixed_size<movement_utils::srv::WalkForward>
  : std::integral_constant<
    bool,
    has_fixed_size<movement_utils::srv::WalkForward_Request>::value &&
    has_fixed_size<movement_utils::srv::WalkForward_Response>::value
  >
{
};

template<>
struct has_bounded_size<movement_utils::srv::WalkForward>
  : std::integral_constant<
    bool,
    has_bounded_size<movement_utils::srv::WalkForward_Request>::value &&
    has_bounded_size<movement_utils::srv::WalkForward_Response>::value
  >
{
};

template<>
struct is_service<movement_utils::srv::WalkForward>
  : std::true_type
{
};

template<>
struct is_service_request<movement_utils::srv::WalkForward_Request>
  : std::true_type
{
};

template<>
struct is_service_response<movement_utils::srv::WalkForward_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // MOVEMENT_UTILS__SRV__DETAIL__WALK_FORWARD__TRAITS_HPP_
