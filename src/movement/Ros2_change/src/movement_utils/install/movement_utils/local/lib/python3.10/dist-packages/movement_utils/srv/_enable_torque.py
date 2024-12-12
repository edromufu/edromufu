# generated from rosidl_generator_py/resource/_idl.py.em
# with input from movement_utils:srv/EnableTorque.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'motor_ids'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_EnableTorque_Request(type):
    """Metaclass of message 'EnableTorque_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('movement_utils')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'movement_utils.srv.EnableTorque_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__enable_torque__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__enable_torque__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__enable_torque__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__enable_torque__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__enable_torque__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class EnableTorque_Request(metaclass=Metaclass_EnableTorque_Request):
    """Message class 'EnableTorque_Request'."""

    __slots__ = [
        '_data',
        '_motor_ids',
    ]

    _fields_and_field_types = {
        'data': 'boolean',
        'motor_ids': 'sequence<int8>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('int8')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.data = kwargs.get('data', bool())
        self.motor_ids = array.array('b', kwargs.get('motor_ids', []))

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.data != other.data:
            return False
        if self.motor_ids != other.motor_ids:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def data(self):
        """Message field 'data'."""
        return self._data

    @data.setter
    def data(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'data' field must be of type 'bool'"
        self._data = value

    @builtins.property
    def motor_ids(self):
        """Message field 'motor_ids'."""
        return self._motor_ids

    @motor_ids.setter
    def motor_ids(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'b', \
                "The 'motor_ids' array.array() must have the type code of 'b'"
            self._motor_ids = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, int) for v in value) and
                 all(val >= -128 and val < 128 for val in value)), \
                "The 'motor_ids' field must be a set or sequence and each value of type 'int' and each integer in [-128, 127]"
        self._motor_ids = array.array('b', value)


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_EnableTorque_Response(type):
    """Metaclass of message 'EnableTorque_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('movement_utils')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'movement_utils.srv.EnableTorque_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__enable_torque__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__enable_torque__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__enable_torque__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__enable_torque__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__enable_torque__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class EnableTorque_Response(metaclass=Metaclass_EnableTorque_Response):
    """Message class 'EnableTorque_Response'."""

    __slots__ = [
        '_success',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.success = kwargs.get('success', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.success != other.success:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value


class Metaclass_EnableTorque(type):
    """Metaclass of service 'EnableTorque'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('movement_utils')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'movement_utils.srv.EnableTorque')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__enable_torque

            from movement_utils.srv import _enable_torque
            if _enable_torque.Metaclass_EnableTorque_Request._TYPE_SUPPORT is None:
                _enable_torque.Metaclass_EnableTorque_Request.__import_type_support__()
            if _enable_torque.Metaclass_EnableTorque_Response._TYPE_SUPPORT is None:
                _enable_torque.Metaclass_EnableTorque_Response.__import_type_support__()


class EnableTorque(metaclass=Metaclass_EnableTorque):
    from movement_utils.srv._enable_torque import EnableTorque_Request as Request
    from movement_utils.srv._enable_torque import EnableTorque_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
