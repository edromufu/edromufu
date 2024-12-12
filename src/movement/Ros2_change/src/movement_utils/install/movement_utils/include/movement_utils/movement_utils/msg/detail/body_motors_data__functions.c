// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from movement_utils:msg/BodyMotorsData.idl
// generated code does not contain a copyright notice
#include "movement_utils/msg/detail/body_motors_data__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
movement_utils__msg__BodyMotorsData__init(movement_utils__msg__BodyMotorsData * msg)
{
  if (!msg) {
    return false;
  }
  // pos_vector
  return true;
}

void
movement_utils__msg__BodyMotorsData__fini(movement_utils__msg__BodyMotorsData * msg)
{
  if (!msg) {
    return;
  }
  // pos_vector
}

bool
movement_utils__msg__BodyMotorsData__are_equal(const movement_utils__msg__BodyMotorsData * lhs, const movement_utils__msg__BodyMotorsData * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // pos_vector
  for (size_t i = 0; i < 18; ++i) {
    if (lhs->pos_vector[i] != rhs->pos_vector[i]) {
      return false;
    }
  }
  return true;
}

bool
movement_utils__msg__BodyMotorsData__copy(
  const movement_utils__msg__BodyMotorsData * input,
  movement_utils__msg__BodyMotorsData * output)
{
  if (!input || !output) {
    return false;
  }
  // pos_vector
  for (size_t i = 0; i < 18; ++i) {
    output->pos_vector[i] = input->pos_vector[i];
  }
  return true;
}

movement_utils__msg__BodyMotorsData *
movement_utils__msg__BodyMotorsData__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  movement_utils__msg__BodyMotorsData * msg = (movement_utils__msg__BodyMotorsData *)allocator.allocate(sizeof(movement_utils__msg__BodyMotorsData), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(movement_utils__msg__BodyMotorsData));
  bool success = movement_utils__msg__BodyMotorsData__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
movement_utils__msg__BodyMotorsData__destroy(movement_utils__msg__BodyMotorsData * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    movement_utils__msg__BodyMotorsData__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
movement_utils__msg__BodyMotorsData__Sequence__init(movement_utils__msg__BodyMotorsData__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  movement_utils__msg__BodyMotorsData * data = NULL;

  if (size) {
    data = (movement_utils__msg__BodyMotorsData *)allocator.zero_allocate(size, sizeof(movement_utils__msg__BodyMotorsData), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = movement_utils__msg__BodyMotorsData__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        movement_utils__msg__BodyMotorsData__fini(&data[i - 1]);
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
movement_utils__msg__BodyMotorsData__Sequence__fini(movement_utils__msg__BodyMotorsData__Sequence * array)
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
      movement_utils__msg__BodyMotorsData__fini(&array->data[i]);
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

movement_utils__msg__BodyMotorsData__Sequence *
movement_utils__msg__BodyMotorsData__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  movement_utils__msg__BodyMotorsData__Sequence * array = (movement_utils__msg__BodyMotorsData__Sequence *)allocator.allocate(sizeof(movement_utils__msg__BodyMotorsData__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = movement_utils__msg__BodyMotorsData__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
movement_utils__msg__BodyMotorsData__Sequence__destroy(movement_utils__msg__BodyMotorsData__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    movement_utils__msg__BodyMotorsData__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
movement_utils__msg__BodyMotorsData__Sequence__are_equal(const movement_utils__msg__BodyMotorsData__Sequence * lhs, const movement_utils__msg__BodyMotorsData__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!movement_utils__msg__BodyMotorsData__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
movement_utils__msg__BodyMotorsData__Sequence__copy(
  const movement_utils__msg__BodyMotorsData__Sequence * input,
  movement_utils__msg__BodyMotorsData__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(movement_utils__msg__BodyMotorsData);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    movement_utils__msg__BodyMotorsData * data =
      (movement_utils__msg__BodyMotorsData *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!movement_utils__msg__BodyMotorsData__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          movement_utils__msg__BodyMotorsData__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!movement_utils__msg__BodyMotorsData__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
