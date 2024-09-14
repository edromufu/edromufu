// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from buttonmessage:msg/Buttonmsg.idl
// generated code does not contain a copyright notice

#ifndef BUTTONMESSAGE__MSG__DETAIL__BUTTONMSG__STRUCT_H_
#define BUTTONMESSAGE__MSG__DETAIL__BUTTONMSG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Buttonmsg in the package buttonmessage.
typedef struct buttonmessage__msg__Buttonmsg
{
  bool but_bhv;
  bool but_rst;
} buttonmessage__msg__Buttonmsg;

// Struct for a sequence of buttonmessage__msg__Buttonmsg.
typedef struct buttonmessage__msg__Buttonmsg__Sequence
{
  buttonmessage__msg__Buttonmsg * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} buttonmessage__msg__Buttonmsg__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // BUTTONMESSAGE__MSG__DETAIL__BUTTONMSG__STRUCT_H_
