// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from vision_msgs:msg/Objects.idl
// generated code does not contain a copyright notice

#ifndef VISION_MSGS__MSG__DETAIL__OBJECTS__STRUCT_H_
#define VISION_MSGS__MSG__DETAIL__OBJECTS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'ball'
#include "vision_msgs/msg/detail/ball__struct.h"
// Member 'goal'
#include "vision_msgs/msg/detail/goal__struct.h"
// Member 'robots'
#include "vision_msgs/msg/detail/robot__struct.h"
// Member 'image'
#include "sensor_msgs/msg/detail/image__struct.h"

/// Struct defined in msg/Objects in the package vision_msgs.
typedef struct vision_msgs__msg__Objects
{
  vision_msgs__msg__Ball ball;
  vision_msgs__msg__Goal goal;
  vision_msgs__msg__Robot__Sequence robots;
  sensor_msgs__msg__Image image;
} vision_msgs__msg__Objects;

// Struct for a sequence of vision_msgs__msg__Objects.
typedef struct vision_msgs__msg__Objects__Sequence
{
  vision_msgs__msg__Objects * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} vision_msgs__msg__Objects__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // VISION_MSGS__MSG__DETAIL__OBJECTS__STRUCT_H_
