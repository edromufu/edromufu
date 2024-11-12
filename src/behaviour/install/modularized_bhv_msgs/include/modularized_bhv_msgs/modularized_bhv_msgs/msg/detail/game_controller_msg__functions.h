// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from modularized_bhv_msgs:msg/GameControllerMsg.idl
// generated code does not contain a copyright notice

#ifndef MODULARIZED_BHV_MSGS__MSG__DETAIL__GAME_CONTROLLER_MSG__FUNCTIONS_H_
#define MODULARIZED_BHV_MSGS__MSG__DETAIL__GAME_CONTROLLER_MSG__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "modularized_bhv_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "modularized_bhv_msgs/msg/detail/game_controller_msg__struct.h"

/// Initialize msg/GameControllerMsg message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * modularized_bhv_msgs__msg__GameControllerMsg
 * )) before or use
 * modularized_bhv_msgs__msg__GameControllerMsg__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
bool
modularized_bhv_msgs__msg__GameControllerMsg__init(modularized_bhv_msgs__msg__GameControllerMsg * msg);

/// Finalize msg/GameControllerMsg message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
void
modularized_bhv_msgs__msg__GameControllerMsg__fini(modularized_bhv_msgs__msg__GameControllerMsg * msg);

/// Create msg/GameControllerMsg message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * modularized_bhv_msgs__msg__GameControllerMsg__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
modularized_bhv_msgs__msg__GameControllerMsg *
modularized_bhv_msgs__msg__GameControllerMsg__create();

/// Destroy msg/GameControllerMsg message.
/**
 * It calls
 * modularized_bhv_msgs__msg__GameControllerMsg__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
void
modularized_bhv_msgs__msg__GameControllerMsg__destroy(modularized_bhv_msgs__msg__GameControllerMsg * msg);

/// Check for msg/GameControllerMsg message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
bool
modularized_bhv_msgs__msg__GameControllerMsg__are_equal(const modularized_bhv_msgs__msg__GameControllerMsg * lhs, const modularized_bhv_msgs__msg__GameControllerMsg * rhs);

/// Copy a msg/GameControllerMsg message.
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
modularized_bhv_msgs__msg__GameControllerMsg__copy(
  const modularized_bhv_msgs__msg__GameControllerMsg * input,
  modularized_bhv_msgs__msg__GameControllerMsg * output);

/// Initialize array of msg/GameControllerMsg messages.
/**
 * It allocates the memory for the number of elements and calls
 * modularized_bhv_msgs__msg__GameControllerMsg__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
bool
modularized_bhv_msgs__msg__GameControllerMsg__Sequence__init(modularized_bhv_msgs__msg__GameControllerMsg__Sequence * array, size_t size);

/// Finalize array of msg/GameControllerMsg messages.
/**
 * It calls
 * modularized_bhv_msgs__msg__GameControllerMsg__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
void
modularized_bhv_msgs__msg__GameControllerMsg__Sequence__fini(modularized_bhv_msgs__msg__GameControllerMsg__Sequence * array);

/// Create array of msg/GameControllerMsg messages.
/**
 * It allocates the memory for the array and calls
 * modularized_bhv_msgs__msg__GameControllerMsg__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
modularized_bhv_msgs__msg__GameControllerMsg__Sequence *
modularized_bhv_msgs__msg__GameControllerMsg__Sequence__create(size_t size);

/// Destroy array of msg/GameControllerMsg messages.
/**
 * It calls
 * modularized_bhv_msgs__msg__GameControllerMsg__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
void
modularized_bhv_msgs__msg__GameControllerMsg__Sequence__destroy(modularized_bhv_msgs__msg__GameControllerMsg__Sequence * array);

/// Check for msg/GameControllerMsg message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_modularized_bhv_msgs
bool
modularized_bhv_msgs__msg__GameControllerMsg__Sequence__are_equal(const modularized_bhv_msgs__msg__GameControllerMsg__Sequence * lhs, const modularized_bhv_msgs__msg__GameControllerMsg__Sequence * rhs);

/// Copy an array of msg/GameControllerMsg messages.
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
modularized_bhv_msgs__msg__GameControllerMsg__Sequence__copy(
  const modularized_bhv_msgs__msg__GameControllerMsg__Sequence * input,
  modularized_bhv_msgs__msg__GameControllerMsg__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // MODULARIZED_BHV_MSGS__MSG__DETAIL__GAME_CONTROLLER_MSG__FUNCTIONS_H_
