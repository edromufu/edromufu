function q = IK_leg(BodyP, BodyR, D, A, B , FootPos, FootR)

p2 = BodyP + BodyR * [0 D 0]'; %posição absoluta do quadril
r = FootR' * (p2 - FootPos);  % vetor do pé ao lower_body
C = norm(r); % distância do pé ao lower_body

c5 = (C^2-A^2-B^2)/(2.0*A*B);
if c5 >= 1 
    q5 = 0.0;
elseif c5 <= -1
    q5 = pi;
else
    q5 = acos(c5);  % knee pitch
end

alpha = asin(A*sin(pi-q5)/C);

q7 = atan2(r(2), r(3));

q6 = -atan2(r(1),sign(r(3))*sqrt(r(2)^2+r(3)^2)) - alpha;


R = BodyR' * FootR * Rroll(-q7) * Rpitch(-q6-q5); %% hipZ*hipX*hipY
q2  = atan2(-R(1,2),R(2,2));   % hip yaw
q3 = atan2(R(3,2),-R(1,2)*sin(q2) + R(2,2)*cos(q2));  % hip roll
q4 = atan2( -R(3,1), R(3,3));               % hip pitch


q = [q2 q3 q4 q5 q6 q7]';