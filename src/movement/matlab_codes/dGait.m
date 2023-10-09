dSetupBipedRobot();
% Parâmetros da marcha
stepHeight = 0.05;

% Variáveis de controle da marcha
leg = 0; %0=direita, 1=esquerda
stage = 1; %1=subida, -1=descida

count = 0;
while true
  % Escolhe o pé a ser movido, sua nova posição e indexes
  % dos motores utilizados no atual estágio da marcha na uLINK
  if leg
    newFootPos = uLINK(LFOOT).p + [0 0 stage*stepHeight]';
    currentFoot = LFOOT;
  else
    newFootPos = uLINK(RFOOT).p + [0 0 stage*stepHeight]';
    currentFoot = RFOOT;
  end
  
  % Cálculo da cinemática inversa
  joint_angles = tInverseKinematics(newFootPos, eye(3), currentFoot, uLINK);
  
  % Envia à robô a rotação de cada junta naquele instante e a desenha
  for motorIndex = 1:length(uLINK)
      uLINK(motorIndex).q = joint_angles(motorIndex);
  end

  dForwardKinematics(1);
  nDrawRobot();
  
  if uLINK(currentFoot).p(3) > 0.06
      break;
  end
%  disp(uLINK(currentFoot).p)
%   disp(uLINK(RHIP_UX).q)
%   disp(uLINK(RHIP_UY).q)
%   disp(uLINK(RANKLE_UY).q)
%   disp(uLINK(RANKLE_UX).q)
%   disp('-----------------');
  pause(0.2);

  % Troca de estágio e perna da marcha
    if stage == -1
       leg = not(leg);
    end
  stage = -stage;
  count = count + 1;
end
disp(count/4);