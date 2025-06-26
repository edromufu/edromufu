// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from modularized_bhv_msgs:msg/CurrentStateMsg.idl
// generated code does not contain a copyright notice

#ifndef MODULARIZED_BHV_MSGS__MSG__DETAIL__CURRENT_STATE_MSG__STRUCT_HPP_
#define MODULARIZED_BHV_MSGS__MSG__DETAIL__CURRENT_STATE_MSG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__modularized_bhv_msgs__msg__CurrentStateMsg __attribute__((deprecated))
#else
# define DEPRECATED__modularized_bhv_msgs__msg__CurrentStateMsg __declspec(deprecated)
#endif

namespace modularized_bhv_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct CurrentStateMsg_
{
  using Type = CurrentStateMsg_<ContainerAllocator>;

  explicit CurrentStateMsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->current_state = "";
    }
  }

  explicit CurrentStateMsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : current_state(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->current_state = "";
    }
  }

  // field types and members
  using _current_state_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _current_state_type current_state;

  // setters for named parameter idiom
  Type & set__current_state(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->current_state = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    modularized_bhv_msgs::msg::CurrentStateMsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const modularized_bhv_msgs::msg::CurrentStateMsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<modularized_bhv_msgs::msg::CurrentStateMsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<modularized_bhv_msgs::msg::CurrentStateMsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      modularized_bhv_msgs::msg::CurrentStateMsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<modularized_bhv_msgs::msg::CurrentStateMsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      modularized_bhv_msgs::msg::CurrentStateMsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<modularized_bhv_msgs::msg::CurrentStateMsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<modularized_bhv_msgs::msg::CurrentStateMsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<modularized_bhv_msgs::msg::CurrentStateMsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__modularized_bhv_msgs__msg__CurrentStateMsg
    std::shared_ptr<modularized_bhv_msgs::msg::CurrentStateMsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__modularized_bhv_msgs__msg__CurrentStateMsg
    std::shared_ptr<modularized_bhv_msgs::msg::CurrentStateMsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CurrentStateMsg_ & other) const
  {
    if (this->current_state != other.current_state) {
      return false;
    }
    return true;
  }
  bool operator!=(const CurrentStateMsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CurrentStateMsg_

// alias to use template instance with default allocator
using CurrentStateMsg =
  modularized_bhv_msgs::msg::CurrentStateMsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace modularized_bhv_msgs

#endif  // MODULARIZED_BHV_MSGS__MSG__DETAIL__CURRENT_STATE_MSG__STRUCT_HPP_
