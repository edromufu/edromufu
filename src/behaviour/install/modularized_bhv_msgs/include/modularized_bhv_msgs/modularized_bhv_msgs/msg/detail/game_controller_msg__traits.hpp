// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from modularized_bhv_msgs:msg/GameControllerMsg.idl
// generated code does not contain a copyright notice

#ifndef MODULARIZED_BHV_MSGS__MSG__DETAIL__GAME_CONTROLLER_MSG__TRAITS_HPP_
#define MODULARIZED_BHV_MSGS__MSG__DETAIL__GAME_CONTROLLER_MSG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "modularized_bhv_msgs/msg/detail/game_controller_msg__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace modularized_bhv_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const GameControllerMsg & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: game_state
  {
    out << "game_state: ";
    rosidl_generator_traits::value_to_yaml(msg.game_state, out);
    out << ", ";
  }

  // member: secondary_state
  {
    out << "secondary_state: ";
    rosidl_generator_traits::value_to_yaml(msg.secondary_state, out);
    out << ", ";
  }

  // member: secondary_state_team
  {
    out << "secondary_state_team: ";
    rosidl_generator_traits::value_to_yaml(msg.secondary_state_team, out);
    out << ", ";
  }

  // member: secondary_state_mode
  {
    out << "secondary_state_mode: ";
    rosidl_generator_traits::value_to_yaml(msg.secondary_state_mode, out);
    out << ", ";
  }

  // member: first_half
  {
    out << "first_half: ";
    rosidl_generator_traits::value_to_yaml(msg.first_half, out);
    out << ", ";
  }

  // member: own_score
  {
    out << "own_score: ";
    rosidl_generator_traits::value_to_yaml(msg.own_score, out);
    out << ", ";
  }

  // member: rival_score
  {
    out << "rival_score: ";
    rosidl_generator_traits::value_to_yaml(msg.rival_score, out);
    out << ", ";
  }

  // member: seconds_remaining
  {
    out << "seconds_remaining: ";
    rosidl_generator_traits::value_to_yaml(msg.seconds_remaining, out);
    out << ", ";
  }

  // member: secondary_seconds_remaining
  {
    out << "secondary_seconds_remaining: ";
    rosidl_generator_traits::value_to_yaml(msg.secondary_seconds_remaining, out);
    out << ", ";
  }

  // member: has_kick_off
  {
    out << "has_kick_off: ";
    rosidl_generator_traits::value_to_yaml(msg.has_kick_off, out);
    out << ", ";
  }

  // member: penalized
  {
    out << "penalized: ";
    rosidl_generator_traits::value_to_yaml(msg.penalized, out);
    out << ", ";
  }

  // member: seconds_till_unpenalized
  {
    out << "seconds_till_unpenalized: ";
    rosidl_generator_traits::value_to_yaml(msg.seconds_till_unpenalized, out);
    out << ", ";
  }

  // member: team_color
  {
    out << "team_color: ";
    rosidl_generator_traits::value_to_yaml(msg.team_color, out);
    out << ", ";
  }

  // member: drop_in_team
  {
    out << "drop_in_team: ";
    rosidl_generator_traits::value_to_yaml(msg.drop_in_team, out);
    out << ", ";
  }

  // member: drop_in_time
  {
    out << "drop_in_time: ";
    rosidl_generator_traits::value_to_yaml(msg.drop_in_time, out);
    out << ", ";
  }

  // member: penalty_shot
  {
    out << "penalty_shot: ";
    rosidl_generator_traits::value_to_yaml(msg.penalty_shot, out);
    out << ", ";
  }

  // member: single_shots
  {
    out << "single_shots: ";
    rosidl_generator_traits::value_to_yaml(msg.single_shots, out);
    out << ", ";
  }

  // member: coach_message
  {
    out << "coach_message: ";
    rosidl_generator_traits::value_to_yaml(msg.coach_message, out);
    out << ", ";
  }

  // member: team_mates_with_penalty
  {
    if (msg.team_mates_with_penalty.size() == 0) {
      out << "team_mates_with_penalty: []";
    } else {
      out << "team_mates_with_penalty: [";
      size_t pending_items = msg.team_mates_with_penalty.size();
      for (auto item : msg.team_mates_with_penalty) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: team_mates_with_red_card
  {
    if (msg.team_mates_with_red_card.size() == 0) {
      out << "team_mates_with_red_card: []";
    } else {
      out << "team_mates_with_red_card: [";
      size_t pending_items = msg.team_mates_with_red_card.size();
      for (auto item : msg.team_mates_with_red_card) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GameControllerMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: game_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "game_state: ";
    rosidl_generator_traits::value_to_yaml(msg.game_state, out);
    out << "\n";
  }

  // member: secondary_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "secondary_state: ";
    rosidl_generator_traits::value_to_yaml(msg.secondary_state, out);
    out << "\n";
  }

  // member: secondary_state_team
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "secondary_state_team: ";
    rosidl_generator_traits::value_to_yaml(msg.secondary_state_team, out);
    out << "\n";
  }

  // member: secondary_state_mode
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "secondary_state_mode: ";
    rosidl_generator_traits::value_to_yaml(msg.secondary_state_mode, out);
    out << "\n";
  }

  // member: first_half
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "first_half: ";
    rosidl_generator_traits::value_to_yaml(msg.first_half, out);
    out << "\n";
  }

  // member: own_score
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "own_score: ";
    rosidl_generator_traits::value_to_yaml(msg.own_score, out);
    out << "\n";
  }

  // member: rival_score
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rival_score: ";
    rosidl_generator_traits::value_to_yaml(msg.rival_score, out);
    out << "\n";
  }

  // member: seconds_remaining
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "seconds_remaining: ";
    rosidl_generator_traits::value_to_yaml(msg.seconds_remaining, out);
    out << "\n";
  }

  // member: secondary_seconds_remaining
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "secondary_seconds_remaining: ";
    rosidl_generator_traits::value_to_yaml(msg.secondary_seconds_remaining, out);
    out << "\n";
  }

  // member: has_kick_off
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "has_kick_off: ";
    rosidl_generator_traits::value_to_yaml(msg.has_kick_off, out);
    out << "\n";
  }

  // member: penalized
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "penalized: ";
    rosidl_generator_traits::value_to_yaml(msg.penalized, out);
    out << "\n";
  }

  // member: seconds_till_unpenalized
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "seconds_till_unpenalized: ";
    rosidl_generator_traits::value_to_yaml(msg.seconds_till_unpenalized, out);
    out << "\n";
  }

  // member: team_color
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "team_color: ";
    rosidl_generator_traits::value_to_yaml(msg.team_color, out);
    out << "\n";
  }

  // member: drop_in_team
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "drop_in_team: ";
    rosidl_generator_traits::value_to_yaml(msg.drop_in_team, out);
    out << "\n";
  }

  // member: drop_in_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "drop_in_time: ";
    rosidl_generator_traits::value_to_yaml(msg.drop_in_time, out);
    out << "\n";
  }

  // member: penalty_shot
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "penalty_shot: ";
    rosidl_generator_traits::value_to_yaml(msg.penalty_shot, out);
    out << "\n";
  }

  // member: single_shots
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "single_shots: ";
    rosidl_generator_traits::value_to_yaml(msg.single_shots, out);
    out << "\n";
  }

  // member: coach_message
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "coach_message: ";
    rosidl_generator_traits::value_to_yaml(msg.coach_message, out);
    out << "\n";
  }

  // member: team_mates_with_penalty
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.team_mates_with_penalty.size() == 0) {
      out << "team_mates_with_penalty: []\n";
    } else {
      out << "team_mates_with_penalty:\n";
      for (auto item : msg.team_mates_with_penalty) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: team_mates_with_red_card
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.team_mates_with_red_card.size() == 0) {
      out << "team_mates_with_red_card: []\n";
    } else {
      out << "team_mates_with_red_card:\n";
      for (auto item : msg.team_mates_with_red_card) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GameControllerMsg & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace modularized_bhv_msgs

namespace rosidl_generator_traits
{

[[deprecated("use modularized_bhv_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const modularized_bhv_msgs::msg::GameControllerMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  modularized_bhv_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use modularized_bhv_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const modularized_bhv_msgs::msg::GameControllerMsg & msg)
{
  return modularized_bhv_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<modularized_bhv_msgs::msg::GameControllerMsg>()
{
  return "modularized_bhv_msgs::msg::GameControllerMsg";
}

template<>
inline const char * name<modularized_bhv_msgs::msg::GameControllerMsg>()
{
  return "modularized_bhv_msgs/msg/GameControllerMsg";
}

template<>
struct has_fixed_size<modularized_bhv_msgs::msg::GameControllerMsg>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<modularized_bhv_msgs::msg::GameControllerMsg>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<modularized_bhv_msgs::msg::GameControllerMsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MODULARIZED_BHV_MSGS__MSG__DETAIL__GAME_CONTROLLER_MSG__TRAITS_HPP_
