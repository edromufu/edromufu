function nFakeFowardKinematics(j)
global robotCopy

if j == 0 return; end
if j ~= 1
    mom = robotCopy(j).mother;
    robotCopy(j).p = robotCopy(mom).R * robotCopy(j).b + robotCopy(mom).p;
    robotCopy(j).R = robotCopy(mom).R * dRodrigues(robotCopy(j).a, robotCopy(j).q);
end
nFakeFowardKinematics(robotCopy(j).sister);
nFakeFowardKinematics(robotCopy(j).child);
