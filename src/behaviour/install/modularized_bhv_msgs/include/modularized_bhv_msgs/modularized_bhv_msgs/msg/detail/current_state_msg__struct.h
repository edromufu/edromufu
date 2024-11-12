// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from modularized_bhv_msgs:msg/CurrentStateMsg.idl
// generated code does not contain a copyright notice

#ifndef MODULARIZED_BHV_MSGS__MSG__DETAIL__CURRENT_STATE_MSG__STRUCT_H_
#define MODULARIZED_BHV_MSGS__MSG__DETAIL__CURRENT_STATE_MSG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'current_state'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/CurrentStateMsg in the package modularized_bhv_msgs.
typedef struct modularized_bhv_msgs__msg__CurrentStateMsg
{
  rosidl_runtime_c__String current_state;
} modularized_bhv_msgs__msg__CurrentStateMsg;

// Struct for a sequence of modularized_bhv_msgs__msg__CurrentStateMsg.
typedef struct modularized_bhv_msgs__msg__CurrentStateMsg__Sequence
{
  modularized_bhv_msgs__msg__CurrentStateMsg * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} modularized_bhv_msgs__msg__CurrentStateMsg__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MODULARIZED_BHV_MSGS__MSG__DETAIL__CURRENT_STATE_MSG__STRUCT_H_
