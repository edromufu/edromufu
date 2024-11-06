// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from potmessage:msg/Buttonmsg.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "potmessage/msg/detail/buttonmsg__rosidl_typesupport_introspection_c.h"
#include "potmessage/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "potmessage/msg/detail/buttonmsg__functions.h"
#include "potmessage/msg/detail/buttonmsg__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void potmessage__msg__Buttonmsg__rosidl_typesupport_introspection_c__Buttonmsg_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  potmessage__msg__Buttonmsg__init(message_memory);
}

void potmessage__msg__Buttonmsg__rosidl_typesupport_introspection_c__Buttonmsg_fini_function(void * message_memory)
{
  potmessage__msg__Buttonmsg__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember potmessage__msg__Buttonmsg__rosidl_typesupport_introspection_c__Buttonmsg_message_member_array[2] = {
  {
    "bot1",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(potmessage__msg__Buttonmsg, bot1),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "bot2",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(potmessage__msg__Buttonmsg, bot2),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers potmessage__msg__Buttonmsg__rosidl_typesupport_introspection_c__Buttonmsg_message_members = {
  "potmessage__msg",  // message namespace
  "Buttonmsg",  // message name
  2,  // number of fields
  sizeof(potmessage__msg__Buttonmsg),
  potmessage__msg__Buttonmsg__rosidl_typesupport_introspection_c__Buttonmsg_message_member_array,  // message members
  potmessage__msg__Buttonmsg__rosidl_typesupport_introspection_c__Buttonmsg_init_function,  // function to initialize message memory (memory has to be allocated)
  potmessage__msg__Buttonmsg__rosidl_typesupport_introspection_c__Buttonmsg_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t potmessage__msg__Buttonmsg__rosidl_typesupport_introspection_c__Buttonmsg_message_type_support_handle = {
  0,
  &potmessage__msg__Buttonmsg__rosidl_typesupport_introspection_c__Buttonmsg_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_potmessage
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, potmessage, msg, Buttonmsg)() {
  if (!potmessage__msg__Buttonmsg__rosidl_typesupport_introspection_c__Buttonmsg_message_type_support_handle.typesupport_identifier) {
    potmessage__msg__Buttonmsg__rosidl_typesupport_introspection_c__Buttonmsg_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &potmessage__msg__Buttonmsg__rosidl_typesupport_introspection_c__Buttonmsg_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
