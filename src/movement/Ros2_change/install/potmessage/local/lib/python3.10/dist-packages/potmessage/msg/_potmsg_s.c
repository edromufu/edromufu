// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from potmessage:msg/Potmsg.idl
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
#include "potmessage/msg/detail/potmsg__struct.h"
#include "potmessage/msg/detail/potmsg__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool potmessage__msg__potmsg__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[30];
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
    assert(strncmp("potmessage.msg._potmsg.Potmsg", full_classname_dest, 29) == 0);
  }
  potmessage__msg__Potmsg * ros_message = _ros_message;
  {  // pot1
    PyObject * field = PyObject_GetAttrString(_pymsg, "pot1");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->pot1 = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // pot2
    PyObject * field = PyObject_GetAttrString(_pymsg, "pot2");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->pot2 = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // pot3
    PyObject * field = PyObject_GetAttrString(_pymsg, "pot3");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->pot3 = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // pot4
    PyObject * field = PyObject_GetAttrString(_pymsg, "pot4");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->pot4 = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // pot5
    PyObject * field = PyObject_GetAttrString(_pymsg, "pot5");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->pot5 = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // pot6
    PyObject * field = PyObject_GetAttrString(_pymsg, "pot6");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->pot6 = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // pot7
    PyObject * field = PyObject_GetAttrString(_pymsg, "pot7");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->pot7 = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // pot8
    PyObject * field = PyObject_GetAttrString(_pymsg, "pot8");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->pot8 = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // imu1
    PyObject * field = PyObject_GetAttrString(_pymsg, "imu1");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->imu1 = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // imu2
    PyObject * field = PyObject_GetAttrString(_pymsg, "imu2");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->imu2 = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // imu3
    PyObject * field = PyObject_GetAttrString(_pymsg, "imu3");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->imu3 = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * potmessage__msg__potmsg__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Potmsg */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("potmessage.msg._potmsg");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Potmsg");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  potmessage__msg__Potmsg * ros_message = (potmessage__msg__Potmsg *)raw_ros_message;
  {  // pot1
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->pot1);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pot1", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pot2
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->pot2);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pot2", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pot3
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->pot3);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pot3", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pot4
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->pot4);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pot4", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pot5
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->pot5);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pot5", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pot6
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->pot6);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pot6", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pot7
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->pot7);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pot7", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pot8
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->pot8);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pot8", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // imu1
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->imu1);
    {
      int rc = PyObject_SetAttrString(_pymessage, "imu1", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // imu2
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->imu2);
    {
      int rc = PyObject_SetAttrString(_pymessage, "imu2", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // imu3
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->imu3);
    {
      int rc = PyObject_SetAttrString(_pymessage, "imu3", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
