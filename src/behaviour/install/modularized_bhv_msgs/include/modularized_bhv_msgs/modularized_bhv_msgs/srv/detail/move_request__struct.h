// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from modularized_bhv_msgs:srv/MoveRequest.idl
// generated code does not contain a copyright notice

#ifndef MODULARIZED_BHV_MSGS__SRV__DETAIL__MOVE_REQUEST__STRUCT_H_
#define MODULARIZED_BHV_MSGS__SRV__DETAIL__MOVE_REQUEST__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'move_request'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/MoveRequest in the package modularized_bhv_msgs.
typedef struct modularized_bhv_msgs__srv__MoveRequest_Request
{
  rosidl_runtime_c__String move_request;
} modularized_bhv_msgs__srv__MoveRequest_Request;

// Struct for a sequence of modularized_bhv_msgs__srv__MoveRequest_Request.
typedef struct modularized_bhv_msgs__srv__MoveRequest_Request__Sequence
{
  modularized_bhv_msgs__srv__MoveRequest_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} modularized_bhv_msgs__srv__MoveRequest_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/MoveRequest in the package modularized_bhv_msgs.
typedef struct modularized_bhv_msgs__srv__MoveRequest_Response
{
  bool success;
} modularized_bhv_msgs__srv__MoveRequest_Response;

// Struct for a sequence of modularized_bhv_msgs__srv__MoveRequest_Response.
typedef struct modularized_bhv_msgs__srv__MoveRequest_Response__Sequence
{
  modularized_bhv_msgs__srv__MoveRequest_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} modularized_bhv_msgs__srv__MoveRequest_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MODULARIZED_BHV_MSGS__SRV__DETAIL__MOVE_REQUEST__STRUCT_H_
