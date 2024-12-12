// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from movement_utils:msg/BodyMotorsData.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__MSG__DETAIL__BODY_MOTORS_DATA__STRUCT_HPP_
#define MOVEMENT_UTILS__MSG__DETAIL__BODY_MOTORS_DATA__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__movement_utils__msg__BodyMotorsData __attribute__((deprecated))
#else
# define DEPRECATED__movement_utils__msg__BodyMotorsData __declspec(deprecated)
#endif

namespace movement_utils
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct BodyMotorsData_
{
  using Type = BodyMotorsData_<ContainerAllocator>;

  explicit BodyMotorsData_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<float, 18>::iterator, float>(this->pos_vector.begin(), this->pos_vector.end(), 0.0f);
    }
  }

  explicit BodyMotorsData_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pos_vector(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<float, 18>::iterator, float>(this->pos_vector.begin(), this->pos_vector.end(), 0.0f);
    }
  }

  // field types and members
  using _pos_vector_type =
    std::array<float, 18>;
  _pos_vector_type pos_vector;

  // setters for named parameter idiom
  Type & set__pos_vector(
    const std::array<float, 18> & _arg)
  {
    this->pos_vector = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    movement_utils::msg::BodyMotorsData_<ContainerAllocator> *;
  using ConstRawPtr =
    const movement_utils::msg::BodyMotorsData_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<movement_utils::msg::BodyMotorsData_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<movement_utils::msg::BodyMotorsData_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      movement_utils::msg::BodyMotorsData_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<movement_utils::msg::BodyMotorsData_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      movement_utils::msg::BodyMotorsData_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<movement_utils::msg::BodyMotorsData_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<movement_utils::msg::BodyMotorsData_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<movement_utils::msg::BodyMotorsData_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__movement_utils__msg__BodyMotorsData
    std::shared_ptr<movement_utils::msg::BodyMotorsData_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__movement_utils__msg__BodyMotorsData
    std::shared_ptr<movement_utils::msg::BodyMotorsData_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const BodyMotorsData_ & other) const
  {
    if (this->pos_vector != other.pos_vector) {
      return false;
    }
    return true;
  }
  bool operator!=(const BodyMotorsData_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct BodyMotorsData_

// alias to use template instance with default allocator
using BodyMotorsData =
  movement_utils::msg::BodyMotorsData_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace movement_utils

#endif  // MOVEMENT_UTILS__MSG__DETAIL__BODY_MOTORS_DATA__STRUCT_HPP_
