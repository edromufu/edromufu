// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from movement_utils:srv/WalkForward.idl
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
#include "movement_utils/srv/detail/walk_forward__struct.h"
#include "movement_utils/srv/detail/walk_forward__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool movement_utils__srv__walk_forward__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[53];
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
    assert(strncmp("movement_utils.srv._walk_forward.WalkForward_Request", full_classname_dest, 52) == 0);
  }
  movement_utils__srv__WalkForward_Request * ros_message = _ros_message;
  {  // support_foot
    PyObject * field = PyObject_GetAttrString(_pymsg, "support_foot");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->support_foot = (int8_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // steps_number
    PyObject * field = PyObject_GetAttrString(_pymsg, "steps_number");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->steps_number = (int8_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * movement_utils__srv__walk_forward__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of WalkForward_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("movement_utils.srv._walk_forward");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "WalkForward_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  movement_utils__srv__WalkForward_Request * ros_message = (movement_utils__srv__WalkForward_Request *)raw_ros_message;
  {  // support_foot
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->support_foot);
    {
      int rc = PyObject_SetAttrString(_pymessage, "support_foot", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // steps_number
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->steps_number);
    {
      int rc = PyObject_SetAttrString(_pymessage, "steps_number", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "movement_utils/srv/detail/walk_forward__struct.h"
// already included above
// #include "movement_utils/srv/detail/walk_forward__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool movement_utils__srv__walk_forward__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[54];
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
    assert(strncmp("movement_utils.srv._walk_forward.WalkForward_Response", full_classname_dest, 53) == 0);
  }
  movement_utils__srv__WalkForward_Response * ros_message = _ros_message;
  {  // success
    PyObject * field = PyObject_GetAttrString(_pymsg, "success");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->success = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * movement_utils__srv__walk_forward__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of WalkForward_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("movement_utils.srv._walk_forward");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "WalkForward_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  movement_utils__srv__WalkForward_Response * ros_message = (movement_utils__srv__WalkForward_Response *)raw_ros_message;
  {  // success
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->success ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "success", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
