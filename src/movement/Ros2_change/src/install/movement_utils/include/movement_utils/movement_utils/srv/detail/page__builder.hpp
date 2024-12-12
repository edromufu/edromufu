// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from movement_utils:srv/Page.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__SRV__DETAIL__PAGE__BUILDER_HPP_
#define MOVEMENT_UTILS__SRV__DETAIL__PAGE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "movement_utils/srv/detail/page__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace movement_utils
{

namespace srv
{

namespace builder
{

class Init_Page_Request_page_name
{
public:
  Init_Page_Request_page_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::movement_utils::srv::Page_Request page_name(::movement_utils::srv::Page_Request::_page_name_type arg)
  {
    msg_.page_name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::movement_utils::srv::Page_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::movement_utils::srv::Page_Request>()
{
  return movement_utils::srv::builder::Init_Page_Request_page_name();
}

}  // namespace movement_utils


namespace movement_utils
{

namespace srv
{

namespace builder
{

class Init_Page_Response_success
{
public:
  Init_Page_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::movement_utils::srv::Page_Response success(::movement_utils::srv::Page_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::movement_utils::srv::Page_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::movement_utils::srv::Page_Response>()
{
  return movement_utils::srv::builder::Init_Page_Response_success();
}

}  // namespace movement_utils

#endif  // MOVEMENT_UTILS__SRV__DETAIL__PAGE__BUILDER_HPP_
