function J = tCalcJacobian(idx)
% Jacobian matrix of current configration in World frame
global robotCopy

jsize = length(idx);
target = robotCopy(idx(end)).p;   % absolute target position
J = zeros(6,jsize);

for n=1:jsize
    j = idx(n);
    a = robotCopy(j).R * robotCopy(j).a; % joint axis vector in world frame
    J(:,n) = [cross(a, target - robotCopy(j).p) ; a ];
end

