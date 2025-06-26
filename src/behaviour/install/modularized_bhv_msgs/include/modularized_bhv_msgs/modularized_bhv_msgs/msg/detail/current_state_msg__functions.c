// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from modularized_bhv_msgs:msg/CurrentStateMsg.idl
// generated code does not contain a copyright notice
#include "modularized_bhv_msgs/msg/detail/current_state_msg__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `current_state`
#include "rosidl_runtime_c/string_functions.h"

bool
modularized_bhv_msgs__msg__CurrentStateMsg__init(modularized_bhv_msgs__msg__CurrentStateMsg * msg)
{
  if (!msg) {
    return false;
  }
  // current_state
  if (!rosidl_runtime_c__String__init(&msg->current_state)) {
    modularized_bhv_msgs__msg__CurrentStateMsg__fini(msg);
    return false;
  }
  return true;
}

void
modularized_bhv_msgs__msg__CurrentStateMsg__fini(modularized_bhv_msgs__msg__CurrentStateMsg * msg)
{
  if (!msg) {
    return;
  }
  // current_state
  rosidl_runtime_c__String__fini(&msg->current_state);
}

bool
modularized_bhv_msgs__msg__CurrentStateMsg__are_equal(const modularized_bhv_msgs__msg__CurrentStateMsg * lhs, const modularized_bhv_msgs__msg__CurrentStateMsg * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // current_state
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->current_state), &(rhs->current_state)))
  {
    return false;
  }
  return true;
}

bool
modularized_bhv_msgs__msg__CurrentStateMsg__copy(
  const modularized_bhv_msgs__msg__CurrentStateMsg * input,
  modularized_bhv_msgs__msg__CurrentStateMsg * output)
{
  if (!input || !output) {
    return false;
  }
  // current_state
  if (!rosidl_runtime_c__String__copy(
      &(input->current_state), &(output->current_state)))
  {
    return false;
  }
  return true;
}

modularized_bhv_msgs__msg__CurrentStateMsg *
modularized_bhv_msgs__msg__CurrentStateMsg__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  modularized_bhv_msgs__msg__CurrentStateMsg * msg = (modularized_bhv_msgs__msg__CurrentStateMsg *)allocator.allocate(sizeof(modularized_bhv_msgs__msg__CurrentStateMsg), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(modularized_bhv_msgs__msg__CurrentStateMsg));
  bool success = modularized_bhv_msgs__msg__CurrentStateMsg__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
modularized_bhv_msgs__msg__CurrentStateMsg__destroy(modularized_bhv_msgs__msg__CurrentStateMsg * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    modularized_bhv_msgs__msg__CurrentStateMsg__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
modularized_bhv_msgs__msg__CurrentStateMsg__Sequence__init(modularized_bhv_msgs__msg__CurrentStateMsg__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  modularized_bhv_msgs__msg__CurrentStateMsg * data = NULL;

  if (size) {
    data = (modularized_bhv_msgs__msg__CurrentStateMsg *)allocator.zero_allocate(size, sizeof(modularized_bhv_msgs__msg__CurrentStateMsg), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = modularized_bhv_msgs__msg__CurrentStateMsg__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        modularized_bhv_msgs__msg__CurrentStateMsg__fini(&data[i - 1]);
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
modularized_bhv_msgs__msg__CurrentStateMsg__Sequence__fini(modularized_bhv_msgs__msg__CurrentStateMsg__Sequence * array)
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
      modularized_bhv_msgs__msg__CurrentStateMsg__fini(&array->data[i]);
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

modularized_bhv_msgs__msg__CurrentStateMsg__Sequence *
modularized_bhv_msgs__msg__CurrentStateMsg__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  modularized_bhv_msgs__msg__CurrentStateMsg__Sequence * array = (modularized_bhv_msgs__msg__CurrentStateMsg__Sequence *)allocator.allocate(sizeof(modularized_bhv_msgs__msg__CurrentStateMsg__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = modularized_bhv_msgs__msg__CurrentStateMsg__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
modularized_bhv_msgs__msg__CurrentStateMsg__Sequence__destroy(modularized_bhv_msgs__msg__CurrentStateMsg__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    modularized_bhv_msgs__msg__CurrentStateMsg__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
modularized_bhv_msgs__msg__CurrentStateMsg__Sequence__are_equal(const modularized_bhv_msgs__msg__CurrentStateMsg__Sequence * lhs, const modularized_bhv_msgs__msg__CurrentStateMsg__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!modularized_bhv_msgs__msg__CurrentStateMsg__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
modularized_bhv_msgs__msg__CurrentStateMsg__Sequence__copy(
  const modularized_bhv_msgs__msg__CurrentStateMsg__Sequence * input,
  modularized_bhv_msgs__msg__CurrentStateMsg__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(modularized_bhv_msgs__msg__CurrentStateMsg);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    modularized_bhv_msgs__msg__CurrentStateMsg * data =
      (modularized_bhv_msgs__msg__CurrentStateMsg *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!modularized_bhv_msgs__msg__CurrentStateMsg__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          modularized_bhv_msgs__msg__CurrentStateMsg__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!modularized_bhv_msgs__msg__CurrentStateMsg__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
