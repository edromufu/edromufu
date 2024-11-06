// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from potmessage:msg/Buttonmsg.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "potmessage/msg/detail/buttonmsg__struct.hpp"
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

void Buttonmsg_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) potmessage::msg::Buttonmsg(_init);
}

void Buttonmsg_fini_function(void * message_memory)
{
  auto typed_message = static_cast<potmessage::msg::Buttonmsg *>(message_memory);
  typed_message->~Buttonmsg();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Buttonmsg_message_member_array[2] = {
  {
    "bot1",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(potmessage::msg::Buttonmsg, bot1),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "bot2",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(potmessage::msg::Buttonmsg, bot2),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Buttonmsg_message_members = {
  "potmessage::msg",  // message namespace
  "Buttonmsg",  // message name
  2,  // number of fields
  sizeof(potmessage::msg::Buttonmsg),
  Buttonmsg_message_member_array,  // message members
  Buttonmsg_init_function,  // function to initialize message memory (memory has to be allocated)
  Buttonmsg_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Buttonmsg_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Buttonmsg_message_members,
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
get_message_type_support_handle<potmessage::msg::Buttonmsg>()
{
  return &::potmessage::msg::rosidl_typesupport_introspection_cpp::Buttonmsg_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, potmessage, msg, Buttonmsg)() {
  return &::potmessage::msg::rosidl_typesupport_introspection_cpp::Buttonmsg_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
