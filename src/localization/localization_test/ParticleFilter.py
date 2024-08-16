import numpy as np
from filterpy.monte_carlo import systematic_resample
from numpy.random import randn, uniform

class ParticleFilter():

    # Contructor
    def __init__(self, N, fov, minRange, maxRange, intersections, previousPositionKnown = False, mean = [0,0,0], standardDeviation = [0,0,0], xRange = [0,1000], yRange = [0,1000], headingRange = [0,360]):
        self.N = N  #Número de partículas.
        self.fov = fov  #Campo de visão do robô.
        self.neckAngle = 0
        
        #Intervalo de distância para considerar uma interseção válida.
        self.minRange = minRange 
        self.maxRange = maxRange
        self.intersections = intersections  #Lista de interseções conhecidas no mapa.
        self.reflect = False    # Variável que sinaliza se deve refletir o mapa ou não

        # Cria partículas iniciais com distribuição uniforme ou Gaussiana, dependendo de previousPositionKnown.
        if previousPositionKnown:   #Indica se a posição anterior do robô é conhecida.
            self.particles = self.create_gaussian_particles(mean, standardDeviation)    #média (mean) e desvio padrão (standardDeviation): Parâmetros para gerar partículas com distribuição Gaussiana.
        else:
            self.particles = self.create_uniform_particles(xRange, yRange, headingRange)    #xRange, yRange e headingRange: Intervalos para gerar partículas com distribuição uniforme.

        # Inicializa os pesos das partículas com valores iguais.
        self.weights = np.array([1/self.N]*self.N)
        self.estimate()

    # Gera partículas distribuídas uniformemente dentro dos intervalos fornecidos (xRange, yRange, headingRange).
    def create_uniform_particles(self, xRange, yRange, headingRange):
        particles = np.empty((self.N, 3))   #Cria um array vazio para armazenar as partículas, N x 3.

        #Gera posições x, y e angulos uniformemente distribuídas no intervalo xRange, yRange e headingRange.
        particles[:, 0] = uniform(xRange[0], xRange[1], size=self.N)    
        particles[:, 1] = uniform(yRange[0], yRange[1], size=self.N) 
        particles[:, 2] = uniform(headingRange[0], headingRange[1], size=self.N)    
        
        particles[:, 2] += 360  #Adiciona 360 graus para garantir que os ângulos sejam positivos.
        particles[:, 2] %= 360  #Normaliza os ângulos para o intervalo [0, 360) graus.

        return particles.astype(int)    # Retorna as partículas convertidas para inteiros.

    # Gera partículas distribuídas segundo uma distribuição Gaussiana com a média (mean) e desvio padrão (standardDeviation) fornecidos.
    def create_gaussian_particles(self, mean, standardDeviation):
        particles = np.empty((self.N, 3))   #Cria um array vazio para armazenar as partículas.

        #Gera posições x,y e ângulos com distribuição Gaussiana com média mean[0],mean[1],mean[2] e desvio padrão standardDeviation[0],standardDeviation[1],standardDeviation[2] respectivamente.
        particles[:, 0] = mean[0] + (randn(self.N) * standardDeviation[0])
        particles[:, 1] = mean[1] + (randn(self.N) * standardDeviation[1])
        particles[:, 2] = mean[2] + (randn(self.N) * standardDeviation[2])

        particles[:, 2] += 360      #Adiciona 360 graus para garantir que os ângulos sejam positivos.
        particles[:, 2] %= 360      #Normaliza os ângulos para o intervalo [0, 360) graus.
        return particles.astype(int)    #Retorna as partículas convertidas para inteiros.

    # Prevê a posição futura das partículas com base no movimento do robô (passo) e um erro associado (erro).
    def predict(self, passo, erro,limit = (0,0)):
        # passo e erro = [dx,dy,dtheta]
        # O passo se refere a orientação do robô
        self.particles[:, 2] += (passo[2] + (randn(self.N) * erro[2])).astype(int)  #Atualiza o ângulo de orientação das partículas com o passo de rotação (passo[1]) e um erro Gaussiano (erro[1]).
        self.particles[:, 2] %= 360 #Normaliza os ângulos para o intervalo [0, 360) graus.
        
        # Calcula a distância percorrida com o passo de translação (passo[i]) e um erro Gaussiano (erro[i]).
        distx = passo[0] + (randn(self.N) * erro[0])
        disty = passo[1] + (randn(self.N) * erro[1])
        
        #Atualiza a posição x e y das partículas com base no ângulo de orientação e na distância percorrida.
        self.particles[:, 0] += ( 
            distx * np.cos(self.particles[:, 2]*np.pi/180) + 
            disty * np.sin(self.particles[:, 2]*np.pi/180)
            ).astype(int)
        self.particles[:, 1] += (
            distx * np.sin(self.particles[:, 2]*np.pi/180) -
            disty * np.cos(self.particles[:, 2]*np.pi/180)  
            ).astype(int)
        
        #Reflete as partículas em relação ao meio do campo
        for i in range(len(self.particles)*int(self.reflect)):
            if self.particles[i,0] < (limit[0][0]+limit[1][0])/2:
                self.particles[i,0] = -self.particles[i,0]+limit[1][0]+limit[0][0]
                self.particles[i,2] = (-self.particles[i,2]+180)%360
                self.particles[i,1] = -self.particles[i,1]+limit[1][1]+limit[0][1]
                self.particles[i,2] = (-self.particles[i,2]+360)%360

    # Verifica quais interseções estão dentro do campo de visão (FOV) de uma partícula, considerando a posição e orientação da partícula.
    def checkFOV(self, particle):
        
        seen = []   #Inicializa a lista de interseções vistas pela partícula.c
        for intersection in self.intersections:     #Itera sobre todas as interseções conhecidas no campo.
            distX = particle[0] - intersection[0][0]    #Calcula a diferença x entre a partícula e a interseção.
            distY = particle[1] - intersection[0][1]    #Calcula a diferença y entre a partícula e a interseção.
            distance = (distX**2 + distY**2)**0.5       #Calcula a distância euclidiana entre a partícula e a interseção.  

            if distance <= self.maxRange and distance >= self.minRange: #Verifica se a interseção está dentro do intervalo de distância.
                #Cálculo do ângulo entre a partícula e a interseção: 
                if distX == 0 and distY<0:
                    angle = np.pi/2 #Se distX for 0 e distY for negativo, o ângulo é π/2.
                elif distX == 0 and distY>0:
                    angle = -np.pi/2    #Se distX for 0 e distY for positivo, o ângulo é -π/2.
                elif distY == 0 and distX<0:
                    angle = 0       #Se distY for 0 e distX for negativo, o ângulo é 0.
                elif distY == 0 and distX>0:
                    angle = np.pi   #angle = np.pi: Se distY for 0 e distX for positivo, o ângulo é π.
                elif distX<0:
                    angle = np.arctan(distY/distX)      #Se distX for negativo, o ângulo é o arco tangente de distY sobre distX.
                elif distX>0:
                    angle = np.arctan(distY/distX) - np.pi*np.sign(np.arctan(distY/distX))  #Se distX for positivo, o ângulo é o arco tangente de distY sobre distX menos π vezes o sinal do arco tangente.
                else: 
                    pass

                angle = (angle + 2*np.pi)%(2*np.pi) #Normaliza o ângulo para o intervalo [0, 2π).
                
                #Verificação do campo de visão (FOV):
                limLeft = ((particle[2]+self.neckAngle)*np.pi/180+self.fov/2)%(2*np.pi)  #Calcula o angulo de limite esquerdo do campo de visão.
                limRight = ((particle[2]+self.neckAngle)*np.pi/180-self.fov/2)%(2*np.pi) #Calcula o angulo de limite direito do campo de visão.
                if limLeft >= limRight and angle <= limLeft and angle >= limRight:  #Verifica se o ângulo está dentro do campo de visão quando a particula não engloba o ângulo 0
                    angle_seen = angle*180/np.pi - particle[2]
                    seen.append([intersection,angle_seen])   #Adiciona a interseção à lista de interseções vistas.
                elif limLeft < limRight and (angle <= limLeft or angle >= limRight):    #Verifica se o ângulo está dentro do campo de visão quando a partícula engloba o angulo 0
                    angle_seen = angle*180/np.pi - particle[2]
                    seen.append([intersection,angle_seen])   #Adiciona a interseção à lista de interseções vistas.

        return seen     #Retorna a lista de interseções vistas pela partícula.

    # Calcula o número efetivo de partículas para verificar a necessidade de reamostragem (resample).
    def neff(self):
        return 1. / np.sum(np.square(self.weights)) #Calcula o número efetivo de partículas como o inverso da soma dos quadrados dos pesos.
    
    # Reamostra as partículas com base nos pesos, utilizando o método de reamostragem sistemática (systematic_resample).
    def resample_from_index(self):
        indexes = systematic_resample(self.weights) #Realiza a reamostragem sistemática com base nos pesos das partículas.
        # resample according to indexes
        self.particles[:] = self.particles[indexes]     #Atualiza as partículas com base nos índices reamostrados.
        self.weights.fill(1.0 / self.N)     #Redefine os pesos das partículas para que cada partícula tenha um peso igual.

    # Estima a posição do robô calculando a média e a variância ponderada das partículas (nao estima a direcao)
    def estimate(self):
        #pos = self.particles[:, 0:2]    #Obtém as posições x e y das partículas.
        pos = self.particles

        #Calcula o seno e cosseno de cada angulo para fazer a média do angulo em coordenadas (x,y) e prevenir problemas com ângulos numericamente distantes, mas fisicamente pertos
        mean_sin = np.average(np.sin(np.deg2rad(self.particles[:,2])), weights=self.weights, axis=0)
        mean_cos = np.average(np.cos(np.deg2rad(self.particles[:,2])), weights=self.weights, axis=0)
        mean_angle = np.rad2deg(np.arctan2(mean_sin,mean_cos))  # Converte as coordenas em ângulo em graus
        mean_angle %= 360 #Normaliza os ângulos para o intervalo [0, 360) graus.
        print(mean_angle)
        
        self.mean = np.average(pos[:,0:2], weights=self.weights, axis=0)   #Calcula a média ponderada das posições das partículas.
        self.mean = np.concatenate((self.mean, [mean_angle]),axis=0).astype(int)    #Adiciona a média dos ângulos ao vetor
        self.var  = np.average((pos - self.mean)**2, weights=self.weights, axis=0)  #Calcula a variância ponderada das posições das partículas.
        self.deviation = (self.var)**0.5    #Calcula o desvio padrão a partir da variância.

    #### Utilities ####

    # Simula o movimento de um robô 2D aplicando um passo (passo).
    def moveRobot(robot, passo,limit,reflect):
        robot[2] += passo[2]    #Atualiza o ângulo de orientação do robô com o passo de rotação (passo[1]).
        robot[0] += int(passo[0]*np.cos(robot[2]*np.pi/180) + passo[1]*np.sin(robot[2]*np.pi/180))    #Atualiza a posição x do robô com base no ângulo de orientação e na distância percorrida.
        robot[1] += int(passo[0]*np.sin(robot[2]*np.pi/180) - passo[1]*np.cos(robot[2]*np.pi/180))    #Atualiza a posição y do robô com base no ângulo de orientação e na distância percorrida.
        
        robot[2] += 360  #Adiciona 360 graus para garantir que os ângulos sejam positivos.
        robot[2] %= 360  #Normaliza os ângulos para o intervalo [0, 360) graus.
        
        # Reflete a robô em relação ao meio do campo

        if reflect and robot[0] < (limit[0][0]+limit[1][0])/2:
            robot[0] = -robot[0]+limit[1][0]+limit[0][0]
            robot[2] = (-robot[2]+180)%360
            robot[1] = -robot[1]+limit[1][1]+limit[0][1]
            robot[2] = (-robot[2]+360)%360
        
        return robot    #Retorna a posição atualizada do robô.

    def calculate_weights(self, answer, sensor_noise,limit):
        #measured distances: Distancias medidas pela robo de possíveis landmarks
        #landmarks: pontos de referência no mapa, dentro do campo de visão da particula
        m = len(answer)
        
        for i, particle in enumerate(self.particles):
            # Se a partícula estiver fora do campo seu peso é zerado
            if particle[0]<limit[0][0] or particle[1]<limit[0][1] or particle[0]>limit[1][0] or particle[1]>limit[1][1]:
                self.weights[i] = 0.0
                continue

            particleAnswer = self.checkFOV(particle) #Verifica quais interseções estão na linha de visão da partícula.
            l = len(particleAnswer)
            total_prob = 1.0
            for measured_distance in answer:
                best_prob = 0.0
                for landmark, landmark_angle in particleAnswer:
                    # Compara se o índice do landmark é diferente do da distância medida e se não é 6, índice que representa landmark desconhecido
                    if landmark[2]!=measured_distance[1]: continue

                    # Calcular a distância euclidiana entre a partícula e cada ponto de referência
                    dx = particle[0] - landmark[0][0]
                    dy = particle[1] - landmark[0][1]
                    simulated_distance = np.sqrt(dx**2 + dy**2)

                    # Comparar as distâncias simuladas com as medidas e calcular o peso usando função densidade de probabilidade
                    prob = np.exp(-((simulated_distance - measured_distance[0])**2) / (2 * sensor_noise**2) - 0.001*(landmark_angle - measured_distance[2])**2)
                    #prob = np.exp(- 0.0001*(landmark_angle - measured_distance[2])**2)

                    # Ajuste de probabilidade para partículas que detectam mais informação que a robô
                    if m<l: prob*=m/l

                    # Define a melhor probabilidade da measured distance em relação ao landmark
                    best_prob = max(best_prob, prob)
                
                total_prob *= best_prob
        
            self.weights[i] = total_prob    #Atualiza o peso da partícula da iteração com o valor calculado.
            self.weights[i] += 1e-300   #Evita que o peso seja zero.
    
        self.weights = np.divide(self.weights,sum(self.weights))    #Normaliza os pesos para que a soma seja 1.
