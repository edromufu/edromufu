// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from vision_msgs:msg/Webotsmsg.idl
// generated code does not contain a copyright notice

#ifndef VISION_MSGS__MSG__DETAIL__WEBOTSMSG__STRUCT_H_
#define VISION_MSGS__MSG__DETAIL__WEBOTSMSG__STRUCT_H_

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
// Member 'leftgoalpost'
#include "vision_msgs/msg/detail/leftgoalpost__struct.h"
// Member 'rightgoalpost'
#include "vision_msgs/msg/detail/rightgoalpost__struct.h"

/// Struct defined in msg/Webotsmsg in the package vision_msgs.
typedef struct vision_msgs__msg__Webotsmsg
{
  bool searching;
  uint8_t fps;
  vision_msgs__msg__Ball ball;
  vision_msgs__msg__Leftgoalpost leftgoalpost;
  vision_msgs__msg__Rightgoalpost rightgoalpost;
} vision_msgs__msg__Webotsmsg;

// Struct for a sequence of vision_msgs__msg__Webotsmsg.
typedef struct vision_msgs__msg__Webotsmsg__Sequence
{
  vision_msgs__msg__Webotsmsg * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} vision_msgs__msg__Webotsmsg__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // VISION_MSGS__MSG__DETAIL__WEBOTSMSG__STRUCT_H_
