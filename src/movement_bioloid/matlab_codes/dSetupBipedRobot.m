%%% SetupBipedRobot.m
%%% Set biped robot structure of Figure 2.19, 2.20
%%% Field definition: Table 2.1 Link Parameters
clear
clc
close all

global uLINK

ToDeg = 180/pi;
ToRad = pi/180;
UX = [1 0 0]';
UY = [0 1 0]';
UZ = [0 0 1]';

uLINK    = struct('name','COM'    , 'sister', 0, 'child', 2, 'b',[0  0    0.27]','a',UZ,'q',0);

uLINK(2) = struct('name','RHIP_UZ' , 'sister', 8, 'child', 3, 'b',[0 -0.035 -0.044]'   ,'a',UZ,'q',0);
uLINK(3) = struct('name','RHIP_UX' , 'sister', 0, 'child', 4, 'b',[-0.035  0     -0.03]'   ,'a',UX,'q',0);
uLINK(4) = struct('name','RHIP_UY' , 'sister', 0, 'child', 5, 'b',[0.035  0   0]'   ,'a',UY,'q',0);
uLINK(5) = struct('name','RKNEE' , 'sister', 0, 'child', 6, 'b',[-0.015  0  -0.071]' ,'a',UY,'q',0);
uLINK(6) = struct('name','RANKLE_UY' , 'sister', 0, 'child', 7, 'b',[0  0  -0.093]' ,'a',UY,'q',0);
uLINK(7) = struct('name','RANKLE_UX' , 'sister', 0, 'child', 15, 'b',[-0.03  0   0]' ,'a',UX,'q',0);

uLINK(8) = struct('name','LHIP_UZ' , 'sister', 0, 'child', 9, 'b',[0 0.035 -0.044]'   ,'a',UZ,'q',0);
uLINK(9) = struct('name','LHIP_UX' , 'sister', 0, 'child',10, 'b',[-0.035  0     -0.03]'   ,'a',UX,'q',0);
uLINK(10)= struct('name','LHIP_UY' , 'sister', 0, 'child',11, 'b',[0.035  0   0]'   ,'a',UY,'q',0);
uLINK(11)= struct('name','LKNEE' , 'sister', 0, 'child',12, 'b',[-0.015  0  -0.071]' ,'a',UY,'q',0);
uLINK(12)= struct('name','LANKLE_UY' , 'sister', 0, 'child',13, 'b',[0  0  -0.093]' ,'a',UY,'q',0);
uLINK(13)= struct('name','LANKLE_UX' , 'sister', 0, 'child', 14, 'b',[-0.03  0   0]' ,'a',UX,'q',0);

uLINK(14)= struct('name','LFOOT' , 'sister', 0, 'child', 0, 'b',[0.025	0	-0.032]' ,'a',UX,'q',0);
uLINK(15)= struct('name','RFOOT' , 'sister', 0, 'child', 0, 'b',[0.025	0	-0.032]' ,'a',UX,'q',0);

dFindMother(1);   % Find mother link from sister and child data

%%% Substitute the ID to the link name variables. For example, BODY=1.
for n=1:length(uLINK)
    eval([uLINK(n).name,'=',num2str(n),';']);
end

uLINK(1).p = uLINK(1).b;
uLINK(1).R = eye(3);
dForwardKinematics(1);

[uLINK(14).vertex,uLINK(14).face]   = nMakeBox([0.095 0.058 0.008] ,[0.095 0.058 0.008]/2);     % Foot
[uLINK(15).vertex,uLINK(15).face] = nMakeBox([0.095 0.058 0.008] ,[0.095 0.058 0.008]/2);     % Foot