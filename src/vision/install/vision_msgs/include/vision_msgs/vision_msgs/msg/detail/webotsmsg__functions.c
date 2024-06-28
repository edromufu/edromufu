// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from vision_msgs:msg/Webotsmsg.idl
// generated code does not contain a copyright notice
#include "vision_msgs/msg/detail/webotsmsg__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `ball`
#include "vision_msgs/msg/detail/ball__functions.h"
// Member `leftgoalpost`
#include "vision_msgs/msg/detail/leftgoalpost__functions.h"
// Member `rightgoalpost`
#include "vision_msgs/msg/detail/rightgoalpost__functions.h"

bool
vision_msgs__msg__Webotsmsg__init(vision_msgs__msg__Webotsmsg * msg)
{
  if (!msg) {
    return false;
  }
  // searching
  // fps
  // ball
  if (!vision_msgs__msg__Ball__init(&msg->ball)) {
    vision_msgs__msg__Webotsmsg__fini(msg);
    return false;
  }
  // leftgoalpost
  if (!vision_msgs__msg__Leftgoalpost__init(&msg->leftgoalpost)) {
    vision_msgs__msg__Webotsmsg__fini(msg);
    return false;
  }
  // rightgoalpost
  if (!vision_msgs__msg__Rightgoalpost__init(&msg->rightgoalpost)) {
    vision_msgs__msg__Webotsmsg__fini(msg);
    return false;
  }
  return true;
}

void
vision_msgs__msg__Webotsmsg__fini(vision_msgs__msg__Webotsmsg * msg)
{
  if (!msg) {
    return;
  }
  // searching
  // fps
  // ball
  vision_msgs__msg__Ball__fini(&msg->ball);
  // leftgoalpost
  vision_msgs__msg__Leftgoalpost__fini(&msg->leftgoalpost);
  // rightgoalpost
  vision_msgs__msg__Rightgoalpost__fini(&msg->rightgoalpost);
}

bool
vision_msgs__msg__Webotsmsg__are_equal(const vision_msgs__msg__Webotsmsg * lhs, const vision_msgs__msg__Webotsmsg * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // searching
  if (lhs->searching != rhs->searching) {
    return false;
  }
  // fps
  if (lhs->fps != rhs->fps) {
    return false;
  }
  // ball
  if (!vision_msgs__msg__Ball__are_equal(
      &(lhs->ball), &(rhs->ball)))
  {
    return false;
  }
  // leftgoalpost
  if (!vision_msgs__msg__Leftgoalpost__are_equal(
      &(lhs->leftgoalpost), &(rhs->leftgoalpost)))
  {
    return false;
  }
  // rightgoalpost
  if (!vision_msgs__msg__Rightgoalpost__are_equal(
      &(lhs->rightgoalpost), &(rhs->rightgoalpost)))
  {
    return false;
  }
  return true;
}

bool
vision_msgs__msg__Webotsmsg__copy(
  const vision_msgs__msg__Webotsmsg * input,
  vision_msgs__msg__Webotsmsg * output)
{
  if (!input || !output) {
    return false;
  }
  // searching
  output->searching = input->searching;
  // fps
  output->fps = input->fps;
  // ball
  if (!vision_msgs__msg__Ball__copy(
      &(input->ball), &(output->ball)))
  {
    return false;
  }
  // leftgoalpost
  if (!vision_msgs__msg__Leftgoalpost__copy(
      &(input->leftgoalpost), &(output->leftgoalpost)))
  {
    return false;
  }
  // rightgoalpost
  if (!vision_msgs__msg__Rightgoalpost__copy(
      &(input->rightgoalpost), &(output->rightgoalpost)))
  {
    return false;
  }
  return true;
}

vision_msgs__msg__Webotsmsg *
vision_msgs__msg__Webotsmsg__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  vision_msgs__msg__Webotsmsg * msg = (vision_msgs__msg__Webotsmsg *)allocator.allocate(sizeof(vision_msgs__msg__Webotsmsg), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(vision_msgs__msg__Webotsmsg));
  bool success = vision_msgs__msg__Webotsmsg__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
vision_msgs__msg__Webotsmsg__destroy(vision_msgs__msg__Webotsmsg * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    vision_msgs__msg__Webotsmsg__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
vision_msgs__msg__Webotsmsg__Sequence__init(vision_msgs__msg__Webotsmsg__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  vision_msgs__msg__Webotsmsg * data = NULL;

  if (size) {
    data = (vision_msgs__msg__Webotsmsg *)allocator.zero_allocate(size, sizeof(vision_msgs__msg__Webotsmsg), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = vision_msgs__msg__Webotsmsg__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        vision_msgs__msg__Webotsmsg__fini(&data[i - 1]);
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
vision_msgs__msg__Webotsmsg__Sequence__fini(vision_msgs__msg__Webotsmsg__Sequence * array)
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
      vision_msgs__msg__Webotsmsg__fini(&array->data[i]);
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

vision_msgs__msg__Webotsmsg__Sequence *
vision_msgs__msg__Webotsmsg__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  vision_msgs__msg__Webotsmsg__Sequence * array = (vision_msgs__msg__Webotsmsg__Sequence *)allocator.allocate(sizeof(vision_msgs__msg__Webotsmsg__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = vision_msgs__msg__Webotsmsg__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
vision_msgs__msg__Webotsmsg__Sequence__destroy(vision_msgs__msg__Webotsmsg__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    vision_msgs__msg__Webotsmsg__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
vision_msgs__msg__Webotsmsg__Sequence__are_equal(const vision_msgs__msg__Webotsmsg__Sequence * lhs, const vision_msgs__msg__Webotsmsg__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!vision_msgs__msg__Webotsmsg__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
vision_msgs__msg__Webotsmsg__Sequence__copy(
  const vision_msgs__msg__Webotsmsg__Sequence * input,
  vision_msgs__msg__Webotsmsg__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(vision_msgs__msg__Webotsmsg);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    vision_msgs__msg__Webotsmsg * data =
      (vision_msgs__msg__Webotsmsg *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!vision_msgs__msg__Webotsmsg__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          vision_msgs__msg__Webotsmsg__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!vision_msgs__msg__Webotsmsg__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
