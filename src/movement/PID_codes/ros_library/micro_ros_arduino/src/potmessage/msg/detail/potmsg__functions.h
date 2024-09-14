// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from potmessage:msg/Potmsg.idl
// generated code does not contain a copyright notice

#ifndef POTMESSAGE__MSG__DETAIL__POTMSG__FUNCTIONS_H_
#define POTMESSAGE__MSG__DETAIL__POTMSG__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "potmessage/msg/rosidl_generator_c__visibility_control.h"

#include "potmessage/msg/detail/potmsg__struct.h"

/// Initialize msg/Potmsg message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * potmessage__msg__Potmsg
 * )) before or use
 * potmessage__msg__Potmsg__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_potmessage
bool
potmessage__msg__Potmsg__init(potmessage__msg__Potmsg * msg);

/// Finalize msg/Potmsg message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_potmessage
void
potmessage__msg__Potmsg__fini(potmessage__msg__Potmsg * msg);

/// Create msg/Potmsg message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * potmessage__msg__Potmsg__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_potmessage
potmessage__msg__Potmsg *
potmessage__msg__Potmsg__create();

/// Destroy msg/Potmsg message.
/**
 * It calls
 * potmessage__msg__Potmsg__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_potmessage
void
potmessage__msg__Potmsg__destroy(potmessage__msg__Potmsg * msg);

/// Check for msg/Potmsg message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_potmessage
bool
potmessage__msg__Potmsg__are_equal(const potmessage__msg__Potmsg * lhs, const potmessage__msg__Potmsg * rhs);

/// Copy a msg/Potmsg message.
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
ROSIDL_GENERATOR_C_PUBLIC_potmessage
bool
potmessage__msg__Potmsg__copy(
  const potmessage__msg__Potmsg * input,
  potmessage__msg__Potmsg * output);

/// Initialize array of msg/Potmsg messages.
/**
 * It allocates the memory for the number of elements and calls
 * potmessage__msg__Potmsg__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_potmessage
bool
potmessage__msg__Potmsg__Sequence__init(potmessage__msg__Potmsg__Sequence * array, size_t size);

/// Finalize array of msg/Potmsg messages.
/**
 * It calls
 * potmessage__msg__Potmsg__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_potmessage
void
potmessage__msg__Potmsg__Sequence__fini(potmessage__msg__Potmsg__Sequence * array);

/// Create array of msg/Potmsg messages.
/**
 * It allocates the memory for the array and calls
 * potmessage__msg__Potmsg__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_potmessage
potmessage__msg__Potmsg__Sequence *
potmessage__msg__Potmsg__Sequence__create(size_t size);

/// Destroy array of msg/Potmsg messages.
/**
 * It calls
 * potmessage__msg__Potmsg__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_potmessage
void
potmessage__msg__Potmsg__Sequence__destroy(potmessage__msg__Potmsg__Sequence * array);

/// Check for msg/Potmsg message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_potmessage
bool
potmessage__msg__Potmsg__Sequence__are_equal(const potmessage__msg__Potmsg__Sequence * lhs, const potmessage__msg__Potmsg__Sequence * rhs);

/// Copy an array of msg/Potmsg messages.
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
ROSIDL_GENERATOR_C_PUBLIC_potmessage
bool
potmessage__msg__Potmsg__Sequence__copy(
  const potmessage__msg__Potmsg__Sequence * input,
  potmessage__msg__Potmsg__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // POTMESSAGE__MSG__DETAIL__POTMSG__FUNCTIONS_H_
