// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from modularized_bhv_msgs:msg/StateMachineMsg.idl
// generated code does not contain a copyright notice

#ifndef MODULARIZED_BHV_MSGS__MSG__DETAIL__STATE_MACHINE_MSG__STRUCT_HPP_
#define MODULARIZED_BHV_MSGS__MSG__DETAIL__STATE_MACHINE_MSG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__modularized_bhv_msgs__msg__StateMachineMsg __attribute__((deprecated))
#else
# define DEPRECATED__modularized_bhv_msgs__msg__StateMachineMsg __declspec(deprecated)
#endif

namespace modularized_bhv_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct StateMachineMsg_
{
  using Type = StateMachineMsg_<ContainerAllocator>;

  explicit StateMachineMsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->ball_position = "";
      this->ball_close = false;
      this->ball_found = false;
      this->fall_state = "";
      this->hor_motor_out_of_center = "";
      this->head_kick_check = false;
    }
  }

  explicit StateMachineMsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : ball_position(_alloc),
    fall_state(_alloc),
    hor_motor_out_of_center(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->ball_position = "";
      this->ball_close = false;
      this->ball_found = false;
      this->fall_state = "";
      this->hor_motor_out_of_center = "";
      this->head_kick_check = false;
    }
  }

  // field types and members
  using _ball_position_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _ball_position_type ball_position;
  using _ball_close_type =
    bool;
  _ball_close_type ball_close;
  using _ball_found_type =
    bool;
  _ball_found_type ball_found;
  using _fall_state_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _fall_state_type fall_state;
  using _hor_motor_out_of_center_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _hor_motor_out_of_center_type hor_motor_out_of_center;
  using _head_kick_check_type =
    bool;
  _head_kick_check_type head_kick_check;

  // setters for named parameter idiom
  Type & set__ball_position(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->ball_position = _arg;
    return *this;
  }
  Type & set__ball_close(
    const bool & _arg)
  {
    this->ball_close = _arg;
    return *this;
  }
  Type & set__ball_found(
    const bool & _arg)
  {
    this->ball_found = _arg;
    return *this;
  }
  Type & set__fall_state(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->fall_state = _arg;
    return *this;
  }
  Type & set__hor_motor_out_of_center(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->hor_motor_out_of_center = _arg;
    return *this;
  }
  Type & set__head_kick_check(
    const bool & _arg)
  {
    this->head_kick_check = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    modularized_bhv_msgs::msg::StateMachineMsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const modularized_bhv_msgs::msg::StateMachineMsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<modularized_bhv_msgs::msg::StateMachineMsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<modularized_bhv_msgs::msg::StateMachineMsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      modularized_bhv_msgs::msg::StateMachineMsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<modularized_bhv_msgs::msg::StateMachineMsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      modularized_bhv_msgs::msg::StateMachineMsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<modularized_bhv_msgs::msg::StateMachineMsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<modularized_bhv_msgs::msg::StateMachineMsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<modularized_bhv_msgs::msg::StateMachineMsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__modularized_bhv_msgs__msg__StateMachineMsg
    std::shared_ptr<modularized_bhv_msgs::msg::StateMachineMsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__modularized_bhv_msgs__msg__StateMachineMsg
    std::shared_ptr<modularized_bhv_msgs::msg::StateMachineMsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const StateMachineMsg_ & other) const
  {
    if (this->ball_position != other.ball_position) {
      return false;
    }
    if (this->ball_close != other.ball_close) {
      return false;
    }
    if (this->ball_found != other.ball_found) {
      return false;
    }
    if (this->fall_state != other.fall_state) {
      return false;
    }
    if (this->hor_motor_out_of_center != other.hor_motor_out_of_center) {
      return false;
    }
    if (this->head_kick_check != other.head_kick_check) {
      return false;
    }
    return true;
  }
  bool operator!=(const StateMachineMsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct StateMachineMsg_

// alias to use template instance with default allocator
using StateMachineMsg =
  modularized_bhv_msgs::msg::StateMachineMsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace modularized_bhv_msgs

#endif  // MODULARIZED_BHV_MSGS__MSG__DETAIL__STATE_MACHINE_MSG__STRUCT_HPP_
