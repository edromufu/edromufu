// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from potmessage:msg/Potmsg.idl
// generated code does not contain a copyright notice

#ifndef POTMESSAGE__MSG__DETAIL__POTMSG__STRUCT_HPP_
#define POTMESSAGE__MSG__DETAIL__POTMSG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__potmessage__msg__Potmsg __attribute__((deprecated))
#else
# define DEPRECATED__potmessage__msg__Potmsg __declspec(deprecated)
#endif

namespace potmessage
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Potmsg_
{
  using Type = Potmsg_<ContainerAllocator>;

  explicit Potmsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->pot1 = 0l;
      this->pot2 = 0l;
      this->pot3 = 0l;
      this->pot4 = 0l;
      this->pot5 = 0l;
      this->pot6 = 0l;
      this->pot7 = 0l;
      this->pot8 = 0l;
      this->imu1 = 0l;
      this->imu2 = 0l;
      this->imu3 = 0l;
    }
  }

  explicit Potmsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->pot1 = 0l;
      this->pot2 = 0l;
      this->pot3 = 0l;
      this->pot4 = 0l;
      this->pot5 = 0l;
      this->pot6 = 0l;
      this->pot7 = 0l;
      this->pot8 = 0l;
      this->imu1 = 0l;
      this->imu2 = 0l;
      this->imu3 = 0l;
    }
  }

  // field types and members
  using _pot1_type =
    int32_t;
  _pot1_type pot1;
  using _pot2_type =
    int32_t;
  _pot2_type pot2;
  using _pot3_type =
    int32_t;
  _pot3_type pot3;
  using _pot4_type =
    int32_t;
  _pot4_type pot4;
  using _pot5_type =
    int32_t;
  _pot5_type pot5;
  using _pot6_type =
    int32_t;
  _pot6_type pot6;
  using _pot7_type =
    int32_t;
  _pot7_type pot7;
  using _pot8_type =
    int32_t;
  _pot8_type pot8;
  using _imu1_type =
    int32_t;
  _imu1_type imu1;
  using _imu2_type =
    int32_t;
  _imu2_type imu2;
  using _imu3_type =
    int32_t;
  _imu3_type imu3;

  // setters for named parameter idiom
  Type & set__pot1(
    const int32_t & _arg)
  {
    this->pot1 = _arg;
    return *this;
  }
  Type & set__pot2(
    const int32_t & _arg)
  {
    this->pot2 = _arg;
    return *this;
  }
  Type & set__pot3(
    const int32_t & _arg)
  {
    this->pot3 = _arg;
    return *this;
  }
  Type & set__pot4(
    const int32_t & _arg)
  {
    this->pot4 = _arg;
    return *this;
  }
  Type & set__pot5(
    const int32_t & _arg)
  {
    this->pot5 = _arg;
    return *this;
  }
  Type & set__pot6(
    const int32_t & _arg)
  {
    this->pot6 = _arg;
    return *this;
  }
  Type & set__pot7(
    const int32_t & _arg)
  {
    this->pot7 = _arg;
    return *this;
  }
  Type & set__pot8(
    const int32_t & _arg)
  {
    this->pot8 = _arg;
    return *this;
  }
  Type & set__imu1(
    const int32_t & _arg)
  {
    this->imu1 = _arg;
    return *this;
  }
  Type & set__imu2(
    const int32_t & _arg)
  {
    this->imu2 = _arg;
    return *this;
  }
  Type & set__imu3(
    const int32_t & _arg)
  {
    this->imu3 = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    potmessage::msg::Potmsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const potmessage::msg::Potmsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<potmessage::msg::Potmsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<potmessage::msg::Potmsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      potmessage::msg::Potmsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<potmessage::msg::Potmsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      potmessage::msg::Potmsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<potmessage::msg::Potmsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<potmessage::msg::Potmsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<potmessage::msg::Potmsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__potmessage__msg__Potmsg
    std::shared_ptr<potmessage::msg::Potmsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__potmessage__msg__Potmsg
    std::shared_ptr<potmessage::msg::Potmsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Potmsg_ & other) const
  {
    if (this->pot1 != other.pot1) {
      return false;
    }
    if (this->pot2 != other.pot2) {
      return false;
    }
    if (this->pot3 != other.pot3) {
      return false;
    }
    if (this->pot4 != other.pot4) {
      return false;
    }
    if (this->pot5 != other.pot5) {
      return false;
    }
    if (this->pot6 != other.pot6) {
      return false;
    }
    if (this->pot7 != other.pot7) {
      return false;
    }
    if (this->pot8 != other.pot8) {
      return false;
    }
    if (this->imu1 != other.imu1) {
      return false;
    }
    if (this->imu2 != other.imu2) {
      return false;
    }
    if (this->imu3 != other.imu3) {
      return false;
    }
    return true;
  }
  bool operator!=(const Potmsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Potmsg_

// alias to use template instance with default allocator
using Potmsg =
  potmessage::msg::Potmsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace potmessage

#endif  // POTMESSAGE__MSG__DETAIL__POTMSG__STRUCT_HPP_
