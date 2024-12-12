// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from movement_utils:srv/WalkForward.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__SRV__DETAIL__WALK_FORWARD__STRUCT_H_
#define MOVEMENT_UTILS__SRV__DETAIL__WALK_FORWARD__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/WalkForward in the package movement_utils.
typedef struct movement_utils__srv__WalkForward_Request
{
  int8_t support_foot;
  int8_t steps_number;
} movement_utils__srv__WalkForward_Request;

// Struct for a sequence of movement_utils__srv__WalkForward_Request.
typedef struct movement_utils__srv__WalkForward_Request__Sequence
{
  movement_utils__srv__WalkForward_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} movement_utils__srv__WalkForward_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/WalkForward in the package movement_utils.
typedef struct movement_utils__srv__WalkForward_Response
{
  bool success;
} movement_utils__srv__WalkForward_Response;

// Struct for a sequence of movement_utils__srv__WalkForward_Response.
typedef struct movement_utils__srv__WalkForward_Response__Sequence
{
  movement_utils__srv__WalkForward_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} movement_utils__srv__WalkForward_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MOVEMENT_UTILS__SRV__DETAIL__WALK_FORWARD__STRUCT_H_
