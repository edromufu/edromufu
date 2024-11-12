// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from modularized_bhv_msgs:srv/MoveRequest.idl
// generated code does not contain a copyright notice

#ifndef MODULARIZED_BHV_MSGS__SRV__DETAIL__MOVE_REQUEST__STRUCT_HPP_
#define MODULARIZED_BHV_MSGS__SRV__DETAIL__MOVE_REQUEST__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__modularized_bhv_msgs__srv__MoveRequest_Request __attribute__((deprecated))
#else
# define DEPRECATED__modularized_bhv_msgs__srv__MoveRequest_Request __declspec(deprecated)
#endif

namespace modularized_bhv_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MoveRequest_Request_
{
  using Type = MoveRequest_Request_<ContainerAllocator>;

  explicit MoveRequest_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->move_request = "";
    }
  }

  explicit MoveRequest_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : move_request(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->move_request = "";
    }
  }

  // field types and members
  using _move_request_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _move_request_type move_request;

  // setters for named parameter idiom
  Type & set__move_request(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->move_request = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    modularized_bhv_msgs::srv::MoveRequest_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const modularized_bhv_msgs::srv::MoveRequest_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<modularized_bhv_msgs::srv::MoveRequest_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<modularized_bhv_msgs::srv::MoveRequest_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      modularized_bhv_msgs::srv::MoveRequest_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<modularized_bhv_msgs::srv::MoveRequest_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      modularized_bhv_msgs::srv::MoveRequest_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<modularized_bhv_msgs::srv::MoveRequest_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<modularized_bhv_msgs::srv::MoveRequest_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<modularized_bhv_msgs::srv::MoveRequest_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__modularized_bhv_msgs__srv__MoveRequest_Request
    std::shared_ptr<modularized_bhv_msgs::srv::MoveRequest_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__modularized_bhv_msgs__srv__MoveRequest_Request
    std::shared_ptr<modularized_bhv_msgs::srv::MoveRequest_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MoveRequest_Request_ & other) const
  {
    if (this->move_request != other.move_request) {
      return false;
    }
    return true;
  }
  bool operator!=(const MoveRequest_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MoveRequest_Request_

// alias to use template instance with default allocator
using MoveRequest_Request =
  modularized_bhv_msgs::srv::MoveRequest_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace modularized_bhv_msgs


#ifndef _WIN32
# define DEPRECATED__modularized_bhv_msgs__srv__MoveRequest_Response __attribute__((deprecated))
#else
# define DEPRECATED__modularized_bhv_msgs__srv__MoveRequest_Response __declspec(deprecated)
#endif

namespace modularized_bhv_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MoveRequest_Response_
{
  using Type = MoveRequest_Response_<ContainerAllocator>;

  explicit MoveRequest_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit MoveRequest_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    modularized_bhv_msgs::srv::MoveRequest_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const modularized_bhv_msgs::srv::MoveRequest_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<modularized_bhv_msgs::srv::MoveRequest_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<modularized_bhv_msgs::srv::MoveRequest_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      modularized_bhv_msgs::srv::MoveRequest_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<modularized_bhv_msgs::srv::MoveRequest_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      modularized_bhv_msgs::srv::MoveRequest_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<modularized_bhv_msgs::srv::MoveRequest_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<modularized_bhv_msgs::srv::MoveRequest_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<modularized_bhv_msgs::srv::MoveRequest_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__modularized_bhv_msgs__srv__MoveRequest_Response
    std::shared_ptr<modularized_bhv_msgs::srv::MoveRequest_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__modularized_bhv_msgs__srv__MoveRequest_Response
    std::shared_ptr<modularized_bhv_msgs::srv::MoveRequest_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MoveRequest_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const MoveRequest_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MoveRequest_Response_

// alias to use template instance with default allocator
using MoveRequest_Response =
  modularized_bhv_msgs::srv::MoveRequest_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace modularized_bhv_msgs

namespace modularized_bhv_msgs
{

namespace srv
{

struct MoveRequest
{
  using Request = modularized_bhv_msgs::srv::MoveRequest_Request;
  using Response = modularized_bhv_msgs::srv::MoveRequest_Response;
};

}  // namespace srv

}  // namespace modularized_bhv_msgs

#endif  // MODULARIZED_BHV_MSGS__SRV__DETAIL__MOVE_REQUEST__STRUCT_HPP_
