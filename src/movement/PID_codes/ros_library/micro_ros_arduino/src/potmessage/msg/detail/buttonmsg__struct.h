// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from potmessage:msg/Buttonmsg.idl
// generated code does not contain a copyright notice

#ifndef POTMESSAGE__MSG__DETAIL__BUTTONMSG__STRUCT_H_
#define POTMESSAGE__MSG__DETAIL__BUTTONMSG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Buttonmsg in the package potmessage.
typedef struct potmessage__msg__Buttonmsg
{
  bool bot1;
  bool bot2;
} potmessage__msg__Buttonmsg;

// Struct for a sequence of potmessage__msg__Buttonmsg.
typedef struct potmessage__msg__Buttonmsg__Sequence
{
  potmessage__msg__Buttonmsg * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} potmessage__msg__Buttonmsg__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // POTMESSAGE__MSG__DETAIL__BUTTONMSG__STRUCT_H_
