from ParticleFilter import ParticleFilter as pf
from FieldGenerator import FieldGenerator as fg

from numpy.random import randn, uniform,rand, randint
import numpy as np
import time
import cv2 as cv

# Utiliza o método checkFOV do filtro de partículas para obter as interseções visíveis pelo robô.
def runVision(robot, particleFilter):
    
    intersections = particleFilter.checkFOV(robot)  # Chama o método checkFOV do filtro de partículas para verificar as interseções no campo de visão do robô.
    dist=[]
    angle_noise=40

    falsePositive = 0.0  #Chance de detectar uma interseção que não existe no mapa
    falseNegative = 0.2  #Chance de não detectar alguma das interseções
    
    for intersec, angle in intersections:
        distX = robot[0] - intersec[0][0]    #Calcula a diferença x entre a partícula e a interseção.
        distY = robot[1] - intersec[0][1]    #Calcula a diferença y entre a partícula e a interseção.
        distance = (distX**2 + distY**2)**0.5+sensor_noise*randn(1)     #Calcula a distância e adiciona um erro a cada interseção
        # Simula falsos negativos na detecção de interseções
        if rand() < falseNegative: 
            #print("Falso negativo")
            continue 
        # Adiciona o índice a distância 
        # for n in range(8): if intersec[2]==n: value=(distance,n, angle)
        if intersec[2]==0: value=(distance,0, angle+angle_noise*randn(1))       # Se o índice for 0, identificou o meio do campo
        elif intersec[2]==1: value=(distance,1, angle+angle_noise*randn(1))     # Se o índice for 1, identificou a marca de penalty    
        elif intersec[2]==4: value=(distance,4, angle+angle_noise*randn(1))     # Se o índice for 4, identificou trave esquerda
        elif intersec[2]==5: value=(distance,5, angle+angle_noise*randn(1))     # Se o índice for 5, identificou trave direita
        elif intersec[2]==2: value=(distance,2, angle+angle_noise*randn(1))     # Se o índice for 2, identificou interseção dupla 
        elif intersec[2]==3: value=(distance,3, angle+angle_noise*randn(1))     # Se o índice for 3, identificou interseção tripla 
        elif intersec[2]==6: value=(distance,6, angle+angle_noise*randn(1))     # Se o índice for 3, identificou interseção do circulo central
        dist.append(value)


    
    # Simula falsos positivos na detecção de interseções
    if rand() < falsePositive: 
        #print("Falso positivo")
        dist.append((uniform(30,300),randint(1, 5),uniform(0,fov)))    # Adiciona a lista dist uma distância entre 30 e 300 e um índice entre 1 e 5

    return dist # Retorna as interseções encontradas.

# Executa uma iteração do filtro de partículas:
def runParticleFilter(particleFilter, robotVision, robotVariaton, desvioPos, desvioAngle,sensor_noise,limit):
    # Atualiza as posições das partículas de acordo com a variação do robô e os erros de posição e ângulo.
    particleFilter.predict(robotVariaton,(desvioPos,desvioPos,desvioAngle),limit)

    # Atualiza os pesos das partículas com base nas observações visuais.
    particleFilter.calculate_weights(robotVision, sensor_noise,limit)
    
    # Verifica se o número efetivo de partículas é menor que metade do total. Se sim, faz a reamostragem.
    if particleFilter.neff() < (N/2):
        particleFilter.resample_from_index()

    # Calcula a media e variancia
    particleFilter.estimate()   # Calcula a média e variância das partículas.

def show2Dfield(robot,particles):
    field = fg.generate()   # Gera a representação visual do campo.
    field = fg.drawInField(field)   # Colore e desenha as interseções no campo
    field = fg.drawParticles(field, particles, drawFov=False, fov=fov, minRange=minRange, maxRange=maxRange,neckAngle=robot[3])    # Desenha as partículas no campo.
    if viewRobot: field = fg.drawParticle(field, robot, fov, minRange, maxRange, drawFov=True, color=[0,100,200],robo=True,)  # Desenha a posição do robô no campo.
    return field    # Retorna a imagem do campo com as partículas e o robô desenhados.

