# generated from rosidl_generator_py/resource/_idl.py.em
# with input from modularized_bhv_msgs:msg/GameControllerMsg.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_GameControllerMsg(type):
    """Metaclass of message 'GameControllerMsg'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'GAMESTATE_INITAL': 0,
        'GAMESTATE_READY': 1,
        'GAMESTATE_SET': 2,
        'GAMESTATE_PLAYING': 3,
        'GAMESTATE_FINISHED': 4,
        'STATE_NORMAL': 0,
        'STATE_PENALTYSHOOT': 1,
        'STATE_OVERTIME': 2,
        'STATE_TIMEOUT': 3,
        'STATE_DIRECT_FREEKICK': 4,
        'STATE_INDIRECT_FREEKICK': 5,
        'STATE_PENALTYKICK': 6,
        'STATE_CORNER_KICK': 7,
        'STATE_GOAL_KICK': 8,
        'STATE_THROW_IN': 9,
        'MODE_PREPARATION': 0,
        'MODE_PLACING': 1,
        'MODE_END': 2,
        'BLUE': 0,
        'RED': 1,
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
                'modularized_bhv_msgs.msg.GameControllerMsg')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__game_controller_msg
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__game_controller_msg
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__game_controller_msg
            cls._TYPE_SUPPORT = module.type_support_msg__msg__game_controller_msg
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__game_controller_msg

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'GAMESTATE_INITAL': cls.__constants['GAMESTATE_INITAL'],
            'GAMESTATE_READY': cls.__constants['GAMESTATE_READY'],
            'GAMESTATE_SET': cls.__constants['GAMESTATE_SET'],
            'GAMESTATE_PLAYING': cls.__constants['GAMESTATE_PLAYING'],
            'GAMESTATE_FINISHED': cls.__constants['GAMESTATE_FINISHED'],
            'STATE_NORMAL': cls.__constants['STATE_NORMAL'],
            'STATE_PENALTYSHOOT': cls.__constants['STATE_PENALTYSHOOT'],
            'STATE_OVERTIME': cls.__constants['STATE_OVERTIME'],
            'STATE_TIMEOUT': cls.__constants['STATE_TIMEOUT'],
            'STATE_DIRECT_FREEKICK': cls.__constants['STATE_DIRECT_FREEKICK'],
            'STATE_INDIRECT_FREEKICK': cls.__constants['STATE_INDIRECT_FREEKICK'],
            'STATE_PENALTYKICK': cls.__constants['STATE_PENALTYKICK'],
            'STATE_CORNER_KICK': cls.__constants['STATE_CORNER_KICK'],
            'STATE_GOAL_KICK': cls.__constants['STATE_GOAL_KICK'],
            'STATE_THROW_IN': cls.__constants['STATE_THROW_IN'],
            'MODE_PREPARATION': cls.__constants['MODE_PREPARATION'],
            'MODE_PLACING': cls.__constants['MODE_PLACING'],
            'MODE_END': cls.__constants['MODE_END'],
            'BLUE': cls.__constants['BLUE'],
            'RED': cls.__constants['RED'],
            'GAME_STATE__DEFAULT': 3,
            'SECONDARY_STATE__DEFAULT': 0,
        }

    @property
    def GAMESTATE_INITAL(self):
        """Message constant 'GAMESTATE_INITAL'."""
        return Metaclass_GameControllerMsg.__constants['GAMESTATE_INITAL']

    @property
    def GAMESTATE_READY(self):
        """Message constant 'GAMESTATE_READY'."""
        return Metaclass_GameControllerMsg.__constants['GAMESTATE_READY']

    @property
    def GAMESTATE_SET(self):
        """Message constant 'GAMESTATE_SET'."""
        return Metaclass_GameControllerMsg.__constants['GAMESTATE_SET']

    @property
    def GAMESTATE_PLAYING(self):
        """Message constant 'GAMESTATE_PLAYING'."""
        return Metaclass_GameControllerMsg.__constants['GAMESTATE_PLAYING']

    @property
    def GAMESTATE_FINISHED(self):
        """Message constant 'GAMESTATE_FINISHED'."""
        return Metaclass_GameControllerMsg.__constants['GAMESTATE_FINISHED']

    @property
    def STATE_NORMAL(self):
        """Message constant 'STATE_NORMAL'."""
        return Metaclass_GameControllerMsg.__constants['STATE_NORMAL']

    @property
    def STATE_PENALTYSHOOT(self):
        """Message constant 'STATE_PENALTYSHOOT'."""
        return Metaclass_GameControllerMsg.__constants['STATE_PENALTYSHOOT']

    @property
    def STATE_OVERTIME(self):
        """Message constant 'STATE_OVERTIME'."""
        return Metaclass_GameControllerMsg.__constants['STATE_OVERTIME']

    @property
    def STATE_TIMEOUT(self):
        """Message constant 'STATE_TIMEOUT'."""
        return Metaclass_GameControllerMsg.__constants['STATE_TIMEOUT']

    @property
    def STATE_DIRECT_FREEKICK(self):
        """Message constant 'STATE_DIRECT_FREEKICK'."""
        return Metaclass_GameControllerMsg.__constants['STATE_DIRECT_FREEKICK']

    @property
    def STATE_INDIRECT_FREEKICK(self):
        """Message constant 'STATE_INDIRECT_FREEKICK'."""
        return Metaclass_GameControllerMsg.__constants['STATE_INDIRECT_FREEKICK']

    @property
    def STATE_PENALTYKICK(self):
        """Message constant 'STATE_PENALTYKICK'."""
        return Metaclass_GameControllerMsg.__constants['STATE_PENALTYKICK']

    @property
    def STATE_CORNER_KICK(self):
        """Message constant 'STATE_CORNER_KICK'."""
        return Metaclass_GameControllerMsg.__constants['STATE_CORNER_KICK']

    @property
    def STATE_GOAL_KICK(self):
        """Message constant 'STATE_GOAL_KICK'."""
        return Metaclass_GameControllerMsg.__constants['STATE_GOAL_KICK']

    @property
    def STATE_THROW_IN(self):
        """Message constant 'STATE_THROW_IN'."""
        return Metaclass_GameControllerMsg.__constants['STATE_THROW_IN']

    @property
    def MODE_PREPARATION(self):
        """Message constant 'MODE_PREPARATION'."""
        return Metaclass_GameControllerMsg.__constants['MODE_PREPARATION']

    @property
    def MODE_PLACING(self):
        """Message constant 'MODE_PLACING'."""
        return Metaclass_GameControllerMsg.__constants['MODE_PLACING']

    @property
    def MODE_END(self):
        """Message constant 'MODE_END'."""
        return Metaclass_GameControllerMsg.__constants['MODE_END']

    @property
    def BLUE(self):
        """Message constant 'BLUE'."""
        return Metaclass_GameControllerMsg.__constants['BLUE']

    @property
    def RED(self):
        """Message constant 'RED'."""
        return Metaclass_GameControllerMsg.__constants['RED']

    @property
    def GAME_STATE__DEFAULT(cls):
        """Return default value for message field 'game_state'."""
        return 3

    @property
    def SECONDARY_STATE__DEFAULT(cls):
        """Return default value for message field 'secondary_state'."""
        return 0


class GameControllerMsg(metaclass=Metaclass_GameControllerMsg):
    """
    Message class 'GameControllerMsg'.

    Constants:
      GAMESTATE_INITAL
      GAMESTATE_READY
      GAMESTATE_SET
      GAMESTATE_PLAYING
      GAMESTATE_FINISHED
      STATE_NORMAL
      STATE_PENALTYSHOOT
      STATE_OVERTIME
      STATE_TIMEOUT
      STATE_DIRECT_FREEKICK
      STATE_INDIRECT_FREEKICK
      STATE_PENALTYKICK
      STATE_CORNER_KICK
      STATE_GOAL_KICK
      STATE_THROW_IN
      MODE_PREPARATION
      MODE_PLACING
      MODE_END
      BLUE
      RED
    """

    __slots__ = [
        '_header',
        '_game_state',
        '_secondary_state',
        '_secondary_state_team',
        '_secondary_state_mode',
        '_first_half',
        '_own_score',
        '_rival_score',
        '_seconds_remaining',
        '_secondary_seconds_remaining',
        '_has_kick_off',
        '_penalized',
        '_seconds_till_unpenalized',
        '_team_color',
        '_drop_in_team',
        '_drop_in_time',
        '_penalty_shot',
        '_single_shots',
        '_coach_message',
        '_team_mates_with_penalty',
        '_team_mates_with_red_card',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'game_state': 'uint8',
        'secondary_state': 'uint8',
        'secondary_state_team': 'uint8',
        'secondary_state_mode': 'uint8',
        'first_half': 'boolean',
        'own_score': 'uint8',
        'rival_score': 'uint8',
        'seconds_remaining': 'int16',
        'secondary_seconds_remaining': 'int16',
        'has_kick_off': 'boolean',
        'penalized': 'boolean',
        'seconds_till_unpenalized': 'uint16',
        'team_color': 'uint8',
        'drop_in_team': 'boolean',
        'drop_in_time': 'uint16',
        'penalty_shot': 'uint8',
        'single_shots': 'uint16',
        'coach_message': 'string',
        'team_mates_with_penalty': 'sequence<boolean>',
        'team_mates_with_red_card': 'sequence<boolean>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('boolean')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('boolean')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.game_state = kwargs.get(
            'game_state', GameControllerMsg.GAME_STATE__DEFAULT)
        self.secondary_state = kwargs.get(
            'secondary_state', GameControllerMsg.SECONDARY_STATE__DEFAULT)
        self.secondary_state_team = kwargs.get('secondary_state_team', int())
        self.secondary_state_mode = kwargs.get('secondary_state_mode', int())
        self.first_half = kwargs.get('first_half', bool())
        self.own_score = kwargs.get('own_score', int())
        self.rival_score = kwargs.get('rival_score', int())
        self.seconds_remaining = kwargs.get('seconds_remaining', int())
        self.secondary_seconds_remaining = kwargs.get('secondary_seconds_remaining', int())
        self.has_kick_off = kwargs.get('has_kick_off', bool())
        self.penalized = kwargs.get('penalized', bool())
        self.seconds_till_unpenalized = kwargs.get('seconds_till_unpenalized', int())
        self.team_color = kwargs.get('team_color', int())
        self.drop_in_team = kwargs.get('drop_in_team', bool())
        self.drop_in_time = kwargs.get('drop_in_time', int())
        self.penalty_shot = kwargs.get('penalty_shot', int())
        self.single_shots = kwargs.get('single_shots', int())
        self.coach_message = kwargs.get('coach_message', str())
        self.team_mates_with_penalty = kwargs.get('team_mates_with_penalty', [])
        self.team_mates_with_red_card = kwargs.get('team_mates_with_red_card', [])

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
        if self.header != other.header:
            return False
        if self.game_state != other.game_state:
            return False
        if self.secondary_state != other.secondary_state:
            return False
        if self.secondary_state_team != other.secondary_state_team:
            return False
        if self.secondary_state_mode != other.secondary_state_mode:
            return False
        if self.first_half != other.first_half:
            return False
        if self.own_score != other.own_score:
            return False
        if self.rival_score != other.rival_score:
            return False
        if self.seconds_remaining != other.seconds_remaining:
            return False
        if self.secondary_seconds_remaining != other.secondary_seconds_remaining:
            return False
        if self.has_kick_off != other.has_kick_off:
            return False
        if self.penalized != other.penalized:
            return False
        if self.seconds_till_unpenalized != other.seconds_till_unpenalized:
            return False
        if self.team_color != other.team_color:
            return False
        if self.drop_in_team != other.drop_in_team:
            return False
        if self.drop_in_time != other.drop_in_time:
            return False
        if self.penalty_shot != other.penalty_shot:
            return False
        if self.single_shots != other.single_shots:
            return False
        if self.coach_message != other.coach_message:
            return False
        if self.team_mates_with_penalty != other.team_mates_with_penalty:
            return False
        if self.team_mates_with_red_card != other.team_mates_with_red_card:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if __debug__:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @builtins.property
    def game_state(self):
        """Message field 'game_state'."""
        return self._game_state

    @game_state.setter
    def game_state(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'game_state' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'game_state' field must be an unsigned integer in [0, 255]"
        self._game_state = value

    @builtins.property
    def secondary_state(self):
        """Message field 'secondary_state'."""
        return self._secondary_state

    @secondary_state.setter
    def secondary_state(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'secondary_state' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'secondary_state' field must be an unsigned integer in [0, 255]"
        self._secondary_state = value

    @builtins.property
    def secondary_state_team(self):
        """Message field 'secondary_state_team'."""
        return self._secondary_state_team

    @secondary_state_team.setter
    def secondary_state_team(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'secondary_state_team' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'secondary_state_team' field must be an unsigned integer in [0, 255]"
        self._secondary_state_team = value

    @builtins.property
    def secondary_state_mode(self):
        """Message field 'secondary_state_mode'."""
        return self._secondary_state_mode

    @secondary_state_mode.setter
    def secondary_state_mode(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'secondary_state_mode' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'secondary_state_mode' field must be an unsigned integer in [0, 255]"
        self._secondary_state_mode = value

    @builtins.property
    def first_half(self):
        """Message field 'first_half'."""
        return self._first_half

    @first_half.setter
    def first_half(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'first_half' field must be of type 'bool'"
        self._first_half = value

    @builtins.property
    def own_score(self):
        """Message field 'own_score'."""
        return self._own_score

    @own_score.setter
    def own_score(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'own_score' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'own_score' field must be an unsigned integer in [0, 255]"
        self._own_score = value

    @builtins.property
    def rival_score(self):
        """Message field 'rival_score'."""
        return self._rival_score

    @rival_score.setter
    def rival_score(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'rival_score' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'rival_score' field must be an unsigned integer in [0, 255]"
        self._rival_score = value

    @builtins.property
    def seconds_remaining(self):
        """Message field 'seconds_remaining'."""
        return self._seconds_remaining

    @seconds_remaining.setter
    def seconds_remaining(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'seconds_remaining' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'seconds_remaining' field must be an integer in [-32768, 32767]"
        self._seconds_remaining = value

    @builtins.property
    def secondary_seconds_remaining(self):
        """Message field 'secondary_seconds_remaining'."""
        return self._secondary_seconds_remaining

    @secondary_seconds_remaining.setter
    def secondary_seconds_remaining(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'secondary_seconds_remaining' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'secondary_seconds_remaining' field must be an integer in [-32768, 32767]"
        self._secondary_seconds_remaining = value

    @builtins.property
    def has_kick_off(self):
        """Message field 'has_kick_off'."""
        return self._has_kick_off

    @has_kick_off.setter
    def has_kick_off(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'has_kick_off' field must be of type 'bool'"
        self._has_kick_off = value

    @builtins.property
    def penalized(self):
        """Message field 'penalized'."""
        return self._penalized

    @penalized.setter
    def penalized(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'penalized' field must be of type 'bool'"
        self._penalized = value

    @builtins.property
    def seconds_till_unpenalized(self):
        """Message field 'seconds_till_unpenalized'."""
        return self._seconds_till_unpenalized

    @seconds_till_unpenalized.setter
    def seconds_till_unpenalized(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'seconds_till_unpenalized' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'seconds_till_unpenalized' field must be an unsigned integer in [0, 65535]"
        self._seconds_till_unpenalized = value

    @builtins.property
    def team_color(self):
        """Message field 'team_color'."""
        return self._team_color

    @team_color.setter
    def team_color(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'team_color' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'team_color' field must be an unsigned integer in [0, 255]"
        self._team_color = value

    @builtins.property
    def drop_in_team(self):
        """Message field 'drop_in_team'."""
        return self._drop_in_team

    @drop_in_team.setter
    def drop_in_team(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'drop_in_team' field must be of type 'bool'"
        self._drop_in_team = value

    @builtins.property
    def drop_in_time(self):
        """Message field 'drop_in_time'."""
        return self._drop_in_time

    @drop_in_time.setter
    def drop_in_time(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'drop_in_time' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'drop_in_time' field must be an unsigned integer in [0, 65535]"
        self._drop_in_time = value

    @builtins.property
    def penalty_shot(self):
        """Message field 'penalty_shot'."""
        return self._penalty_shot

    @penalty_shot.setter
    def penalty_shot(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'penalty_shot' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'penalty_shot' field must be an unsigned integer in [0, 255]"
        self._penalty_shot = value

    @builtins.property
    def single_shots(self):
        """Message field 'single_shots'."""
        return self._single_shots

    @single_shots.setter
    def single_shots(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'single_shots' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'single_shots' field must be an unsigned integer in [0, 65535]"
        self._single_shots = value

    @builtins.property
    def coach_message(self):
        """Message field 'coach_message'."""
        return self._coach_message

    @coach_message.setter
    def coach_message(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'coach_message' field must be of type 'str'"
        self._coach_message = value

    @builtins.property
    def team_mates_with_penalty(self):
        """Message field 'team_mates_with_penalty'."""
        return self._team_mates_with_penalty

    @team_mates_with_penalty.setter
    def team_mates_with_penalty(self, value):
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
                 all(isinstance(v, bool) for v in value) and
                 True), \
                "The 'team_mates_with_penalty' field must be a set or sequence and each value of type 'bool'"
        self._team_mates_with_penalty = value

    @builtins.property
    def team_mates_with_red_card(self):
        """Message field 'team_mates_with_red_card'."""
        return self._team_mates_with_red_card

    @team_mates_with_red_card.setter
    def team_mates_with_red_card(self, value):
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
                 all(isinstance(v, bool) for v in value) and
                 True), \
                "The 'team_mates_with_red_card' field must be a set or sequence and each value of type 'bool'"
        self._team_mates_with_red_card = value
