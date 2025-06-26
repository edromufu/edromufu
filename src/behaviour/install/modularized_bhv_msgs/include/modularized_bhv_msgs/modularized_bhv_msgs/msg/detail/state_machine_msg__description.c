// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from modularized_bhv_msgs:msg/StateMachineMsg.idl
// generated code does not contain a copyright notice

#include "modularized_bhv_msgs/msg/detail/state_machine_msg__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
const rosidl_type_hash_t *
modularized_bhv_msgs__msg__StateMachineMsg__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x76, 0x0b, 0xb9, 0x5a, 0xd6, 0x4f, 0x7f, 0x16,
      0x53, 0x5d, 0xb3, 0x2d, 0x27, 0x15, 0xc0, 0xa9,
      0xb5, 0x5b, 0x6f, 0x45, 0x05, 0x0f, 0x6f, 0x93,
      0xf5, 0xbd, 0xad, 0xb1, 0x27, 0x5b, 0x03, 0xf8,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char modularized_bhv_msgs__msg__StateMachineMsg__TYPE_NAME[] = "modularized_bhv_msgs/msg/StateMachineMsg";

// Define type names, field names, and default values
static char modularized_bhv_msgs__msg__StateMachineMsg__FIELD_NAME__ball_position[] = "ball_position";
static char modularized_bhv_msgs__msg__StateMachineMsg__FIELD_NAME__ball_close[] = "ball_close";
static char modularized_bhv_msgs__msg__StateMachineMsg__FIELD_NAME__ball_found[] = "ball_found";
static char modularized_bhv_msgs__msg__StateMachineMsg__FIELD_NAME__fall_state[] = "fall_state";
static char modularized_bhv_msgs__msg__StateMachineMsg__FIELD_NAME__hor_motor_out_of_center[] = "hor_motor_out_of_center";
static char modularized_bhv_msgs__msg__StateMachineMsg__FIELD_NAME__head_kick_check[] = "head_kick_check";

static rosidl_runtime_c__type_description__Field modularized_bhv_msgs__msg__StateMachineMsg__FIELDS[] = {
  {
    {modularized_bhv_msgs__msg__StateMachineMsg__FIELD_NAME__ball_position, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {modularized_bhv_msgs__msg__StateMachineMsg__FIELD_NAME__ball_close, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {modularized_bhv_msgs__msg__StateMachineMsg__FIELD_NAME__ball_found, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {modularized_bhv_msgs__msg__StateMachineMsg__FIELD_NAME__fall_state, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {modularized_bhv_msgs__msg__StateMachineMsg__FIELD_NAME__hor_motor_out_of_center, 23, 23},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {modularized_bhv_msgs__msg__StateMachineMsg__FIELD_NAME__head_kick_check, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
modularized_bhv_msgs__msg__StateMachineMsg__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {modularized_bhv_msgs__msg__StateMachineMsg__TYPE_NAME, 40, 40},
      {modularized_bhv_msgs__msg__StateMachineMsg__FIELDS, 6, 6},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "string ball_position\n"
  "bool ball_close\n"
  "bool ball_found\n"
  "string fall_state\n"
  "string hor_motor_out_of_center\n"
  "bool head_kick_check";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
modularized_bhv_msgs__msg__StateMachineMsg__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {modularized_bhv_msgs__msg__StateMachineMsg__TYPE_NAME, 40, 40},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 123, 123},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
modularized_bhv_msgs__msg__StateMachineMsg__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *modularized_bhv_msgs__msg__StateMachineMsg__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
