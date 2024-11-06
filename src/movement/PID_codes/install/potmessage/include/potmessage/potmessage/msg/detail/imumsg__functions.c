// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from potmessage:msg/Imumsg.idl
// generated code does not contain a copyright notice
#include "potmessage/msg/detail/imumsg__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
potmessage__msg__Imumsg__init(potmessage__msg__Imumsg * msg)
{
  if (!msg) {
    return false;
  }
  // imu
  return true;
}

void
potmessage__msg__Imumsg__fini(potmessage__msg__Imumsg * msg)
{
  if (!msg) {
    return;
  }
  // imu
}

bool
potmessage__msg__Imumsg__are_equal(const potmessage__msg__Imumsg * lhs, const potmessage__msg__Imumsg * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // imu
  for (size_t i = 0; i < 4; ++i) {
    if (lhs->imu[i] != rhs->imu[i]) {
      return false;
    }
  }
  return true;
}

bool
potmessage__msg__Imumsg__copy(
  const potmessage__msg__Imumsg * input,
  potmessage__msg__Imumsg * output)
{
  if (!input || !output) {
    return false;
  }
  // imu
  for (size_t i = 0; i < 4; ++i) {
    output->imu[i] = input->imu[i];
  }
  return true;
}

potmessage__msg__Imumsg *
potmessage__msg__Imumsg__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  potmessage__msg__Imumsg * msg = (potmessage__msg__Imumsg *)allocator.allocate(sizeof(potmessage__msg__Imumsg), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(potmessage__msg__Imumsg));
  bool success = potmessage__msg__Imumsg__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
potmessage__msg__Imumsg__destroy(potmessage__msg__Imumsg * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    potmessage__msg__Imumsg__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
potmessage__msg__Imumsg__Sequence__init(potmessage__msg__Imumsg__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  potmessage__msg__Imumsg * data = NULL;

  if (size) {
    data = (potmessage__msg__Imumsg *)allocator.zero_allocate(size, sizeof(potmessage__msg__Imumsg), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = potmessage__msg__Imumsg__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        potmessage__msg__Imumsg__fini(&data[i - 1]);
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
potmessage__msg__Imumsg__Sequence__fini(potmessage__msg__Imumsg__Sequence * array)
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
      potmessage__msg__Imumsg__fini(&array->data[i]);
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

potmessage__msg__Imumsg__Sequence *
potmessage__msg__Imumsg__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  potmessage__msg__Imumsg__Sequence * array = (potmessage__msg__Imumsg__Sequence *)allocator.allocate(sizeof(potmessage__msg__Imumsg__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = potmessage__msg__Imumsg__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
potmessage__msg__Imumsg__Sequence__destroy(potmessage__msg__Imumsg__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    potmessage__msg__Imumsg__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
potmessage__msg__Imumsg__Sequence__are_equal(const potmessage__msg__Imumsg__Sequence * lhs, const potmessage__msg__Imumsg__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!potmessage__msg__Imumsg__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
potmessage__msg__Imumsg__Sequence__copy(
  const potmessage__msg__Imumsg__Sequence * input,
  potmessage__msg__Imumsg__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(potmessage__msg__Imumsg);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    potmessage__msg__Imumsg * data =
      (potmessage__msg__Imumsg *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!potmessage__msg__Imumsg__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          potmessage__msg__Imumsg__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!potmessage__msg__Imumsg__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
