# generated from rosidl_generator_py/resource/_idl.py.em
# with input from movement_utils:srv/WalkForward.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_WalkForward_Request(type):
    """Metaclass of message 'WalkForward_Request'."""

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
                'movement_utils.srv.WalkForward_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__walk_forward__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__walk_forward__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__walk_forward__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__walk_forward__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__walk_forward__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class WalkForward_Request(metaclass=Metaclass_WalkForward_Request):
    """Message class 'WalkForward_Request'."""

    __slots__ = [
        '_support_foot',
        '_steps_number',
    ]

    _fields_and_field_types = {
        'support_foot': 'int8',
        'steps_number': 'int8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.support_foot = kwargs.get('support_foot', int())
        self.steps_number = kwargs.get('steps_number', int())

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
        if self.support_foot != other.support_foot:
            return False
        if self.steps_number != other.steps_number:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def support_foot(self):
        """Message field 'support_foot'."""
        return self._support_foot

    @support_foot.setter
    def support_foot(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'support_foot' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'support_foot' field must be an integer in [-128, 127]"
        self._support_foot = value

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


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_WalkForward_Response(type):
    """Metaclass of message 'WalkForward_Response'."""

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
                'movement_utils.srv.WalkForward_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__walk_forward__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__walk_forward__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__walk_forward__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__walk_forward__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__walk_forward__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class WalkForward_Response(metaclass=Metaclass_WalkForward_Response):
    """Message class 'WalkForward_Response'."""

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


class Metaclass_WalkForward(type):
    """Metaclass of service 'WalkForward'."""

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
                'movement_utils.srv.WalkForward')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__walk_forward

            from movement_utils.srv import _walk_forward
            if _walk_forward.Metaclass_WalkForward_Request._TYPE_SUPPORT is None:
                _walk_forward.Metaclass_WalkForward_Request.__import_type_support__()
            if _walk_forward.Metaclass_WalkForward_Response._TYPE_SUPPORT is None:
                _walk_forward.Metaclass_WalkForward_Response.__import_type_support__()


class WalkForward(metaclass=Metaclass_WalkForward):
    from movement_utils.srv._walk_forward import WalkForward_Request as Request
    from movement_utils.srv._walk_forward import WalkForward_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
