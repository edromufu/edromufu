dSetupBipedRobot()
newFootPos = uLINK(LFOOT).p + [0.05 0 0.05]';
currentFoot = LFOOT;

joint_angles = tInverseKinematics(newFootPos, eye(3), currentFoot, uLINK)
nDrawRobot()