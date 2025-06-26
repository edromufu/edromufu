// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from modularized_bhv_msgs:srv/MoveRequest.idl
// generated code does not contain a copyright notice
#include "modularized_bhv_msgs/srv/detail/move_request__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `move_request`
#include "rosidl_runtime_c/string_functions.h"

bool
modularized_bhv_msgs__srv__MoveRequest_Request__init(modularized_bhv_msgs__srv__MoveRequest_Request * msg)
{
  if (!msg) {
    return false;
  }
  // move_request
  if (!rosidl_runtime_c__String__init(&msg->move_request)) {
    modularized_bhv_msgs__srv__MoveRequest_Request__fini(msg);
    return false;
  }
  return true;
}

void
modularized_bhv_msgs__srv__MoveRequest_Request__fini(modularized_bhv_msgs__srv__MoveRequest_Request * msg)
{
  if (!msg) {
    return;
  }
  // move_request
  rosidl_runtime_c__String__fini(&msg->move_request);
}

bool
modularized_bhv_msgs__srv__MoveRequest_Request__are_equal(const modularized_bhv_msgs__srv__MoveRequest_Request * lhs, const modularized_bhv_msgs__srv__MoveRequest_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // move_request
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->move_request), &(rhs->move_request)))
  {
    return false;
  }
  return true;
}

bool
modularized_bhv_msgs__srv__MoveRequest_Request__copy(
  const modularized_bhv_msgs__srv__MoveRequest_Request * input,
  modularized_bhv_msgs__srv__MoveRequest_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // move_request
  if (!rosidl_runtime_c__String__copy(
      &(input->move_request), &(output->move_request)))
  {
    return false;
  }
  return true;
}

