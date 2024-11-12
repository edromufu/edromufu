// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from modularized_bhv_msgs:msg/StateMachineMsg.idl
// generated code does not contain a copyright notice

#ifndef MODULARIZED_BHV_MSGS__MSG__DETAIL__STATE_MACHINE_MSG__FUNCTIONS_H_
#define MODULARIZED_BHV_MSGS__MSG__DETAIL__STATE_MACHINE_MSG__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "modularized_bhv_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "modularized_bhv_msgs/msg/detail/state_machine_msg__struct.h"

/// Initialize msg/StateMachineMsg message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * modularized_bhv_msgs__msg__StateMachineMsg
 * )) before or use
 * modularized_bhv_msgs__msg__StateMachineMsg__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
bool
modularized_bhv_msgs__msg__StateMachineMsg__init(modularized_bhv_msgs__msg__StateMachineMsg * msg);

/// Finalize msg/StateMachineMsg message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
void
modularized_bhv_msgs__msg__StateMachineMsg__fini(modularized_bhv_msgs__msg__StateMachineMsg * msg);

/// Create msg/StateMachineMsg message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * modularized_bhv_msgs__msg__StateMachineMsg__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
modularized_bhv_msgs__msg__StateMachineMsg *
modularized_bhv_msgs__msg__StateMachineMsg__create();

/// Destroy msg/StateMachineMsg message.
/**
 * It calls
 * modularized_bhv_msgs__msg__StateMachineMsg__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
void
modularized_bhv_msgs__msg__StateMachineMsg__destroy(modularized_bhv_msgs__msg__StateMachineMsg * msg);

/// Check for msg/StateMachineMsg message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
bool
modularized_bhv_msgs__msg__StateMachineMsg__are_equal(const modularized_bhv_msgs__msg__StateMachineMsg * lhs, const modularized_bhv_msgs__msg__StateMachineMsg * rhs);

/// Copy a msg/StateMachineMsg message.
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
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
bool
modularized_bhv_msgs__msg__StateMachineMsg__copy(
  const modularized_bhv_msgs__msg__StateMachineMsg * input,
  modularized_bhv_msgs__msg__StateMachineMsg * output);

/// Initialize array of msg/StateMachineMsg messages.
/**
 * It allocates the memory for the number of elements and calls
 * modularized_bhv_msgs__msg__StateMachineMsg__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
bool
modularized_bhv_msgs__msg__StateMachineMsg__Sequence__init(modularized_bhv_msgs__msg__StateMachineMsg__Sequence * array, size_t size);

/// Finalize array of msg/StateMachineMsg messages.
/**
 * It calls
 * modularized_bhv_msgs__msg__StateMachineMsg__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
void
modularized_bhv_msgs__msg__StateMachineMsg__Sequence__fini(modularized_bhv_msgs__msg__StateMachineMsg__Sequence * array);

/// Create array of msg/StateMachineMsg messages.
/**
 * It allocates the memory for the array and calls
 * modularized_bhv_msgs__msg__StateMachineMsg__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
modularized_bhv_msgs__msg__StateMachineMsg__Sequence *
modularized_bhv_msgs__msg__StateMachineMsg__Sequence__create(size_t size);

/// Destroy array of msg/StateMachineMsg messages.
/**
 * It calls
 * modularized_bhv_msgs__msg__StateMachineMsg__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
void
modularized_bhv_msgs__msg__StateMachineMsg__Sequence__destroy(modularized_bhv_msgs__msg__StateMachineMsg__Sequence * array);

/// Check for msg/StateMachineMsg message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
bool
modularized_bhv_msgs__msg__StateMachineMsg__Sequence__are_equal(const modularized_bhv_msgs__msg__StateMachineMsg__Sequence * lhs, const modularized_bhv_msgs__msg__StateMachineMsg__Sequence * rhs);

/// Copy an array of msg/StateMachineMsg messages.
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
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
bool
modularized_bhv_msgs__msg__StateMachineMsg__Sequence__copy(
  const modularized_bhv_msgs__msg__StateMachineMsg__Sequence * input,
  modularized_bhv_msgs__msg__StateMachineMsg__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // MODULARIZED_BHV_MSGS__MSG__DETAIL__STATE_MACHINE_MSG__FUNCTIONS_H_
