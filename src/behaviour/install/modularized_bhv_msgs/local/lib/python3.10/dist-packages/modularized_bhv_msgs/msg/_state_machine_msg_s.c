// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from modularized_bhv_msgs:msg/StateMachineMsg.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "modularized_bhv_msgs/msg/detail/state_machine_msg__struct.h"
#include "modularized_bhv_msgs/msg/detail/state_machine_msg__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool modularized_bhv_msgs__msg__state_machine_msg__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[60];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("modularized_bhv_msgs.msg._state_machine_msg.StateMachineMsg", full_classname_dest, 59) == 0);
  }
  modularized_bhv_msgs__msg__StateMachineMsg * ros_message = _ros_message;
  {  // ball_position
    PyObject * field = PyObject_GetAttrString(_pymsg, "ball_position");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->ball_position, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // ball_close
    PyObject * field = PyObject_GetAttrString(_pymsg, "ball_close");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->ball_close = (Py_True == field);
    Py_DECREF(field);
  }
  {  // ball_found
    PyObject * field = PyObject_GetAttrString(_pymsg, "ball_found");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->ball_found = (Py_True == field);
    Py_DECREF(field);
  }
  {  // fall_state
    PyObject * field = PyObject_GetAttrString(_pymsg, "fall_state");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->fall_state, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // hor_motor_out_of_center
    PyObject * field = PyObject_GetAttrString(_pymsg, "hor_motor_out_of_center");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->hor_motor_out_of_center, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // head_kick_check
    PyObject * field = PyObject_GetAttrString(_pymsg, "head_kick_check");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->head_kick_check = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * modularized_bhv_msgs__msg__state_machine_msg__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of StateMachineMsg */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("modularized_bhv_msgs.msg._state_machine_msg");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "StateMachineMsg");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  modularized_bhv_msgs__msg__StateMachineMsg * ros_message = (modularized_bhv_msgs__msg__StateMachineMsg *)raw_ros_message;
  {  // ball_position
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->ball_position.data,
      strlen(ros_message->ball_position.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "ball_position", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ball_close
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->ball_close ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ball_close", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ball_found
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->ball_found ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ball_found", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // fall_state
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->fall_state.data,
      strlen(ros_message->fall_state.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "fall_state", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // hor_motor_out_of_center
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->hor_motor_out_of_center.data,
      strlen(ros_message->hor_motor_out_of_center.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "hor_motor_out_of_center", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // head_kick_check
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->head_kick_check ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "head_kick_check", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
