# generated from rosidl_generator_py/resource/_idl.py.em
# with input from vision_msgs:msg/Webotsmsg.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Webotsmsg(type):
    """Metaclass of message 'Webotsmsg'."""

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
            module = import_type_support('vision_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'vision_msgs.msg.Webotsmsg')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__webotsmsg
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__webotsmsg
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__webotsmsg
            cls._TYPE_SUPPORT = module.type_support_msg__msg__webotsmsg
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__webotsmsg

            from vision_msgs.msg import Ball
            if Ball.__class__._TYPE_SUPPORT is None:
                Ball.__class__.__import_type_support__()

            from vision_msgs.msg import Leftgoalpost
            if Leftgoalpost.__class__._TYPE_SUPPORT is None:
                Leftgoalpost.__class__.__import_type_support__()

            from vision_msgs.msg import Rightgoalpost
            if Rightgoalpost.__class__._TYPE_SUPPORT is None:
                Rightgoalpost.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Webotsmsg(metaclass=Metaclass_Webotsmsg):
    """Message class 'Webotsmsg'."""

    __slots__ = [
        '_searching',
        '_fps',
        '_ball',
        '_leftgoalpost',
        '_rightgoalpost',
    ]

    _fields_and_field_types = {
        'searching': 'boolean',
        'fps': 'uint8',
        'ball': 'vision_msgs/Ball',
        'leftgoalpost': 'vision_msgs/Leftgoalpost',
        'rightgoalpost': 'vision_msgs/Rightgoalpost',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['vision_msgs', 'msg'], 'Ball'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['vision_msgs', 'msg'], 'Leftgoalpost'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['vision_msgs', 'msg'], 'Rightgoalpost'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.searching = kwargs.get('searching', bool())
        self.fps = kwargs.get('fps', int())
        from vision_msgs.msg import Ball
        self.ball = kwargs.get('ball', Ball())
        from vision_msgs.msg import Leftgoalpost
        self.leftgoalpost = kwargs.get('leftgoalpost', Leftgoalpost())
        from vision_msgs.msg import Rightgoalpost
        self.rightgoalpost = kwargs.get('rightgoalpost', Rightgoalpost())

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
        if self.searching != other.searching:
            return False
        if self.fps != other.fps:
            return False
        if self.ball != other.ball:
            return False
        if self.leftgoalpost != other.leftgoalpost:
            return False
        if self.rightgoalpost != other.rightgoalpost:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def searching(self):
        """Message field 'searching'."""
        return self._searching

    @searching.setter
    def searching(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'searching' field must be of type 'bool'"
        self._searching = value

    @builtins.property
    def fps(self):
        """Message field 'fps'."""
        return self._fps

    @fps.setter
    def fps(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'fps' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'fps' field must be an unsigned integer in [0, 255]"
        self._fps = value

    @builtins.property
    def ball(self):
        """Message field 'ball'."""
        return self._ball

    @ball.setter
    def ball(self, value):
        if __debug__:
            from vision_msgs.msg import Ball
            assert \
                isinstance(value, Ball), \
                "The 'ball' field must be a sub message of type 'Ball'"
        self._ball = value

    @builtins.property
    def leftgoalpost(self):
        """Message field 'leftgoalpost'."""
        return self._leftgoalpost

    @leftgoalpost.setter
    def leftgoalpost(self, value):
        if __debug__:
            from vision_msgs.msg import Leftgoalpost
            assert \
                isinstance(value, Leftgoalpost), \
                "The 'leftgoalpost' field must be a sub message of type 'Leftgoalpost'"
        self._leftgoalpost = value

    @builtins.property
    def rightgoalpost(self):
        """Message field 'rightgoalpost'."""
        return self._rightgoalpost

    @rightgoalpost.setter
    def rightgoalpost(self, value):
        if __debug__:
            from vision_msgs.msg import Rightgoalpost
            assert \
                isinstance(value, Rightgoalpost), \
                "The 'rightgoalpost' field must be a sub message of type 'Rightgoalpost'"
        self._rightgoalpost = value
