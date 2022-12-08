#!/usr/bin/env python3
#coding=utf-8

import movement_controller
import numpy as np

import rospy
from std_msgs.msg import Float32

from controller import Supervisor

#Vetores de posição e rotação do robô no início
standStillRobotTranslationStart = [-0.0007, -0.00426, 0.454]
standStillRobotRotationStart    = [0.00395, -0.00539, 0.99997, 1.55527]

#Parametros da caminhada
TIME_TO_RUN = 30
TIME_FALL_SECURITY = 4

#Parametros de avaliacao
acceptableAX = 0.134
acceptableAY = 0.3004
acceptableAZ = 0.4413
rotationGap = [acceptableAX, acceptableAY, acceptableAZ]

#Parametros da busca sistemática
bLimitVel = 0
tLimitVel = 0.36
step = 0.02
velVec = np.arange(bLimitVel, tLimitVel+step, step)

#Parametros designados:
#Hericles: [0, 0.1]
#Peroleo: [0.12, 0.22]
#Pedro: [0.24, 0.34]
#Exemplo para valores do Hericles:
yourBottomLimit = 0
yourTopLimit =  0.1

vzIndividual = np.arange(yourBottomLimit, yourTopLimit+step, step)

class Optimization(object):
    ###########################FUNÇÕES DO CÓDIGO###########################

    #Construtor, inicializa todas as variáveis utilizadas para manipulação durante a otimização
    def __init__(self):
        #Inicialização da "Constantes" da biblioteca do Webots
        self.natasha = Supervisor()
        self.timeStep = int(self.natasha.getBasicTimeStep())
        
        self.accel_sensor = self.natasha.getDevice('Accelerometer') #Definição e ativação do Acelerômetro
        self.accel_sensor.enable(self.timeStep)

        self.touch_sensors = [self.natasha.getDevice('LTouch Sensor'), self.natasha.getDevice('RTouch Sensor')]
        for sensor in self.touch_sensors:
            sensor.enable(self.timeStep)

        #Inicilização de outros controladores
        self.movement = movement_controller.ControllerMovement(self.natasha)

        #Inicialização do node da Natasha e captura dos seus campos de translação e rotação
        self.natasha_node = self.natasha.getSelf()
        self.natasha_translation_field = self.natasha_node.getField('translation')
        self.natasha_rotation_field = self.natasha_node.getField('rotation')

        #Inicialização das variáveis de fluxo do código
        self.firstLoop = True
        self.fallCount = 0

        #Inicialização das variáveis para a fitness
        self.timeVector = []
        self.LbumperVector = []
        self.RbumperVector = []
        self.initialXYZ = []
        self.finalXYZ = []

        #TEMPORÁRIO
        self.pubTest = rospy.Publisher('test', Float32, queue_size= 100)
        self.testMsg = Float32()

    #Define o loop do código
    def start(self):

        if self.firstLoop: #Primeiro loop
            self.firstLoop = False
            self.reset()  #8secs
            self.wait(TIME_TO_RUN/3.75) #8secs
            self.evalBase()       

        for i in range(len(velVec)):   #Loops seguintes com os parametros variando
            for j in range(len(velVec)):
                for k in range(len(vzIndividual)): 

                    while not self.isResetOk(): #Verifica as condições setadas de reset (bumpers e acelerometros)
                        self.reset() #8secs
                        self.wait(TIME_TO_RUN/3.75) #8secs

                    self.vectVel = [ round(velVec[i],2) , round(velVec[j],2) , round(vzIndividual[k],2) ]
                    self.walk(TIME_TO_RUN) #30 secs

                    self.evalFitness()

    #Função que determina um tempo a ser rodado na simulação
    def wait(self, seconds):
        for i in range(int(1000*seconds/self.timeStep)):
            self.natasha.step(self.timeStep)

    ###########################FUNÇÕES DO RESET###########################

    #Função com a chamada de todas os algoritmos necessarios para o reset da robô
    def reset(self):
        # 8 sec in sim

        self.resetMotors() #3 sec in sim
        self.resetPosition() #2 sec in sim
        self.goToFP() #3 sec in sim
    
    #Função que retorna os motores para posição 0
    def resetMotors(self):
        reset_motors_time = 3

        self.movement.zeros()

        self.wait(reset_motors_time)   

    #Função que realiza o reposicionamento da robô através dos vetores típicos da situação inicial e anulação temporária da física
    def resetPosition(self):
        reset_position_time = 2

        self.natasha.simulationResetPhysics()
        self.natasha_translation_field.setSFVec3f(standStillRobotTranslationStart)
        self.natasha.simulationResetPhysics()
        self.natasha_rotation_field.setSFRotation(standStillRobotRotationStart)
        self.natasha.simulationResetPhysics()

        self.wait(reset_position_time)   

    #Função que seta os motores para a pose inicial, a fim de padronizar o começo
    def goToFP(self):
        go_to_fp_time = 3

        self.movement.goToFP()

        self.wait(go_to_fp_time)

    ###########################FUNÇÕES DE AVALIAÇÃO DO RESET###########################

    #Função que captura os dados do primeiro reset
    def evalBase(self):
        [accel_x, accel_y, accel_z] = self.accel_sensor.getValues()

        [self.BASEAX, self.BASEAY, self.BASEAZ] = [accel_x, accel_y, accel_z]

    #Função que utiliza os bumpers para verificar se ambos estão em contato, ou seja,
    #a robô está de pé após o reset. Após isso realiza uma verificação dos parâmetros
    #de aceleração da robô, para verificar se o reset é bom o suficiente.
    def isResetOk(self):
        if self.touch_sensors[0].getValue() and self.touch_sensors[1].getValue(): #Avaliação dos bumpers
            gapAX, gapAY, gapAZ = self.evalGap() 
            if gapAX < rotationGap[0] and gapAY < rotationGap[1] and gapAZ < rotationGap[2]: #Avaliação das acelerações medidas 
                    return True
           
        return False

    #Função para avaliar o gap dos parametros de translação e de rotação da robo 
    #a cada reset em relação ao primeiro reset
    def evalGap(self):
        [accel_x, accel_y, accel_z] = self.accel_sensor.getValues()

        #Captura a diferença para a situação base daquele caso para cada variavel 
        axdiff = abs(self.BASEAX - accel_x)
        aydiff = abs(self.BASEAY - accel_y)
        azdiff = abs(self.BASEAZ - accel_z)

        return (axdiff, aydiff, azdiff)

    ###########################FUNÇÕES DA CAMINHADA###########################

    #Função que aciona a variação dos motores com base no tópico opencm/conversion
    #com walk_flag ativo
    def walk(self, seconds):
        self.fallCount = 0
        self.movement.changeWalkFlag(True, self.vectVel)

        for i in range(int(1000*seconds/self.timeStep)):
            self.movement.positionFunction() 
            self.natasha.step(self.timeStep) #Caminhada

            if(self.dynamCapture(i)): #Checagem de interrupção
                break

        self.movement.changeWalkFlag(False, self.vectVel)


    #Função que captura quaisquer dados necessários para o fitness que precisam
    #ser capturados durante a caminhada
    def dynamCapture(self, currentStep):

        #Captura de um vetor de tempo para avaliação
        self.timeVector += [round( (currentStep+1)*0.016 , 4)]

        #Captura dos sensores de passos para contagem de passo
        self.LbumperVector += [self.touch_sensors[0].getValue()]
        self.RbumperVector += [self.touch_sensors[1].getValue()]

        #Verificando se ambos os pés não estão em contato com o chão e incrementando/resetando
        #o parametro de avaliação de queda
        if(not self.LbumperVector[currentStep] and not self.RbumperVector[currentStep]):
            self.fallCount += 1
        else:
            self.fallCount = 0
        
        #Captura das posições finais e iniciais
        if(currentStep == 0):
            self.initialXYZ = self.natasha_translation_field.getSFVec3f()

        if(currentStep == 1874 ):
            self.finalXYZ = self.natasha_translation_field.getSFVec3f()

        if(self.fallCount > 1000*TIME_FALL_SECURITY/self.timeStep): #Caso de queda, captura a posição final e para a caminhada
            self.finalXYZ = self.natasha_translation_field.getSFVec3f()
            return True
        else:
            return False

    ###########################FUNÇÕES DA CAMINHADA###########################

    #Função com a chamada de todas os algoritmos necessarios para avaliação
    #da run atual da robô
    def evalFitness(self):
        self.parametersCalc()
        self.parametersReset()
    
    #Função que realiza as rotinas necessárias para tornar úteis o dados
    #capturados da run atual da robô
    def parametersCalc(self):
        #Captura do dados inputados da run
        velocities = self.vectVel
        #Calculo do tempo de caminhada da robô
        walkedTime = (self.timeVector[len(self.timeVector)-1] - TIME_FALL_SECURITY)

        #Calculo do deslocamento da robô
        deltaVec = [0]*3
        for index in range(len(self.initialXYZ)):
            deltaVec[index] = self.finalXYZ[index] - self.initialXYZ[index]

        #Calculo do numero de passos da robô
        lSteps = 0 #Esquerdo
        for i in range(len(self.LbumperVector)):
            if i > 0:
                if self.LbumperVector[i] == 1 and self.LbumperVector[i-1] == 0:
                    lSteps += 1
        
        rSteps = 0 #Direito
        for i in range(len(self.RbumperVector)):
            if i > 0:
                if self.RbumperVector[i] == 1 and self.RbumperVector[i-1] == 0:
                    rSteps += 1

        self.paramtersSave(velocities, walkedTime, deltaVec, lSteps, rSteps)

    #Função que realiza o reset para a próxima geração das variaveis
    #dos dados sobre a run
    def parametersReset(self):
        self.timeVector.clear()
        self.LbumperVector.clear()
        self.RbumperVector.clear()
        self.initialXYZ.clear()
        self.finalXYZ.clear()

    def paramtersSave(self, velocities, walkedTime, deltaVec, lSteps, rSteps):
        txt = ( '------------------------------------------------------------------------------------------\n' +
                'Velocidades: [' + str(velocities[0]) + ']  ' + '[' + str(velocities[1]) + ']  ' + '[' + str(velocities[2]) + ']\n' +
                'Distancias: [' + str(deltaVec[0]) + ']  ' + '[' + str(deltaVec[1]) + ']  ' + '[' + str(deltaVec[2]) + ']\n' +
                'Passos Esquerda: [' + str(lSteps) + ']  ' + 'Passos Direita: [' + str(rSteps) + ']\n' +
                'Tempo de caminhada: [' + str(walkedTime) +']\n' +
                '------------------------------------------------------------------------------------------\n\n'
              )
        
        with open("paramtersTxt.txt", "ab") as f:
          	f.write(txt.encode('utf-8', 'ignore'))

if __name__ == '__main__':
    rospy.init_node('Optimization_webots_node', anonymous=False)
    controller = Optimization()
    controller.start()
    rospy.spin()
