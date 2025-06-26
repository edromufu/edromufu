// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from modularized_bhv_msgs:srv/MoveRequest.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "modularized_bhv_msgs/srv/detail/move_request__rosidl_typesupport_introspection_c.h"
#include "modularized_bhv_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "modularized_bhv_msgs/srv/detail/move_request__functions.h"
#include "modularized_bhv_msgs/srv/detail/move_request__struct.h"


// Include directives for member types
// Member `move_request`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void modularized_bhv_msgs__srv__MoveRequest_Request__rosidl_typesupport_introspection_c__MoveRequest_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  modularized_bhv_msgs__srv__MoveRequest_Request__init(message_memory);
}

void modularized_bhv_msgs__srv__MoveRequest_Request__rosidl_typesupport_introspection_c__MoveRequest_Request_fini_function(void * message_memory)
{
  modularized_bhv_msgs__srv__MoveRequest_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember modularized_bhv_msgs__srv__MoveRequest_Request__rosidl_typesupport_introspection_c__MoveRequest_Request_message_member_array[1] = {
  {
    "move_request",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__srv__MoveRequest_Request, move_request),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers modularized_bhv_msgs__srv__MoveRequest_Request__rosidl_typesupport_introspection_c__MoveRequest_Request_message_members = {
  "modularized_bhv_msgs__srv",  // message namespace
  "MoveRequest_Request",  // message name
  1,  // number of fields
  sizeof(modularized_bhv_msgs__srv__MoveRequest_Request),
  modularized_bhv_msgs__srv__MoveRequest_Request__rosidl_typesupport_introspection_c__MoveRequest_Request_message_member_array,  // message members
  modularized_bhv_msgs__srv__MoveRequest_Request__rosidl_typesupport_introspection_c__MoveRequest_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  modularized_bhv_msgs__srv__MoveRequest_Request__rosidl_typesupport_introspection_c__MoveRequest_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t modularized_bhv_msgs__srv__MoveRequest_Request__rosidl_typesupport_introspection_c__MoveRequest_Request_message_type_support_handle = {
  0,
  &modularized_bhv_msgs__srv__MoveRequest_Request__rosidl_typesupport_introspection_c__MoveRequest_Request_message_members,
  get_message_typesupport_handle_function,
  &modularized_bhv_msgs__srv__MoveRequest_Request__get_type_hash,
  &modularized_bhv_msgs__srv__MoveRequest_Request__get_type_description,
  &modularized_bhv_msgs__srv__MoveRequest_Request__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_modularized_bhv_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, modularized_bhv_msgs, srv, MoveRequest_Request)() {
  if (!modularized_bhv_msgs__srv__MoveRequest_Request__rosidl_typesupport_introspection_c__MoveRequest_Request_message_type_support_handle.typesupport_identifier) {
    modularized_bhv_msgs__srv__MoveRequest_Request__rosidl_typesupport_introspection_c__MoveRequest_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &modularized_bhv_msgs__srv__MoveRequest_Request__rosidl_typesupport_introspection_c__MoveRequest_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "modularized_bhv_msgs/srv/detail/move_request__rosidl_typesupport_introspection_c.h"
// already included above
// #include "modularized_bhv_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "modularized_bhv_msgs/srv/detail/move_request__functions.h"
// already included above
// #include "modularized_bhv_msgs/srv/detail/move_request__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void modularized_bhv_msgs__srv__MoveRequest_Response__rosidl_typesupport_introspection_c__MoveRequest_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  modularized_bhv_msgs__srv__MoveRequest_Response__init(message_memory);
}

void modularized_bhv_msgs__srv__MoveRequest_Response__rosidl_typesupport_introspection_c__MoveRequest_Response_fini_function(void * message_memory)
{
  modularized_bhv_msgs__srv__MoveRequest_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember modularized_bhv_msgs__srv__MoveRequest_Response__rosidl_typesupport_introspection_c__MoveRequest_Response_message_member_array[1] = {
  {
    "success",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__srv__MoveRequest_Response, success),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers modularized_bhv_msgs__srv__MoveRequest_Response__rosidl_typesupport_introspection_c__MoveRequest_Response_message_members = {
  "modularized_bhv_msgs__srv",  // message namespace
  "MoveRequest_Response",  // message name
  1,  // number of fields
  sizeof(modularized_bhv_msgs__srv__MoveRequest_Response),
  modularized_bhv_msgs__srv__MoveRequest_Response__rosidl_typesupport_introspection_c__MoveRequest_Response_message_member_array,  // message members
  modularized_bhv_msgs__srv__MoveRequest_Response__rosidl_typesupport_introspection_c__MoveRequest_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  modularized_bhv_msgs__srv__MoveRequest_Response__rosidl_typesupport_introspection_c__MoveRequest_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t modularized_bhv_msgs__srv__MoveRequest_Response__rosidl_typesupport_introspection_c__MoveRequest_Response_message_type_support_handle = {
  0,
  &modularized_bhv_msgs__srv__MoveRequest_Response__rosidl_typesupport_introspection_c__MoveRequest_Response_message_members,
  get_message_typesupport_handle_function,
  &modularized_bhv_msgs__srv__MoveRequest_Response__get_type_hash,
  &modularized_bhv_msgs__srv__MoveRequest_Response__get_type_description,
  &modularized_bhv_msgs__srv__MoveRequest_Response__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_modularized_bhv_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, modularized_bhv_msgs, srv, MoveRequest_Response)() {
  if (!modularized_bhv_msgs__srv__MoveRequest_Response__rosidl_typesupport_introspection_c__MoveRequest_Response_message_type_support_handle.typesupport_identifier) {
    modularized_bhv_msgs__srv__MoveRequest_Response__rosidl_typesupport_introspection_c__MoveRequest_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &modularized_bhv_msgs__srv__MoveRequest_Response__rosidl_typesupport_introspection_c__MoveRequest_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "modularized_bhv_msgs/srv/detail/move_request__rosidl_typesupport_introspection_c.h"
// already included above
// #include "modularized_bhv_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "modularized_bhv_msgs/srv/detail/move_request__functions.h"
// already included above
// #include "modularized_bhv_msgs/srv/detail/move_request__struct.h"


// Include directives for member types
// Member `info`
#include "service_msgs/msg/service_event_info.h"
// Member `info`
#include "service_msgs/msg/detail/service_event_info__rosidl_typesupport_introspection_c.h"
// Member `request`
// Member `response`
#include "modularized_bhv_msgs/srv/move_request.h"
// Member `request`
// Member `response`
// already included above
// #include "modularized_bhv_msgs/srv/detail/move_request__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__MoveRequest_Event_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  modularized_bhv_msgs__srv__MoveRequest_Event__init(message_memory);
}

void modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__MoveRequest_Event_fini_function(void * message_memory)
{
  modularized_bhv_msgs__srv__MoveRequest_Event__fini(message_memory);
}

size_t modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__size_function__MoveRequest_Event__request(
  const void * untyped_member)
{
  const modularized_bhv_msgs__srv__MoveRequest_Request__Sequence * member =
    (const modularized_bhv_msgs__srv__MoveRequest_Request__Sequence *)(untyped_member);
  return member->size;
}

const void * modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__get_const_function__MoveRequest_Event__request(
  const void * untyped_member, size_t index)
{
  const modularized_bhv_msgs__srv__MoveRequest_Request__Sequence * member =
    (const modularized_bhv_msgs__srv__MoveRequest_Request__Sequence *)(untyped_member);
  return &member->data[index];
}

void * modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__get_function__MoveRequest_Event__request(
  void * untyped_member, size_t index)
{
  modularized_bhv_msgs__srv__MoveRequest_Request__Sequence * member =
    (modularized_bhv_msgs__srv__MoveRequest_Request__Sequence *)(untyped_member);
  return &member->data[index];
}

void modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__fetch_function__MoveRequest_Event__request(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const modularized_bhv_msgs__srv__MoveRequest_Request * item =
    ((const modularized_bhv_msgs__srv__MoveRequest_Request *)
    modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__get_const_function__MoveRequest_Event__request(untyped_member, index));
  modularized_bhv_msgs__srv__MoveRequest_Request * value =
    (modularized_bhv_msgs__srv__MoveRequest_Request *)(untyped_value);
  *value = *item;
}

void modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__assign_function__MoveRequest_Event__request(
  void * untyped_member, size_t index, const void * untyped_value)
{
  modularized_bhv_msgs__srv__MoveRequest_Request * item =
    ((modularized_bhv_msgs__srv__MoveRequest_Request *)
    modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__get_function__MoveRequest_Event__request(untyped_member, index));
  const modularized_bhv_msgs__srv__MoveRequest_Request * value =
    (const modularized_bhv_msgs__srv__MoveRequest_Request *)(untyped_value);
  *item = *value;
}

bool modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__resize_function__MoveRequest_Event__request(
  void * untyped_member, size_t size)
{
  modularized_bhv_msgs__srv__MoveRequest_Request__Sequence * member =
    (modularized_bhv_msgs__srv__MoveRequest_Request__Sequence *)(untyped_member);
  modularized_bhv_msgs__srv__MoveRequest_Request__Sequence__fini(member);
  return modularized_bhv_msgs__srv__MoveRequest_Request__Sequence__init(member, size);
}

size_t modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__size_function__MoveRequest_Event__response(
  const void * untyped_member)
{
  const modularized_bhv_msgs__srv__MoveRequest_Response__Sequence * member =
    (const modularized_bhv_msgs__srv__MoveRequest_Response__Sequence *)(untyped_member);
  return member->size;
}

const void * modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__get_const_function__MoveRequest_Event__response(
  const void * untyped_member, size_t index)
{
  const modularized_bhv_msgs__srv__MoveRequest_Response__Sequence * member =
    (const modularized_bhv_msgs__srv__MoveRequest_Response__Sequence *)(untyped_member);
  return &member->data[index];
}

void * modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__get_function__MoveRequest_Event__response(
  void * untyped_member, size_t index)
{
  modularized_bhv_msgs__srv__MoveRequest_Response__Sequence * member =
    (modularized_bhv_msgs__srv__MoveRequest_Response__Sequence *)(untyped_member);
  return &member->data[index];
}

void modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__fetch_function__MoveRequest_Event__response(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const modularized_bhv_msgs__srv__MoveRequest_Response * item =
    ((const modularized_bhv_msgs__srv__MoveRequest_Response *)
    modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__get_const_function__MoveRequest_Event__response(untyped_member, index));
  modularized_bhv_msgs__srv__MoveRequest_Response * value =
    (modularized_bhv_msgs__srv__MoveRequest_Response *)(untyped_value);
  *value = *item;
}

void modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__assign_function__MoveRequest_Event__response(
  void * untyped_member, size_t index, const void * untyped_value)
{
  modularized_bhv_msgs__srv__MoveRequest_Response * item =
    ((modularized_bhv_msgs__srv__MoveRequest_Response *)
    modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__get_function__MoveRequest_Event__response(untyped_member, index));
  const modularized_bhv_msgs__srv__MoveRequest_Response * value =
    (const modularized_bhv_msgs__srv__MoveRequest_Response *)(untyped_value);
  *item = *value;
}

bool modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__resize_function__MoveRequest_Event__response(
  void * untyped_member, size_t size)
{
  modularized_bhv_msgs__srv__MoveRequest_Response__Sequence * member =
    (modularized_bhv_msgs__srv__MoveRequest_Response__Sequence *)(untyped_member);
  modularized_bhv_msgs__srv__MoveRequest_Response__Sequence__fini(member);
  return modularized_bhv_msgs__srv__MoveRequest_Response__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__MoveRequest_Event_message_member_array[3] = {
  {
    "info",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__srv__MoveRequest_Event, info),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "request",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(modularized_bhv_msgs__srv__MoveRequest_Event, request),  // bytes offset in struct
    NULL,  // default value
    modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__size_function__MoveRequest_Event__request,  // size() function pointer
    modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__get_const_function__MoveRequest_Event__request,  // get_const(index) function pointer
    modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__get_function__MoveRequest_Event__request,  // get(index) function pointer
    modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__fetch_function__MoveRequest_Event__request,  // fetch(index, &value) function pointer
    modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__assign_function__MoveRequest_Event__request,  // assign(index, value) function pointer
    modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__resize_function__MoveRequest_Event__request  // resize(index) function pointer
  },
  {
    "response",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(modularized_bhv_msgs__srv__MoveRequest_Event, response),  // bytes offset in struct
    NULL,  // default value
    modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__size_function__MoveRequest_Event__response,  // size() function pointer
    modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__get_const_function__MoveRequest_Event__response,  // get_const(index) function pointer
    modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__get_function__MoveRequest_Event__response,  // get(index) function pointer
    modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__fetch_function__MoveRequest_Event__response,  // fetch(index, &value) function pointer
    modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__assign_function__MoveRequest_Event__response,  // assign(index, value) function pointer
    modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__resize_function__MoveRequest_Event__response  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__MoveRequest_Event_message_members = {
  "modularized_bhv_msgs__srv",  // message namespace
  "MoveRequest_Event",  // message name
  3,  // number of fields
  sizeof(modularized_bhv_msgs__srv__MoveRequest_Event),
  modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__MoveRequest_Event_message_member_array,  // message members
  modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__MoveRequest_Event_init_function,  // function to initialize message memory (memory has to be allocated)
  modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__MoveRequest_Event_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__MoveRequest_Event_message_type_support_handle = {
  0,
  &modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__MoveRequest_Event_message_members,
  get_message_typesupport_handle_function,
  &modularized_bhv_msgs__srv__MoveRequest_Event__get_type_hash,
  &modularized_bhv_msgs__srv__MoveRequest_Event__get_type_description,
  &modularized_bhv_msgs__srv__MoveRequest_Event__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_modularized_bhv_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, modularized_bhv_msgs, srv, MoveRequest_Event)() {
  modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__MoveRequest_Event_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_msgs, msg, ServiceEventInfo)();
  modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__MoveRequest_Event_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, modularized_bhv_msgs, srv, MoveRequest_Request)();
  modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__MoveRequest_Event_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, modularized_bhv_msgs, srv, MoveRequest_Response)();
  if (!modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__MoveRequest_Event_message_type_support_handle.typesupport_identifier) {
    modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__MoveRequest_Event_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__MoveRequest_Event_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "modularized_bhv_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "modularized_bhv_msgs/srv/detail/move_request__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers modularized_bhv_msgs__srv__detail__move_request__rosidl_typesupport_introspection_c__MoveRequest_service_members = {
  "modularized_bhv_msgs__srv",  // service namespace
  "MoveRequest",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // modularized_bhv_msgs__srv__detail__move_request__rosidl_typesupport_introspection_c__MoveRequest_Request_message_type_support_handle,
  NULL,  // response message
  // modularized_bhv_msgs__srv__detail__move_request__rosidl_typesupport_introspection_c__MoveRequest_Response_message_type_support_handle
  NULL  // event_message
  // modularized_bhv_msgs__srv__detail__move_request__rosidl_typesupport_introspection_c__MoveRequest_Response_message_type_support_handle
};


static rosidl_service_type_support_t modularized_bhv_msgs__srv__detail__move_request__rosidl_typesupport_introspection_c__MoveRequest_service_type_support_handle = {
  0,
  &modularized_bhv_msgs__srv__detail__move_request__rosidl_typesupport_introspection_c__MoveRequest_service_members,
  get_service_typesupport_handle_function,
  &modularized_bhv_msgs__srv__MoveRequest_Request__rosidl_typesupport_introspection_c__MoveRequest_Request_message_type_support_handle,
  &modularized_bhv_msgs__srv__MoveRequest_Response__rosidl_typesupport_introspection_c__MoveRequest_Response_message_type_support_handle,
  &modularized_bhv_msgs__srv__MoveRequest_Event__rosidl_typesupport_introspection_c__MoveRequest_Event_message_type_support_handle,
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_CREATE_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    modularized_bhv_msgs,
    srv,
    MoveRequest
  ),
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_DESTROY_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    modularized_bhv_msgs,
    srv,
    MoveRequest
  ),
  &modularized_bhv_msgs__srv__MoveRequest__get_type_hash,
  &modularized_bhv_msgs__srv__MoveRequest__get_type_description,
  &modularized_bhv_msgs__srv__MoveRequest__get_type_description_sources,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, modularized_bhv_msgs, srv, MoveRequest_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, modularized_bhv_msgs, srv, MoveRequest_Response)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, modularized_bhv_msgs, srv, MoveRequest_Event)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_modularized_bhv_msgs
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, modularized_bhv_msgs, srv, MoveRequest)() {
  if (!modularized_bhv_msgs__srv__detail__move_request__rosidl_typesupport_introspection_c__MoveRequest_service_type_support_handle.typesupport_identifier) {
    modularized_bhv_msgs__srv__detail__move_request__rosidl_typesupport_introspection_c__MoveRequest_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)modularized_bhv_msgs__srv__detail__move_request__rosidl_typesupport_introspection_c__MoveRequest_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, modularized_bhv_msgs, srv, MoveRequest_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, modularized_bhv_msgs, srv, MoveRequest_Response)()->data;
  }
  if (!service_members->event_members_) {
    service_members->event_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, modularized_bhv_msgs, srv, MoveRequest_Event)()->data;
  }

  return &modularized_bhv_msgs__srv__detail__move_request__rosidl_typesupport_introspection_c__MoveRequest_service_type_support_handle;
}
