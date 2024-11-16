function nDrawAllJoints(j)
global uLINK
radius    = 0.004;
len       = 0.015;
joint_col = 0;

if j ~= 0  
    if ~isempty(uLINK(j).vertex)
        vert = uLINK(j).R * uLINK(j).vertex;
        for k = 1:3
            vert(k,:) = vert(k,:) + uLINK(j).p(k); % adding x,y,z to all vertex
        end
        nDrawPolygon(vert, uLINK(j).face,0);
    end
    
    hold on
    
    i = uLINK(j).mother;
    if i ~= 0
        nConnect3D(uLINK(i).p,uLINK(j).p,'k',2);
    end
    nDrawCylinder(uLINK(j).p, uLINK(j).R * uLINK(j).a, radius,len, joint_col);
    
    
    nDrawAllJoints(uLINK(j).child);
    nDrawAllJoints(uLINK(j).sister);
end