def feedbackMovement(robot, desvioPos, desvioAngle):

    dx=0
    dy=0
    dtheta=0
    dneck=0
    
    # Definição da variação do robô por meio das teclas
    #! Gambiarra
    if key==ord("w"): dx=5
    elif key==ord("s"): dx=-5
    elif key==ord("a"): dy=-5
    elif key == ord("d"): dy=5
    elif key== ord("q"): dtheta=5
    elif key==ord("e"): dtheta=-5
    elif key== ord("z"): dneck=5
    elif key==ord("x"): dneck=-5
    elif key==ord("0"): robot[3]=0

    initPasso = [dx,dy,dtheta]  #Define um passo inicial

    # Adiciona um desvio aleatório ao passo.
    passo = [int(initPasso[0]+desvioPos*randn(1)[0]),
             int(initPasso[1]+desvioPos*randn(1)[0]),
             int(initPasso[2]+desvioAngle*randn(1)[0])]   
    
    robot = pf.moveRobot(robot,passo,limit,particleFilter.reflect) # Atualiza a posição do robô com base no passo.
    robot[3] += dneck+360
    robot[3] %= 360
    particleFilter.neckAngle = robot[3]

    return robot,passo


if __name__ == '__main__':
    
    # Parametros para o filtro de particulas
    N = 250   # Número de partículas.
    camHeight = 80
    camAngle = np.pi/4
    fov = 80/180 * np.pi # Campo de visão (em radianos).

    #! Os valores de minRange e maxRange serão mudados
    minRange = 30   # camHeight * np.tan(camAngle-fov/2)    # Alcance mínimo de visão em cm
    maxRange = 240  # camHeight * np.tan(camAngle+fov/4)    # Alcance máximo de visão em cm

    # Parâmetros para a simulação do robô
    desvioPos = 10   # Desvio padrão da posição x e y.
    desvioAngle = 15 # Desvio padrão do ângulo.
    sensor_noise = 30 # Desvio de medição de distância

    # Desvio para o caso em que a robô se perca
    desvioPosLost = 50
    desvioAngleLost = 45
  
    # Posição e direção iniciais do robô.
    initX = randint(fg.padding,fg.padding +fg.fieldLenght)
    initY = randint(fg.padding,fg.padding+fg.fieldWidth)
    initHeading = randint(0, 360)
    initNeck = 0


    # Inicializa a posição do robô.
    robot =np.array((initX, initY, initHeading, initNeck))#(525-200, 315, -180))
    robot[2] = (robot[2]+360)%360   # Garante que o ângulo do robô esteja entre 0 e 360 graus.
    robot[3] = (robot[3]+360)%360   # Garante que o ângulo do pescoço esteja entre 0 e 360 graus.

    robotFound = False  # Indica se o robô foi encontrado.
    showField = True    # Indica se o campo deve ser exibido.
    viewRobot = False # Indica se a robô aparecerá na simulção

    #limit = np.array([[fg.padding,fg.padding],[fg.padding + fg.fieldLenght,fg.padding+fg.fieldWidth]])    #Limites das particulas no campo
    limit = np.array([[0,0],[fg.padding*2 +fg.fieldLenght,fg.padding*2+fg.fieldWidth]])    #Limites das particulas na imagem

    # Range das partículas
    xRange = [fg.padding,fg.padding+fg.fieldLenght]
    yRange = [fg.padding,fg.padding+fg.fieldWidth]

    # Inicializa o filtro de partículas
    #standardDeviation: Desvio padrão das partículas quando tiver uma ultima posição conhecida
    particleFilter = pf(N,fov,minRange,maxRange,fg.fieldIntersections, previousPositionKnown=True, 
                        mean = robot, standardDeviation = [desvioPosLost,desvioPosLost,desvioAngleLost],
                        xRange = xRange, yRange = yRange, headingRange = [0,360])
 
    
    particleFilter.reflect = False # Define se as partículas ficarão espelhadas em relação ao meio do campo
    particleFilter.neckAngle = initNeck # Define se as partículas ficarão espelhadas em relação ao meio do campo

    start_time = time.time()    # Armazena o tempo inicial para calcular o tempo de execução.
    key = 0     # Inicializa a variável que conterá a tecla perssionada na imagem

    # Executa o filtro de partículas até que o robô seja encontrado.
    mean1,mean2,mean3 = np.array([0,0,0])*3
    while robotFound == False:

        # Obtém o feedback da variacao da posicao e direção do movimento
        robot,robotVariaton = feedbackMovement(robot, 0, 0) # Atualiza a posição do robô com feedback do movimento e retorna a variação do passo
        
        robotVision = runVision(robot,particleFilter)   # Obtem as interseções visíveis pelo robô.

        # Desenha o campo e as partículas se showField for verdadeiro:
        if showField:
            field = show2Dfield(robot,particleFilter.particles) # Desenha o campo.

            mean1 = mean2
            mean2 = mean3
            mean3 = particleFilter.mean
            mov_avg=list(((mean1+mean2+mean3)/3).astype(int))
            mov_avg.append(robot[3])
            
            # Desenha a posição mais provável de estar a robo de acordo com o filtro de particulas
            if not viewRobot: field = fg.drawParticle(field, mov_avg, fov, minRange, maxRange, drawFov=True, color=[200,10,250],robo=True)


            # Se o desvio for menor que um certo valor, desenha um circulo na posição média das partículas
            if (particleFilter.deviation[0]**2+particleFilter.deviation[1]**2<30**2): # Desenha a partícula se o desvio for menor que 30
                cv.circle(field,(int(particleFilter.mean[0]),int(particleFilter.mean[1])),15,[0,100,200],3)

                #fg.drawParticle(field, particleFilter.mean,fov, minRange, maxRange, drawFov=True, robo=True)

            cv.imshow("2D Particle filter",cv.flip(field,0))    # Exibe o campo.
            key = cv.waitKey(10) # Espera 10 ms antes de continuar.
        
        # Simula o erro da medição de movimento adicionando um desvio aleatório
        robotVariaton[0:2]+=desvioPos*randn(1)[0]
        robotVariaton[2]+=desvioAngle*randn(1)[0]
        #robotVariaton=np.array([0,0,robotVariaton[2]])

        # Se não identificar interseções itera no filtro de partículas sem considerar erro de posição, para diminuir a dispersão das partículas
        if robotVision==[]: runParticleFilter(particleFilter, robotVision, robotVariaton, 0, 0,sensor_noise,limit) # Executa uma iteração do filtro de partículas
        else: runParticleFilter(particleFilter, robotVision, robotVariaton, desvioPos, desvioAngle,sensor_noise,limit)

        # Para iterar considerando sempre o erro de medição
        #runParticleFilter(particleFilter, robotVision, robotVariaton, desvioPos, desvioAngle,sensor_noise,limit)
        
        # Finaliza o loop com a tecla ESC (27)
        if key == 27:
            break
    end_time = time.time()  # Armazena o tempo final.

    print(f'Convergiu para {particleFilter.mean} com desvio {np.round(particleFilter.deviation)} com  {end_time - start_time} segundos')  # Imprime a posição estimada e o tempo de execução.
    print(f'Posicao real em {robot[0],robot[1],robot[2]%360}') # Imprime a posição real do robô.
    print(f'Diferença real em {particleFilter.mean-robot[0:3]}')

    # Desenha o campo final se showField for verdadeiro
    if showField:
        cv.circle(field,(int(particleFilter.mean[0]),int(particleFilter.mean[1])),15,[0,100,200],3) # Desenha um círculo na posição estimada.
        cv.circle(field,(int(robot[0]),int(robot[1])),15,[0,0,250],3)
        cv.imshow("2D Particle filter",cv.flip(field,0))    # Exibe o campo.
        cv.waitKey(0)   # Espera até que uma tecla seja pressionada.
        cv.destroyAllWindows()  # Fecha todas as janelas.
