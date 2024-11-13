// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from movement_utils:msg/HeadMotorsData.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__MSG__DETAIL__HEAD_MOTORS_DATA__STRUCT_H_
#define MOVEMENT_UTILS__MSG__DETAIL__HEAD_MOTORS_DATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/HeadMotorsData in the package movement_utils.
typedef struct movement_utils__msg__HeadMotorsData
{
  float pos_vector[2];
} movement_utils__msg__HeadMotorsData;

// Struct for a sequence of movement_utils__msg__HeadMotorsData.
typedef struct movement_utils__msg__HeadMotorsData__Sequence
{
  movement_utils__msg__HeadMotorsData * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} movement_utils__msg__HeadMotorsData__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MOVEMENT_UTILS__MSG__DETAIL__HEAD_MOTORS_DATA__STRUCT_H_
