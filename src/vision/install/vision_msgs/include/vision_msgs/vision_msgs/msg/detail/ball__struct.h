// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from vision_msgs:msg/Ball.idl
// generated code does not contain a copyright notice

#ifndef VISION_MSGS__MSG__DETAIL__BALL__STRUCT_H_
#define VISION_MSGS__MSG__DETAIL__BALL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Ball in the package vision_msgs.
typedef struct vision_msgs__msg__Ball
{
  bool found;
  int32_t x;
  int32_t y;
  int32_t roi_width;
  int32_t roi_height;
} vision_msgs__msg__Ball;

// Struct for a sequence of vision_msgs__msg__Ball.
typedef struct vision_msgs__msg__Ball__Sequence
{
  vision_msgs__msg__Ball * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} vision_msgs__msg__Ball__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // VISION_MSGS__MSG__DETAIL__BALL__STRUCT_H_
