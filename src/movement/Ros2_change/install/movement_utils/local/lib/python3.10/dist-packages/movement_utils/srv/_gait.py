# generated from rosidl_generator_py/resource/_idl.py.em
# with input from movement_utils:srv/Gait.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Gait_Request(type):
    """Metaclass of message 'Gait_Request'."""

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
                'movement_utils.srv.Gait_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__gait__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__gait__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__gait__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__gait__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__gait__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Gait_Request(metaclass=Metaclass_Gait_Request):
    """Message class 'Gait_Request'."""

    __slots__ = [
        '_steps_number',
        '_step_height',
    ]

    _fields_and_field_types = {
        'steps_number': 'int8',
        'step_height': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.steps_number = kwargs.get('steps_number', int())
        self.step_height = kwargs.get('step_height', float())

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
        if self.steps_number != other.steps_number:
            return False
        if self.step_height != other.step_height:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def steps_number(self):
        """Message field 'steps_number'."""
        return self._steps_number

    @steps_number.setter
    def steps_number(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'steps_number' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'steps_number' field must be an integer in [-128, 127]"
        self._steps_number = value

    @builtins.property
    def step_height(self):
        """Message field 'step_height'."""
        return self._step_height

    @step_height.setter
    def step_height(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'step_height' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'step_height' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._step_height = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_Gait_Response(type):
    """Metaclass of message 'Gait_Response'."""

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
                'movement_utils.srv.Gait_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__gait__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__gait__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__gait__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__gait__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__gait__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Gait_Response(metaclass=Metaclass_Gait_Response):
    """Message class 'Gait_Response'."""

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


class Metaclass_Gait(type):
    """Metaclass of service 'Gait'."""

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
                'movement_utils.srv.Gait')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__gait

            from movement_utils.srv import _gait
            if _gait.Metaclass_Gait_Request._TYPE_SUPPORT is None:
                _gait.Metaclass_Gait_Request.__import_type_support__()
            if _gait.Metaclass_Gait_Response._TYPE_SUPPORT is None:
                _gait.Metaclass_Gait_Response.__import_type_support__()


class Gait(metaclass=Metaclass_Gait):
    from movement_utils.srv._gait import Gait_Request as Request
    from movement_utils.srv._gait import Gait_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
