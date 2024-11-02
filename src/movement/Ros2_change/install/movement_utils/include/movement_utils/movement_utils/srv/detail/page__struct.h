// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from movement_utils:srv/Page.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__SRV__DETAIL__PAGE__STRUCT_H_
#define MOVEMENT_UTILS__SRV__DETAIL__PAGE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'page_name'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/Page in the package movement_utils.
typedef struct movement_utils__srv__Page_Request
{
  rosidl_runtime_c__String page_name;
} movement_utils__srv__Page_Request;

// Struct for a sequence of movement_utils__srv__Page_Request.
typedef struct movement_utils__srv__Page_Request__Sequence
{
  movement_utils__srv__Page_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} movement_utils__srv__Page_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Page in the package movement_utils.
typedef struct movement_utils__srv__Page_Response
{
  bool success;
} movement_utils__srv__Page_Response;

// Struct for a sequence of movement_utils__srv__Page_Response.
typedef struct movement_utils__srv__Page_Response__Sequence
{
  movement_utils__srv__Page_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} movement_utils__srv__Page_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MOVEMENT_UTILS__SRV__DETAIL__PAGE__STRUCT_H_
