// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from movement_utils:srv/Page.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__SRV__DETAIL__PAGE__STRUCT_HPP_
#define MOVEMENT_UTILS__SRV__DETAIL__PAGE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__movement_utils__srv__Page_Request __attribute__((deprecated))
#else
# define DEPRECATED__movement_utils__srv__Page_Request __declspec(deprecated)
#endif

namespace movement_utils
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Page_Request_
{
  using Type = Page_Request_<ContainerAllocator>;

  explicit Page_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->page_name = "";
    }
  }

  explicit Page_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : page_name(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->page_name = "";
    }
  }

  // field types and members
  using _page_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _page_name_type page_name;

  // setters for named parameter idiom
  Type & set__page_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->page_name = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    movement_utils::srv::Page_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const movement_utils::srv::Page_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<movement_utils::srv::Page_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<movement_utils::srv::Page_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::Page_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::Page_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::Page_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::Page_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<movement_utils::srv::Page_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<movement_utils::srv::Page_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__movement_utils__srv__Page_Request
    std::shared_ptr<movement_utils::srv::Page_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__movement_utils__srv__Page_Request
    std::shared_ptr<movement_utils::srv::Page_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Page_Request_ & other) const
  {
    if (this->page_name != other.page_name) {
      return false;
    }
    return true;
  }
  bool operator!=(const Page_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Page_Request_

// alias to use template instance with default allocator
using Page_Request =
  movement_utils::srv::Page_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace movement_utils


#ifndef _WIN32
# define DEPRECATED__movement_utils__srv__Page_Response __attribute__((deprecated))
#else
# define DEPRECATED__movement_utils__srv__Page_Response __declspec(deprecated)
#endif

namespace movement_utils
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Page_Response_
{
  using Type = Page_Response_<ContainerAllocator>;

  explicit Page_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit Page_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    movement_utils::srv::Page_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const movement_utils::srv::Page_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<movement_utils::srv::Page_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<movement_utils::srv::Page_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::Page_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::Page_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      movement_utils::srv::Page_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<movement_utils::srv::Page_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<movement_utils::srv::Page_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<movement_utils::srv::Page_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__movement_utils__srv__Page_Response
    std::shared_ptr<movement_utils::srv::Page_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__movement_utils__srv__Page_Response
    std::shared_ptr<movement_utils::srv::Page_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Page_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const Page_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Page_Response_

// alias to use template instance with default allocator
using Page_Response =
  movement_utils::srv::Page_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace movement_utils

namespace movement_utils
{

namespace srv
{

struct Page
{
  using Request = movement_utils::srv::Page_Request;
  using Response = movement_utils::srv::Page_Response;
};

}  // namespace srv

}  // namespace movement_utils

#endif  // MOVEMENT_UTILS__SRV__DETAIL__PAGE__STRUCT_HPP_
