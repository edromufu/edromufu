// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from imumessage:msg/Imumsg.idl
// generated code does not contain a copyright notice

#ifndef IMUMESSAGE__MSG__DETAIL__IMUMSG__STRUCT_H_
#define IMUMESSAGE__MSG__DETAIL__IMUMSG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Imumsg in the package imumessage.
typedef struct imumessage__msg__Imumsg
{
  int32_t imu1;
  int32_t imu2;
  int32_t imu3;
} imumessage__msg__Imumsg;

// Struct for a sequence of imumessage__msg__Imumsg.
typedef struct imumessage__msg__Imumsg__Sequence
{
  imumessage__msg__Imumsg * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} imumessage__msg__Imumsg__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // IMUMESSAGE__MSG__DETAIL__IMUMSG__STRUCT_H_
