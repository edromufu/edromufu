
import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32MultiArray, Float32  # Para movimento como um vetor (x, y)
#from sensor_msgs.msg import Imu  # Para dados do IMU
from vision_msgs.msg import *

from ParticleFilter import ParticleFilter as pf
from FieldGenerator import FieldGenerator as fg


from numpy.random import randn, uniform,rand, randint
import numpy as np
import time
import cv2 as cv

#mexer na rnvision e nos pesos de oimu, conferir pesos de angulos do pescoço e da robo, se estão certos

class Localization(Node):
    
    def __init__(self, node_name):

        super().__init__(node_name)
        self.get_logger().info('Nó, iniciado')

        self.simulation = self.declare_parameter('loc/simulation',False).get_parameter_value().bool_value
        self.N = self.declare_parameter('loc/number',250).get_parameter_value().integer_value   # Número de partículas.
        
        self.fov = 80/180 * np.pi # Campo de visão (em radianos).

        # Inicializa a posição do robô.[x, y, IMUangle=0, neckUZ], #! definir valores
        self.robot = np.array(self.declare_parameter('loc/initpos',[0,0,0,0]).get_parameter_value().integer_array_value)

        self.robot =np.array((randint(fg.padding,fg.padding +fg.fieldLenght), randint(fg.padding,fg.padding+fg.fieldWidth), randint(0, 360), 0))#(525-200, 315, -180))

        self.robot[2] = (self.robot[2]+360)%360   # Garante que o ângulo do robô esteja entre 0 e 360 graus.
        self.robot[3] = (self.robot[3]+360)%360   # Garante que o ângulo do pescoço esteja entre 0 e 360 graus.
        self.lastPhi = self.robot[2]

        # Assinatura dos tópicos  #! Mudar nome dos topicos e das mensagens
        self.movement_subscription = self.create_subscription(Float32MultiArray, 'movement_topic',self.movement_callback,10)
        self.vision_subscription = self.create_subscription(Webotsmsg, 'vision2BhvTopic', self.vision_callback, 10)  # Tópico de visão
        self.imu_subscription = self.create_subscription(Float32, 'imu_topic', self.imu_callback, 10)   #! corrigir msgs neste codigo e no teste


        # Armazena os dados das mensagens recebidas #! Inicializar com valores padrões ou garantir uso de valores existentes no loop
        self.movement_data = None
        self.vision_data = None
        self.imu_data = None

        # Configuração do timer para rodar o localizationLoop a cada X segundos
        self.timer_period = 0.01  # em segundos
        self.timer = self.create_timer(self.timer_period, self.localizationLoop)

        # Parametros da camera para o filtro de particulas
        self.camHeight = 70
        self.camRange = 300
        self.minRange = 30   

        # Parâmetros para a simulação do robô
        self.desvioPos = 10   # Desvio padrão da posição x e y.
        self.desvioAngle = 15 # Desvio padrão do ângulo.
        self.sensor_noise = 60 # Desvio de medição de distância
        self.angle_noise = 10 # Desvio de cálculo do ângulo de um objeto em relação ao centro da camera
        self.IMU_noise = 10 # Desvio de medição do IMU

        # Desvio para o caso em que a robô se perca
        desvioPosLost = 50
        desvioAngleLost = 45

        self.robotFound = False  # Indica se o robô foi encontrado.
        self.showField = self.declare_parameter('loc/showfield',self.simulation).get_parameter_value().bool_value or True   # Indica se o campo deve ser exibido.
        self.viewRobot = self.simulation # Indica se a robô aparecerá na simulção 

        #limit = np.array([[fg.padding,fg.padding],[fg.padding + fg.fieldLenght,fg.padding+fg.fieldWidth]])    #Limites das particulas no campo
        self.limit = np.array([[0,0],[fg.padding*2 +fg.fieldLenght,fg.padding*2+fg.fieldWidth]])    #Limites das particulas na imagem

        # Range das partículas
        xRange = [fg.padding,fg.padding+fg.fieldLenght]
        yRange = [fg.padding,fg.padding+fg.fieldWidth]

        # Inicializa o filtro de partículas
        #standardDeviation: Desvio padrão das partículas quando tiver uma ultima posição conhecida
        self.particleFilter = pf(self.N,self.fov,self.minRange,fg.fieldIntersections, previousPositionKnown=False, 
                            mean = self.robot, standardDeviation = [desvioPosLost,desvioPosLost,desvioAngleLost],
                            xRange = xRange, yRange = yRange, headingRange = [0,360])
    
        
        self.particleFilter.reflect = True # Define se as partículas ficarão espelhadas em relação ao meio do campo
        self.phi0 = self.robot[2] #! Conferir se não dá erro

    def localizationLoop(self):

        #if self.movement_data is None or self.vision_data is None or self.imu_data is None:
        if self.movement_data is None or self.imu_data is None:
            self.get_logger().info('Aguardando dados dos tópicos...')
            return  # Se algum dos dados não foi recebido, espera até a próxima execução

        
        # Obtém o feedback da variacao da posicao e direção do movimento [delta_x,delta_y,IMUangle,neckUZ]
        self.infoRobot = self.feedbackMovement() # Atualiza a posição do robô com feedback do movimento e retorna a variação do passo
        phiVariation = self.infoRobot[2] - self.lastPhi
        self.lastPhi = self.infoRobot[2]
        
        if self.vision_data is not None or self.simulation:
            robotVision = self.runVision()   # Obtem as interseções visíveis pelo robô.
        else: 
            robotVision = []

        if self.simulation: 
            # Move a robô
            step = np.concatenate((self.infoRobot[0:2],[phiVariation]))
            
            self.robot = pf.moveRobot(self.robot,step,self.limit,self.particleFilter.reflect) # Atualiza a posição do robô com base no passo.
            self.robot[3] = self.infoRobot[3]


            # Simula o erro da medição de movimento adicionando um desvio aleatório
            self.infoRobot[0:2]+=self.desvioPos*randn(1)[0]
            phiVariation+=self.desvioAngle*randn(1)[0]

        # Desenha o campo e as partículas se showField for verdadeiro:
        if self.showField:

            field = self.show2Dfield() # Desenha o campo.

            cv.imshow("2D Particle filter",cv.flip(field,0))    # Exibe o campo.
            key = cv.waitKey(10) # Espera 10 ms antes de continuar.

            if key == 27:
                cv.destroyAllWindows()
                self.get_logger().warn('Sucesso! Alvo atingido!')
                self.timer.cancel()  # Cancela o timer
                rclpy.shutdown()  # Isso encerra o spin()
                print(3)

        robotVariation = [self.infoRobot[0],self.infoRobot[1],phiVariation]

        # Se não identificar interseções itera no filtro de partículas sem considerar erro de posição, para diminuir a dispersão das partículas
        if robotVision==[]: self.runParticleFilter(robotVariation, robotVision, 0, 0,self.limit) # Executa uma iteração do filtro de partículas
        else: self.runParticleFilter(robotVariation, robotVision, self.desvioPos, self.desvioAngle,self.limit)

        if (self.particleFilter.deviation[0]**2+self.particleFilter.deviation[1]**2<10**2) and (self.particleFilter.deviation[2]**2 < 5**2):
            self.robotFound = True
            print("Found")
        print('Part', self.particleFilter.mean)
        print('Robo', self.robot[0:3])

    def runParticleFilter(self,robotVariation, robotVision, desvioPos, desvioAngle, limit): 

        # Atualiza as posições das partículas de acordo com a variação do robô e os erros de posição e ângulo.
        self.particleFilter.predict(robotVariation,(desvioPos,desvioPos,desvioAngle),limit)

        # Atualiza os pesos das partículas com base nas observações visuais.
        self.particleFilter.calculate_weights(robotVision, self.sensor_noise, self.angle_noise, self.IMU_noise, limit,self.camRange,self.infoRobot[3],self.infoRobot[2], self.robotFound)
        
        # Verifica se o número efetivo de partículas é menor que metade do total. Se sim, faz a reamostragem.
        if self.particleFilter.neff() < (self.N/2):
            self.particleFilter.resample_from_index()

        # Calcula a média e variância das partículas.
        self.particleFilter.estimate()   

    def show2Dfield(self):
        field = fg.generate()   # Gera a representação visual do campo.
        field = fg.drawInField(field)   # Colore e desenha as interseções no campo
        field = fg.drawParticles(field, self.particleFilter.particles, drawFov=False, fov=self.fov, minRange=self.minRange, maxRange=self.camRange,neckAngle=self.infoRobot[3])    # Desenha as partículas no campo.
        
        # Visualiza a posição real da robô ou a posição estimada
        if self.viewRobot: field = fg.drawParticle(field, self.robot, self.fov, self.minRange, self.camRange, drawFov=True, color=[0,100,200],robo=True,)  # Desenha a posição do robô no campo.
        else: 
            field = fg.drawParticle(field, list(self.particleFilter.mean)+[self.infoRobot[3]], self.fov, self.minRange, self.camRange, drawFov=True, color=[200,10,250],robo=True)  # Desenha a posição mais provável de estar a robo de acordo com o filtro de particulas
            
        # Se o desvio for menor que um certo valor, desenha um circulo na posição média das partículas
        if (self.particleFilter.deviation[0]**2+self.particleFilter.deviation[1]**2<30**2): # Desenha a partícula se o desvio for menor que 30
            cv.circle(field,(int(self.particleFilter.mean[0]),int(self.particleFilter.mean[1])),15,[0,100,200],3)

        return field    # Retorna a imagem do campo com as partículas e o robô desenhados.

    def runVision(self):
        #! Penalty e center são iguais
        #! Organizar 
        width = 640
        msg = self.vision_data
        if self.simulation: 
             return self.runVisionSimulation(self.robot,self.particleFilter,self.camRange,self.infoRobot[3])

        center = [msg.center.x, msg.center.x_position, msg.center.z_position]
        penalty = [None, None, None]
        l_intersection = [msg.l_intersection.x, msg.l_intersection.x_position, msg.l_intersection.z_position]
        t_intersection = [msg.t_intersection.x, msg.t_intersection.x_position, msg.t_intersection.z_position]
        rightgoal = [msg.rightgoal.x,msg.rightgoal.x_position,msg.rightgoal.z_position]
        leftgoal = [msg.leftgoal.x,msg.leftgoal.x_position,msg.leftgoal.z_position]
        x_intersection = [msg.x_intersection.x, msg.x_intersection.x_position, msg.x_intersection.z_position]

        # Defina as mensagens dos objetos organizados na ordem dos índices
        objects_msgs = [center, penalty, l_intersection, t_intersection, rightgoal, leftgoal, x_intersection]


        # Inicializa uma lista para armazenar as detecções processadas
        dist = []   

        # Itera sobre cada tipo de objeto e calcula distância, índice e ângulo
        for index, objects in enumerate(objects_msgs):
                if objects[0] is None:
                    continue  # Ignora objetos com valores None (como penalty)
                
                # Calcula a distância horizontal até o objeto
                distance = (np.sqrt(np.array(objects[1])**2 + np.array(objects[2])**2)) 

                # Calcula o ângulo do objeto até o centro da câmera
                angle = self.fov*(np.array(objects[0])-width*0.5)/width  

                # Adiciona o resultado à lista dist com o índice do tipo de objeto
                dist.append((distance, index, angle))

        return dist  # Retorna as distâncias calculadas e o índice de cada objeto

        
    
    # Utiliza o método checkFOV do filtro de partículas para obter as interseções visíveis pelo robô.
    def runVisionSimulation(self, robot, particleFilter,maxRange,neckUZ):
        
        intersections = particleFilter.checkFOV(robot,maxRange,neckUZ)  # Chama o método checkFOV do filtro de partículas para verificar as interseções no campo de visão do robô.
        dist=[]

        falsePositive = 0.0  #Chance de detectar uma interseção que não existe no mapa
        falseNegative = 0.2  #Chance de não detectar alguma das interseções

        for intersec, angle in intersections:
            distX = robot[0] - intersec[0][0]    #Calcula a diferença x entre a partícula e a interseção.
            distY = robot[1] - intersec[0][1]    #Calcula a diferença y entre a partícula e a interseção.
            distance = (distX**2 + distY**2)**0.5+self.sensor_noise*randn(1)     #Calcula a distância e adiciona um erro a cada interseção
            # Simula falsos negativos na detecção de interseções
            if rand() < falseNegative: 
                #print("Falso negativo")
                continue 
            # Adiciona o índice a distância 
            # for n in range(8): if intersec[2]==n: value=(distance,n, angle)
            if intersec[2]==0: value=(distance,0, angle+self.angle_noise*randn(1))       # Se o índice for 0, identificou o meio do campo
            elif intersec[2]==1: value=(distance,1, angle+self.angle_noise*randn(1))     # Se o índice for 1, identificou a marca de penalty    
            elif intersec[2]==4: value=(distance,4, angle+self.angle_noise*randn(1))     # Se o índice for 4, identificou trave esquerda
            elif intersec[2]==5: value=(distance,5, angle+self.angle_noise*randn(1))     # Se o índice for 5, identificou trave direita
            elif intersec[2]==2: value=(distance,2, angle+self.angle_noise*randn(1))     # Se o índice for 2, identificou interseção dupla 
            elif intersec[2]==3: value=(distance,3, angle+self.angle_noise*randn(1))     # Se o índice for 3, identificou interseção tripla 
            elif intersec[2]==6: value=(distance,6, angle+self.angle_noise*randn(1))     # Se o índice for 6, identificou interseção do circulo central
            dist.append(value)
    
        # Simula falsos positivos na detecção de interseções
        if rand() < falsePositive: 
            #print("Falso positivo")
            dist.append((uniform(30,300),randint(1, 5),uniform(0,self.fov)))    # Adiciona a lista dist uma distância entre 30 e 300 e um índice entre 1 e 5

        return dist # Retorna as interseções encontradas.

    def feedbackMovement(self):
        
        #! Core, walking
        step = self.movement_data.data[0:2]  # Exemplo de extração dos deltas

        #! Core head, data2head
        neckUZ = np.rad2deg(self.movement_data.data[2])  #! Conferir qual indice de neckuz

        
        IMUangle = self.imu_data
        IMUangle %= 360
        
        self.get_logger().info(f'Recebendo feedback: {[step[0],step[1], IMUangle, neckUZ]}')  # Log para depuração
        
        return [int(step[0]),int(step[1]), IMUangle, neckUZ]    # Retorna o passo da robô, o angulo do IMU e o angulo da camera em UZ

    def movement_callback(self, msg):
            self.movement_data = msg  # Armazena os dados do tópico de movimento

    def vision_callback(self, msg):
            self.vision_data = msg  # Armazena os dados do tópico de visão

    def imu_callback(self, msg):
        # Obtém o ângulo em torno do eixo Z (yaw)
        yaw = msg.data

        # Converte o ângulo de radianos para graus
        self.imu_data = np.rad2deg(yaw)

def main():
    rclpy.init()

    node_localization = Localization('Localizacao')

    rclpy.spin(node_localization)  # Mantém o nó rodando para receber as mensagens e rodar o loop
    #! Não finaliza o código

    node_localization.destroy_node()
    print(1)
    rclpy.shutdown()
    print(2)

if __name__=='__main__':
    main()

"""
    while rclpy.ok() and not node.timer_canceled:
        rclpy.spin_once(node)  # Executa o spin uma vez por loop
        
        """