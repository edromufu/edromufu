// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from movement_utils:srv/BodyFeedback.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__SRV__DETAIL__BODY_FEEDBACK__TRAITS_HPP_
#define MOVEMENT_UTILS__SRV__DETAIL__BODY_FEEDBACK__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "movement_utils/srv/detail/body_feedback__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace movement_utils
{

namespace srv
{

inline void to_flow_style_yaml(
  const BodyFeedback_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: dont_use
  {
    out << "dont_use: ";
    rosidl_generator_traits::value_to_yaml(msg.dont_use, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const BodyFeedback_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: dont_use
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "dont_use: ";
    rosidl_generator_traits::value_to_yaml(msg.dont_use, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const BodyFeedback_Request & msg, bool use_flow_style = false)
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
  const movement_utils::srv::BodyFeedback_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  movement_utils::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use movement_utils::srv::to_yaml() instead")]]
inline std::string to_yaml(const movement_utils::srv::BodyFeedback_Request & msg)
{
  return movement_utils::srv::to_yaml(msg);
}

template<>
inline const char * data_type<movement_utils::srv::BodyFeedback_Request>()
{
  return "movement_utils::srv::BodyFeedback_Request";
}

template<>
inline const char * name<movement_utils::srv::BodyFeedback_Request>()
{
  return "movement_utils/srv/BodyFeedback_Request";
}

template<>
struct has_fixed_size<movement_utils::srv::BodyFeedback_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<movement_utils::srv::BodyFeedback_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<movement_utils::srv::BodyFeedback_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace movement_utils
{

namespace srv
{

inline void to_flow_style_yaml(
  const BodyFeedback_Response & msg,
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
  const BodyFeedback_Response & msg,
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

inline std::string to_yaml(const BodyFeedback_Response & msg, bool use_flow_style = false)
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
  const movement_utils::srv::BodyFeedback_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  movement_utils::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use movement_utils::srv::to_yaml() instead")]]
inline std::string to_yaml(const movement_utils::srv::BodyFeedback_Response & msg)
{
  return movement_utils::srv::to_yaml(msg);
}

template<>
inline const char * data_type<movement_utils::srv::BodyFeedback_Response>()
{
  return "movement_utils::srv::BodyFeedback_Response";
}

template<>
inline const char * name<movement_utils::srv::BodyFeedback_Response>()
{
  return "movement_utils/srv/BodyFeedback_Response";
}

template<>
struct has_fixed_size<movement_utils::srv::BodyFeedback_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<movement_utils::srv::BodyFeedback_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<movement_utils::srv::BodyFeedback_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<movement_utils::srv::BodyFeedback>()
{
  return "movement_utils::srv::BodyFeedback";
}

template<>
inline const char * name<movement_utils::srv::BodyFeedback>()
{
  return "movement_utils/srv/BodyFeedback";
}

template<>
struct has_fixed_size<movement_utils::srv::BodyFeedback>
  : std::integral_constant<
    bool,
    has_fixed_size<movement_utils::srv::BodyFeedback_Request>::value &&
    has_fixed_size<movement_utils::srv::BodyFeedback_Response>::value
  >
{
};

template<>
struct has_bounded_size<movement_utils::srv::BodyFeedback>
  : std::integral_constant<
    bool,
    has_bounded_size<movement_utils::srv::BodyFeedback_Request>::value &&
    has_bounded_size<movement_utils::srv::BodyFeedback_Response>::value
  >
{
};

template<>
struct is_service<movement_utils::srv::BodyFeedback>
  : std::true_type
{
};

template<>
struct is_service_request<movement_utils::srv::BodyFeedback_Request>
  : std::true_type
{
};

template<>
struct is_service_response<movement_utils::srv::BodyFeedback_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // MOVEMENT_UTILS__SRV__DETAIL__BODY_FEEDBACK__TRAITS_HPP_
