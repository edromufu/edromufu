// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from movement_utils:srv/HeadFeedback.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "movement_utils/srv/detail/head_feedback__rosidl_typesupport_introspection_c.h"
#include "movement_utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "movement_utils/srv/detail/head_feedback__functions.h"
#include "movement_utils/srv/detail/head_feedback__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void movement_utils__srv__HeadFeedback_Request__rosidl_typesupport_introspection_c__HeadFeedback_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  movement_utils__srv__HeadFeedback_Request__init(message_memory);
}

void movement_utils__srv__HeadFeedback_Request__rosidl_typesupport_introspection_c__HeadFeedback_Request_fini_function(void * message_memory)
{
  movement_utils__srv__HeadFeedback_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember movement_utils__srv__HeadFeedback_Request__rosidl_typesupport_introspection_c__HeadFeedback_Request_message_member_array[1] = {
  {
    "dont_use",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(movement_utils__srv__HeadFeedback_Request, dont_use),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers movement_utils__srv__HeadFeedback_Request__rosidl_typesupport_introspection_c__HeadFeedback_Request_message_members = {
  "movement_utils__srv",  // message namespace
  "HeadFeedback_Request",  // message name
  1,  // number of fields
  sizeof(movement_utils__srv__HeadFeedback_Request),
  movement_utils__srv__HeadFeedback_Request__rosidl_typesupport_introspection_c__HeadFeedback_Request_message_member_array,  // message members
  movement_utils__srv__HeadFeedback_Request__rosidl_typesupport_introspection_c__HeadFeedback_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  movement_utils__srv__HeadFeedback_Request__rosidl_typesupport_introspection_c__HeadFeedback_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t movement_utils__srv__HeadFeedback_Request__rosidl_typesupport_introspection_c__HeadFeedback_Request_message_type_support_handle = {
  0,
  &movement_utils__srv__HeadFeedback_Request__rosidl_typesupport_introspection_c__HeadFeedback_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_movement_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, movement_utils, srv, HeadFeedback_Request)() {
  if (!movement_utils__srv__HeadFeedback_Request__rosidl_typesupport_introspection_c__HeadFeedback_Request_message_type_support_handle.typesupport_identifier) {
    movement_utils__srv__HeadFeedback_Request__rosidl_typesupport_introspection_c__HeadFeedback_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &movement_utils__srv__HeadFeedback_Request__rosidl_typesupport_introspection_c__HeadFeedback_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "movement_utils/srv/detail/head_feedback__rosidl_typesupport_introspection_c.h"
// already included above
// #include "movement_utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "movement_utils/srv/detail/head_feedback__functions.h"
// already included above
// #include "movement_utils/srv/detail/head_feedback__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__HeadFeedback_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  movement_utils__srv__HeadFeedback_Response__init(message_memory);
}

void movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__HeadFeedback_Response_fini_function(void * message_memory)
{
  movement_utils__srv__HeadFeedback_Response__fini(message_memory);
}

size_t movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__size_function__HeadFeedback_Response__pos_vector(
  const void * untyped_member)
{
  (void)untyped_member;
  return 2;
}

const void * movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__get_const_function__HeadFeedback_Response__pos_vector(
  const void * untyped_member, size_t index)
{
  const float * member =
    (const float *)(untyped_member);
  return &member[index];
}

void * movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__get_function__HeadFeedback_Response__pos_vector(
  void * untyped_member, size_t index)
{
  float * member =
    (float *)(untyped_member);
  return &member[index];
}

void movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__fetch_function__HeadFeedback_Response__pos_vector(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__get_const_function__HeadFeedback_Response__pos_vector(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__assign_function__HeadFeedback_Response__pos_vector(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__get_function__HeadFeedback_Response__pos_vector(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

static rosidl_typesupport_introspection_c__MessageMember movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__HeadFeedback_Response_message_member_array[1] = {
  {
    "pos_vector",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    2,  // array size
    false,  // is upper bound
    offsetof(movement_utils__srv__HeadFeedback_Response, pos_vector),  // bytes offset in struct
    NULL,  // default value
    movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__size_function__HeadFeedback_Response__pos_vector,  // size() function pointer
    movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__get_const_function__HeadFeedback_Response__pos_vector,  // get_const(index) function pointer
    movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__get_function__HeadFeedback_Response__pos_vector,  // get(index) function pointer
    movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__fetch_function__HeadFeedback_Response__pos_vector,  // fetch(index, &value) function pointer
    movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__assign_function__HeadFeedback_Response__pos_vector,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__HeadFeedback_Response_message_members = {
  "movement_utils__srv",  // message namespace
  "HeadFeedback_Response",  // message name
  1,  // number of fields
  sizeof(movement_utils__srv__HeadFeedback_Response),
  movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__HeadFeedback_Response_message_member_array,  // message members
  movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__HeadFeedback_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__HeadFeedback_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__HeadFeedback_Response_message_type_support_handle = {
  0,
  &movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__HeadFeedback_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_movement_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, movement_utils, srv, HeadFeedback_Response)() {
  if (!movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__HeadFeedback_Response_message_type_support_handle.typesupport_identifier) {
    movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__HeadFeedback_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &movement_utils__srv__HeadFeedback_Response__rosidl_typesupport_introspection_c__HeadFeedback_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "movement_utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "movement_utils/srv/detail/head_feedback__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers movement_utils__srv__detail__head_feedback__rosidl_typesupport_introspection_c__HeadFeedback_service_members = {
  "movement_utils__srv",  // service namespace
  "HeadFeedback",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // movement_utils__srv__detail__head_feedback__rosidl_typesupport_introspection_c__HeadFeedback_Request_message_type_support_handle,
  NULL  // response message
  // movement_utils__srv__detail__head_feedback__rosidl_typesupport_introspection_c__HeadFeedback_Response_message_type_support_handle
};

static rosidl_service_type_support_t movement_utils__srv__detail__head_feedback__rosidl_typesupport_introspection_c__HeadFeedback_service_type_support_handle = {
  0,
  &movement_utils__srv__detail__head_feedback__rosidl_typesupport_introspection_c__HeadFeedback_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, movement_utils, srv, HeadFeedback_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, movement_utils, srv, HeadFeedback_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_movement_utils
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, movement_utils, srv, HeadFeedback)() {
  if (!movement_utils__srv__detail__head_feedback__rosidl_typesupport_introspection_c__HeadFeedback_service_type_support_handle.typesupport_identifier) {
    movement_utils__srv__detail__head_feedback__rosidl_typesupport_introspection_c__HeadFeedback_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)movement_utils__srv__detail__head_feedback__rosidl_typesupport_introspection_c__HeadFeedback_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, movement_utils, srv, HeadFeedback_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, movement_utils, srv, HeadFeedback_Response)()->data;
  }

  return &movement_utils__srv__detail__head_feedback__rosidl_typesupport_introspection_c__HeadFeedback_service_type_support_handle;
}
