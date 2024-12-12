// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from movement_utils:msg/BodyMotorsData.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__MSG__DETAIL__BODY_MOTORS_DATA__STRUCT_H_
#define MOVEMENT_UTILS__MSG__DETAIL__BODY_MOTORS_DATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/BodyMotorsData in the package movement_utils.
typedef struct movement_utils__msg__BodyMotorsData
{
  float pos_vector[18];
} movement_utils__msg__BodyMotorsData;

// Struct for a sequence of movement_utils__msg__BodyMotorsData.
typedef struct movement_utils__msg__BodyMotorsData__Sequence
{
  movement_utils__msg__BodyMotorsData * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} movement_utils__msg__BodyMotorsData__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MOVEMENT_UTILS__MSG__DETAIL__BODY_MOTORS_DATA__STRUCT_H_
