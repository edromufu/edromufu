% Distâncias utilizadas na cinemática inversa
body2RightHip = uLINK(RLEG_J0).b(2);
body2LeftHip = uLINK(LLEG_J0).b(2);
hip2Knee = abs(uLINK(RLEG_J3).b(3));
knee2Foot = abs(uLINK(RLEG_J4).b(3));

% Parâmetros da marcha
stepHeight = 0.05;
stepDuration = 0.5;
stepSubdivisions = 20;
pauseDuration = 1000*stepDuration/stepSubdivisions;
t = linspace(0,stepDuration,stepSubdivisions);
interpolationFunction = ((1-cos(t*pi/stepDuration))/2);

% Posições constantes do Centro de Massa
comPosition = uLINK(LOWER_BODY).p;
comPosture = uLINK(LOWER_BODY).R;

% Variáveis de controle da marcha
leg = 0; %0=direita, 1=esquerda
stage = 1; %1=subida, -1=descida

joint_interpolation = zeros(6,stepSubdivisions);

while true
    tic
  % Escolhe a posição do pé, qual distância ao COM utilizar na IK e indexes
  % dos motores utilizados no atual estágio da marcha na uLINK
  if leg
    newFootPos = uLINK(LLEG_J5).p + [0 0 stage*stepHeight]';
    body2Hip = body2LeftHip;
    forIncrement = 9;
  else
    newFootPos = uLINK(RLEG_J5).p + [0 0 stage*stepHeight]';
    body2Hip = body2RightHip;
    forIncrement = 3;
  end
  
  % Cálculo da cinemática inversa e interpolação do movimento
  joint_angles = IK_leg(comPosition, comPosture, body2Hip, hip2Knee, knee2Foot, newFootPos, eye(3));
  for index = 1:6
    initialPosition = uLINK(index+forIncrement).q;
    finalPosition = joint_angles(index);
  
    joint_interpolation(index,:) = initialPosition + (finalPosition-initialPosition) * interpolationFunction;
  end
  
  % Envia à robô a rotação de cada junta naquele instante e a desenha
    
  for index = 1:stepSubdivisions
      
      current_joint_angle = joint_interpolation(:,index);
      
      for motorIndex = 1:6
          uLINK(motorIndex+forIncrement).q = current_joint_angle(motorIndex);
      end

      ForwardKinematics(LOWER_BODY);
      delete(gca)
      DrawRobot();
      
      java.lang.Thread.sleep(pauseDuration);

  end
 
  
  % Troca de estágio e perna da marcha
  if stage == -1
      leg = not(leg);
  end
  stage = -stage;
        toc
end