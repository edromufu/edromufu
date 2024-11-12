// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from modularized_bhv_msgs:msg/GameControllerMsg.idl
// generated code does not contain a copyright notice
#include "modularized_bhv_msgs/msg/detail/game_controller_msg__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `coach_message`
#include "rosidl_runtime_c/string_functions.h"
// Member `team_mates_with_penalty`
// Member `team_mates_with_red_card`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
modularized_bhv_msgs__msg__GameControllerMsg__init(modularized_bhv_msgs__msg__GameControllerMsg * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    modularized_bhv_msgs__msg__GameControllerMsg__fini(msg);
    return false;
  }
  // game_state
  msg->game_state = 3;
  // secondary_state
  msg->secondary_state = 0;
  // secondary_state_team
  // secondary_state_mode
  // first_half
  // own_score
  // rival_score
  // seconds_remaining
  // secondary_seconds_remaining
  // has_kick_off
  // penalized
  // seconds_till_unpenalized
  // team_color
  // drop_in_team
  // drop_in_time
  // penalty_shot
  // single_shots
  // coach_message
  if (!rosidl_runtime_c__String__init(&msg->coach_message)) {
    modularized_bhv_msgs__msg__GameControllerMsg__fini(msg);
    return false;
  }
  // team_mates_with_penalty
  if (!rosidl_runtime_c__boolean__Sequence__init(&msg->team_mates_with_penalty, 0)) {
    modularized_bhv_msgs__msg__GameControllerMsg__fini(msg);
    return false;
  }
  // team_mates_with_red_card
  if (!rosidl_runtime_c__boolean__Sequence__init(&msg->team_mates_with_red_card, 0)) {
    modularized_bhv_msgs__msg__GameControllerMsg__fini(msg);
    return false;
  }
  return true;
}

void
modularized_bhv_msgs__msg__GameControllerMsg__fini(modularized_bhv_msgs__msg__GameControllerMsg * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // game_state
  // secondary_state
  // secondary_state_team
  // secondary_state_mode
  // first_half
  // own_score
  // rival_score
  // seconds_remaining
  // secondary_seconds_remaining
  // has_kick_off
  // penalized
  // seconds_till_unpenalized
  // team_color
  // drop_in_team
  // drop_in_time
  // penalty_shot
  // single_shots
  // coach_message
  rosidl_runtime_c__String__fini(&msg->coach_message);
  // team_mates_with_penalty
  rosidl_runtime_c__boolean__Sequence__fini(&msg->team_mates_with_penalty);
  // team_mates_with_red_card
  rosidl_runtime_c__boolean__Sequence__fini(&msg->team_mates_with_red_card);
}

bool
modularized_bhv_msgs__msg__GameControllerMsg__are_equal(const modularized_bhv_msgs__msg__GameControllerMsg * lhs, const modularized_bhv_msgs__msg__GameControllerMsg * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // game_state
  if (lhs->game_state != rhs->game_state) {
    return false;
  }
  // secondary_state
  if (lhs->secondary_state != rhs->secondary_state) {
    return false;
  }
  // secondary_state_team
  if (lhs->secondary_state_team != rhs->secondary_state_team) {
    return false;
  }
  // secondary_state_mode
  if (lhs->secondary_state_mode != rhs->secondary_state_mode) {
    return false;
  }
  // first_half
  if (lhs->first_half != rhs->first_half) {
    return false;
  }
  // own_score
  if (lhs->own_score != rhs->own_score) {
    return false;
  }
  // rival_score
  if (lhs->rival_score != rhs->rival_score) {
    return false;
  }
  // seconds_remaining
  if (lhs->seconds_remaining != rhs->seconds_remaining) {
    return false;
  }
  // secondary_seconds_remaining
  if (lhs->secondary_seconds_remaining != rhs->secondary_seconds_remaining) {
    return false;
  }
  // has_kick_off
  if (lhs->has_kick_off != rhs->has_kick_off) {
    return false;
  }
  // penalized
  if (lhs->penalized != rhs->penalized) {
    return false;
  }
  // seconds_till_unpenalized
  if (lhs->seconds_till_unpenalized != rhs->seconds_till_unpenalized) {
    return false;
  }
  // team_color
  if (lhs->team_color != rhs->team_color) {
    return false;
  }
  // drop_in_team
  if (lhs->drop_in_team != rhs->drop_in_team) {
    return false;
  }
  // drop_in_time
  if (lhs->drop_in_time != rhs->drop_in_time) {
    return false;
  }
  // penalty_shot
  if (lhs->penalty_shot != rhs->penalty_shot) {
    return false;
  }
  // single_shots
  if (lhs->single_shots != rhs->single_shots) {
    return false;
  }
  // coach_message
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->coach_message), &(rhs->coach_message)))
  {
    return false;
  }
  // team_mates_with_penalty
  if (!rosidl_runtime_c__boolean__Sequence__are_equal(
      &(lhs->team_mates_with_penalty), &(rhs->team_mates_with_penalty)))
  {
    return false;
  }
  // team_mates_with_red_card
  if (!rosidl_runtime_c__boolean__Sequence__are_equal(
      &(lhs->team_mates_with_red_card), &(rhs->team_mates_with_red_card)))
  {
    return false;
  }
  return true;
}

