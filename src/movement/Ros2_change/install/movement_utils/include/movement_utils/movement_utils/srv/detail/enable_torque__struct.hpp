// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from movement_utils:srv/EnableTorque.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__SRV__DETAIL__ENABLE_TORQUE__STRUCT_HPP_
#define MOVEMENT_UTILS__SRV__DETAIL__ENABLE_TORQUE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__movement_utils__srv__EnableTorque_Request __attribute__((deprecated))
#else
# define DEPRECATED__movement_utils__srv__EnableTorque_Request __declspec(deprecated)
#endif

namespace movement_utils
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct EnableTorque_Request_
{
  using Type = EnableTorque_Request_<ContainerAllocator>;

  explicit EnableTorque_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->data = false;
    }
  }

  explicit EnableTorque_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->data = false;
    }
  }

  // field types and members
  using _data_type =
    bool;
  _data_type data;
  using _motor_ids_type =
    std::vector<int8_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int8_t>>;
  _motor_ids_type motor_ids;

  // setters for named parameter idiom
  Type & set__data(
    const bool & _arg)
  {
    this->data = _arg;
    return *this;
  }
  Type & set__motor_ids(
    const std::vector<int8_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int8_t>> & _arg)
  {
    this->motor_ids = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    movement_utils::srv::EnableTorque_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const movement_utils::srv::EnableTorque_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<movement_utils::srv::EnableTorque_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<movement_utils::srv::EnableTorque_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::EnableTorque_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::EnableTorque_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::EnableTorque_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::EnableTorque_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<movement_utils::srv::EnableTorque_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<movement_utils::srv::EnableTorque_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__movement_utils__srv__EnableTorque_Request
    std::shared_ptr<movement_utils::srv::EnableTorque_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__movement_utils__srv__EnableTorque_Request
    std::shared_ptr<movement_utils::srv::EnableTorque_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const EnableTorque_Request_ & other) const
  {
    if (this->data != other.data) {
      return false;
    }
    if (this->motor_ids != other.motor_ids) {
      return false;
    }
    return true;
  }
  bool operator!=(const EnableTorque_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct EnableTorque_Request_

// alias to use template instance with default allocator
using EnableTorque_Request =
  movement_utils::srv::EnableTorque_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace movement_utils


#ifndef _WIN32
# define DEPRECATED__movement_utils__srv__EnableTorque_Response __attribute__((deprecated))
#else
# define DEPRECATED__movement_utils__srv__EnableTorque_Response __declspec(deprecated)
#endif

namespace movement_utils
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct EnableTorque_Response_
{
  using Type = EnableTorque_Response_<ContainerAllocator>;

  explicit EnableTorque_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit EnableTorque_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    movement_utils::srv::EnableTorque_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const movement_utils::srv::EnableTorque_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<movement_utils::srv::EnableTorque_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<movement_utils::srv::EnableTorque_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::EnableTorque_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::EnableTorque_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::EnableTorque_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::EnableTorque_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<movement_utils::srv::EnableTorque_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<movement_utils::srv::EnableTorque_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__movement_utils__srv__EnableTorque_Response
    std::shared_ptr<movement_utils::srv::EnableTorque_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__movement_utils__srv__EnableTorque_Response
    std::shared_ptr<movement_utils::srv::EnableTorque_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const EnableTorque_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const EnableTorque_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct EnableTorque_Response_

// alias to use template instance with default allocator
using EnableTorque_Response =
  movement_utils::srv::EnableTorque_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace movement_utils

namespace movement_utils
{

namespace srv
{

struct EnableTorque
{
  using Request = movement_utils::srv::EnableTorque_Request;
  using Response = movement_utils::srv::EnableTorque_Response;
};

}  // namespace srv

}  // namespace movement_utils

#endif  // MOVEMENT_UTILS__SRV__DETAIL__ENABLE_TORQUE__STRUCT_HPP_
