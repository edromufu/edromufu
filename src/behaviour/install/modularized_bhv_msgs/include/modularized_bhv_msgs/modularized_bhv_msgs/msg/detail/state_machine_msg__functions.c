// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from modularized_bhv_msgs:msg/StateMachineMsg.idl
// generated code does not contain a copyright notice
#include "modularized_bhv_msgs/msg/detail/state_machine_msg__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `ball_position`
// Member `fall_state`
// Member `hor_motor_out_of_center`
#include "rosidl_runtime_c/string_functions.h"

bool
modularized_bhv_msgs__msg__StateMachineMsg__init(modularized_bhv_msgs__msg__StateMachineMsg * msg)
{
  if (!msg) {
    return false;
  }
  // ball_position
  if (!rosidl_runtime_c__String__init(&msg->ball_position)) {
    modularized_bhv_msgs__msg__StateMachineMsg__fini(msg);
    return false;
  }
  // ball_close
  // ball_found
  // fall_state
  if (!rosidl_runtime_c__String__init(&msg->fall_state)) {
    modularized_bhv_msgs__msg__StateMachineMsg__fini(msg);
    return false;
  }
  // hor_motor_out_of_center
  if (!rosidl_runtime_c__String__init(&msg->hor_motor_out_of_center)) {
    modularized_bhv_msgs__msg__StateMachineMsg__fini(msg);
    return false;
  }
  // head_kick_check
  return true;
}

void
modularized_bhv_msgs__msg__StateMachineMsg__fini(modularized_bhv_msgs__msg__StateMachineMsg * msg)
{
  if (!msg) {
    return;
  }
  // ball_position
  rosidl_runtime_c__String__fini(&msg->ball_position);
  // ball_close
  // ball_found
  // fall_state
  rosidl_runtime_c__String__fini(&msg->fall_state);
  // hor_motor_out_of_center
  rosidl_runtime_c__String__fini(&msg->hor_motor_out_of_center);
  // head_kick_check
}

bool
modularized_bhv_msgs__msg__StateMachineMsg__are_equal(const modularized_bhv_msgs__msg__StateMachineMsg * lhs, const modularized_bhv_msgs__msg__StateMachineMsg * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // ball_position
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->ball_position), &(rhs->ball_position)))
  {
    return false;
  }
  // ball_close
  if (lhs->ball_close != rhs->ball_close) {
    return false;
  }
  // ball_found
  if (lhs->ball_found != rhs->ball_found) {
    return false;
  }
  // fall_state
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->fall_state), &(rhs->fall_state)))
  {
    return false;
  }
  // hor_motor_out_of_center
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->hor_motor_out_of_center), &(rhs->hor_motor_out_of_center)))
  {
    return false;
  }
  // head_kick_check
  if (lhs->head_kick_check != rhs->head_kick_check) {
    return false;
  }
  return true;
}

bool
modularized_bhv_msgs__msg__StateMachineMsg__copy(
  const modularized_bhv_msgs__msg__StateMachineMsg * input,
  modularized_bhv_msgs__msg__StateMachineMsg * output)
{
  if (!input || !output) {
    return false;
  }
  // ball_position
  if (!rosidl_runtime_c__String__copy(
      &(input->ball_position), &(output->ball_position)))
  {
    return false;
  }
  // ball_close
  output->ball_close = input->ball_close;
  // ball_found
  output->ball_found = input->ball_found;
  // fall_state
  if (!rosidl_runtime_c__String__copy(
      &(input->fall_state), &(output->fall_state)))
  {
    return false;
  }
  // hor_motor_out_of_center
  if (!rosidl_runtime_c__String__copy(
      &(input->hor_motor_out_of_center), &(output->hor_motor_out_of_center)))
  {
    return false;
  }
  // head_kick_check
  output->head_kick_check = input->head_kick_check;
  return true;
}

modularized_bhv_msgs__msg__StateMachineMsg *
modularized_bhv_msgs__msg__StateMachineMsg__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  modularized_bhv_msgs__msg__StateMachineMsg * msg = (modularized_bhv_msgs__msg__StateMachineMsg *)allocator.allocate(sizeof(modularized_bhv_msgs__msg__StateMachineMsg), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(modularized_bhv_msgs__msg__StateMachineMsg));
  bool success = modularized_bhv_msgs__msg__StateMachineMsg__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
modularized_bhv_msgs__msg__StateMachineMsg__destroy(modularized_bhv_msgs__msg__StateMachineMsg * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    modularized_bhv_msgs__msg__StateMachineMsg__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
modularized_bhv_msgs__msg__StateMachineMsg__Sequence__init(modularized_bhv_msgs__msg__StateMachineMsg__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  modularized_bhv_msgs__msg__StateMachineMsg * data = NULL;

  if (size) {
    data = (modularized_bhv_msgs__msg__StateMachineMsg *)allocator.zero_allocate(size, sizeof(modularized_bhv_msgs__msg__StateMachineMsg), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = modularized_bhv_msgs__msg__StateMachineMsg__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        modularized_bhv_msgs__msg__StateMachineMsg__fini(&data[i - 1]);
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
modularized_bhv_msgs__msg__StateMachineMsg__Sequence__fini(modularized_bhv_msgs__msg__StateMachineMsg__Sequence * array)
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
      modularized_bhv_msgs__msg__StateMachineMsg__fini(&array->data[i]);
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

modularized_bhv_msgs__msg__StateMachineMsg__Sequence *
modularized_bhv_msgs__msg__StateMachineMsg__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  modularized_bhv_msgs__msg__StateMachineMsg__Sequence * array = (modularized_bhv_msgs__msg__StateMachineMsg__Sequence *)allocator.allocate(sizeof(modularized_bhv_msgs__msg__StateMachineMsg__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = modularized_bhv_msgs__msg__StateMachineMsg__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
modularized_bhv_msgs__msg__StateMachineMsg__Sequence__destroy(modularized_bhv_msgs__msg__StateMachineMsg__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    modularized_bhv_msgs__msg__StateMachineMsg__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
modularized_bhv_msgs__msg__StateMachineMsg__Sequence__are_equal(const modularized_bhv_msgs__msg__StateMachineMsg__Sequence * lhs, const modularized_bhv_msgs__msg__StateMachineMsg__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!modularized_bhv_msgs__msg__StateMachineMsg__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
modularized_bhv_msgs__msg__StateMachineMsg__Sequence__copy(
  const modularized_bhv_msgs__msg__StateMachineMsg__Sequence * input,
  modularized_bhv_msgs__msg__StateMachineMsg__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(modularized_bhv_msgs__msg__StateMachineMsg);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    modularized_bhv_msgs__msg__StateMachineMsg * data =
      (modularized_bhv_msgs__msg__StateMachineMsg *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!modularized_bhv_msgs__msg__StateMachineMsg__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          modularized_bhv_msgs__msg__StateMachineMsg__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!modularized_bhv_msgs__msg__StateMachineMsg__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
