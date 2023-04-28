function q = tInverseKinematics(newFootAbsPosition, newFootAbsPosture, currentFoot, robot)
clf;

global uLINK
global robotCopy
robotCopy = robot;

Target.p = newFootAbsPosition;
Target.R = newFootAbsPosture;

lambda = 0.7;
idx = tFindRoute(currentFoot); %Encontra os links presentes da base (COM) até o end-effector (pés)
err = tCalcVWerr(Target,robotCopy(currentFoot)); %Encontra o erro da posição e da postura


while norm(err) > 1E-4   
  J  = tCalcJacobian(idx);
  dq = lambda * (J \ err); %Resolve o sistema linear
  
  tVirtuallyMoveJoints(idx, dq); %Altera uma cópia da robô virtualmente para checar o erro da referência
  nFakeFowardKinematics(1);
  err = tCalcVWerr(Target, robotCopy(currentFoot));
end

q = zeros(1,length(robotCopy));
for i=1:length(robotCopy)
    q(i) = robotCopy(i).q;
end

uLINK = robotCopy;
clear robotCopy;