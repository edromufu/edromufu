// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from movement_utils:srv/EnableTorque.idl
// generated code does not contain a copyright notice

#ifndef MOVEMENT_UTILS__SRV__DETAIL__ENABLE_TORQUE__FUNCTIONS_H_
#define MOVEMENT_UTILS__SRV__DETAIL__ENABLE_TORQUE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "movement_utils/msg/rosidl_generator_c__visibility_control.h"

#include "movement_utils/srv/detail/enable_torque__struct.h"

/// Initialize srv/EnableTorque message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * movement_utils__srv__EnableTorque_Request
 * )) before or use
 * movement_utils__srv__EnableTorque_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
bool
movement_utils__srv__EnableTorque_Request__init(movement_utils__srv__EnableTorque_Request * msg);

/// Finalize srv/EnableTorque message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
void
movement_utils__srv__EnableTorque_Request__fini(movement_utils__srv__EnableTorque_Request * msg);

/// Create srv/EnableTorque message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * movement_utils__srv__EnableTorque_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
movement_utils__srv__EnableTorque_Request *
movement_utils__srv__EnableTorque_Request__create();

/// Destroy srv/EnableTorque message.
/**
 * It calls
 * movement_utils__srv__EnableTorque_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
void
movement_utils__srv__EnableTorque_Request__destroy(movement_utils__srv__EnableTorque_Request * msg);

/// Check for srv/EnableTorque message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
bool
movement_utils__srv__EnableTorque_Request__are_equal(const movement_utils__srv__EnableTorque_Request * lhs, const movement_utils__srv__EnableTorque_Request * rhs);

/// Copy a srv/EnableTorque message.
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
movement_utils__srv__EnableTorque_Request__copy(
  const movement_utils__srv__EnableTorque_Request * input,
  movement_utils__srv__EnableTorque_Request * output);

/// Initialize array of srv/EnableTorque messages.
/**
 * It allocates the memory for the number of elements and calls
 * movement_utils__srv__EnableTorque_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
bool
movement_utils__srv__EnableTorque_Request__Sequence__init(movement_utils__srv__EnableTorque_Request__Sequence * array, size_t size);

/// Finalize array of srv/EnableTorque messages.
/**
 * It calls
 * movement_utils__srv__EnableTorque_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
void
movement_utils__srv__EnableTorque_Request__Sequence__fini(movement_utils__srv__EnableTorque_Request__Sequence * array);

/// Create array of srv/EnableTorque messages.
/**
 * It allocates the memory for the array and calls
 * movement_utils__srv__EnableTorque_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
movement_utils__srv__EnableTorque_Request__Sequence *
movement_utils__srv__EnableTorque_Request__Sequence__create(size_t size);

/// Destroy array of srv/EnableTorque messages.
/**
 * It calls
 * movement_utils__srv__EnableTorque_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
void
movement_utils__srv__EnableTorque_Request__Sequence__destroy(movement_utils__srv__EnableTorque_Request__Sequence * array);

/// Check for srv/EnableTorque message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
bool
movement_utils__srv__EnableTorque_Request__Sequence__are_equal(const movement_utils__srv__EnableTorque_Request__Sequence * lhs, const movement_utils__srv__EnableTorque_Request__Sequence * rhs);

/// Copy an array of srv/EnableTorque messages.
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
movement_utils__srv__EnableTorque_Request__Sequence__copy(
  const movement_utils__srv__EnableTorque_Request__Sequence * input,
  movement_utils__srv__EnableTorque_Request__Sequence * output);

/// Initialize srv/EnableTorque message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * movement_utils__srv__EnableTorque_Response
 * )) before or use
 * movement_utils__srv__EnableTorque_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
bool
movement_utils__srv__EnableTorque_Response__init(movement_utils__srv__EnableTorque_Response * msg);

/// Finalize srv/EnableTorque message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
void
movement_utils__srv__EnableTorque_Response__fini(movement_utils__srv__EnableTorque_Response * msg);

/// Create srv/EnableTorque message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * movement_utils__srv__EnableTorque_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
movement_utils__srv__EnableTorque_Response *
movement_utils__srv__EnableTorque_Response__create();

/// Destroy srv/EnableTorque message.
/**
 * It calls
 * movement_utils__srv__EnableTorque_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
void
movement_utils__srv__EnableTorque_Response__destroy(movement_utils__srv__EnableTorque_Response * msg);

/// Check for srv/EnableTorque message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
bool
movement_utils__srv__EnableTorque_Response__are_equal(const movement_utils__srv__EnableTorque_Response * lhs, const movement_utils__srv__EnableTorque_Response * rhs);

/// Copy a srv/EnableTorque message.
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
movement_utils__srv__EnableTorque_Response__copy(
  const movement_utils__srv__EnableTorque_Response * input,
  movement_utils__srv__EnableTorque_Response * output);

/// Initialize array of srv/EnableTorque messages.
/**
 * It allocates the memory for the number of elements and calls
 * movement_utils__srv__EnableTorque_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
bool
movement_utils__srv__EnableTorque_Response__Sequence__init(movement_utils__srv__EnableTorque_Response__Sequence * array, size_t size);

/// Finalize array of srv/EnableTorque messages.
/**
 * It calls
 * movement_utils__srv__EnableTorque_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
void
movement_utils__srv__EnableTorque_Response__Sequence__fini(movement_utils__srv__EnableTorque_Response__Sequence * array);

/// Create array of srv/EnableTorque messages.
/**
 * It allocates the memory for the array and calls
 * movement_utils__srv__EnableTorque_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
movement_utils__srv__EnableTorque_Response__Sequence *
movement_utils__srv__EnableTorque_Response__Sequence__create(size_t size);

/// Destroy array of srv/EnableTorque messages.
/**
 * It calls
 * movement_utils__srv__EnableTorque_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
void
movement_utils__srv__EnableTorque_Response__Sequence__destroy(movement_utils__srv__EnableTorque_Response__Sequence * array);

/// Check for srv/EnableTorque message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_movement_utils
bool
movement_utils__srv__EnableTorque_Response__Sequence__are_equal(const movement_utils__srv__EnableTorque_Response__Sequence * lhs, const movement_utils__srv__EnableTorque_Response__Sequence * rhs);

/// Copy an array of srv/EnableTorque messages.
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
movement_utils__srv__EnableTorque_Response__Sequence__copy(
  const movement_utils__srv__EnableTorque_Response__Sequence * input,
  movement_utils__srv__EnableTorque_Response__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // MOVEMENT_UTILS__SRV__DETAIL__ENABLE_TORQUE__FUNCTIONS_H_
