function dFindMother(j)
global uLINK

if j ~= 0
    if j == 1
        uLINK(j).mother = 0;
    end
    if uLINK(j).child ~= 0  
        uLINK(uLINK(j).child).mother = j;
        dFindMother(uLINK(j).child);
    end
    if uLINK(j).sister ~= 0
        uLINK(uLINK(j).sister).mother = uLINK(j).mother;
        dFindMother(uLINK(j).sister);
    end
end