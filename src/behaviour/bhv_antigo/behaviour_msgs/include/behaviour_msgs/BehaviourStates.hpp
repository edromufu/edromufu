namespace bhv
{
enum States
{
    NONE,
    STAND_STILL,
	SEARCH_BALL,
	CENTER_BALL,
    WALKING,
    ALIGN_BODY,
    GOAL_POSITIONING,
    KICKING,
    FELL,
    SQUAT,
    DEFEND_RIGHT,
    DEFEND_LEFT
};

enum BallTracking
{
    NOTHING,
    TRACKING,
    LOST_BALL,
    CLOSE_TO_KICK,
    CLOSE_TO_DEFEND,
    BALL_RIGHT,
    BALL_LEFT,
    CENTRALIZED,
    TIMEOUT
};
} // namespace bhv
