// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from movement_utils:msg/HeadMotorsData.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__MSG__DETAIL__HEAD_MOTORS_DATA__FUNCTIONS_H_
#define MOVEMENT_UTILS__MSG__DETAIL__HEAD_MOTORS_DATA__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "movement_utils/msg/rosidl_generator_c__visibility_control.h"

#include "movement_utils/msg/detail/head_motors_data__struct.h"

/// Initialize msg/HeadMotorsData message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * movement_utils__msg__HeadMotorsData
 * )) before or use
 * movement_utils__msg__HeadMotorsData__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
bool
movement_utils__msg__HeadMotorsData__init(movement_utils__msg__HeadMotorsData * msg);

/// Finalize msg/HeadMotorsData message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
void
movement_utils__msg__HeadMotorsData__fini(movement_utils__msg__HeadMotorsData * msg);

/// Create msg/HeadMotorsData message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * movement_utils__msg__HeadMotorsData__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
movement_utils__msg__HeadMotorsData *
movement_utils__msg__HeadMotorsData__create();

/// Destroy msg/HeadMotorsData message.
/**
 * It calls
 * movement_utils__msg__HeadMotorsData__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
void
movement_utils__msg__HeadMotorsData__destroy(movement_utils__msg__HeadMotorsData * msg);

/// Check for msg/HeadMotorsData message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
bool
movement_utils__msg__HeadMotorsData__are_equal(const movement_utils__msg__HeadMotorsData * lhs, const movement_utils__msg__HeadMotorsData * rhs);

/// Copy a msg/HeadMotorsData message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
bool
movement_utils__msg__HeadMotorsData__copy(
  const movement_utils__msg__HeadMotorsData * input,
  movement_utils__msg__HeadMotorsData * output);

/// Initialize array of msg/HeadMotorsData messages.
/**
 * It allocates the memory for the number of elements and calls
 * movement_utils__msg__HeadMotorsData__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
bool
movement_utils__msg__HeadMotorsData__Sequence__init(movement_utils__msg__HeadMotorsData__Sequence * array, size_t size);

/// Finalize array of msg/HeadMotorsData messages.
/**
 * It calls
 * movement_utils__msg__HeadMotorsData__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
void
movement_utils__msg__HeadMotorsData__Sequence__fini(movement_utils__msg__HeadMotorsData__Sequence * array);

/// Create array of msg/HeadMotorsData messages.
/**
 * It allocates the memory for the array and calls
 * movement_utils__msg__HeadMotorsData__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
movement_utils__msg__HeadMotorsData__Sequence *
movement_utils__msg__HeadMotorsData__Sequence__create(size_t size);

/// Destroy array of msg/HeadMotorsData messages.
/**
 * It calls
 * movement_utils__msg__HeadMotorsData__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
void
movement_utils__msg__HeadMotorsData__Sequence__destroy(movement_utils__msg__HeadMotorsData__Sequence * array);

/// Check for msg/HeadMotorsData message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
bool
movement_utils__msg__HeadMotorsData__Sequence__are_equal(const movement_utils__msg__HeadMotorsData__Sequence * lhs, const movement_utils__msg__HeadMotorsData__Sequence * rhs);

/// Copy an array of msg/HeadMotorsData messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
bool
movement_utils__msg__HeadMotorsData__Sequence__copy(
  const movement_utils__msg__HeadMotorsData__Sequence * input,
  movement_utils__msg__HeadMotorsData__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // MOVEMENT_UTILS__MSG__DETAIL__HEAD_MOTORS_DATA__FUNCTIONS_H_
