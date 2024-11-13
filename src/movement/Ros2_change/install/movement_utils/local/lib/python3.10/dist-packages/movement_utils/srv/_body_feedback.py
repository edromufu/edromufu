# generated from rosidl_generator_py/resource/_idl.py.em
# with input from movement_utils:srv/BodyFeedback.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_BodyFeedback_Request(type):
    """Metaclass of message 'BodyFeedback_Request'."""

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
                'movement_utils.srv.BodyFeedback_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__body_feedback__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__body_feedback__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__body_feedback__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__body_feedback__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__body_feedback__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class BodyFeedback_Request(metaclass=Metaclass_BodyFeedback_Request):
    """Message class 'BodyFeedback_Request'."""

    __slots__ = [
        '_dont_use',
    ]

    _fields_and_field_types = {
        'dont_use': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.dont_use = kwargs.get('dont_use', bool())

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
        if self.dont_use != other.dont_use:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def dont_use(self):
        """Message field 'dont_use'."""
        return self._dont_use

    @dont_use.setter
    def dont_use(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'dont_use' field must be of type 'bool'"
        self._dont_use = value


# Import statements for member types

# already imported above
# import builtins

import math  # noqa: E402, I100

# Member 'pos_vector'
import numpy  # noqa: E402, I100

# already imported above
# import rosidl_parser.definition


class Metaclass_BodyFeedback_Response(type):
    """Metaclass of message 'BodyFeedback_Response'."""

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
                'movement_utils.srv.BodyFeedback_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__body_feedback__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__body_feedback__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__body_feedback__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__body_feedback__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__body_feedback__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class BodyFeedback_Response(metaclass=Metaclass_BodyFeedback_Response):
    """Message class 'BodyFeedback_Response'."""

    __slots__ = [
        '_pos_vector',
    ]

    _fields_and_field_types = {
        'pos_vector': 'float[18]',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 18),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        if 'pos_vector' not in kwargs:
            self.pos_vector = numpy.zeros(18, dtype=numpy.float32)
        else:
            self.pos_vector = numpy.array(kwargs.get('pos_vector'), dtype=numpy.float32)
            assert self.pos_vector.shape == (18, )

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
        if all(self.pos_vector != other.pos_vector):
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def pos_vector(self):
        """Message field 'pos_vector'."""
        return self._pos_vector

    @pos_vector.setter
    def pos_vector(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float32, \
                "The 'pos_vector' numpy.ndarray() must have the dtype of 'numpy.float32'"
            assert value.size == 18, \
                "The 'pos_vector' numpy.ndarray() must have a size of 18"
            self._pos_vector = value
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
                 len(value) == 18 and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'pos_vector' field must be a set or sequence with length 18 and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._pos_vector = numpy.array(value, dtype=numpy.float32)


class Metaclass_BodyFeedback(type):
    """Metaclass of service 'BodyFeedback'."""

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
                'movement_utils.srv.BodyFeedback')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__body_feedback

            from movement_utils.srv import _body_feedback
            if _body_feedback.Metaclass_BodyFeedback_Request._TYPE_SUPPORT is None:
                _body_feedback.Metaclass_BodyFeedback_Request.__import_type_support__()
            if _body_feedback.Metaclass_BodyFeedback_Response._TYPE_SUPPORT is None:
                _body_feedback.Metaclass_BodyFeedback_Response.__import_type_support__()


class BodyFeedback(metaclass=Metaclass_BodyFeedback):
    from movement_utils.srv._body_feedback import BodyFeedback_Request as Request
    from movement_utils.srv._body_feedback import BodyFeedback_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
