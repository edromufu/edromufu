function tVirtuallyMoveJoints(idx, dq)
global robotCopy

for n=1:length(idx)
    j = idx(n);
    qNew = robotCopy(j).q + dq(n);
##    %Limitando "virtualmente" motores do joelho //limitações nao necessárias
##     if j == 5 || j == 11
##         if qNew < 0
##             qNew = 0;
##         else; if qNew > pi
##                 qNew = pi;
##               end
##         end
##     %Limitando "virtualmente" os placeholders dos pés e COM
##     else
##          if j == 1 || j == 15 || j == 14
##            qNew = 0;
##          end
##     end
    %qNew = wrapToPi(qNew);
    robotCopy(j).q = qNew;
end
