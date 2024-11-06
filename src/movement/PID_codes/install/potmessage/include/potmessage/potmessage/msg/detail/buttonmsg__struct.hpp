// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from potmessage:msg/Buttonmsg.idl
// generated code does not contain a copyright notice

#ifndef POTMESSAGE__MSG__DETAIL__BUTTONMSG__STRUCT_HPP_
#define POTMESSAGE__MSG__DETAIL__BUTTONMSG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__potmessage__msg__Buttonmsg __attribute__((deprecated))
#else
# define DEPRECATED__potmessage__msg__Buttonmsg __declspec(deprecated)
#endif

namespace potmessage
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Buttonmsg_
{
  using Type = Buttonmsg_<ContainerAllocator>;

  explicit Buttonmsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->bot1 = false;
      this->bot2 = false;
    }
  }

  explicit Buttonmsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->bot1 = false;
      this->bot2 = false;
    }
  }

  // field types and members
  using _bot1_type =
    bool;
  _bot1_type bot1;
  using _bot2_type =
    bool;
  _bot2_type bot2;

  // setters for named parameter idiom
  Type & set__bot1(
    const bool & _arg)
  {
    this->bot1 = _arg;
    return *this;
  }
  Type & set__bot2(
    const bool & _arg)
  {
    this->bot2 = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    potmessage::msg::Buttonmsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const potmessage::msg::Buttonmsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<potmessage::msg::Buttonmsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<potmessage::msg::Buttonmsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      potmessage::msg::Buttonmsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<potmessage::msg::Buttonmsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      potmessage::msg::Buttonmsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<potmessage::msg::Buttonmsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<potmessage::msg::Buttonmsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<potmessage::msg::Buttonmsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__potmessage__msg__Buttonmsg
    std::shared_ptr<potmessage::msg::Buttonmsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__potmessage__msg__Buttonmsg
    std::shared_ptr<potmessage::msg::Buttonmsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Buttonmsg_ & other) const
  {
    if (this->bot1 != other.bot1) {
      return false;
    }
    if (this->bot2 != other.bot2) {
      return false;
    }
    return true;
  }
  bool operator!=(const Buttonmsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Buttonmsg_

// alias to use template instance with default allocator
using Buttonmsg =
  potmessage::msg::Buttonmsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace potmessage

#endif  // POTMESSAGE__MSG__DETAIL__BUTTONMSG__STRUCT_HPP_
