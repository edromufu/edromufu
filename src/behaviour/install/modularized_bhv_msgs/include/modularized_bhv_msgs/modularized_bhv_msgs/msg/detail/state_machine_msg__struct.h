// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from modularized_bhv_msgs:msg/StateMachineMsg.idl
// generated code does not contain a copyright notice

#ifndef MODULARIZED_BHV_MSGS__MSG__DETAIL__STATE_MACHINE_MSG__STRUCT_H_
#define MODULARIZED_BHV_MSGS__MSG__DETAIL__STATE_MACHINE_MSG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'ball_position'
// Member 'fall_state'
// Member 'hor_motor_out_of_center'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/StateMachineMsg in the package modularized_bhv_msgs.
typedef struct modularized_bhv_msgs__msg__StateMachineMsg
{
  rosidl_runtime_c__String ball_position;
  bool ball_close;
  bool ball_found;
  rosidl_runtime_c__String fall_state;
  rosidl_runtime_c__String hor_motor_out_of_center;
  bool head_kick_check;
} modularized_bhv_msgs__msg__StateMachineMsg;

// Struct for a sequence of modularized_bhv_msgs__msg__StateMachineMsg.
typedef struct modularized_bhv_msgs__msg__StateMachineMsg__Sequence
{
  modularized_bhv_msgs__msg__StateMachineMsg * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} modularized_bhv_msgs__msg__StateMachineMsg__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MODULARIZED_BHV_MSGS__MSG__DETAIL__STATE_MACHINE_MSG__STRUCT_H_
