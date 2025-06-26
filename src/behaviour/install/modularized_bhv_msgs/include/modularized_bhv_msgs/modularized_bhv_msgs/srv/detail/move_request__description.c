// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from modularized_bhv_msgs:srv/MoveRequest.idl
// generated code does not contain a copyright notice

#include "modularized_bhv_msgs/srv/detail/move_request__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
const rosidl_type_hash_t *
modularized_bhv_msgs__srv__MoveRequest__get_type_hash(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xbc, 0x0c, 0x59, 0xa6, 0x1a, 0x6a, 0x43, 0x14,
      0x24, 0xb9, 0xf1, 0xca, 0x09, 0x94, 0x7b, 0xe6,
      0x1b, 0xc3, 0x97, 0xd8, 0x6c, 0x96, 0x9c, 0xf9,
      0x0f, 0x3b, 0x30, 0x9b, 0x91, 0xad, 0xa7, 0x97,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
const rosidl_type_hash_t *
modularized_bhv_msgs__srv__MoveRequest_Request__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x7d, 0x42, 0x4b, 0xa4, 0xb3, 0x63, 0x4f, 0xab,
      0x8a, 0x26, 0x03, 0x9b, 0x78, 0xed, 0x4f, 0x96,
      0x3f, 0x34, 0x4e, 0xe1, 0x80, 0x78, 0xe0, 0x59,
      0x75, 0x2e, 0x17, 0x0e, 0x73, 0x33, 0xb8, 0xf1,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
const rosidl_type_hash_t *
modularized_bhv_msgs__srv__MoveRequest_Response__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x25, 0xc1, 0xb9, 0x35, 0x30, 0x01, 0xa7, 0xe0,
      0x6d, 0xab, 0xfd, 0x71, 0x59, 0x0b, 0xde, 0xd8,
      0x04, 0x64, 0xcb, 0x58, 0xb2, 0xdc, 0xc3, 0x92,
      0x71, 0x39, 0xb9, 0xfd, 0xce, 0xa5, 0x4a, 0xac,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
const rosidl_type_hash_t *
modularized_bhv_msgs__srv__MoveRequest_Event__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xa4, 0x8b, 0x37, 0x30, 0x7e, 0x10, 0x5d, 0x9a,
      0xbc, 0x61, 0x0f, 0xa8, 0xa2, 0xe4, 0xed, 0x71,
      0x32, 0x8d, 0x75, 0xd1, 0x96, 0x83, 0xa7, 0x88,
      0x37, 0xeb, 0xd8, 0x55, 0x72, 0xfc, 0x66, 0x5d,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "service_msgs/msg/detail/service_event_info__functions.h"
#include "builtin_interfaces/msg/detail/time__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
static const rosidl_type_hash_t service_msgs__msg__ServiceEventInfo__EXPECTED_HASH = {1, {
    0x41, 0xbc, 0xbb, 0xe0, 0x7a, 0x75, 0xc9, 0xb5,
    0x2b, 0xc9, 0x6b, 0xfd, 0x5c, 0x24, 0xd7, 0xf0,
    0xfc, 0x0a, 0x08, 0xc0, 0xcb, 0x79, 0x21, 0xb3,
    0x37, 0x3c, 0x57, 0x32, 0x34, 0x5a, 0x6f, 0x45,
  }};
#endif

static char modularized_bhv_msgs__srv__MoveRequest__TYPE_NAME[] = "modularized_bhv_msgs/srv/MoveRequest";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char modularized_bhv_msgs__srv__MoveRequest_Event__TYPE_NAME[] = "modularized_bhv_msgs/srv/MoveRequest_Event";
static char modularized_bhv_msgs__srv__MoveRequest_Request__TYPE_NAME[] = "modularized_bhv_msgs/srv/MoveRequest_Request";
static char modularized_bhv_msgs__srv__MoveRequest_Response__TYPE_NAME[] = "modularized_bhv_msgs/srv/MoveRequest_Response";
static char service_msgs__msg__ServiceEventInfo__TYPE_NAME[] = "service_msgs/msg/ServiceEventInfo";

// Define type names, field names, and default values
static char modularized_bhv_msgs__srv__MoveRequest__FIELD_NAME__request_message[] = "request_message";
static char modularized_bhv_msgs__srv__MoveRequest__FIELD_NAME__response_message[] = "response_message";
static char modularized_bhv_msgs__srv__MoveRequest__FIELD_NAME__event_message[] = "event_message";

static rosidl_runtime_c__type_description__Field modularized_bhv_msgs__srv__MoveRequest__FIELDS[] = {
  {
    {modularized_bhv_msgs__srv__MoveRequest__FIELD_NAME__request_message, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {modularized_bhv_msgs__srv__MoveRequest_Request__TYPE_NAME, 44, 44},
    },
    {NULL, 0, 0},
  },
  {
    {modularized_bhv_msgs__srv__MoveRequest__FIELD_NAME__response_message, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {modularized_bhv_msgs__srv__MoveRequest_Response__TYPE_NAME, 45, 45},
    },
    {NULL, 0, 0},
  },
  {
    {modularized_bhv_msgs__srv__MoveRequest__FIELD_NAME__event_message, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {modularized_bhv_msgs__srv__MoveRequest_Event__TYPE_NAME, 42, 42},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription modularized_bhv_msgs__srv__MoveRequest__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {modularized_bhv_msgs__srv__MoveRequest_Event__TYPE_NAME, 42, 42},
    {NULL, 0, 0},
  },
  {
    {modularized_bhv_msgs__srv__MoveRequest_Request__TYPE_NAME, 44, 44},
    {NULL, 0, 0},
  },
  {
    {modularized_bhv_msgs__srv__MoveRequest_Response__TYPE_NAME, 45, 45},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
modularized_bhv_msgs__srv__MoveRequest__get_type_description(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {modularized_bhv_msgs__srv__MoveRequest__TYPE_NAME, 36, 36},
      {modularized_bhv_msgs__srv__MoveRequest__FIELDS, 3, 3},
    },
    {modularized_bhv_msgs__srv__MoveRequest__REFERENCED_TYPE_DESCRIPTIONS, 5, 5},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[1].fields = modularized_bhv_msgs__srv__MoveRequest_Event__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = modularized_bhv_msgs__srv__MoveRequest_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[3].fields = modularized_bhv_msgs__srv__MoveRequest_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[4].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char modularized_bhv_msgs__srv__MoveRequest_Request__FIELD_NAME__move_request[] = "move_request";

static rosidl_runtime_c__type_description__Field modularized_bhv_msgs__srv__MoveRequest_Request__FIELDS[] = {
  {
    {modularized_bhv_msgs__srv__MoveRequest_Request__FIELD_NAME__move_request, 12, 12},
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
modularized_bhv_msgs__srv__MoveRequest_Request__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {modularized_bhv_msgs__srv__MoveRequest_Request__TYPE_NAME, 44, 44},
      {modularized_bhv_msgs__srv__MoveRequest_Request__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char modularized_bhv_msgs__srv__MoveRequest_Response__FIELD_NAME__success[] = "success";

static rosidl_runtime_c__type_description__Field modularized_bhv_msgs__srv__MoveRequest_Response__FIELDS[] = {
  {
    {modularized_bhv_msgs__srv__MoveRequest_Response__FIELD_NAME__success, 7, 7},
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
modularized_bhv_msgs__srv__MoveRequest_Response__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {modularized_bhv_msgs__srv__MoveRequest_Response__TYPE_NAME, 45, 45},
      {modularized_bhv_msgs__srv__MoveRequest_Response__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char modularized_bhv_msgs__srv__MoveRequest_Event__FIELD_NAME__info[] = "info";
static char modularized_bhv_msgs__srv__MoveRequest_Event__FIELD_NAME__request[] = "request";
static char modularized_bhv_msgs__srv__MoveRequest_Event__FIELD_NAME__response[] = "response";

static rosidl_runtime_c__type_description__Field modularized_bhv_msgs__srv__MoveRequest_Event__FIELDS[] = {
  {
    {modularized_bhv_msgs__srv__MoveRequest_Event__FIELD_NAME__info, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    },
    {NULL, 0, 0},
  },
  {
    {modularized_bhv_msgs__srv__MoveRequest_Event__FIELD_NAME__request, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {modularized_bhv_msgs__srv__MoveRequest_Request__TYPE_NAME, 44, 44},
    },
    {NULL, 0, 0},
  },
  {
    {modularized_bhv_msgs__srv__MoveRequest_Event__FIELD_NAME__response, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {modularized_bhv_msgs__srv__MoveRequest_Response__TYPE_NAME, 45, 45},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription modularized_bhv_msgs__srv__MoveRequest_Event__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {modularized_bhv_msgs__srv__MoveRequest_Request__TYPE_NAME, 44, 44},
    {NULL, 0, 0},
  },
  {
    {modularized_bhv_msgs__srv__MoveRequest_Response__TYPE_NAME, 45, 45},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
modularized_bhv_msgs__srv__MoveRequest_Event__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {modularized_bhv_msgs__srv__MoveRequest_Event__TYPE_NAME, 42, 42},
      {modularized_bhv_msgs__srv__MoveRequest_Event__FIELDS, 3, 3},
    },
    {modularized_bhv_msgs__srv__MoveRequest_Event__REFERENCED_TYPE_DESCRIPTIONS, 4, 4},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[1].fields = modularized_bhv_msgs__srv__MoveRequest_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = modularized_bhv_msgs__srv__MoveRequest_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[3].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "string move_request\n"
  "---\n"
  "bool success";

static char srv_encoding[] = "srv";
static char implicit_encoding[] = "implicit";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
modularized_bhv_msgs__srv__MoveRequest__get_individual_type_description_source(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {modularized_bhv_msgs__srv__MoveRequest__TYPE_NAME, 36, 36},
    {srv_encoding, 3, 3},
    {toplevel_type_raw_source, 37, 37},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
modularized_bhv_msgs__srv__MoveRequest_Request__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {modularized_bhv_msgs__srv__MoveRequest_Request__TYPE_NAME, 44, 44},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
modularized_bhv_msgs__srv__MoveRequest_Response__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {modularized_bhv_msgs__srv__MoveRequest_Response__TYPE_NAME, 45, 45},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
modularized_bhv_msgs__srv__MoveRequest_Event__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {modularized_bhv_msgs__srv__MoveRequest_Event__TYPE_NAME, 42, 42},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
modularized_bhv_msgs__srv__MoveRequest__get_type_description_sources(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[6];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 6, 6};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *modularized_bhv_msgs__srv__MoveRequest__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *modularized_bhv_msgs__srv__MoveRequest_Event__get_individual_type_description_source(NULL);
    sources[3] = *modularized_bhv_msgs__srv__MoveRequest_Request__get_individual_type_description_source(NULL);
    sources[4] = *modularized_bhv_msgs__srv__MoveRequest_Response__get_individual_type_description_source(NULL);
    sources[5] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
modularized_bhv_msgs__srv__MoveRequest_Request__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *modularized_bhv_msgs__srv__MoveRequest_Request__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
modularized_bhv_msgs__srv__MoveRequest_Response__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *modularized_bhv_msgs__srv__MoveRequest_Response__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
modularized_bhv_msgs__srv__MoveRequest_Event__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[5];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 5, 5};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *modularized_bhv_msgs__srv__MoveRequest_Event__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *modularized_bhv_msgs__srv__MoveRequest_Request__get_individual_type_description_source(NULL);
    sources[3] = *modularized_bhv_msgs__srv__MoveRequest_Response__get_individual_type_description_source(NULL);
    sources[4] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
