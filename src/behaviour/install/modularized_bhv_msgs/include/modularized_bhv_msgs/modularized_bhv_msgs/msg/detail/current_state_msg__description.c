// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from modularized_bhv_msgs:msg/CurrentStateMsg.idl
// generated code does not contain a copyright notice

#include "modularized_bhv_msgs/msg/detail/current_state_msg__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
const rosidl_type_hash_t *
modularized_bhv_msgs__msg__CurrentStateMsg__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xca, 0xde, 0xa3, 0x51, 0x9a, 0xf9, 0xc5, 0x92,
      0xdc, 0x3a, 0xb0, 0xdd, 0x69, 0x92, 0x38, 0x7f,
      0x6f, 0x55, 0x9b, 0xfe, 0x2e, 0xb3, 0xb1, 0x4d,
      0x23, 0x56, 0x73, 0x94, 0xa0, 0x37, 0xf0, 0x8e,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char modularized_bhv_msgs__msg__CurrentStateMsg__TYPE_NAME[] = "modularized_bhv_msgs/msg/CurrentStateMsg";

// Define type names, field names, and default values
static char modularized_bhv_msgs__msg__CurrentStateMsg__FIELD_NAME__current_state[] = "current_state";

static rosidl_runtime_c__type_description__Field modularized_bhv_msgs__msg__CurrentStateMsg__FIELDS[] = {
  {
    {modularized_bhv_msgs__msg__CurrentStateMsg__FIELD_NAME__current_state, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
modularized_bhv_msgs__msg__CurrentStateMsg__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {modularized_bhv_msgs__msg__CurrentStateMsg__TYPE_NAME, 40, 40},
      {modularized_bhv_msgs__msg__CurrentStateMsg__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "string current_state";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
modularized_bhv_msgs__msg__CurrentStateMsg__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {modularized_bhv_msgs__msg__CurrentStateMsg__TYPE_NAME, 40, 40},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 21, 21},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
modularized_bhv_msgs__msg__CurrentStateMsg__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *modularized_bhv_msgs__msg__CurrentStateMsg__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
