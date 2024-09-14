// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from potmessage:msg/Potmsg.idl
// generated code does not contain a copyright notice

#ifndef POTMESSAGE__MSG__DETAIL__POTMSG__STRUCT_H_
#define POTMESSAGE__MSG__DETAIL__POTMSG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Potmsg in the package potmessage.
typedef struct potmessage__msg__Potmsg
{
  float pot1;
  float pot2;
  float pot3;
  float pot4;
  float pot5;
  float pot6;
  float pot7;
  float pot8;
} potmessage__msg__Potmsg;

// Struct for a sequence of potmessage__msg__Potmsg.
typedef struct potmessage__msg__Potmsg__Sequence
{
  potmessage__msg__Potmsg * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} potmessage__msg__Potmsg__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // POTMESSAGE__MSG__DETAIL__POTMSG__STRUCT_H_
