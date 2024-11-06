# generated from rosidl_generator_py/resource/_idl.py.em
# with input from potmessage:msg/Potmsg.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Potmsg(type):
    """Metaclass of message 'Potmsg'."""

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
            module = import_type_support('potmessage')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'potmessage.msg.Potmsg')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__potmsg
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__potmsg
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__potmsg
            cls._TYPE_SUPPORT = module.type_support_msg__msg__potmsg
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__potmsg

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Potmsg(metaclass=Metaclass_Potmsg):
    """Message class 'Potmsg'."""

    __slots__ = [
        '_pot1',
        '_pot2',
        '_pot3',
        '_pot4',
        '_pot5',
        '_pot6',
        '_pot7',
        '_pot8',
    ]

    _fields_and_field_types = {
        'pot1': 'float',
        'pot2': 'float',
        'pot3': 'float',
        'pot4': 'float',
        'pot5': 'float',
        'pot6': 'float',
        'pot7': 'float',
        'pot8': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.pot1 = kwargs.get('pot1', float())
        self.pot2 = kwargs.get('pot2', float())
        self.pot3 = kwargs.get('pot3', float())
        self.pot4 = kwargs.get('pot4', float())
        self.pot5 = kwargs.get('pot5', float())
        self.pot6 = kwargs.get('pot6', float())
        self.pot7 = kwargs.get('pot7', float())
        self.pot8 = kwargs.get('pot8', float())

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
        if self.pot1 != other.pot1:
            return False
        if self.pot2 != other.pot2:
            return False
        if self.pot3 != other.pot3:
            return False
        if self.pot4 != other.pot4:
            return False
        if self.pot5 != other.pot5:
            return False
        if self.pot6 != other.pot6:
            return False
        if self.pot7 != other.pot7:
            return False
        if self.pot8 != other.pot8:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def pot1(self):
        """Message field 'pot1'."""
        return self._pot1

    @pot1.setter
    def pot1(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pot1' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pot1' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pot1 = value

    @builtins.property
    def pot2(self):
        """Message field 'pot2'."""
        return self._pot2

    @pot2.setter
    def pot2(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pot2' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pot2' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pot2 = value

    @builtins.property
    def pot3(self):
        """Message field 'pot3'."""
        return self._pot3

    @pot3.setter
    def pot3(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pot3' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pot3' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pot3 = value

    @builtins.property
    def pot4(self):
        """Message field 'pot4'."""
        return self._pot4

    @pot4.setter
    def pot4(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pot4' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pot4' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pot4 = value

    @builtins.property
    def pot5(self):
        """Message field 'pot5'."""
        return self._pot5

    @pot5.setter
    def pot5(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pot5' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pot5' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pot5 = value

    @builtins.property
    def pot6(self):
        """Message field 'pot6'."""
        return self._pot6

    @pot6.setter
    def pot6(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pot6' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pot6' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pot6 = value

    @builtins.property
    def pot7(self):
        """Message field 'pot7'."""
        return self._pot7

    @pot7.setter
    def pot7(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pot7' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pot7' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pot7 = value

    @builtins.property
    def pot8(self):
        """Message field 'pot8'."""
        return self._pot8

    @pot8.setter
    def pot8(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pot8' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pot8' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pot8 = value
