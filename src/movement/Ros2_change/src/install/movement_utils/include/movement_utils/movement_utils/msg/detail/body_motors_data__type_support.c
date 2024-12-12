// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from movement_utils:msg/BodyMotorsData.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "movement_utils/msg/detail/body_motors_data__rosidl_typesupport_introspection_c.h"
#include "movement_utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "movement_utils/msg/detail/body_motors_data__functions.h"
#include "movement_utils/msg/detail/body_motors_data__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__BodyMotorsData_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  movement_utils__msg__BodyMotorsData__init(message_memory);
}

void movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__BodyMotorsData_fini_function(void * message_memory)
{
  movement_utils__msg__BodyMotorsData__fini(message_memory);
}

size_t movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__size_function__BodyMotorsData__pos_vector(
  const void * untyped_member)
{
  (void)untyped_member;
  return 18;
}

const void * movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__get_const_function__BodyMotorsData__pos_vector(
  const void * untyped_member, size_t index)
{
  const float * member =
    (const float *)(untyped_member);
  return &member[index];
}

void * movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__get_function__BodyMotorsData__pos_vector(
  void * untyped_member, size_t index)
{
  float * member =
    (float *)(untyped_member);
  return &member[index];
}

void movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__fetch_function__BodyMotorsData__pos_vector(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__get_const_function__BodyMotorsData__pos_vector(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__assign_function__BodyMotorsData__pos_vector(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__get_function__BodyMotorsData__pos_vector(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

static rosidl_typesupport_introspection_c__MessageMember movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__BodyMotorsData_message_member_array[1] = {
  {
    "pos_vector",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    18,  // array size
    false,  // is upper bound
    offsetof(movement_utils__msg__BodyMotorsData, pos_vector),  // bytes offset in struct
    NULL,  // default value
    movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__size_function__BodyMotorsData__pos_vector,  // size() function pointer
    movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__get_const_function__BodyMotorsData__pos_vector,  // get_const(index) function pointer
    movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__get_function__BodyMotorsData__pos_vector,  // get(index) function pointer
    movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__fetch_function__BodyMotorsData__pos_vector,  // fetch(index, &value) function pointer
    movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__assign_function__BodyMotorsData__pos_vector,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__BodyMotorsData_message_members = {
  "movement_utils__msg",  // message namespace
  "BodyMotorsData",  // message name
  1,  // number of fields
  sizeof(movement_utils__msg__BodyMotorsData),
  movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__BodyMotorsData_message_member_array,  // message members
  movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__BodyMotorsData_init_function,  // function to initialize message memory (memory has to be allocated)
  movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__BodyMotorsData_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__BodyMotorsData_message_type_support_handle = {
  0,
  &movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__BodyMotorsData_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_movement_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, movement_utils, msg, BodyMotorsData)() {
  if (!movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__BodyMotorsData_message_type_support_handle.typesupport_identifier) {
    movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__BodyMotorsData_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &movement_utils__msg__BodyMotorsData__rosidl_typesupport_introspection_c__BodyMotorsData_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
