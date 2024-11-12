// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from movement_utils:srv/BodyFeedback.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__SRV__DETAIL__BODY_FEEDBACK__BUILDER_HPP_
#define MOVEMENT_UTILS__SRV__DETAIL__BODY_FEEDBACK__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "movement_utils/srv/detail/body_feedback__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace movement_utils
{

namespace srv
{

namespace builder
{

class Init_BodyFeedback_Request_dont_use
{
public:
  Init_BodyFeedback_Request_dont_use()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::movement_utils::srv::BodyFeedback_Request dont_use(::movement_utils::srv::BodyFeedback_Request::_dont_use_type arg)
  {
    msg_.dont_use = std::move(arg);
    return std::move(msg_);
  }

private:
  ::movement_utils::srv::BodyFeedback_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::movement_utils::srv::BodyFeedback_Request>()
{
  return movement_utils::srv::builder::Init_BodyFeedback_Request_dont_use();
}

}  // namespace movement_utils


namespace movement_utils
{

namespace srv
{

namespace builder
{

class Init_BodyFeedback_Response_pos_vector
{
public:
  Init_BodyFeedback_Response_pos_vector()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::movement_utils::srv::BodyFeedback_Response pos_vector(::movement_utils::srv::BodyFeedback_Response::_pos_vector_type arg)
  {
    msg_.pos_vector = std::move(arg);
    return std::move(msg_);
  }

private:
  ::movement_utils::srv::BodyFeedback_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::movement_utils::srv::BodyFeedback_Response>()
{
  return movement_utils::srv::builder::Init_BodyFeedback_Response_pos_vector();
}

}  // namespace movement_utils

#endif  // MOVEMENT_UTILS__SRV__DETAIL__BODY_FEEDBACK__BUILDER_HPP_
