// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from movement_utils:srv/Rotate.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__SRV__DETAIL__ROTATE__STRUCT_H_
#define MOVEMENT_UTILS__SRV__DETAIL__ROTATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Rotate in the package movement_utils.
typedef struct movement_utils__srv__Rotate_Request
{
  int8_t direction;
  int8_t steps_number;
} movement_utils__srv__Rotate_Request;

// Struct for a sequence of movement_utils__srv__Rotate_Request.
typedef struct movement_utils__srv__Rotate_Request__Sequence
{
  movement_utils__srv__Rotate_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} movement_utils__srv__Rotate_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Rotate in the package movement_utils.
typedef struct movement_utils__srv__Rotate_Response
{
  bool success;
} movement_utils__srv__Rotate_Response;

// Struct for a sequence of movement_utils__srv__Rotate_Response.
typedef struct movement_utils__srv__Rotate_Response__Sequence
{
  movement_utils__srv__Rotate_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} movement_utils__srv__Rotate_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MOVEMENT_UTILS__SRV__DETAIL__ROTATE__STRUCT_H_
