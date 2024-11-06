// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from potmessage:msg/Buttonmsg.idl
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
#include "potmessage/msg/detail/buttonmsg__struct.h"
#include "potmessage/msg/detail/buttonmsg__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool potmessage__msg__buttonmsg__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[36];
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
    assert(strncmp("potmessage.msg._buttonmsg.Buttonmsg", full_classname_dest, 35) == 0);
  }
  potmessage__msg__Buttonmsg * ros_message = _ros_message;
  {  // bot1
    PyObject * field = PyObject_GetAttrString(_pymsg, "bot1");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->bot1 = (Py_True == field);
    Py_DECREF(field);
  }
  {  // bot2
    PyObject * field = PyObject_GetAttrString(_pymsg, "bot2");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->bot2 = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * potmessage__msg__buttonmsg__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Buttonmsg */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("potmessage.msg._buttonmsg");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Buttonmsg");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  potmessage__msg__Buttonmsg * ros_message = (potmessage__msg__Buttonmsg *)raw_ros_message;
  {  // bot1
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->bot1 ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "bot1", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // bot2
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->bot2 ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "bot2", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
