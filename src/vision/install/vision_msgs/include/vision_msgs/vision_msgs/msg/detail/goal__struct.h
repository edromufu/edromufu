// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from vision_msgs:msg/Goal.idl
// generated code does not contain a copyright notice

#ifndef VISION_MSGS__MSG__DETAIL__GOAL__STRUCT_H_
#define VISION_MSGS__MSG__DETAIL__GOAL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Goal in the package vision_msgs.
typedef struct vision_msgs__msg__Goal
{
  bool found;
  int32_t x;
  int32_t y;
} vision_msgs__msg__Goal;

// Struct for a sequence of vision_msgs__msg__Goal.
typedef struct vision_msgs__msg__Goal__Sequence
{
  vision_msgs__msg__Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} vision_msgs__msg__Goal__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // VISION_MSGS__MSG__DETAIL__GOAL__STRUCT_H_
