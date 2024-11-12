// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from modularized_bhv_msgs:msg/CurrentStateMsg.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "modularized_bhv_msgs/msg/detail/current_state_msg__rosidl_typesupport_introspection_c.h"
#include "modularized_bhv_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "modularized_bhv_msgs/msg/detail/current_state_msg__functions.h"
#include "modularized_bhv_msgs/msg/detail/current_state_msg__struct.h"


// Include directives for member types
// Member `current_state`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void modularized_bhv_msgs__msg__CurrentStateMsg__rosidl_typesupport_introspection_c__CurrentStateMsg_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  modularized_bhv_msgs__msg__CurrentStateMsg__init(message_memory);
}

void modularized_bhv_msgs__msg__CurrentStateMsg__rosidl_typesupport_introspection_c__CurrentStateMsg_fini_function(void * message_memory)
{
  modularized_bhv_msgs__msg__CurrentStateMsg__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember modularized_bhv_msgs__msg__CurrentStateMsg__rosidl_typesupport_introspection_c__CurrentStateMsg_message_member_array[1] = {
  {
    "current_state",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__CurrentStateMsg, current_state),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers modularized_bhv_msgs__msg__CurrentStateMsg__rosidl_typesupport_introspection_c__CurrentStateMsg_message_members = {
  "modularized_bhv_msgs__msg",  // message namespace
  "CurrentStateMsg",  // message name
  1,  // number of fields
  sizeof(modularized_bhv_msgs__msg__CurrentStateMsg),
  modularized_bhv_msgs__msg__CurrentStateMsg__rosidl_typesupport_introspection_c__CurrentStateMsg_message_member_array,  // message members
  modularized_bhv_msgs__msg__CurrentStateMsg__rosidl_typesupport_introspection_c__CurrentStateMsg_init_function,  // function to initialize message memory (memory has to be allocated)
  modularized_bhv_msgs__msg__CurrentStateMsg__rosidl_typesupport_introspection_c__CurrentStateMsg_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t modularized_bhv_msgs__msg__CurrentStateMsg__rosidl_typesupport_introspection_c__CurrentStateMsg_message_type_support_handle = {
  0,
  &modularized_bhv_msgs__msg__CurrentStateMsg__rosidl_typesupport_introspection_c__CurrentStateMsg_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_modularized_bhv_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, modularized_bhv_msgs, msg, CurrentStateMsg)() {
  if (!modularized_bhv_msgs__msg__CurrentStateMsg__rosidl_typesupport_introspection_c__CurrentStateMsg_message_type_support_handle.typesupport_identifier) {
    modularized_bhv_msgs__msg__CurrentStateMsg__rosidl_typesupport_introspection_c__CurrentStateMsg_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &modularized_bhv_msgs__msg__CurrentStateMsg__rosidl_typesupport_introspection_c__CurrentStateMsg_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
