// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from potmessage:msg/Buttonmsg.idl
// generated code does not contain a copyright notice
#include "potmessage/msg/detail/buttonmsg__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
potmessage__msg__Buttonmsg__init(potmessage__msg__Buttonmsg * msg)
{
  if (!msg) {
    return false;
  }
  // bot1
  // bot2
  return true;
}

void
potmessage__msg__Buttonmsg__fini(potmessage__msg__Buttonmsg * msg)
{
  if (!msg) {
    return;
  }
  // bot1
  // bot2
}

bool
potmessage__msg__Buttonmsg__are_equal(const potmessage__msg__Buttonmsg * lhs, const potmessage__msg__Buttonmsg * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // bot1
  if (lhs->bot1 != rhs->bot1) {
    return false;
  }
  // bot2
  if (lhs->bot2 != rhs->bot2) {
    return false;
  }
  return true;
}

bool
potmessage__msg__Buttonmsg__copy(
  const potmessage__msg__Buttonmsg * input,
  potmessage__msg__Buttonmsg * output)
{
  if (!input || !output) {
    return false;
  }
  // bot1
  output->bot1 = input->bot1;
  // bot2
  output->bot2 = input->bot2;
  return true;
}

potmessage__msg__Buttonmsg *
potmessage__msg__Buttonmsg__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  potmessage__msg__Buttonmsg * msg = (potmessage__msg__Buttonmsg *)allocator.allocate(sizeof(potmessage__msg__Buttonmsg), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(potmessage__msg__Buttonmsg));
  bool success = potmessage__msg__Buttonmsg__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
potmessage__msg__Buttonmsg__destroy(potmessage__msg__Buttonmsg * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    potmessage__msg__Buttonmsg__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
potmessage__msg__Buttonmsg__Sequence__init(potmessage__msg__Buttonmsg__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  potmessage__msg__Buttonmsg * data = NULL;

  if (size) {
    data = (potmessage__msg__Buttonmsg *)allocator.zero_allocate(size, sizeof(potmessage__msg__Buttonmsg), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = potmessage__msg__Buttonmsg__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        potmessage__msg__Buttonmsg__fini(&data[i - 1]);
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
potmessage__msg__Buttonmsg__Sequence__fini(potmessage__msg__Buttonmsg__Sequence * array)
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
      potmessage__msg__Buttonmsg__fini(&array->data[i]);
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

potmessage__msg__Buttonmsg__Sequence *
potmessage__msg__Buttonmsg__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  potmessage__msg__Buttonmsg__Sequence * array = (potmessage__msg__Buttonmsg__Sequence *)allocator.allocate(sizeof(potmessage__msg__Buttonmsg__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = potmessage__msg__Buttonmsg__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
potmessage__msg__Buttonmsg__Sequence__destroy(potmessage__msg__Buttonmsg__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    potmessage__msg__Buttonmsg__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
potmessage__msg__Buttonmsg__Sequence__are_equal(const potmessage__msg__Buttonmsg__Sequence * lhs, const potmessage__msg__Buttonmsg__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!potmessage__msg__Buttonmsg__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
potmessage__msg__Buttonmsg__Sequence__copy(
  const potmessage__msg__Buttonmsg__Sequence * input,
  potmessage__msg__Buttonmsg__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(potmessage__msg__Buttonmsg);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    potmessage__msg__Buttonmsg * data =
      (potmessage__msg__Buttonmsg *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!potmessage__msg__Buttonmsg__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          potmessage__msg__Buttonmsg__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!potmessage__msg__Buttonmsg__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
