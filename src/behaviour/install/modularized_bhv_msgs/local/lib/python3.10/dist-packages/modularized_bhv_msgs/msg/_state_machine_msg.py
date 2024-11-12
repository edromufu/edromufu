# generated from rosidl_generator_py/resource/_idl.py.em
# with input from modularized_bhv_msgs:msg/StateMachineMsg.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_StateMachineMsg(type):
    """Metaclass of message 'StateMachineMsg'."""

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
            module = import_type_support('modularized_bhv_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'modularized_bhv_msgs.msg.StateMachineMsg')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__state_machine_msg
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__state_machine_msg
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__state_machine_msg
            cls._TYPE_SUPPORT = module.type_support_msg__msg__state_machine_msg
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__state_machine_msg

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class StateMachineMsg(metaclass=Metaclass_StateMachineMsg):
    """Message class 'StateMachineMsg'."""

    __slots__ = [
        '_ball_position',
        '_ball_close',
        '_ball_found',
        '_fall_state',
        '_hor_motor_out_of_center',
        '_head_kick_check',
    ]

    _fields_and_field_types = {
        'ball_position': 'string',
        'ball_close': 'boolean',
        'ball_found': 'boolean',
        'fall_state': 'string',
        'hor_motor_out_of_center': 'string',
        'head_kick_check': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.ball_position = kwargs.get('ball_position', str())
        self.ball_close = kwargs.get('ball_close', bool())
        self.ball_found = kwargs.get('ball_found', bool())
        self.fall_state = kwargs.get('fall_state', str())
        self.hor_motor_out_of_center = kwargs.get('hor_motor_out_of_center', str())
        self.head_kick_check = kwargs.get('head_kick_check', bool())

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
        if self.ball_position != other.ball_position:
            return False
        if self.ball_close != other.ball_close:
            return False
        if self.ball_found != other.ball_found:
            return False
        if self.fall_state != other.fall_state:
            return False
        if self.hor_motor_out_of_center != other.hor_motor_out_of_center:
            return False
        if self.head_kick_check != other.head_kick_check:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def ball_position(self):
        """Message field 'ball_position'."""
        return self._ball_position

    @ball_position.setter
    def ball_position(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'ball_position' field must be of type 'str'"
        self._ball_position = value

    @builtins.property
    def ball_close(self):
        """Message field 'ball_close'."""
        return self._ball_close

    @ball_close.setter
    def ball_close(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'ball_close' field must be of type 'bool'"
        self._ball_close = value

    @builtins.property
    def ball_found(self):
        """Message field 'ball_found'."""
        return self._ball_found

    @ball_found.setter
    def ball_found(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'ball_found' field must be of type 'bool'"
        self._ball_found = value

    @builtins.property
    def fall_state(self):
        """Message field 'fall_state'."""
        return self._fall_state

    @fall_state.setter
    def fall_state(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'fall_state' field must be of type 'str'"
        self._fall_state = value

    @builtins.property
    def hor_motor_out_of_center(self):
        """Message field 'hor_motor_out_of_center'."""
        return self._hor_motor_out_of_center

    @hor_motor_out_of_center.setter
    def hor_motor_out_of_center(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'hor_motor_out_of_center' field must be of type 'str'"
        self._hor_motor_out_of_center = value

    @builtins.property
    def head_kick_check(self):
        """Message field 'head_kick_check'."""
        return self._head_kick_check

    @head_kick_check.setter
    def head_kick_check(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'head_kick_check' field must be of type 'bool'"
        self._head_kick_check = value
