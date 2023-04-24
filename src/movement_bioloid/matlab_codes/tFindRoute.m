function idx = tFindRoute(to)
% return the list of joint number connecting ROOT to 'to'
global robotCopy

i = robotCopy(to).mother;
if i == 1
    idx = [to];
else
    idx = [tFindRoute(i) to];
end