bool
modularized_bhv_msgs__msg__GameControllerMsg__copy(
  const modularized_bhv_msgs__msg__GameControllerMsg * input,
  modularized_bhv_msgs__msg__GameControllerMsg * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // game_state
  output->game_state = input->game_state;
  // secondary_state
  output->secondary_state = input->secondary_state;
  // secondary_state_team
  output->secondary_state_team = input->secondary_state_team;
  // secondary_state_mode
  output->secondary_state_mode = input->secondary_state_mode;
  // first_half
  output->first_half = input->first_half;
  // own_score
  output->own_score = input->own_score;
  // rival_score
  output->rival_score = input->rival_score;
  // seconds_remaining
  output->seconds_remaining = input->seconds_remaining;
  // secondary_seconds_remaining
  output->secondary_seconds_remaining = input->secondary_seconds_remaining;
  // has_kick_off
  output->has_kick_off = input->has_kick_off;
  // penalized
  output->penalized = input->penalized;
  // seconds_till_unpenalized
  output->seconds_till_unpenalized = input->seconds_till_unpenalized;
  // team_color
  output->team_color = input->team_color;
  // drop_in_team
  output->drop_in_team = input->drop_in_team;
  // drop_in_time
  output->drop_in_time = input->drop_in_time;
  // penalty_shot
  output->penalty_shot = input->penalty_shot;
  // single_shots
  output->single_shots = input->single_shots;
  // coach_message
  if (!rosidl_runtime_c__String__copy(
      &(input->coach_message), &(output->coach_message)))
  {
    return false;
  }
  // team_mates_with_penalty
  if (!rosidl_runtime_c__boolean__Sequence__copy(
      &(input->team_mates_with_penalty), &(output->team_mates_with_penalty)))
  {
    return false;
  }
  // team_mates_with_red_card
  if (!rosidl_runtime_c__boolean__Sequence__copy(
      &(input->team_mates_with_red_card), &(output->team_mates_with_red_card)))
  {
    return false;
  }
  return true;
}

modularized_bhv_msgs__msg__GameControllerMsg *
modularized_bhv_msgs__msg__GameControllerMsg__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  modularized_bhv_msgs__msg__GameControllerMsg * msg = (modularized_bhv_msgs__msg__GameControllerMsg *)allocator.allocate(sizeof(modularized_bhv_msgs__msg__GameControllerMsg), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(modularized_bhv_msgs__msg__GameControllerMsg));
  bool success = modularized_bhv_msgs__msg__GameControllerMsg__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
modularized_bhv_msgs__msg__GameControllerMsg__destroy(modularized_bhv_msgs__msg__GameControllerMsg * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    modularized_bhv_msgs__msg__GameControllerMsg__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
modularized_bhv_msgs__msg__GameControllerMsg__Sequence__init(modularized_bhv_msgs__msg__GameControllerMsg__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  modularized_bhv_msgs__msg__GameControllerMsg * data = NULL;

  if (size) {
    data = (modularized_bhv_msgs__msg__GameControllerMsg *)allocator.zero_allocate(size, sizeof(modularized_bhv_msgs__msg__GameControllerMsg), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = modularized_bhv_msgs__msg__GameControllerMsg__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        modularized_bhv_msgs__msg__GameControllerMsg__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
modularized_bhv_msgs__msg__GameControllerMsg__Sequence__fini(modularized_bhv_msgs__msg__GameControllerMsg__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      modularized_bhv_msgs__msg__GameControllerMsg__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

modularized_bhv_msgs__msg__GameControllerMsg__Sequence *
modularized_bhv_msgs__msg__GameControllerMsg__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  modularized_bhv_msgs__msg__GameControllerMsg__Sequence * array = (modularized_bhv_msgs__msg__GameControllerMsg__Sequence *)allocator.allocate(sizeof(modularized_bhv_msgs__msg__GameControllerMsg__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = modularized_bhv_msgs__msg__GameControllerMsg__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
modularized_bhv_msgs__msg__GameControllerMsg__Sequence__destroy(modularized_bhv_msgs__msg__GameControllerMsg__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    modularized_bhv_msgs__msg__GameControllerMsg__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
modularized_bhv_msgs__msg__GameControllerMsg__Sequence__are_equal(const modularized_bhv_msgs__msg__GameControllerMsg__Sequence * lhs, const modularized_bhv_msgs__msg__GameControllerMsg__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!modularized_bhv_msgs__msg__GameControllerMsg__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
modularized_bhv_msgs__msg__GameControllerMsg__Sequence__copy(
  const modularized_bhv_msgs__msg__GameControllerMsg__Sequence * input,
  modularized_bhv_msgs__msg__GameControllerMsg__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(modularized_bhv_msgs__msg__GameControllerMsg);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    modularized_bhv_msgs__msg__GameControllerMsg * data =
      (modularized_bhv_msgs__msg__GameControllerMsg *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!modularized_bhv_msgs__msg__GameControllerMsg__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          modularized_bhv_msgs__msg__GameControllerMsg__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!modularized_bhv_msgs__msg__GameControllerMsg__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
