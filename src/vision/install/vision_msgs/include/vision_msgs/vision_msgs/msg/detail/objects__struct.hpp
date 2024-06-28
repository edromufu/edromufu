// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from vision_msgs:msg/Objects.idl
// generated code does not contain a copyright notice

#ifndef VISION_MSGS__MSG__DETAIL__OBJECTS__STRUCT_HPP_
#define VISION_MSGS__MSG__DETAIL__OBJECTS__STRUCT_HPP_

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
// Member 'goal'
#include "vision_msgs/msg/detail/goal__struct.hpp"
// Member 'robots'
#include "vision_msgs/msg/detail/robot__struct.hpp"
// Member 'image'
#include "sensor_msgs/msg/detail/image__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__vision_msgs__msg__Objects __attribute__((deprecated))
#else
# define DEPRECATED__vision_msgs__msg__Objects __declspec(deprecated)
#endif

namespace vision_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Objects_
{
  using Type = Objects_<ContainerAllocator>;

  explicit Objects_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : ball(_init),
    goal(_init),
    image(_init)
  {
    (void)_init;
  }

  explicit Objects_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : ball(_alloc, _init),
    goal(_alloc, _init),
    image(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _ball_type =
    vision_msgs::msg::Ball_<ContainerAllocator>;
  _ball_type ball;
  using _goal_type =
    vision_msgs::msg::Goal_<ContainerAllocator>;
  _goal_type goal;
  using _robots_type =
    std::vector<vision_msgs::msg::Robot_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<vision_msgs::msg::Robot_<ContainerAllocator>>>;
  _robots_type robots;
  using _image_type =
    sensor_msgs::msg::Image_<ContainerAllocator>;
  _image_type image;

  // setters for named parameter idiom
  Type & set__ball(
    const vision_msgs::msg::Ball_<ContainerAllocator> & _arg)
  {
    this->ball = _arg;
    return *this;
  }
  Type & set__goal(
    const vision_msgs::msg::Goal_<ContainerAllocator> & _arg)
  {
    this->goal = _arg;
    return *this;
  }
  Type & set__robots(
    const std::vector<vision_msgs::msg::Robot_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<vision_msgs::msg::Robot_<ContainerAllocator>>> & _arg)
  {
    this->robots = _arg;
    return *this;
  }
  Type & set__image(
    const sensor_msgs::msg::Image_<ContainerAllocator> & _arg)
  {
    this->image = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    vision_msgs::msg::Objects_<ContainerAllocator> *;
  using ConstRawPtr =
    const vision_msgs::msg::Objects_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<vision_msgs::msg::Objects_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<vision_msgs::msg::Objects_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      vision_msgs::msg::Objects_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<vision_msgs::msg::Objects_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      vision_msgs::msg::Objects_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<vision_msgs::msg::Objects_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<vision_msgs::msg::Objects_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<vision_msgs::msg::Objects_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__vision_msgs__msg__Objects
    std::shared_ptr<vision_msgs::msg::Objects_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__vision_msgs__msg__Objects
    std::shared_ptr<vision_msgs::msg::Objects_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Objects_ & other) const
  {
    if (this->ball != other.ball) {
      return false;
    }
    if (this->goal != other.goal) {
      return false;
    }
    if (this->robots != other.robots) {
      return false;
    }
    if (this->image != other.image) {
      return false;
    }
    return true;
  }
  bool operator!=(const Objects_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Objects_

// alias to use template instance with default allocator
using Objects =
  vision_msgs::msg::Objects_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace vision_msgs

#endif  // VISION_MSGS__MSG__DETAIL__OBJECTS__STRUCT_HPP_
