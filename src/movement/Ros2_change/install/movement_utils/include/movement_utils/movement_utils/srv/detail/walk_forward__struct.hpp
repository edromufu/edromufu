// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from movement_utils:srv/WalkForward.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__SRV__DETAIL__WALK_FORWARD__STRUCT_HPP_
#define MOVEMENT_UTILS__SRV__DETAIL__WALK_FORWARD__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__movement_utils__srv__WalkForward_Request __attribute__((deprecated))
#else
# define DEPRECATED__movement_utils__srv__WalkForward_Request __declspec(deprecated)
#endif

namespace movement_utils
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct WalkForward_Request_
{
  using Type = WalkForward_Request_<ContainerAllocator>;

  explicit WalkForward_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->support_foot = 0;
      this->steps_number = 0;
    }
  }

  explicit WalkForward_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->support_foot = 0;
      this->steps_number = 0;
    }
  }

  // field types and members
  using _support_foot_type =
    int8_t;
  _support_foot_type support_foot;
  using _steps_number_type =
    int8_t;
  _steps_number_type steps_number;

  // setters for named parameter idiom
  Type & set__support_foot(
    const int8_t & _arg)
  {
    this->support_foot = _arg;
    return *this;
  }
  Type & set__steps_number(
    const int8_t & _arg)
  {
    this->steps_number = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    movement_utils::srv::WalkForward_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const movement_utils::srv::WalkForward_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<movement_utils::srv::WalkForward_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<movement_utils::srv::WalkForward_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::WalkForward_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::WalkForward_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::WalkForward_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::WalkForward_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<movement_utils::srv::WalkForward_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<movement_utils::srv::WalkForward_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__movement_utils__srv__WalkForward_Request
    std::shared_ptr<movement_utils::srv::WalkForward_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__movement_utils__srv__WalkForward_Request
    std::shared_ptr<movement_utils::srv::WalkForward_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const WalkForward_Request_ & other) const
  {
    if (this->support_foot != other.support_foot) {
      return false;
    }
    if (this->steps_number != other.steps_number) {
      return false;
    }
    return true;
  }
  bool operator!=(const WalkForward_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct WalkForward_Request_

// alias to use template instance with default allocator
using WalkForward_Request =
  movement_utils::srv::WalkForward_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace movement_utils


#ifndef _WIN32
# define DEPRECATED__movement_utils__srv__WalkForward_Response __attribute__((deprecated))
#else
# define DEPRECATED__movement_utils__srv__WalkForward_Response __declspec(deprecated)
#endif

namespace movement_utils
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct WalkForward_Response_
{
  using Type = WalkForward_Response_<ContainerAllocator>;

  explicit WalkForward_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit WalkForward_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    movement_utils::srv::WalkForward_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const movement_utils::srv::WalkForward_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<movement_utils::srv::WalkForward_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<movement_utils::srv::WalkForward_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::WalkForward_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::WalkForward_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::WalkForward_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::WalkForward_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<movement_utils::srv::WalkForward_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<movement_utils::srv::WalkForward_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__movement_utils__srv__WalkForward_Response
    std::shared_ptr<movement_utils::srv::WalkForward_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__movement_utils__srv__WalkForward_Response
    std::shared_ptr<movement_utils::srv::WalkForward_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const WalkForward_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const WalkForward_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct WalkForward_Response_

// alias to use template instance with default allocator
using WalkForward_Response =
  movement_utils::srv::WalkForward_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace movement_utils

namespace movement_utils
{

namespace srv
{

struct WalkForward
{
  using Request = movement_utils::srv::WalkForward_Request;
  using Response = movement_utils::srv::WalkForward_Response;
};

}  // namespace srv

}  // namespace movement_utils

#endif  // MOVEMENT_UTILS__SRV__DETAIL__WALK_FORWARD__STRUCT_HPP_
