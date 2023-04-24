% DrawRobot.m
clf
nDrawAllJoints(1);
view(37.5,30);
axis equal;
xlim([-0.25 0.25])
ylim([-0.25 0.25])
zlim([-0.02 0.3])
grid on
hold on
quiver3(0,0,uLINK(1).p(3),0.12,0,0)