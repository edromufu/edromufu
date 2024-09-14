// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from imumessage:msg/Imumsg.idl
// generated code does not contain a copyright notice

#ifndef IMUMESSAGE__MSG__DETAIL__IMUMSG__FUNCTIONS_H_
#define IMUMESSAGE__MSG__DETAIL__IMUMSG__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "imumessage/msg/rosidl_generator_c__visibility_control.h"

#include "imumessage/msg/detail/imumsg__struct.h"

/// Initialize msg/Imumsg message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * imumessage__msg__Imumsg
 * )) before or use
 * imumessage__msg__Imumsg__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_imumessage
bool
imumessage__msg__Imumsg__init(imumessage__msg__Imumsg * msg);

/// Finalize msg/Imumsg message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_imumessage
void
imumessage__msg__Imumsg__fini(imumessage__msg__Imumsg * msg);

/// Create msg/Imumsg message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * imumessage__msg__Imumsg__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_imumessage
imumessage__msg__Imumsg *
imumessage__msg__Imumsg__create();

/// Destroy msg/Imumsg message.
/**
 * It calls
 * imumessage__msg__Imumsg__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_imumessage
void
imumessage__msg__Imumsg__destroy(imumessage__msg__Imumsg * msg);

/// Check for msg/Imumsg message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_imumessage
bool
imumessage__msg__Imumsg__are_equal(const imumessage__msg__Imumsg * lhs, const imumessage__msg__Imumsg * rhs);

/// Copy a msg/Imumsg message.
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
ROSIDL_GENERATOR_C_PUBLIC_imumessage
bool
imumessage__msg__Imumsg__copy(
  const imumessage__msg__Imumsg * input,
  imumessage__msg__Imumsg * output);

/// Initialize array of msg/Imumsg messages.
/**
 * It allocates the memory for the number of elements and calls
 * imumessage__msg__Imumsg__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_imumessage
bool
imumessage__msg__Imumsg__Sequence__init(imumessage__msg__Imumsg__Sequence * array, size_t size);

/// Finalize array of msg/Imumsg messages.
/**
 * It calls
 * imumessage__msg__Imumsg__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_imumessage
void
imumessage__msg__Imumsg__Sequence__fini(imumessage__msg__Imumsg__Sequence * array);

/// Create array of msg/Imumsg messages.
/**
 * It allocates the memory for the array and calls
 * imumessage__msg__Imumsg__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_imumessage
imumessage__msg__Imumsg__Sequence *
imumessage__msg__Imumsg__Sequence__create(size_t size);

/// Destroy array of msg/Imumsg messages.
/**
 * It calls
 * imumessage__msg__Imumsg__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_imumessage
void
imumessage__msg__Imumsg__Sequence__destroy(imumessage__msg__Imumsg__Sequence * array);

/// Check for msg/Imumsg message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_imumessage
bool
imumessage__msg__Imumsg__Sequence__are_equal(const imumessage__msg__Imumsg__Sequence * lhs, const imumessage__msg__Imumsg__Sequence * rhs);

/// Copy an array of msg/Imumsg messages.
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
ROSIDL_GENERATOR_C_PUBLIC_imumessage
bool
imumessage__msg__Imumsg__Sequence__copy(
  const imumessage__msg__Imumsg__Sequence * input,
  imumessage__msg__Imumsg__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // IMUMESSAGE__MSG__DETAIL__IMUMSG__FUNCTIONS_H_
