// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from modularized_bhv_msgs:msg/GameControllerMsg.idl
// generated code does not contain a copyright notice

#ifndef MODULARIZED_BHV_MSGS__MSG__DETAIL__GAME_CONTROLLER_MSG__STRUCT_H_
#define MODULARIZED_BHV_MSGS__MSG__DETAIL__GAME_CONTROLLER_MSG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'GAMESTATE_INITAL'.
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__GAMESTATE_INITAL = 0
};

/// Constant 'GAMESTATE_READY'.
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__GAMESTATE_READY = 1
};

/// Constant 'GAMESTATE_SET'.
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__GAMESTATE_SET = 2
};

/// Constant 'GAMESTATE_PLAYING'.
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__GAMESTATE_PLAYING = 3
};

/// Constant 'GAMESTATE_FINISHED'.
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__GAMESTATE_FINISHED = 4
};

/// Constant 'STATE_NORMAL'.
/**
  * Secondary state, penaltyshoot is penalty shootout at the end of the game,
  * penaltykick is a kick during the game
 */
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__STATE_NORMAL = 0
};

/// Constant 'STATE_PENALTYSHOOT'.
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__STATE_PENALTYSHOOT = 1
};

/// Constant 'STATE_OVERTIME'.
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__STATE_OVERTIME = 2
};

/// Constant 'STATE_TIMEOUT'.
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__STATE_TIMEOUT = 3
};

/// Constant 'STATE_DIRECT_FREEKICK'.
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__STATE_DIRECT_FREEKICK = 4
};

/// Constant 'STATE_INDIRECT_FREEKICK'.
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__STATE_INDIRECT_FREEKICK = 5
};

/// Constant 'STATE_PENALTYKICK'.
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__STATE_PENALTYKICK = 6
};

/// Constant 'STATE_CORNER_KICK'.
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__STATE_CORNER_KICK = 7
};

/// Constant 'STATE_GOAL_KICK'.
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__STATE_GOAL_KICK = 8
};

/// Constant 'STATE_THROW_IN'.
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__STATE_THROW_IN = 9
};

/// Constant 'MODE_PREPARATION'.
/**
  * The secondary state contains a sub mode in which phase of execution the secondary state is
 */
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__MODE_PREPARATION = 0
};

/// Constant 'MODE_PLACING'.
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__MODE_PLACING = 1
};

/// Constant 'MODE_END'.
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__MODE_END = 2
};

/// Constant 'BLUE'.
/**
  * Team colors
 */
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__BLUE = 0
};

/// Constant 'RED'.
enum
{
  modularized_bhv_msgs__msg__GameControllerMsg__RED = 1
};

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'coach_message'
#include "rosidl_runtime_c/string.h"
// Member 'team_mates_with_penalty'
// Member 'team_mates_with_red_card'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in msg/GameControllerMsg in the package modularized_bhv_msgs.
typedef struct modularized_bhv_msgs__msg__GameControllerMsg
{
  std_msgs__msg__Header header;
  uint8_t game_state;
  uint8_t secondary_state;
  /// For newest version of game controller
  /// Tells which team has the free kick or penalty kick
  uint8_t secondary_state_team;
  uint8_t secondary_state_mode;
  bool first_half;
  uint8_t own_score;
  uint8_t rival_score;
  /// Seconds remaining for the game half
  int16_t seconds_remaining;
  /// Seconds remaining for things like kickoff
  int16_t secondary_seconds_remaining;
  bool has_kick_off;
  bool penalized;
  uint16_t seconds_till_unpenalized;
  uint8_t team_color;
  bool drop_in_team;
  uint16_t drop_in_time;
  /// The number of the current penalty shot during penalty shootout
  uint8_t penalty_shot;
  /// a binary pattern indicating the successful penalty shots (1 for successful, 0 for unsuccessful)
  uint16_t single_shots;
  rosidl_runtime_c__String coach_message;
  rosidl_runtime_c__boolean__Sequence team_mates_with_penalty;
  rosidl_runtime_c__boolean__Sequence team_mates_with_red_card;
} modularized_bhv_msgs__msg__GameControllerMsg;

// Struct for a sequence of modularized_bhv_msgs__msg__GameControllerMsg.
typedef struct modularized_bhv_msgs__msg__GameControllerMsg__Sequence
{
  modularized_bhv_msgs__msg__GameControllerMsg * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} modularized_bhv_msgs__msg__GameControllerMsg__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MODULARIZED_BHV_MSGS__MSG__DETAIL__GAME_CONTROLLER_MSG__STRUCT_H_
