// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from movement_utils:msg/HeadMotorsData.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "movement_utils/msg/detail/head_motors_data__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace movement_utils
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void HeadMotorsData_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) movement_utils::msg::HeadMotorsData(_init);
}

void HeadMotorsData_fini_function(void * message_memory)
{
  auto typed_message = static_cast<movement_utils::msg::HeadMotorsData *>(message_memory);
  typed_message->~HeadMotorsData();
}

size_t size_function__HeadMotorsData__pos_vector(const void * untyped_member)
{
  (void)untyped_member;
  return 2;
}

const void * get_const_function__HeadMotorsData__pos_vector(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<float, 2> *>(untyped_member);
  return &member[index];
}

void * get_function__HeadMotorsData__pos_vector(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<float, 2> *>(untyped_member);
  return &member[index];
}

void fetch_function__HeadMotorsData__pos_vector(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__HeadMotorsData__pos_vector(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__HeadMotorsData__pos_vector(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__HeadMotorsData__pos_vector(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember HeadMotorsData_message_member_array[1] = {
  {
    "pos_vector",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    2,  // array size
    false,  // is upper bound
    offsetof(movement_utils::msg::HeadMotorsData, pos_vector),  // bytes offset in struct
    nullptr,  // default value
    size_function__HeadMotorsData__pos_vector,  // size() function pointer
    get_const_function__HeadMotorsData__pos_vector,  // get_const(index) function pointer
    get_function__HeadMotorsData__pos_vector,  // get(index) function pointer
    fetch_function__HeadMotorsData__pos_vector,  // fetch(index, &value) function pointer
    assign_function__HeadMotorsData__pos_vector,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers HeadMotorsData_message_members = {
  "movement_utils::msg",  // message namespace
  "HeadMotorsData",  // message name
  1,  // number of fields
  sizeof(movement_utils::msg::HeadMotorsData),
  HeadMotorsData_message_member_array,  // message members
  HeadMotorsData_init_function,  // function to initialize message memory (memory has to be allocated)
  HeadMotorsData_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t HeadMotorsData_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &HeadMotorsData_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace movement_utils


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<movement_utils::msg::HeadMotorsData>()
{
  return &::movement_utils::msg::rosidl_typesupport_introspection_cpp::HeadMotorsData_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, movement_utils, msg, HeadMotorsData)() {
  return &::movement_utils::msg::rosidl_typesupport_introspection_cpp::HeadMotorsData_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
