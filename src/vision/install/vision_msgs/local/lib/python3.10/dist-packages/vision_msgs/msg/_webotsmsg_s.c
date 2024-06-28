// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from vision_msgs:msg/Webotsmsg.idl
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
#include "vision_msgs/msg/detail/webotsmsg__struct.h"
#include "vision_msgs/msg/detail/webotsmsg__functions.h"

bool vision_msgs__msg__ball__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * vision_msgs__msg__ball__convert_to_py(void * raw_ros_message);
bool vision_msgs__msg__leftgoalpost__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * vision_msgs__msg__leftgoalpost__convert_to_py(void * raw_ros_message);
bool vision_msgs__msg__rightgoalpost__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * vision_msgs__msg__rightgoalpost__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool vision_msgs__msg__webotsmsg__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[37];
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
    assert(strncmp("vision_msgs.msg._webotsmsg.Webotsmsg", full_classname_dest, 36) == 0);
  }
  vision_msgs__msg__Webotsmsg * ros_message = _ros_message;
  {  // searching
    PyObject * field = PyObject_GetAttrString(_pymsg, "searching");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->searching = (Py_True == field);
    Py_DECREF(field);
  }
  {  // fps
    PyObject * field = PyObject_GetAttrString(_pymsg, "fps");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->fps = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // ball
    PyObject * field = PyObject_GetAttrString(_pymsg, "ball");
    if (!field) {
      return false;
    }
    if (!vision_msgs__msg__ball__convert_from_py(field, &ros_message->ball)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // leftgoalpost
    PyObject * field = PyObject_GetAttrString(_pymsg, "leftgoalpost");
    if (!field) {
      return false;
    }
    if (!vision_msgs__msg__leftgoalpost__convert_from_py(field, &ros_message->leftgoalpost)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // rightgoalpost
    PyObject * field = PyObject_GetAttrString(_pymsg, "rightgoalpost");
    if (!field) {
      return false;
    }
    if (!vision_msgs__msg__rightgoalpost__convert_from_py(field, &ros_message->rightgoalpost)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * vision_msgs__msg__webotsmsg__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Webotsmsg */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("vision_msgs.msg._webotsmsg");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Webotsmsg");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  vision_msgs__msg__Webotsmsg * ros_message = (vision_msgs__msg__Webotsmsg *)raw_ros_message;
  {  // searching
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->searching ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "searching", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // fps
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->fps);
    {
      int rc = PyObject_SetAttrString(_pymessage, "fps", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ball
    PyObject * field = NULL;
    field = vision_msgs__msg__ball__convert_to_py(&ros_message->ball);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "ball", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // leftgoalpost
    PyObject * field = NULL;
    field = vision_msgs__msg__leftgoalpost__convert_to_py(&ros_message->leftgoalpost);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "leftgoalpost", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // rightgoalpost
    PyObject * field = NULL;
    field = vision_msgs__msg__rightgoalpost__convert_to_py(&ros_message->rightgoalpost);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "rightgoalpost", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
