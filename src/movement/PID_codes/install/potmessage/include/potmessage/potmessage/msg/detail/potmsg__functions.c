// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from potmessage:msg/Potmsg.idl
// generated code does not contain a copyright notice
#include "potmessage/msg/detail/potmsg__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
potmessage__msg__Potmsg__init(potmessage__msg__Potmsg * msg)
{
  if (!msg) {
    return false;
  }
  // pot1
  // pot2
  // pot3
  // pot4
  // pot5
  // pot6
  // pot7
  // pot8
  return true;
}

void
potmessage__msg__Potmsg__fini(potmessage__msg__Potmsg * msg)
{
  if (!msg) {
    return;
  }
  // pot1
  // pot2
  // pot3
  // pot4
  // pot5
  // pot6
  // pot7
  // pot8
}

bool
potmessage__msg__Potmsg__are_equal(const potmessage__msg__Potmsg * lhs, const potmessage__msg__Potmsg * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // pot1
  if (lhs->pot1 != rhs->pot1) {
    return false;
  }
  // pot2
  if (lhs->pot2 != rhs->pot2) {
    return false;
  }
  // pot3
  if (lhs->pot3 != rhs->pot3) {
    return false;
  }
  // pot4
  if (lhs->pot4 != rhs->pot4) {
    return false;
  }
  // pot5
  if (lhs->pot5 != rhs->pot5) {
    return false;
  }
  // pot6
  if (lhs->pot6 != rhs->pot6) {
    return false;
  }
  // pot7
  if (lhs->pot7 != rhs->pot7) {
    return false;
  }
  // pot8
  if (lhs->pot8 != rhs->pot8) {
    return false;
  }
  return true;
}

bool
potmessage__msg__Potmsg__copy(
  const potmessage__msg__Potmsg * input,
  potmessage__msg__Potmsg * output)
{
  if (!input || !output) {
    return false;
  }
  // pot1
  output->pot1 = input->pot1;
  // pot2
  output->pot2 = input->pot2;
  // pot3
  output->pot3 = input->pot3;
  // pot4
  output->pot4 = input->pot4;
  // pot5
  output->pot5 = input->pot5;
  // pot6
  output->pot6 = input->pot6;
  // pot7
  output->pot7 = input->pot7;
  // pot8
  output->pot8 = input->pot8;
  return true;
}

potmessage__msg__Potmsg *
potmessage__msg__Potmsg__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  potmessage__msg__Potmsg * msg = (potmessage__msg__Potmsg *)allocator.allocate(sizeof(potmessage__msg__Potmsg), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(potmessage__msg__Potmsg));
  bool success = potmessage__msg__Potmsg__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
potmessage__msg__Potmsg__destroy(potmessage__msg__Potmsg * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    potmessage__msg__Potmsg__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
potmessage__msg__Potmsg__Sequence__init(potmessage__msg__Potmsg__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  potmessage__msg__Potmsg * data = NULL;

  if (size) {
    data = (potmessage__msg__Potmsg *)allocator.zero_allocate(size, sizeof(potmessage__msg__Potmsg), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = potmessage__msg__Potmsg__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        potmessage__msg__Potmsg__fini(&data[i - 1]);
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
potmessage__msg__Potmsg__Sequence__fini(potmessage__msg__Potmsg__Sequence * array)
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
      potmessage__msg__Potmsg__fini(&array->data[i]);
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

potmessage__msg__Potmsg__Sequence *
potmessage__msg__Potmsg__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  potmessage__msg__Potmsg__Sequence * array = (potmessage__msg__Potmsg__Sequence *)allocator.allocate(sizeof(potmessage__msg__Potmsg__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = potmessage__msg__Potmsg__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
potmessage__msg__Potmsg__Sequence__destroy(potmessage__msg__Potmsg__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    potmessage__msg__Potmsg__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
potmessage__msg__Potmsg__Sequence__are_equal(const potmessage__msg__Potmsg__Sequence * lhs, const potmessage__msg__Potmsg__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!potmessage__msg__Potmsg__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
potmessage__msg__Potmsg__Sequence__copy(
  const potmessage__msg__Potmsg__Sequence * input,
  potmessage__msg__Potmsg__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(potmessage__msg__Potmsg);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    potmessage__msg__Potmsg * data =
      (potmessage__msg__Potmsg *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!potmessage__msg__Potmsg__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          potmessage__msg__Potmsg__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!potmessage__msg__Potmsg__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
