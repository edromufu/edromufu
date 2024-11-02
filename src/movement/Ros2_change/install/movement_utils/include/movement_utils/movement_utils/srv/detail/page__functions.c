// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from movement_utils:srv/Page.idl
// generated code does not contain a copyright notice
#include "movement_utils/srv/detail/page__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `page_name`
#include "rosidl_runtime_c/string_functions.h"

bool
movement_utils__srv__Page_Request__init(movement_utils__srv__Page_Request * msg)
{
  if (!msg) {
    return false;
  }
  // page_name
  if (!rosidl_runtime_c__String__init(&msg->page_name)) {
    movement_utils__srv__Page_Request__fini(msg);
    return false;
  }
  return true;
}

void
movement_utils__srv__Page_Request__fini(movement_utils__srv__Page_Request * msg)
{
  if (!msg) {
    return;
  }
  // page_name
  rosidl_runtime_c__String__fini(&msg->page_name);
}

bool
movement_utils__srv__Page_Request__are_equal(const movement_utils__srv__Page_Request * lhs, const movement_utils__srv__Page_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // page_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->page_name), &(rhs->page_name)))
  {
    return false;
  }
  return true;
}

bool
movement_utils__srv__Page_Request__copy(
  const movement_utils__srv__Page_Request * input,
  movement_utils__srv__Page_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // page_name
  if (!rosidl_runtime_c__String__copy(
      &(input->page_name), &(output->page_name)))
  {
    return false;
  }
  return true;
}

movement_utils__srv__Page_Request *
movement_utils__srv__Page_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  movement_utils__srv__Page_Request * msg = (movement_utils__srv__Page_Request *)allocator.allocate(sizeof(movement_utils__srv__Page_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(movement_utils__srv__Page_Request));
  bool success = movement_utils__srv__Page_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
movement_utils__srv__Page_Request__destroy(movement_utils__srv__Page_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    movement_utils__srv__Page_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
movement_utils__srv__Page_Request__Sequence__init(movement_utils__srv__Page_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  movement_utils__srv__Page_Request * data = NULL;

  if (size) {
    data = (movement_utils__srv__Page_Request *)allocator.zero_allocate(size, sizeof(movement_utils__srv__Page_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = movement_utils__srv__Page_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        movement_utils__srv__Page_Request__fini(&data[i - 1]);
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
movement_utils__srv__Page_Request__Sequence__fini(movement_utils__srv__Page_Request__Sequence * array)
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
      movement_utils__srv__Page_Request__fini(&array->data[i]);
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

movement_utils__srv__Page_Request__Sequence *
movement_utils__srv__Page_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  movement_utils__srv__Page_Request__Sequence * array = (movement_utils__srv__Page_Request__Sequence *)allocator.allocate(sizeof(movement_utils__srv__Page_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = movement_utils__srv__Page_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
movement_utils__srv__Page_Request__Sequence__destroy(movement_utils__srv__Page_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    movement_utils__srv__Page_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
movement_utils__srv__Page_Request__Sequence__are_equal(const movement_utils__srv__Page_Request__Sequence * lhs, const movement_utils__srv__Page_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!movement_utils__srv__Page_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
movement_utils__srv__Page_Request__Sequence__copy(
  const movement_utils__srv__Page_Request__Sequence * input,
  movement_utils__srv__Page_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(movement_utils__srv__Page_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    movement_utils__srv__Page_Request * data =
      (movement_utils__srv__Page_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!movement_utils__srv__Page_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          movement_utils__srv__Page_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!movement_utils__srv__Page_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
movement_utils__srv__Page_Response__init(movement_utils__srv__Page_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  return true;
}

void
movement_utils__srv__Page_Response__fini(movement_utils__srv__Page_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
}

bool
movement_utils__srv__Page_Response__are_equal(const movement_utils__srv__Page_Response * lhs, const movement_utils__srv__Page_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  return true;
}

bool
movement_utils__srv__Page_Response__copy(
  const movement_utils__srv__Page_Response * input,
  movement_utils__srv__Page_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  return true;
}

movement_utils__srv__Page_Response *
movement_utils__srv__Page_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  movement_utils__srv__Page_Response * msg = (movement_utils__srv__Page_Response *)allocator.allocate(sizeof(movement_utils__srv__Page_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(movement_utils__srv__Page_Response));
  bool success = movement_utils__srv__Page_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
movement_utils__srv__Page_Response__destroy(movement_utils__srv__Page_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    movement_utils__srv__Page_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
movement_utils__srv__Page_Response__Sequence__init(movement_utils__srv__Page_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  movement_utils__srv__Page_Response * data = NULL;

  if (size) {
    data = (movement_utils__srv__Page_Response *)allocator.zero_allocate(size, sizeof(movement_utils__srv__Page_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = movement_utils__srv__Page_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        movement_utils__srv__Page_Response__fini(&data[i - 1]);
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
movement_utils__srv__Page_Response__Sequence__fini(movement_utils__srv__Page_Response__Sequence * array)
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
      movement_utils__srv__Page_Response__fini(&array->data[i]);
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

movement_utils__srv__Page_Response__Sequence *
movement_utils__srv__Page_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  movement_utils__srv__Page_Response__Sequence * array = (movement_utils__srv__Page_Response__Sequence *)allocator.allocate(sizeof(movement_utils__srv__Page_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = movement_utils__srv__Page_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
movement_utils__srv__Page_Response__Sequence__destroy(movement_utils__srv__Page_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    movement_utils__srv__Page_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
movement_utils__srv__Page_Response__Sequence__are_equal(const movement_utils__srv__Page_Response__Sequence * lhs, const movement_utils__srv__Page_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!movement_utils__srv__Page_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
movement_utils__srv__Page_Response__Sequence__copy(
  const movement_utils__srv__Page_Response__Sequence * input,
  movement_utils__srv__Page_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(movement_utils__srv__Page_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    movement_utils__srv__Page_Response * data =
      (movement_utils__srv__Page_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!movement_utils__srv__Page_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          movement_utils__srv__Page_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!movement_utils__srv__Page_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
