function dForwardKinematics(j)
global uLINK

if j == 0 return; end
if j ~= 1
    mom = uLINK(j).mother;
    uLINK(j).p = uLINK(mom).R * uLINK(j).b + uLINK(mom).p;
    uLINK(j).R = uLINK(mom).R * dRodrigues(uLINK(j).a, uLINK(j).q);
end
dForwardKinematics(uLINK(j).sister);
dForwardKinematics(uLINK(j).child);
