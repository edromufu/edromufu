// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from modularized_bhv_msgs:msg/GameControllerMsg.idl
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
#include "modularized_bhv_msgs/msg/detail/game_controller_msg__struct.h"
#include "modularized_bhv_msgs/msg/detail/game_controller_msg__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool modularized_bhv_msgs__msg__game_controller_msg__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[64];
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
    assert(strncmp("modularized_bhv_msgs.msg._game_controller_msg.GameControllerMsg", full_classname_dest, 63) == 0);
  }
  modularized_bhv_msgs__msg__GameControllerMsg * ros_message = _ros_message;
  {  // header
    PyObject * field = PyObject_GetAttrString(_pymsg, "header");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__header__convert_from_py(field, &ros_message->header)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // game_state
    PyObject * field = PyObject_GetAttrString(_pymsg, "game_state");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->game_state = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // secondary_state
    PyObject * field = PyObject_GetAttrString(_pymsg, "secondary_state");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->secondary_state = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // secondary_state_team
    PyObject * field = PyObject_GetAttrString(_pymsg, "secondary_state_team");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->secondary_state_team = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // secondary_state_mode
    PyObject * field = PyObject_GetAttrString(_pymsg, "secondary_state_mode");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->secondary_state_mode = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // first_half
    PyObject * field = PyObject_GetAttrString(_pymsg, "first_half");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->first_half = (Py_True == field);
    Py_DECREF(field);
  }
  {  // own_score
    PyObject * field = PyObject_GetAttrString(_pymsg, "own_score");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->own_score = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // rival_score
    PyObject * field = PyObject_GetAttrString(_pymsg, "rival_score");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->rival_score = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // seconds_remaining
    PyObject * field = PyObject_GetAttrString(_pymsg, "seconds_remaining");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->seconds_remaining = (int16_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // secondary_seconds_remaining
    PyObject * field = PyObject_GetAttrString(_pymsg, "secondary_seconds_remaining");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->secondary_seconds_remaining = (int16_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // has_kick_off
    PyObject * field = PyObject_GetAttrString(_pymsg, "has_kick_off");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->has_kick_off = (Py_True == field);
    Py_DECREF(field);
  }
  {  // penalized
    PyObject * field = PyObject_GetAttrString(_pymsg, "penalized");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->penalized = (Py_True == field);
    Py_DECREF(field);
  }
  {  // seconds_till_unpenalized
    PyObject * field = PyObject_GetAttrString(_pymsg, "seconds_till_unpenalized");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->seconds_till_unpenalized = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // team_color
    PyObject * field = PyObject_GetAttrString(_pymsg, "team_color");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->team_color = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // drop_in_team
    PyObject * field = PyObject_GetAttrString(_pymsg, "drop_in_team");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->drop_in_team = (Py_True == field);
    Py_DECREF(field);
  }
  {  // drop_in_time
    PyObject * field = PyObject_GetAttrString(_pymsg, "drop_in_time");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->drop_in_time = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // penalty_shot
    PyObject * field = PyObject_GetAttrString(_pymsg, "penalty_shot");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->penalty_shot = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // single_shots
    PyObject * field = PyObject_GetAttrString(_pymsg, "single_shots");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->single_shots = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // coach_message
    PyObject * field = PyObject_GetAttrString(_pymsg, "coach_message");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->coach_message, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // team_mates_with_penalty
    PyObject * field = PyObject_GetAttrString(_pymsg, "team_mates_with_penalty");
    if (!field) {
      return false;
    }
    if (PyObject_CheckBuffer(field)) {
      // Optimization for converting arrays of primitives
      Py_buffer view;
      int rc = PyObject_GetBuffer(field, &view, PyBUF_SIMPLE);
      if (rc < 0) {
        Py_DECREF(field);
        return false;
      }
      Py_ssize_t size = view.len / sizeof(bool);
      if (!rosidl_runtime_c__boolean__Sequence__init(&(ros_message->team_mates_with_penalty), size)) {
        PyErr_SetString(PyExc_RuntimeError, "unable to create boolean__Sequence ros_message");
        PyBuffer_Release(&view);
        Py_DECREF(field);
        return false;
      }
      bool * dest = ros_message->team_mates_with_penalty.data;
      rc = PyBuffer_ToContiguous(dest, &view, view.len, 'C');
      if (rc < 0) {
        PyBuffer_Release(&view);
        Py_DECREF(field);
        return false;
      }
      PyBuffer_Release(&view);
    } else {
      PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'team_mates_with_penalty'");
      if (!seq_field) {
        Py_DECREF(field);
        return false;
      }
      Py_ssize_t size = PySequence_Size(field);
      if (-1 == size) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
      if (!rosidl_runtime_c__boolean__Sequence__init(&(ros_message->team_mates_with_penalty), size)) {
        PyErr_SetString(PyExc_RuntimeError, "unable to create boolean__Sequence ros_message");
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
      bool * dest = ros_message->team_mates_with_penalty.data;
      for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject * item = PySequence_Fast_GET_ITEM(seq_field, i);
        if (!item) {
          Py_DECREF(seq_field);
          Py_DECREF(field);
          return false;
        }
        assert(PyBool_Check(item));
        bool tmp = (item == Py_True);
        memcpy(&dest[i], &tmp, sizeof(bool));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }
  {  // team_mates_with_red_card
    PyObject * field = PyObject_GetAttrString(_pymsg, "team_mates_with_red_card");
    if (!field) {
      return false;
    }
    if (PyObject_CheckBuffer(field)) {
      // Optimization for converting arrays of primitives
      Py_buffer view;
      int rc = PyObject_GetBuffer(field, &view, PyBUF_SIMPLE);
      if (rc < 0) {
        Py_DECREF(field);
        return false;
      }
      Py_ssize_t size = view.len / sizeof(bool);
      if (!rosidl_runtime_c__boolean__Sequence__init(&(ros_message->team_mates_with_red_card), size)) {
        PyErr_SetString(PyExc_RuntimeError, "unable to create boolean__Sequence ros_message");
        PyBuffer_Release(&view);
        Py_DECREF(field);
        return false;
      }
      bool * dest = ros_message->team_mates_with_red_card.data;
      rc = PyBuffer_ToContiguous(dest, &view, view.len, 'C');
      if (rc < 0) {
        PyBuffer_Release(&view);
        Py_DECREF(field);
        return false;
      }
      PyBuffer_Release(&view);
    } else {
      PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'team_mates_with_red_card'");
      if (!seq_field) {
        Py_DECREF(field);
        return false;
      }
      Py_ssize_t size = PySequence_Size(field);
      if (-1 == size) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
      if (!rosidl_runtime_c__boolean__Sequence__init(&(ros_message->team_mates_with_red_card), size)) {
        PyErr_SetString(PyExc_RuntimeError, "unable to create boolean__Sequence ros_message");
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
      bool * dest = ros_message->team_mates_with_red_card.data;
      for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject * item = PySequence_Fast_GET_ITEM(seq_field, i);
        if (!item) {
          Py_DECREF(seq_field);
          Py_DECREF(field);
          return false;
        }
        assert(PyBool_Check(item));
        bool tmp = (item == Py_True);
        memcpy(&dest[i], &tmp, sizeof(bool));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * modularized_bhv_msgs__msg__game_controller_msg__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of GameControllerMsg */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("modularized_bhv_msgs.msg._game_controller_msg");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "GameControllerMsg");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  modularized_bhv_msgs__msg__GameControllerMsg * ros_message = (modularized_bhv_msgs__msg__GameControllerMsg *)raw_ros_message;
  {  // header
    PyObject * field = NULL;
    field = std_msgs__msg__header__convert_to_py(&ros_message->header);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "header", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // game_state
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->game_state);
    {
      int rc = PyObject_SetAttrString(_pymessage, "game_state", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // secondary_state
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->secondary_state);
    {
      int rc = PyObject_SetAttrString(_pymessage, "secondary_state", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // secondary_state_team
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->secondary_state_team);
    {
      int rc = PyObject_SetAttrString(_pymessage, "secondary_state_team", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // secondary_state_mode
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->secondary_state_mode);
    {
      int rc = PyObject_SetAttrString(_pymessage, "secondary_state_mode", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // first_half
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->first_half ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "first_half", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // own_score
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->own_score);
    {
      int rc = PyObject_SetAttrString(_pymessage, "own_score", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // rival_score
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->rival_score);
    {
      int rc = PyObject_SetAttrString(_pymessage, "rival_score", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // seconds_remaining
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->seconds_remaining);
    {
      int rc = PyObject_SetAttrString(_pymessage, "seconds_remaining", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // secondary_seconds_remaining
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->secondary_seconds_remaining);
    {
      int rc = PyObject_SetAttrString(_pymessage, "secondary_seconds_remaining", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // has_kick_off
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->has_kick_off ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "has_kick_off", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // penalized
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->penalized ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "penalized", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // seconds_till_unpenalized
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->seconds_till_unpenalized);
    {
      int rc = PyObject_SetAttrString(_pymessage, "seconds_till_unpenalized", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // team_color
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->team_color);
    {
      int rc = PyObject_SetAttrString(_pymessage, "team_color", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // drop_in_team
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->drop_in_team ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "drop_in_team", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // drop_in_time
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->drop_in_time);
    {
      int rc = PyObject_SetAttrString(_pymessage, "drop_in_time", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // penalty_shot
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->penalty_shot);
    {
      int rc = PyObject_SetAttrString(_pymessage, "penalty_shot", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // single_shots
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->single_shots);
    {
      int rc = PyObject_SetAttrString(_pymessage, "single_shots", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // coach_message
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->coach_message.data,
      strlen(ros_message->coach_message.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "coach_message", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // team_mates_with_penalty
    PyObject * field = NULL;
    size_t size = ros_message->team_mates_with_penalty.size;
    bool * src = ros_message->team_mates_with_penalty.data;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    for (size_t i = 0; i < size; ++i) {
      int rc = PyList_SetItem(field, i, PyBool_FromLong(src[i] ? 1 : 0));
      (void)rc;
      assert(rc == 0);
    }
    assert(PySequence_Check(field));
    {
      int rc = PyObject_SetAttrString(_pymessage, "team_mates_with_penalty", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // team_mates_with_red_card
    PyObject * field = NULL;
    size_t size = ros_message->team_mates_with_red_card.size;
    bool * src = ros_message->team_mates_with_red_card.data;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    for (size_t i = 0; i < size; ++i) {
      int rc = PyList_SetItem(field, i, PyBool_FromLong(src[i] ? 1 : 0));
      (void)rc;
      assert(rc == 0);
    }
    assert(PySequence_Check(field));
    {
      int rc = PyObject_SetAttrString(_pymessage, "team_mates_with_red_card", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