modularized_bhv_msgs__srv__MoveRequest_Request *
modularized_bhv_msgs__srv__MoveRequest_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  modularized_bhv_msgs__srv__MoveRequest_Request * msg = (modularized_bhv_msgs__srv__MoveRequest_Request *)allocator.allocate(sizeof(modularized_bhv_msgs__srv__MoveRequest_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(modularized_bhv_msgs__srv__MoveRequest_Request));
  bool success = modularized_bhv_msgs__srv__MoveRequest_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
modularized_bhv_msgs__srv__MoveRequest_Request__destroy(modularized_bhv_msgs__srv__MoveRequest_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    modularized_bhv_msgs__srv__MoveRequest_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
modularized_bhv_msgs__srv__MoveRequest_Request__Sequence__init(modularized_bhv_msgs__srv__MoveRequest_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  modularized_bhv_msgs__srv__MoveRequest_Request * data = NULL;

  if (size) {
    data = (modularized_bhv_msgs__srv__MoveRequest_Request *)allocator.zero_allocate(size, sizeof(modularized_bhv_msgs__srv__MoveRequest_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = modularized_bhv_msgs__srv__MoveRequest_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        modularized_bhv_msgs__srv__MoveRequest_Request__fini(&data[i - 1]);
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
modularized_bhv_msgs__srv__MoveRequest_Request__Sequence__fini(modularized_bhv_msgs__srv__MoveRequest_Request__Sequence * array)
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
      modularized_bhv_msgs__srv__MoveRequest_Request__fini(&array->data[i]);
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

modularized_bhv_msgs__srv__MoveRequest_Request__Sequence *
modularized_bhv_msgs__srv__MoveRequest_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  modularized_bhv_msgs__srv__MoveRequest_Request__Sequence * array = (modularized_bhv_msgs__srv__MoveRequest_Request__Sequence *)allocator.allocate(sizeof(modularized_bhv_msgs__srv__MoveRequest_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = modularized_bhv_msgs__srv__MoveRequest_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
modularized_bhv_msgs__srv__MoveRequest_Request__Sequence__destroy(modularized_bhv_msgs__srv__MoveRequest_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    modularized_bhv_msgs__srv__MoveRequest_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
modularized_bhv_msgs__srv__MoveRequest_Request__Sequence__are_equal(const modularized_bhv_msgs__srv__MoveRequest_Request__Sequence * lhs, const modularized_bhv_msgs__srv__MoveRequest_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!modularized_bhv_msgs__srv__MoveRequest_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
modularized_bhv_msgs__srv__MoveRequest_Request__Sequence__copy(
  const modularized_bhv_msgs__srv__MoveRequest_Request__Sequence * input,
  modularized_bhv_msgs__srv__MoveRequest_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(modularized_bhv_msgs__srv__MoveRequest_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    modularized_bhv_msgs__srv__MoveRequest_Request * data =
      (modularized_bhv_msgs__srv__MoveRequest_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!modularized_bhv_msgs__srv__MoveRequest_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          modularized_bhv_msgs__srv__MoveRequest_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!modularized_bhv_msgs__srv__MoveRequest_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
modularized_bhv_msgs__srv__MoveRequest_Response__init(modularized_bhv_msgs__srv__MoveRequest_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  return true;
}

void
modularized_bhv_msgs__srv__MoveRequest_Response__fini(modularized_bhv_msgs__srv__MoveRequest_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
}

bool
modularized_bhv_msgs__srv__MoveRequest_Response__are_equal(const modularized_bhv_msgs__srv__MoveRequest_Response * lhs, const modularized_bhv_msgs__srv__MoveRequest_Response * rhs)
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
modularized_bhv_msgs__srv__MoveRequest_Response__copy(
  const modularized_bhv_msgs__srv__MoveRequest_Response * input,
  modularized_bhv_msgs__srv__MoveRequest_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  return true;
}

modularized_bhv_msgs__srv__MoveRequest_Response *
modularized_bhv_msgs__srv__MoveRequest_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  modularized_bhv_msgs__srv__MoveRequest_Response * msg = (modularized_bhv_msgs__srv__MoveRequest_Response *)allocator.allocate(sizeof(modularized_bhv_msgs__srv__MoveRequest_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(modularized_bhv_msgs__srv__MoveRequest_Response));
  bool success = modularized_bhv_msgs__srv__MoveRequest_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
modularized_bhv_msgs__srv__MoveRequest_Response__destroy(modularized_bhv_msgs__srv__MoveRequest_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    modularized_bhv_msgs__srv__MoveRequest_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
modularized_bhv_msgs__srv__MoveRequest_Response__Sequence__init(modularized_bhv_msgs__srv__MoveRequest_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  modularized_bhv_msgs__srv__MoveRequest_Response * data = NULL;

  if (size) {
    data = (modularized_bhv_msgs__srv__MoveRequest_Response *)allocator.zero_allocate(size, sizeof(modularized_bhv_msgs__srv__MoveRequest_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = modularized_bhv_msgs__srv__MoveRequest_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        modularized_bhv_msgs__srv__MoveRequest_Response__fini(&data[i - 1]);
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
modularized_bhv_msgs__srv__MoveRequest_Response__Sequence__fini(modularized_bhv_msgs__srv__MoveRequest_Response__Sequence * array)
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
      modularized_bhv_msgs__srv__MoveRequest_Response__fini(&array->data[i]);
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

modularized_bhv_msgs__srv__MoveRequest_Response__Sequence *
modularized_bhv_msgs__srv__MoveRequest_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  modularized_bhv_msgs__srv__MoveRequest_Response__Sequence * array = (modularized_bhv_msgs__srv__MoveRequest_Response__Sequence *)allocator.allocate(sizeof(modularized_bhv_msgs__srv__MoveRequest_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = modularized_bhv_msgs__srv__MoveRequest_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
modularized_bhv_msgs__srv__MoveRequest_Response__Sequence__destroy(modularized_bhv_msgs__srv__MoveRequest_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    modularized_bhv_msgs__srv__MoveRequest_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
modularized_bhv_msgs__srv__MoveRequest_Response__Sequence__are_equal(const modularized_bhv_msgs__srv__MoveRequest_Response__Sequence * lhs, const modularized_bhv_msgs__srv__MoveRequest_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!modularized_bhv_msgs__srv__MoveRequest_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
modularized_bhv_msgs__srv__MoveRequest_Response__Sequence__copy(
  const modularized_bhv_msgs__srv__MoveRequest_Response__Sequence * input,
  modularized_bhv_msgs__srv__MoveRequest_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(modularized_bhv_msgs__srv__MoveRequest_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    modularized_bhv_msgs__srv__MoveRequest_Response * data =
      (modularized_bhv_msgs__srv__MoveRequest_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!modularized_bhv_msgs__srv__MoveRequest_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          modularized_bhv_msgs__srv__MoveRequest_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!modularized_bhv_msgs__srv__MoveRequest_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `info`
#include "service_msgs/msg/detail/service_event_info__functions.h"
// Member `request`
// Member `response`
// already included above
// #include "modularized_bhv_msgs/srv/detail/move_request__functions.h"

bool
modularized_bhv_msgs__srv__MoveRequest_Event__init(modularized_bhv_msgs__srv__MoveRequest_Event * msg)
{
  if (!msg) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__init(&msg->info)) {
    modularized_bhv_msgs__srv__MoveRequest_Event__fini(msg);
    return false;
  }
  // request
  if (!modularized_bhv_msgs__srv__MoveRequest_Request__Sequence__init(&msg->request, 0)) {
    modularized_bhv_msgs__srv__MoveRequest_Event__fini(msg);
    return false;
  }
  // response
  if (!modularized_bhv_msgs__srv__MoveRequest_Response__Sequence__init(&msg->response, 0)) {
    modularized_bhv_msgs__srv__MoveRequest_Event__fini(msg);
    return false;
  }
  return true;
}

void
modularized_bhv_msgs__srv__MoveRequest_Event__fini(modularized_bhv_msgs__srv__MoveRequest_Event * msg)
{
  if (!msg) {
    return;
  }
  // info
  service_msgs__msg__ServiceEventInfo__fini(&msg->info);
  // request
  modularized_bhv_msgs__srv__MoveRequest_Request__Sequence__fini(&msg->request);
  // response
  modularized_bhv_msgs__srv__MoveRequest_Response__Sequence__fini(&msg->response);
}

bool
modularized_bhv_msgs__srv__MoveRequest_Event__are_equal(const modularized_bhv_msgs__srv__MoveRequest_Event * lhs, const modularized_bhv_msgs__srv__MoveRequest_Event * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__are_equal(
      &(lhs->info), &(rhs->info)))
  {
    return false;
  }
  // request
  if (!modularized_bhv_msgs__srv__MoveRequest_Request__Sequence__are_equal(
      &(lhs->request), &(rhs->request)))
  {
    return false;
  }
  // response
  if (!modularized_bhv_msgs__srv__MoveRequest_Response__Sequence__are_equal(
      &(lhs->response), &(rhs->response)))
  {
    return false;
  }
  return true;
}

bool
modularized_bhv_msgs__srv__MoveRequest_Event__copy(
  const modularized_bhv_msgs__srv__MoveRequest_Event * input,
  modularized_bhv_msgs__srv__MoveRequest_Event * output)
{
  if (!input || !output) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__copy(
      &(input->info), &(output->info)))
  {
    return false;
  }
  // request
  if (!modularized_bhv_msgs__srv__MoveRequest_Request__Sequence__copy(
      &(input->request), &(output->request)))
  {
    return false;
  }
  // response
  if (!modularized_bhv_msgs__srv__MoveRequest_Response__Sequence__copy(
      &(input->response), &(output->response)))
  {
    return false;
  }
  return true;
}

modularized_bhv_msgs__srv__MoveRequest_Event *
modularized_bhv_msgs__srv__MoveRequest_Event__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  modularized_bhv_msgs__srv__MoveRequest_Event * msg = (modularized_bhv_msgs__srv__MoveRequest_Event *)allocator.allocate(sizeof(modularized_bhv_msgs__srv__MoveRequest_Event), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(modularized_bhv_msgs__srv__MoveRequest_Event));
  bool success = modularized_bhv_msgs__srv__MoveRequest_Event__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
modularized_bhv_msgs__srv__MoveRequest_Event__destroy(modularized_bhv_msgs__srv__MoveRequest_Event * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    modularized_bhv_msgs__srv__MoveRequest_Event__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
modularized_bhv_msgs__srv__MoveRequest_Event__Sequence__init(modularized_bhv_msgs__srv__MoveRequest_Event__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  modularized_bhv_msgs__srv__MoveRequest_Event * data = NULL;

  if (size) {
    data = (modularized_bhv_msgs__srv__MoveRequest_Event *)allocator.zero_allocate(size, sizeof(modularized_bhv_msgs__srv__MoveRequest_Event), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = modularized_bhv_msgs__srv__MoveRequest_Event__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        modularized_bhv_msgs__srv__MoveRequest_Event__fini(&data[i - 1]);
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
modularized_bhv_msgs__srv__MoveRequest_Event__Sequence__fini(modularized_bhv_msgs__srv__MoveRequest_Event__Sequence * array)
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
      modularized_bhv_msgs__srv__MoveRequest_Event__fini(&array->data[i]);
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

modularized_bhv_msgs__srv__MoveRequest_Event__Sequence *
modularized_bhv_msgs__srv__MoveRequest_Event__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  modularized_bhv_msgs__srv__MoveRequest_Event__Sequence * array = (modularized_bhv_msgs__srv__MoveRequest_Event__Sequence *)allocator.allocate(sizeof(modularized_bhv_msgs__srv__MoveRequest_Event__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = modularized_bhv_msgs__srv__MoveRequest_Event__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
modularized_bhv_msgs__srv__MoveRequest_Event__Sequence__destroy(modularized_bhv_msgs__srv__MoveRequest_Event__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    modularized_bhv_msgs__srv__MoveRequest_Event__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
modularized_bhv_msgs__srv__MoveRequest_Event__Sequence__are_equal(const modularized_bhv_msgs__srv__MoveRequest_Event__Sequence * lhs, const modularized_bhv_msgs__srv__MoveRequest_Event__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!modularized_bhv_msgs__srv__MoveRequest_Event__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
modularized_bhv_msgs__srv__MoveRequest_Event__Sequence__copy(
  const modularized_bhv_msgs__srv__MoveRequest_Event__Sequence * input,
  modularized_bhv_msgs__srv__MoveRequest_Event__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(modularized_bhv_msgs__srv__MoveRequest_Event);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    modularized_bhv_msgs__srv__MoveRequest_Event * data =
      (modularized_bhv_msgs__srv__MoveRequest_Event *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!modularized_bhv_msgs__srv__MoveRequest_Event__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          modularized_bhv_msgs__srv__MoveRequest_Event__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!modularized_bhv_msgs__srv__MoveRequest_Event__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
