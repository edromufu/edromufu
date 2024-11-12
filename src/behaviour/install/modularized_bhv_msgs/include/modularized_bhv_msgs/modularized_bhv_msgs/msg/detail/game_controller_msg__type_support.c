// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from modularized_bhv_msgs:msg/GameControllerMsg.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "modularized_bhv_msgs/msg/detail/game_controller_msg__rosidl_typesupport_introspection_c.h"
#include "modularized_bhv_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "modularized_bhv_msgs/msg/detail/game_controller_msg__functions.h"
#include "modularized_bhv_msgs/msg/detail/game_controller_msg__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `coach_message`
#include "rosidl_runtime_c/string_functions.h"
// Member `team_mates_with_penalty`
// Member `team_mates_with_red_card`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__GameControllerMsg_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  modularized_bhv_msgs__msg__GameControllerMsg__init(message_memory);
}

void modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__GameControllerMsg_fini_function(void * message_memory)
{
  modularized_bhv_msgs__msg__GameControllerMsg__fini(message_memory);
}

size_t modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__size_function__GameControllerMsg__team_mates_with_penalty(
  const void * untyped_member)
{
  const rosidl_runtime_c__boolean__Sequence * member =
    (const rosidl_runtime_c__boolean__Sequence *)(untyped_member);
  return member->size;
}

const void * modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__get_const_function__GameControllerMsg__team_mates_with_penalty(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__boolean__Sequence * member =
    (const rosidl_runtime_c__boolean__Sequence *)(untyped_member);
  return &member->data[index];
}

void * modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__get_function__GameControllerMsg__team_mates_with_penalty(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__boolean__Sequence * member =
    (rosidl_runtime_c__boolean__Sequence *)(untyped_member);
  return &member->data[index];
}

void modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__fetch_function__GameControllerMsg__team_mates_with_penalty(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const bool * item =
    ((const bool *)
    modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__get_const_function__GameControllerMsg__team_mates_with_penalty(untyped_member, index));
  bool * value =
    (bool *)(untyped_value);
  *value = *item;
}

void modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__assign_function__GameControllerMsg__team_mates_with_penalty(
  void * untyped_member, size_t index, const void * untyped_value)
{
  bool * item =
    ((bool *)
    modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__get_function__GameControllerMsg__team_mates_with_penalty(untyped_member, index));
  const bool * value =
    (const bool *)(untyped_value);
  *item = *value;
}

bool modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__resize_function__GameControllerMsg__team_mates_with_penalty(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__boolean__Sequence * member =
    (rosidl_runtime_c__boolean__Sequence *)(untyped_member);
  rosidl_runtime_c__boolean__Sequence__fini(member);
  return rosidl_runtime_c__boolean__Sequence__init(member, size);
}

size_t modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__size_function__GameControllerMsg__team_mates_with_red_card(
  const void * untyped_member)
{
  const rosidl_runtime_c__boolean__Sequence * member =
    (const rosidl_runtime_c__boolean__Sequence *)(untyped_member);
  return member->size;
}

const void * modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__get_const_function__GameControllerMsg__team_mates_with_red_card(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__boolean__Sequence * member =
    (const rosidl_runtime_c__boolean__Sequence *)(untyped_member);
  return &member->data[index];
}

void * modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__get_function__GameControllerMsg__team_mates_with_red_card(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__boolean__Sequence * member =
    (rosidl_runtime_c__boolean__Sequence *)(untyped_member);
  return &member->data[index];
}

void modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__fetch_function__GameControllerMsg__team_mates_with_red_card(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const bool * item =
    ((const bool *)
    modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__get_const_function__GameControllerMsg__team_mates_with_red_card(untyped_member, index));
  bool * value =
    (bool *)(untyped_value);
  *value = *item;
}

void modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__assign_function__GameControllerMsg__team_mates_with_red_card(
  void * untyped_member, size_t index, const void * untyped_value)
{
  bool * item =
    ((bool *)
    modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__get_function__GameControllerMsg__team_mates_with_red_card(untyped_member, index));
  const bool * value =
    (const bool *)(untyped_value);
  *item = *value;
}

bool modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__resize_function__GameControllerMsg__team_mates_with_red_card(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__boolean__Sequence * member =
    (rosidl_runtime_c__boolean__Sequence *)(untyped_member);
  rosidl_runtime_c__boolean__Sequence__fini(member);
  return rosidl_runtime_c__boolean__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__GameControllerMsg_message_member_array[21] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "game_state",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, game_state),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "secondary_state",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, secondary_state),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "secondary_state_team",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, secondary_state_team),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "secondary_state_mode",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, secondary_state_mode),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "first_half",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, first_half),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "own_score",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, own_score),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "rival_score",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, rival_score),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "seconds_remaining",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, seconds_remaining),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "secondary_seconds_remaining",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, secondary_seconds_remaining),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "has_kick_off",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, has_kick_off),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "penalized",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, penalized),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "seconds_till_unpenalized",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, seconds_till_unpenalized),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "team_color",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, team_color),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "drop_in_team",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, drop_in_team),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "drop_in_time",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, drop_in_time),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "penalty_shot",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, penalty_shot),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "single_shots",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, single_shots),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "coach_message",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, coach_message),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "team_mates_with_penalty",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, team_mates_with_penalty),  // bytes offset in struct
    NULL,  // default value
    modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__size_function__GameControllerMsg__team_mates_with_penalty,  // size() function pointer
    modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__get_const_function__GameControllerMsg__team_mates_with_penalty,  // get_const(index) function pointer
    modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__get_function__GameControllerMsg__team_mates_with_penalty,  // get(index) function pointer
    modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__fetch_function__GameControllerMsg__team_mates_with_penalty,  // fetch(index, &value) function pointer
    modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__assign_function__GameControllerMsg__team_mates_with_penalty,  // assign(index, value) function pointer
    modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__resize_function__GameControllerMsg__team_mates_with_penalty  // resize(index) function pointer
  },
  {
    "team_mates_with_red_card",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(modularized_bhv_msgs__msg__GameControllerMsg, team_mates_with_red_card),  // bytes offset in struct
    NULL,  // default value
    modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__size_function__GameControllerMsg__team_mates_with_red_card,  // size() function pointer
    modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__get_const_function__GameControllerMsg__team_mates_with_red_card,  // get_const(index) function pointer
    modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__get_function__GameControllerMsg__team_mates_with_red_card,  // get(index) function pointer
    modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__fetch_function__GameControllerMsg__team_mates_with_red_card,  // fetch(index, &value) function pointer
    modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__assign_function__GameControllerMsg__team_mates_with_red_card,  // assign(index, value) function pointer
    modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__resize_function__GameControllerMsg__team_mates_with_red_card  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__GameControllerMsg_message_members = {
  "modularized_bhv_msgs__msg",  // message namespace
  "GameControllerMsg",  // message name
  21,  // number of fields
  sizeof(modularized_bhv_msgs__msg__GameControllerMsg),
  modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__GameControllerMsg_message_member_array,  // message members
  modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__GameControllerMsg_init_function,  // function to initialize message memory (memory has to be allocated)
  modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__GameControllerMsg_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__GameControllerMsg_message_type_support_handle = {
  0,
  &modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__GameControllerMsg_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_modularized_bhv_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, modularized_bhv_msgs, msg, GameControllerMsg)() {
  modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__GameControllerMsg_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  if (!modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__GameControllerMsg_message_type_support_handle.typesupport_identifier) {
    modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__GameControllerMsg_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &modularized_bhv_msgs__msg__GameControllerMsg__rosidl_typesupport_introspection_c__GameControllerMsg_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
