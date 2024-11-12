// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from modularized_bhv_msgs:msg/GameControllerMsg.idl
// generated code does not contain a copyright notice

#ifndef MODULARIZED_BHV_MSGS__MSG__DETAIL__GAME_CONTROLLER_MSG__BUILDER_HPP_
#define MODULARIZED_BHV_MSGS__MSG__DETAIL__GAME_CONTROLLER_MSG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "modularized_bhv_msgs/msg/detail/game_controller_msg__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace modularized_bhv_msgs
{

namespace msg
{

namespace builder
{

class Init_GameControllerMsg_team_mates_with_red_card
{
public:
  explicit Init_GameControllerMsg_team_mates_with_red_card(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  ::modularized_bhv_msgs::msg::GameControllerMsg team_mates_with_red_card(::modularized_bhv_msgs::msg::GameControllerMsg::_team_mates_with_red_card_type arg)
  {
    msg_.team_mates_with_red_card = std::move(arg);
    return std::move(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_team_mates_with_penalty
{
public:
  explicit Init_GameControllerMsg_team_mates_with_penalty(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  Init_GameControllerMsg_team_mates_with_red_card team_mates_with_penalty(::modularized_bhv_msgs::msg::GameControllerMsg::_team_mates_with_penalty_type arg)
  {
    msg_.team_mates_with_penalty = std::move(arg);
    return Init_GameControllerMsg_team_mates_with_red_card(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_coach_message
{
public:
  explicit Init_GameControllerMsg_coach_message(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  Init_GameControllerMsg_team_mates_with_penalty coach_message(::modularized_bhv_msgs::msg::GameControllerMsg::_coach_message_type arg)
  {
    msg_.coach_message = std::move(arg);
    return Init_GameControllerMsg_team_mates_with_penalty(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_single_shots
{
public:
  explicit Init_GameControllerMsg_single_shots(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  Init_GameControllerMsg_coach_message single_shots(::modularized_bhv_msgs::msg::GameControllerMsg::_single_shots_type arg)
  {
    msg_.single_shots = std::move(arg);
    return Init_GameControllerMsg_coach_message(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_penalty_shot
{
public:
  explicit Init_GameControllerMsg_penalty_shot(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  Init_GameControllerMsg_single_shots penalty_shot(::modularized_bhv_msgs::msg::GameControllerMsg::_penalty_shot_type arg)
  {
    msg_.penalty_shot = std::move(arg);
    return Init_GameControllerMsg_single_shots(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_drop_in_time
{
public:
  explicit Init_GameControllerMsg_drop_in_time(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  Init_GameControllerMsg_penalty_shot drop_in_time(::modularized_bhv_msgs::msg::GameControllerMsg::_drop_in_time_type arg)
  {
    msg_.drop_in_time = std::move(arg);
    return Init_GameControllerMsg_penalty_shot(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_drop_in_team
{
public:
  explicit Init_GameControllerMsg_drop_in_team(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  Init_GameControllerMsg_drop_in_time drop_in_team(::modularized_bhv_msgs::msg::GameControllerMsg::_drop_in_team_type arg)
  {
    msg_.drop_in_team = std::move(arg);
    return Init_GameControllerMsg_drop_in_time(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_team_color
{
public:
  explicit Init_GameControllerMsg_team_color(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  Init_GameControllerMsg_drop_in_team team_color(::modularized_bhv_msgs::msg::GameControllerMsg::_team_color_type arg)
  {
    msg_.team_color = std::move(arg);
    return Init_GameControllerMsg_drop_in_team(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_seconds_till_unpenalized
{
public:
  explicit Init_GameControllerMsg_seconds_till_unpenalized(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  Init_GameControllerMsg_team_color seconds_till_unpenalized(::modularized_bhv_msgs::msg::GameControllerMsg::_seconds_till_unpenalized_type arg)
  {
    msg_.seconds_till_unpenalized = std::move(arg);
    return Init_GameControllerMsg_team_color(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_penalized
{
public:
  explicit Init_GameControllerMsg_penalized(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  Init_GameControllerMsg_seconds_till_unpenalized penalized(::modularized_bhv_msgs::msg::GameControllerMsg::_penalized_type arg)
  {
    msg_.penalized = std::move(arg);
    return Init_GameControllerMsg_seconds_till_unpenalized(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_has_kick_off
{
public:
  explicit Init_GameControllerMsg_has_kick_off(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  Init_GameControllerMsg_penalized has_kick_off(::modularized_bhv_msgs::msg::GameControllerMsg::_has_kick_off_type arg)
  {
    msg_.has_kick_off = std::move(arg);
    return Init_GameControllerMsg_penalized(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_secondary_seconds_remaining
{
public:
  explicit Init_GameControllerMsg_secondary_seconds_remaining(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  Init_GameControllerMsg_has_kick_off secondary_seconds_remaining(::modularized_bhv_msgs::msg::GameControllerMsg::_secondary_seconds_remaining_type arg)
  {
    msg_.secondary_seconds_remaining = std::move(arg);
    return Init_GameControllerMsg_has_kick_off(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_seconds_remaining
{
public:
  explicit Init_GameControllerMsg_seconds_remaining(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  Init_GameControllerMsg_secondary_seconds_remaining seconds_remaining(::modularized_bhv_msgs::msg::GameControllerMsg::_seconds_remaining_type arg)
  {
    msg_.seconds_remaining = std::move(arg);
    return Init_GameControllerMsg_secondary_seconds_remaining(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_rival_score
{
public:
  explicit Init_GameControllerMsg_rival_score(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  Init_GameControllerMsg_seconds_remaining rival_score(::modularized_bhv_msgs::msg::GameControllerMsg::_rival_score_type arg)
  {
    msg_.rival_score = std::move(arg);
    return Init_GameControllerMsg_seconds_remaining(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_own_score
{
public:
  explicit Init_GameControllerMsg_own_score(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  Init_GameControllerMsg_rival_score own_score(::modularized_bhv_msgs::msg::GameControllerMsg::_own_score_type arg)
  {
    msg_.own_score = std::move(arg);
    return Init_GameControllerMsg_rival_score(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_first_half
{
public:
  explicit Init_GameControllerMsg_first_half(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  Init_GameControllerMsg_own_score first_half(::modularized_bhv_msgs::msg::GameControllerMsg::_first_half_type arg)
  {
    msg_.first_half = std::move(arg);
    return Init_GameControllerMsg_own_score(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_secondary_state_mode
{
public:
  explicit Init_GameControllerMsg_secondary_state_mode(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  Init_GameControllerMsg_first_half secondary_state_mode(::modularized_bhv_msgs::msg::GameControllerMsg::_secondary_state_mode_type arg)
  {
    msg_.secondary_state_mode = std::move(arg);
    return Init_GameControllerMsg_first_half(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_secondary_state_team
{
public:
  explicit Init_GameControllerMsg_secondary_state_team(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  Init_GameControllerMsg_secondary_state_mode secondary_state_team(::modularized_bhv_msgs::msg::GameControllerMsg::_secondary_state_team_type arg)
  {
    msg_.secondary_state_team = std::move(arg);
    return Init_GameControllerMsg_secondary_state_mode(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_secondary_state
{
public:
  explicit Init_GameControllerMsg_secondary_state(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  Init_GameControllerMsg_secondary_state_team secondary_state(::modularized_bhv_msgs::msg::GameControllerMsg::_secondary_state_type arg)
  {
    msg_.secondary_state = std::move(arg);
    return Init_GameControllerMsg_secondary_state_team(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_game_state
{
public:
  explicit Init_GameControllerMsg_game_state(::modularized_bhv_msgs::msg::GameControllerMsg & msg)
  : msg_(msg)
  {}
  Init_GameControllerMsg_secondary_state game_state(::modularized_bhv_msgs::msg::GameControllerMsg::_game_state_type arg)
  {
    msg_.game_state = std::move(arg);
    return Init_GameControllerMsg_secondary_state(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

class Init_GameControllerMsg_header
{
public:
  Init_GameControllerMsg_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GameControllerMsg_game_state header(::modularized_bhv_msgs::msg::GameControllerMsg::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_GameControllerMsg_game_state(msg_);
  }

private:
  ::modularized_bhv_msgs::msg::GameControllerMsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::modularized_bhv_msgs::msg::GameControllerMsg>()
{
  return modularized_bhv_msgs::msg::builder::Init_GameControllerMsg_header();
}

}  // namespace modularized_bhv_msgs

#endif  // MODULARIZED_BHV_MSGS__MSG__DETAIL__GAME_CONTROLLER_MSG__BUILDER_HPP_
