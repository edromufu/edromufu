// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from vision_msgs:msg/Leftgoalpost.idl
// generated code does not contain a copyright notice

#ifndef VISION_MSGS__MSG__DETAIL__LEFTGOALPOST__STRUCT_H_
#define VISION_MSGS__MSG__DETAIL__LEFTGOALPOST__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Leftgoalpost in the package vision_msgs.
typedef struct vision_msgs__msg__Leftgoalpost
{
  bool found;
  int32_t x;
  int32_t y;
  int32_t roi_width;
  int32_t roi_height;
} vision_msgs__msg__Leftgoalpost;

// Struct for a sequence of vision_msgs__msg__Leftgoalpost.
typedef struct vision_msgs__msg__Leftgoalpost__Sequence
{
  vision_msgs__msg__Leftgoalpost * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} vision_msgs__msg__Leftgoalpost__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // VISION_MSGS__MSG__DETAIL__LEFTGOALPOST__STRUCT_H_
