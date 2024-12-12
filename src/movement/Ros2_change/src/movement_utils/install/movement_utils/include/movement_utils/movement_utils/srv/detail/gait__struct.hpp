// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from movement_utils:srv/Gait.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__SRV__DETAIL__GAIT__STRUCT_HPP_
#define MOVEMENT_UTILS__SRV__DETAIL__GAIT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__movement_utils__srv__Gait_Request __attribute__((deprecated))
#else
# define DEPRECATED__movement_utils__srv__Gait_Request __declspec(deprecated)
#endif

namespace movement_utils
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Gait_Request_
{
  using Type = Gait_Request_<ContainerAllocator>;

  explicit Gait_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->steps_number = 0;
      this->step_height = 0.0f;
    }
  }

  explicit Gait_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->steps_number = 0;
      this->step_height = 0.0f;
    }
  }

  // field types and members
  using _steps_number_type =
    int8_t;
  _steps_number_type steps_number;
  using _step_height_type =
    float;
  _step_height_type step_height;

  // setters for named parameter idiom
  Type & set__steps_number(
    const int8_t & _arg)
  {
    this->steps_number = _arg;
    return *this;
  }
  Type & set__step_height(
    const float & _arg)
  {
    this->step_height = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    movement_utils::srv::Gait_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const movement_utils::srv::Gait_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<movement_utils::srv::Gait_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<movement_utils::srv::Gait_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::Gait_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::Gait_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::Gait_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::Gait_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<movement_utils::srv::Gait_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<movement_utils::srv::Gait_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__movement_utils__srv__Gait_Request
    std::shared_ptr<movement_utils::srv::Gait_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__movement_utils__srv__Gait_Request
    std::shared_ptr<movement_utils::srv::Gait_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Gait_Request_ & other) const
  {
    if (this->steps_number != other.steps_number) {
      return false;
    }
    if (this->step_height != other.step_height) {
      return false;
    }
    return true;
  }
  bool operator!=(const Gait_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Gait_Request_

// alias to use template instance with default allocator
using Gait_Request =
  movement_utils::srv::Gait_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace movement_utils


#ifndef _WIN32
# define DEPRECATED__movement_utils__srv__Gait_Response __attribute__((deprecated))
#else
# define DEPRECATED__movement_utils__srv__Gait_Response __declspec(deprecated)
#endif

namespace movement_utils
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Gait_Response_
{
  using Type = Gait_Response_<ContainerAllocator>;

  explicit Gait_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit Gait_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    movement_utils::srv::Gait_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const movement_utils::srv::Gait_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<movement_utils::srv::Gait_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<movement_utils::srv::Gait_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::Gait_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::Gait_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::Gait_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::Gait_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<movement_utils::srv::Gait_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<movement_utils::srv::Gait_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__movement_utils__srv__Gait_Response
    std::shared_ptr<movement_utils::srv::Gait_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__movement_utils__srv__Gait_Response
    std::shared_ptr<movement_utils::srv::Gait_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Gait_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const Gait_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Gait_Response_

// alias to use template instance with default allocator
using Gait_Response =
  movement_utils::srv::Gait_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace movement_utils

namespace movement_utils
{

namespace srv
{

struct Gait
{
  using Request = movement_utils::srv::Gait_Request;
  using Response = movement_utils::srv::Gait_Response;
};

}  // namespace srv

}  // namespace movement_utils

#endif  // MOVEMENT_UTILS__SRV__DETAIL__GAIT__STRUCT_HPP_
