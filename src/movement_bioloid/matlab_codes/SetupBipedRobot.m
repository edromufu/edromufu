%%% SetupBipedRobot.m
%%% Set biped robot structure with Naju's dimensions

global uLINK

UX = [1 0 0]';
UY = [0 1 0]';
UZ = [0 0 1]';

%{
name: Campo reservado para o nome da junta.

sister: Campo definido através do index do elemento que ocupa o mesmo
"andar" na árvore.

child: Campo definido através do index do elemento que ocupa o ramo
esquerdo no "andar" abaixo na árvore.

b: Campo definido pelo vetor que sai da "mother" de um elemento e chega no
elemento.

a: Campo que define o tipo de rotação da junta (em torno do eixo X, Y ou
Z).

q: Campo que recebe a rotação da junta.
%}

% Este processo pode ser substituído pela leitura de um arquivo
uLINK = struct('name', 'CONNECT_LINK', 'sister', 0, 'child', 2, 'b', [0  0  0.341]', 'a', UZ, 'q', 0);

uLINK(2) = struct('name', 'LOWER_BODY', 'sister', 3, 'child', 4, 'b', [0  0  -0.125]', 'a', UZ, 'q', 0);
uLINK(3) = struct('name', 'UPPER_BODY', 'sister', 0, 'child', 16, 'b', [0  0  0.125]', 'a', UZ, 'q', 0);

% Quadril direito
uLINK(4) = struct('name','RLEG_6' , 'sister', 10, 'child', 5, 'b',[0  -0.0425  0]'   ,'a',UZ,'q',0);
uLINK(5) = struct('name','RLEG_J1' , 'sister', 0, 'child', 6, 'b',[0  0   0]'   ,'a',UX,'q',0);
uLINK(6) = struct('name','RLEG_J2' , 'sister', 0, 'child', 7, 'b',[0  0   0]'   ,'a',UY,'q',0);

% Joelho direito
uLINK(7) = struct('name','RLEG_J3' , 'sister', 0, 'child', 8, 'b',[0  0  -0.111]' ,'a',UY,'q',0);

% Pé direito
uLINK(8) = struct('name','RLEG_J4' , 'sister', 0, 'child', 9, 'b',[0  0  -0.0705]' ,'a',UY,'q',0);
uLINK(9) = struct('name','RLEG_J5' , 'sister', 0, 'child', 0, 'b',[0  0   0  ]' ,'a',UX,'q',0);

% Quadril esquerdo
uLINK(10) = struct('name','LLEG_J0' , 'sister', 0, 'child', 11, 'b',[0  0.0425  0]'   ,'a',UZ,'q',0);
uLINK(11) = struct('name','LLEG_J1' , 'sister', 0, 'child',12, 'b',[0  0   0]'   ,'a',UX,'q',0);
uLINK(12)= struct('name','LLEG_J2' , 'sister', 0, 'child',13, 'b',[0  0   0]'   ,'a',UY,'q',0);

% Joelho esquerdo
uLINK(13)= struct('name','LLEG_J3' , 'sister', 0, 'child',14, 'b',[0  0  -0.111]' ,'a',UY,'q',0);

% Pé esquerdo
uLINK(14)= struct('name','LLEG_J4' , 'sister', 0, 'child', 15, 'b',[0  0  -0.0705]' ,'a',UY,'q',0);
uLINK(15)= struct('name','LLEG_J5' , 'sister', 0, 'child', 0, 'b',[0  0   0]' ,'a',UX,'q',0);

% Braço direito
uLINK(16)= struct('name','RARM_J0' , 'sister', 19, 'child', 17, 'b',[0  -0.075  0]' ,'a',-UX,'q',0);
uLINK(17)= struct('name','RARM_J1' , 'sister', 0, 'child', 18, 'b',[0 0 0]' , 'a', UY,'q',0);
uLINK(18)= struct('name','RARM_J2' , 'sister', 0, 'child', 22, 'b',[0 0 -0.083]' ,'a', -UY,'q',0);

% Braço esquerdo
uLINK(19)= struct('name','RARM_J0' , 'sister', 0, 'child', 20, 'b',[0  0.075  0]' ,'a',UX,'q',0);
uLINK(20)= struct('name','RARM_J1' , 'sister', 0, 'child', 21, 'b',[0 0 0]' , 'a', UY,'q',0);
uLINK(21)= struct('name','RARM_J2' , 'sister', 0, 'child', 23, 'b',[0 0 -0.083]' ,'a', -UY,'q',0);

% Placeholders para final do braço
uLINK(22)= struct('name','RHAND' , 'sister', 0, 'child', 0, 'b',[0 0 -0.083]' ,'a',UZ,'q',0);
uLINK(23)= struct('name','LHAND' , 'sister', 0, 'child', 0, 'b',[0 0 -0.083]' ,'a',UZ,'q',0);

FindMother(1);   % Algoritmo para definir as "mothers" de todas as juntas.

%%% Substitute the ID to the link name variables. For example, BODY=1.
for n=1:length(uLINK)
    eval([uLINK(n).name,'=',num2str(n),';']);
end

uLINK(1).p = [0  0  0.314]'; %Define posição absoluta do tronco
uLINK(1).R = eye(3); %Define postura absoluta do tronco
ForwardKinematics(1); %Encontra a posição e postura de todas as outras juntas com base nos parâmetros definidos

torsoDims = [0.03 0.12 0.25];
footDims = [0.1 0.05 0.01];
handDims = [0.03 0.03 0.03];

[uLINK(1).vertex,uLINK(1).face]   = MakeBox(torsoDims  , torsoDims/2);    % "Caixa" para tronco

                                                      %Raio das juntas + Altura do pé
[uLINK(9).vertex,uLINK(9).face]   = MakeBox(footDims ,[footDims(1)/2 footDims(2)/2 0.01+footDims(3)]);     % "Caixa" para pé esquerdo
[uLINK(15).vertex,uLINK(15).face] = MakeBox(footDims ,[footDims(1)/2 footDims(2)/2 0.01+footDims(3)]);     % "Caixa" para pé direito

[uLINK(22).vertex,uLINK(22).face]   = MakeBox(handDims ,[handDims(1)/2 handDims(2)/2 handDims(3)/2]);
[uLINK(23).vertex,uLINK(23).face]   = MakeBox(handDims ,[handDims(1)/2 handDims(2)/2 handDims(3)/2]);
