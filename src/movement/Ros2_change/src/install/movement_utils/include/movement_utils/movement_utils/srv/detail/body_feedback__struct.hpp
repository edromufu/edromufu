// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from movement_utils:srv/BodyFeedback.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__SRV__DETAIL__BODY_FEEDBACK__STRUCT_HPP_
#define MOVEMENT_UTILS__SRV__DETAIL__BODY_FEEDBACK__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__movement_utils__srv__BodyFeedback_Request __attribute__((deprecated))
#else
# define DEPRECATED__movement_utils__srv__BodyFeedback_Request __declspec(deprecated)
#endif

namespace movement_utils
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct BodyFeedback_Request_
{
  using Type = BodyFeedback_Request_<ContainerAllocator>;

  explicit BodyFeedback_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->dont_use = false;
    }
  }

  explicit BodyFeedback_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->dont_use = false;
    }
  }

  // field types and members
  using _dont_use_type =
    bool;
  _dont_use_type dont_use;

  // setters for named parameter idiom
  Type & set__dont_use(
    const bool & _arg)
  {
    this->dont_use = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    movement_utils::srv::BodyFeedback_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const movement_utils::srv::BodyFeedback_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<movement_utils::srv::BodyFeedback_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<movement_utils::srv::BodyFeedback_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::BodyFeedback_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::BodyFeedback_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::BodyFeedback_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::BodyFeedback_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<movement_utils::srv::BodyFeedback_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<movement_utils::srv::BodyFeedback_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__movement_utils__srv__BodyFeedback_Request
    std::shared_ptr<movement_utils::srv::BodyFeedback_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__movement_utils__srv__BodyFeedback_Request
    std::shared_ptr<movement_utils::srv::BodyFeedback_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const BodyFeedback_Request_ & other) const
  {
    if (this->dont_use != other.dont_use) {
      return false;
    }
    return true;
  }
  bool operator!=(const BodyFeedback_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct BodyFeedback_Request_

// alias to use template instance with default allocator
using BodyFeedback_Request =
  movement_utils::srv::BodyFeedback_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace movement_utils


#ifndef _WIN32
# define DEPRECATED__movement_utils__srv__BodyFeedback_Response __attribute__((deprecated))
#else
# define DEPRECATED__movement_utils__srv__BodyFeedback_Response __declspec(deprecated)
#endif

namespace movement_utils
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct BodyFeedback_Response_
{
  using Type = BodyFeedback_Response_<ContainerAllocator>;

  explicit BodyFeedback_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<float, 18>::iterator, float>(this->pos_vector.begin(), this->pos_vector.end(), 0.0f);
    }
  }

  explicit BodyFeedback_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    movement_utils::srv::BodyFeedback_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const movement_utils::srv::BodyFeedback_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<movement_utils::srv::BodyFeedback_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<movement_utils::srv::BodyFeedback_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::BodyFeedback_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::BodyFeedback_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::BodyFeedback_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::BodyFeedback_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<movement_utils::srv::BodyFeedback_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<movement_utils::srv::BodyFeedback_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__movement_utils__srv__BodyFeedback_Response
    std::shared_ptr<movement_utils::srv::BodyFeedback_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__movement_utils__srv__BodyFeedback_Response
    std::shared_ptr<movement_utils::srv::BodyFeedback_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const BodyFeedback_Response_ & other) const
  {
    if (this->pos_vector != other.pos_vector) {
      return false;
    }
    return true;
  }
  bool operator!=(const BodyFeedback_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct BodyFeedback_Response_

// alias to use template instance with default allocator
using BodyFeedback_Response =
  movement_utils::srv::BodyFeedback_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace movement_utils

namespace movement_utils
{

namespace srv
{

struct BodyFeedback
{
  using Request = movement_utils::srv::BodyFeedback_Request;
  using Response = movement_utils::srv::BodyFeedback_Response;
};

}  // namespace srv

}  // namespace movement_utils

#endif  // MOVEMENT_UTILS__SRV__DETAIL__BODY_FEEDBACK__STRUCT_HPP_
