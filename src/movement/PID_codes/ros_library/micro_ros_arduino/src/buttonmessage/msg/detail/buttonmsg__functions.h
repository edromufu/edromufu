// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from buttonmessage:msg/Buttonmsg.idl
// generated code does not contain a copyright notice

#ifndef BUTTONMESSAGE__MSG__DETAIL__BUTTONMSG__FUNCTIONS_H_
#define BUTTONMESSAGE__MSG__DETAIL__BUTTONMSG__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "buttonmessage/msg/rosidl_generator_c__visibility_control.h"

#include "buttonmessage/msg/detail/buttonmsg__struct.h"

/// Initialize msg/Buttonmsg message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * buttonmessage__msg__Buttonmsg
 * )) before or use
 * buttonmessage__msg__Buttonmsg__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_buttonmessage
bool
buttonmessage__msg__Buttonmsg__init(buttonmessage__msg__Buttonmsg * msg);

/// Finalize msg/Buttonmsg message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_buttonmessage
void
buttonmessage__msg__Buttonmsg__fini(buttonmessage__msg__Buttonmsg * msg);

/// Create msg/Buttonmsg message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * buttonmessage__msg__Buttonmsg__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_buttonmessage
buttonmessage__msg__Buttonmsg *
buttonmessage__msg__Buttonmsg__create();

/// Destroy msg/Buttonmsg message.
/**
 * It calls
 * buttonmessage__msg__Buttonmsg__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_buttonmessage
void
buttonmessage__msg__Buttonmsg__destroy(buttonmessage__msg__Buttonmsg * msg);

/// Check for msg/Buttonmsg message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_buttonmessage
bool
buttonmessage__msg__Buttonmsg__are_equal(const buttonmessage__msg__Buttonmsg * lhs, const buttonmessage__msg__Buttonmsg * rhs);

/// Copy a msg/Buttonmsg message.
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
ROSIDL_GENERATOR_C_PUBLIC_buttonmessage
bool
buttonmessage__msg__Buttonmsg__copy(
  const buttonmessage__msg__Buttonmsg * input,
  buttonmessage__msg__Buttonmsg * output);

/// Initialize array of msg/Buttonmsg messages.
/**
 * It allocates the memory for the number of elements and calls
 * buttonmessage__msg__Buttonmsg__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_buttonmessage
bool
buttonmessage__msg__Buttonmsg__Sequence__init(buttonmessage__msg__Buttonmsg__Sequence * array, size_t size);

/// Finalize array of msg/Buttonmsg messages.
/**
 * It calls
 * buttonmessage__msg__Buttonmsg__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_buttonmessage
void
buttonmessage__msg__Buttonmsg__Sequence__fini(buttonmessage__msg__Buttonmsg__Sequence * array);

/// Create array of msg/Buttonmsg messages.
/**
 * It allocates the memory for the array and calls
 * buttonmessage__msg__Buttonmsg__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_buttonmessage
buttonmessage__msg__Buttonmsg__Sequence *
buttonmessage__msg__Buttonmsg__Sequence__create(size_t size);

/// Destroy array of msg/Buttonmsg messages.
/**
 * It calls
 * buttonmessage__msg__Buttonmsg__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_buttonmessage
void
buttonmessage__msg__Buttonmsg__Sequence__destroy(buttonmessage__msg__Buttonmsg__Sequence * array);

/// Check for msg/Buttonmsg message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_buttonmessage
bool
buttonmessage__msg__Buttonmsg__Sequence__are_equal(const buttonmessage__msg__Buttonmsg__Sequence * lhs, const buttonmessage__msg__Buttonmsg__Sequence * rhs);

/// Copy an array of msg/Buttonmsg messages.
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
ROSIDL_GENERATOR_C_PUBLIC_buttonmessage
bool
buttonmessage__msg__Buttonmsg__Sequence__copy(
  const buttonmessage__msg__Buttonmsg__Sequence * input,
  buttonmessage__msg__Buttonmsg__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // BUTTONMESSAGE__MSG__DETAIL__BUTTONMSG__FUNCTIONS_H_
