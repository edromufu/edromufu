// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from vision_msgs:msg/Leftgoalpost.idl
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
#include "vision_msgs/msg/detail/leftgoalpost__struct.h"
#include "vision_msgs/msg/detail/leftgoalpost__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool vision_msgs__msg__leftgoalpost__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[43];
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
    assert(strncmp("vision_msgs.msg._leftgoalpost.Leftgoalpost", full_classname_dest, 42) == 0);
  }
  vision_msgs__msg__Leftgoalpost * ros_message = _ros_message;
  {  // found
    PyObject * field = PyObject_GetAttrString(_pymsg, "found");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->found = (Py_True == field);
    Py_DECREF(field);
  }
  {  // x
    PyObject * field = PyObject_GetAttrString(_pymsg, "x");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->x = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // y
    PyObject * field = PyObject_GetAttrString(_pymsg, "y");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->y = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // roi_width
    PyObject * field = PyObject_GetAttrString(_pymsg, "roi_width");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->roi_width = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // roi_height
    PyObject * field = PyObject_GetAttrString(_pymsg, "roi_height");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->roi_height = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * vision_msgs__msg__leftgoalpost__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Leftgoalpost */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("vision_msgs.msg._leftgoalpost");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Leftgoalpost");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  vision_msgs__msg__Leftgoalpost * ros_message = (vision_msgs__msg__Leftgoalpost *)raw_ros_message;
  {  // found
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->found ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "found", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // x
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // y
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // roi_width
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->roi_width);
    {
      int rc = PyObject_SetAttrString(_pymessage, "roi_width", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // roi_height
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->roi_height);
    {
      int rc = PyObject_SetAttrString(_pymessage, "roi_height", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
