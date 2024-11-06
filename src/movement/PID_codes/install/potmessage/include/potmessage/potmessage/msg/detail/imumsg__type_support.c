// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from potmessage:msg/Imumsg.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "potmessage/msg/detail/imumsg__rosidl_typesupport_introspection_c.h"
#include "potmessage/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "potmessage/msg/detail/imumsg__functions.h"
#include "potmessage/msg/detail/imumsg__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__Imumsg_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  potmessage__msg__Imumsg__init(message_memory);
}

void potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__Imumsg_fini_function(void * message_memory)
{
  potmessage__msg__Imumsg__fini(message_memory);
}

size_t potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__size_function__Imumsg__imu(
  const void * untyped_member)
{
  (void)untyped_member;
  return 4;
}

const void * potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__get_const_function__Imumsg__imu(
  const void * untyped_member, size_t index)
{
  const float * member =
    (const float *)(untyped_member);
  return &member[index];
}

void * potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__get_function__Imumsg__imu(
  void * untyped_member, size_t index)
{
  float * member =
    (float *)(untyped_member);
  return &member[index];
}

void potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__fetch_function__Imumsg__imu(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__get_const_function__Imumsg__imu(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__assign_function__Imumsg__imu(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__get_function__Imumsg__imu(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

static rosidl_typesupport_introspection_c__MessageMember potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__Imumsg_message_member_array[1] = {
  {
    "imu",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    4,  // array size
    false,  // is upper bound
    offsetof(potmessage__msg__Imumsg, imu),  // bytes offset in struct
    NULL,  // default value
    potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__size_function__Imumsg__imu,  // size() function pointer
    potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__get_const_function__Imumsg__imu,  // get_const(index) function pointer
    potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__get_function__Imumsg__imu,  // get(index) function pointer
    potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__fetch_function__Imumsg__imu,  // fetch(index, &value) function pointer
    potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__assign_function__Imumsg__imu,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__Imumsg_message_members = {
  "potmessage__msg",  // message namespace
  "Imumsg",  // message name
  1,  // number of fields
  sizeof(potmessage__msg__Imumsg),
  potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__Imumsg_message_member_array,  // message members
  potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__Imumsg_init_function,  // function to initialize message memory (memory has to be allocated)
  potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__Imumsg_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__Imumsg_message_type_support_handle = {
  0,
  &potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__Imumsg_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_potmessage
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, potmessage, msg, Imumsg)() {
  if (!potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__Imumsg_message_type_support_handle.typesupport_identifier) {
    potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__Imumsg_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &potmessage__msg__Imumsg__rosidl_typesupport_introspection_c__Imumsg_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
