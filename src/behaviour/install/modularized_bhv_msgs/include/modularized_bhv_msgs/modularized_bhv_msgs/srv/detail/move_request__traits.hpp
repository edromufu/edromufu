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

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__traits.hpp"

namespace modularized_bhv_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const MoveRequest_Event & msg,
  std::ostream & out)
{
  out << "{";
  // member: info
  {
    out << "info: ";
    to_flow_style_yaml(msg.info, out);
    out << ", ";
  }

  // member: request
  {
    if (msg.request.size() == 0) {
      out << "request: []";
    } else {
      out << "request: [";
      size_t pending_items = msg.request.size();
      for (auto item : msg.request) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: response
  {
    if (msg.response.size() == 0) {
      out << "response: []";
    } else {
      out << "response: [";
      size_t pending_items = msg.response.size();
      for (auto item : msg.response) {
        to_flow_style_yaml(item, out);
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
  const MoveRequest_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: info
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "info:\n";
    to_block_style_yaml(msg.info, out, indentation + 2);
  }

  // member: request
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.request.size() == 0) {
      out << "request: []\n";
    } else {
      out << "request:\n";
      for (auto item : msg.request) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: response
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.response.size() == 0) {
      out << "response: []\n";
    } else {
      out << "response:\n";
      for (auto item : msg.response) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MoveRequest_Event & msg, bool use_flow_style = false)
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
  const modularized_bhv_msgs::srv::MoveRequest_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  modularized_bhv_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use modularized_bhv_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const modularized_bhv_msgs::srv::MoveRequest_Event & msg)
{
  return modularized_bhv_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<modularized_bhv_msgs::srv::MoveRequest_Event>()
{
  return "modularized_bhv_msgs::srv::MoveRequest_Event";
}

template<>
inline const char * name<modularized_bhv_msgs::srv::MoveRequest_Event>()
{
  return "modularized_bhv_msgs/srv/MoveRequest_Event";
}

template<>
struct has_fixed_size<modularized_bhv_msgs::srv::MoveRequest_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<modularized_bhv_msgs::srv::MoveRequest_Event>
  : std::integral_constant<bool, has_bounded_size<modularized_bhv_msgs::srv::MoveRequest_Request>::value && has_bounded_size<modularized_bhv_msgs::srv::MoveRequest_Response>::value && has_bounded_size<service_msgs::msg::ServiceEventInfo>::value> {};

template<>
struct is_message<modularized_bhv_msgs::srv::MoveRequest_Event>
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
