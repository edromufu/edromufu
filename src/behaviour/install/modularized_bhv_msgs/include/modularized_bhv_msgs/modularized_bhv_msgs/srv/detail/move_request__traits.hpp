// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from modularized_bhv_msgs:srv/MoveRequest.idl
// generated code does not contain a copyright notice

#ifndef MODULARIZED_BHV_MSGS__SRV__DETAIL__MOVE_REQUEST__TRAITS_HPP_
#define MODULARIZED_BHV_MSGS__SRV__DETAIL__MOVE_REQUEST__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "modularized_bhv_msgs/srv/detail/move_request__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace modularized_bhv_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const MoveRequest_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: move_request
  {
    out << "move_request: ";
    rosidl_generator_traits::value_to_yaml(msg.move_request, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MoveRequest_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: move_request
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "move_request: ";
    rosidl_generator_traits::value_to_yaml(msg.move_request, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MoveRequest_Request & msg, bool use_flow_style = false)
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

}  // namespace modularized_bhv_msgs

namespace rosidl_generator_traits
{

[[deprecated("use modularized_bhv_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const modularized_bhv_msgs::srv::MoveRequest_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  modularized_bhv_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use modularized_bhv_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const modularized_bhv_msgs::srv::MoveRequest_Request & msg)
{
  return modularized_bhv_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<modularized_bhv_msgs::srv::MoveRequest_Request>()
{
  return "modularized_bhv_msgs::srv::MoveRequest_Request";
}

template<>
inline const char * name<modularized_bhv_msgs::srv::MoveRequest_Request>()
{
  return "modularized_bhv_msgs/srv/MoveRequest_Request";
}

template<>
struct has_fixed_size<modularized_bhv_msgs::srv::MoveRequest_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<modularized_bhv_msgs::srv::MoveRequest_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<modularized_bhv_msgs::srv::MoveRequest_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace modularized_bhv_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const MoveRequest_Response & msg,
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
  const MoveRequest_Response & msg,
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

inline std::string to_yaml(const MoveRequest_Response & msg, bool use_flow_style = false)
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

}  // namespace modularized_bhv_msgs

namespace rosidl_generator_traits
{

[[deprecated("use modularized_bhv_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const modularized_bhv_msgs::srv::MoveRequest_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  modularized_bhv_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use modularized_bhv_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const modularized_bhv_msgs::srv::MoveRequest_Response & msg)
{
  return modularized_bhv_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<modularized_bhv_msgs::srv::MoveRequest_Response>()
{
  return "modularized_bhv_msgs::srv::MoveRequest_Response";
}

template<>
inline const char * name<modularized_bhv_msgs::srv::MoveRequest_Response>()
{
  return "modularized_bhv_msgs/srv/MoveRequest_Response";
}

template<>
struct has_fixed_size<modularized_bhv_msgs::srv::MoveRequest_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<modularized_bhv_msgs::srv::MoveRequest_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<modularized_bhv_msgs::srv::MoveRequest_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<modularized_bhv_msgs::srv::MoveRequest>()
{
  return "modularized_bhv_msgs::srv::MoveRequest";
}

template<>
inline const char * name<modularized_bhv_msgs::srv::MoveRequest>()
{
  return "modularized_bhv_msgs/srv/MoveRequest";
}

template<>
struct has_fixed_size<modularized_bhv_msgs::srv::MoveRequest>
  : std::integral_constant<
    bool,
    has_fixed_size<modularized_bhv_msgs::srv::MoveRequest_Request>::value &&
    has_fixed_size<modularized_bhv_msgs::srv::MoveRequest_Response>::value
  >
{
};

template<>
struct has_bounded_size<modularized_bhv_msgs::srv::MoveRequest>
  : std::integral_constant<
    bool,
    has_bounded_size<modularized_bhv_msgs::srv::MoveRequest_Request>::value &&
    has_bounded_size<modularized_bhv_msgs::srv::MoveRequest_Response>::value
  >
{
};

template<>
struct is_service<modularized_bhv_msgs::srv::MoveRequest>
  : std::true_type
{
};

template<>
struct is_service_request<modularized_bhv_msgs::srv::MoveRequest_Request>
  : std::true_type
{
};

template<>
struct is_service_response<modularized_bhv_msgs::srv::MoveRequest_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // MODULARIZED_BHV_MSGS__SRV__DETAIL__MOVE_REQUEST__TRAITS_HPP_
