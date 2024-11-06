// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from potmessage:msg/Imumsg.idl
// generated code does not contain a copyright notice

#ifndef POTMESSAGE__MSG__DETAIL__IMUMSG__STRUCT_HPP_
#define POTMESSAGE__MSG__DETAIL__IMUMSG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__potmessage__msg__Imumsg __attribute__((deprecated))
#else
# define DEPRECATED__potmessage__msg__Imumsg __declspec(deprecated)
#endif

namespace potmessage
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Imumsg_
{
  using Type = Imumsg_<ContainerAllocator>;

  explicit Imumsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<float, 4>::iterator, float>(this->imu.begin(), this->imu.end(), 0.0f);
    }
  }

  explicit Imumsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : imu(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<float, 4>::iterator, float>(this->imu.begin(), this->imu.end(), 0.0f);
    }
  }

  // field types and members
  using _imu_type =
    std::array<float, 4>;
  _imu_type imu;

  // setters for named parameter idiom
  Type & set__imu(
    const std::array<float, 4> & _arg)
  {
    this->imu = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    potmessage::msg::Imumsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const potmessage::msg::Imumsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<potmessage::msg::Imumsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<potmessage::msg::Imumsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      potmessage::msg::Imumsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<potmessage::msg::Imumsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      potmessage::msg::Imumsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<potmessage::msg::Imumsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<potmessage::msg::Imumsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<potmessage::msg::Imumsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__potmessage__msg__Imumsg
    std::shared_ptr<potmessage::msg::Imumsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__potmessage__msg__Imumsg
    std::shared_ptr<potmessage::msg::Imumsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Imumsg_ & other) const
  {
    if (this->imu != other.imu) {
      return false;
    }
    return true;
  }
  bool operator!=(const Imumsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Imumsg_

// alias to use template instance with default allocator
using Imumsg =
  potmessage::msg::Imumsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace potmessage

#endif  // POTMESSAGE__MSG__DETAIL__IMUMSG__STRUCT_HPP_
