// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from potmessage:msg/Imumsg.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "potmessage/msg/detail/imumsg__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace potmessage
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void Imumsg_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) potmessage::msg::Imumsg(_init);
}

void Imumsg_fini_function(void * message_memory)
{
  auto typed_message = static_cast<potmessage::msg::Imumsg *>(message_memory);
  typed_message->~Imumsg();
}

size_t size_function__Imumsg__imu(const void * untyped_member)
{
  (void)untyped_member;
  return 4;
}

const void * get_const_function__Imumsg__imu(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<float, 4> *>(untyped_member);
  return &member[index];
}

void * get_function__Imumsg__imu(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<float, 4> *>(untyped_member);
  return &member[index];
}

void fetch_function__Imumsg__imu(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__Imumsg__imu(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__Imumsg__imu(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__Imumsg__imu(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Imumsg_message_member_array[1] = {
  {
    "imu",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    4,  // array size
    false,  // is upper bound
    offsetof(potmessage::msg::Imumsg, imu),  // bytes offset in struct
    nullptr,  // default value
    size_function__Imumsg__imu,  // size() function pointer
    get_const_function__Imumsg__imu,  // get_const(index) function pointer
    get_function__Imumsg__imu,  // get(index) function pointer
    fetch_function__Imumsg__imu,  // fetch(index, &value) function pointer
    assign_function__Imumsg__imu,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Imumsg_message_members = {
  "potmessage::msg",  // message namespace
  "Imumsg",  // message name
  1,  // number of fields
  sizeof(potmessage::msg::Imumsg),
  Imumsg_message_member_array,  // message members
  Imumsg_init_function,  // function to initialize message memory (memory has to be allocated)
  Imumsg_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Imumsg_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Imumsg_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace potmessage


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<potmessage::msg::Imumsg>()
{
  return &::potmessage::msg::rosidl_typesupport_introspection_cpp::Imumsg_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, potmessage, msg, Imumsg)() {
  return &::potmessage::msg::rosidl_typesupport_introspection_cpp::Imumsg_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
