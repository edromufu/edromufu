// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from vision_msgs:msg/Webotsmsg.idl
// generated code does not contain a copyright notice

#ifndef VISION_MSGS__MSG__DETAIL__WEBOTSMSG__STRUCT_HPP_
#define VISION_MSGS__MSG__DETAIL__WEBOTSMSG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'ball'
#include "vision_msgs/msg/detail/ball__struct.hpp"
// Member 'leftgoalpost'
#include "vision_msgs/msg/detail/leftgoalpost__struct.hpp"
// Member 'rightgoalpost'
#include "vision_msgs/msg/detail/rightgoalpost__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__vision_msgs__msg__Webotsmsg __attribute__((deprecated))
#else
# define DEPRECATED__vision_msgs__msg__Webotsmsg __declspec(deprecated)
#endif

namespace vision_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Webotsmsg_
{
  using Type = Webotsmsg_<ContainerAllocator>;

  explicit Webotsmsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : ball(_init),
    leftgoalpost(_init),
    rightgoalpost(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->searching = false;
      this->fps = 0;
    }
  }

  explicit Webotsmsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : ball(_alloc, _init),
    leftgoalpost(_alloc, _init),
    rightgoalpost(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->searching = false;
      this->fps = 0;
    }
  }

  // field types and members
  using _searching_type =
    bool;
  _searching_type searching;
  using _fps_type =
    uint8_t;
  _fps_type fps;
  using _ball_type =
    vision_msgs::msg::Ball_<ContainerAllocator>;
  _ball_type ball;
  using _leftgoalpost_type =
    vision_msgs::msg::Leftgoalpost_<ContainerAllocator>;
  _leftgoalpost_type leftgoalpost;
  using _rightgoalpost_type =
    vision_msgs::msg::Rightgoalpost_<ContainerAllocator>;
  _rightgoalpost_type rightgoalpost;

  // setters for named parameter idiom
  Type & set__searching(
    const bool & _arg)
  {
    this->searching = _arg;
    return *this;
  }
  Type & set__fps(
    const uint8_t & _arg)
  {
    this->fps = _arg;
    return *this;
  }
  Type & set__ball(
    const vision_msgs::msg::Ball_<ContainerAllocator> & _arg)
  {
    this->ball = _arg;
    return *this;
  }
  Type & set__leftgoalpost(
    const vision_msgs::msg::Leftgoalpost_<ContainerAllocator> & _arg)
  {
    this->leftgoalpost = _arg;
    return *this;
  }
  Type & set__rightgoalpost(
    const vision_msgs::msg::Rightgoalpost_<ContainerAllocator> & _arg)
  {
    this->rightgoalpost = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    vision_msgs::msg::Webotsmsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const vision_msgs::msg::Webotsmsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<vision_msgs::msg::Webotsmsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<vision_msgs::msg::Webotsmsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      vision_msgs::msg::Webotsmsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<vision_msgs::msg::Webotsmsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      vision_msgs::msg::Webotsmsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<vision_msgs::msg::Webotsmsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<vision_msgs::msg::Webotsmsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<vision_msgs::msg::Webotsmsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__vision_msgs__msg__Webotsmsg
    std::shared_ptr<vision_msgs::msg::Webotsmsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__vision_msgs__msg__Webotsmsg
    std::shared_ptr<vision_msgs::msg::Webotsmsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Webotsmsg_ & other) const
  {
    if (this->searching != other.searching) {
      return false;
    }
    if (this->fps != other.fps) {
      return false;
    }
    if (this->ball != other.ball) {
      return false;
    }
    if (this->leftgoalpost != other.leftgoalpost) {
      return false;
    }
    if (this->rightgoalpost != other.rightgoalpost) {
      return false;
    }
    return true;
  }
  bool operator!=(const Webotsmsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Webotsmsg_

// alias to use template instance with default allocator
using Webotsmsg =
  vision_msgs::msg::Webotsmsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace vision_msgs

#endif  // VISION_MSGS__MSG__DETAIL__WEBOTSMSG__STRUCT_HPP_
