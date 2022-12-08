#!/usr/bin/env python3
#coding=utf-8

import rospy
from modularized_bhv_msgs.msg import simMovMsg as motorMsg  #Mensagem associada ao tópico utilizado para receber info dos motores

#Limites relacionados aos motores da cabeça em radianos
[lookRightLimit, lookLeftLimit] = [1.7,-1.7] #Intervalos extremos 
[lookDownLimit, lookUpLimit] = [1.47,0]  #dos motores do pescoço
[centerRightHorLimit, centerLeftHorLimit] = [0.09, -0.09]
ifBallCenteredKickable = 1.3 #Parâmetro que descreve angulação mínima da cabeça na vertical para que, caso a bola esteja centralizada, o chute irá bem

#Parametros da configuração do tópico das posições dos motores
simMov2BhvTopic = '/webots/motors' #String do topico associado as infos dos motores, de onde sera tirada a posicao do pescoco
[indexHorPosition, indexVerPosition] = [0,1] #Index da posição da informação dos motores no vetor

#Parametros de variacao "por step" da cabeça
[horizontalStepsNumber,verticalStepsNumber] = [10,10] #Dita o quão divisível é o range dos motores
deltaX = round(abs((lookRightLimit - lookLeftLimit)/horizontalStepsNumber),2) #Valor em radianos da variação de 1 step no motor horizontal
deltaY = round(abs((lookDownLimit - lookUpLimit)/verticalStepsNumber),2) #Valor em radianos da variação de 1 step no motor vertical

class NeckInterpreter():

    def __init__(self):
        """
        Construtor:
        - Define as variaveis do ROS
        - Define e inicializa variaveis do código
        """

        #Variaveis do ROS
        rospy.Subscriber(simMov2BhvTopic, motorMsg, self.callback_positions)

        #Variaveis de código
        self.horLimitAccomplished = False
        self.verLimitAccomplished = False
        self.verAngleAccomplished = False
        self.horMotorOutOfCenter = False

        self.verMotorPosition = 0
        self.horMotorPosition = 0

        self.headPossibleMovements = []

    #Funcao chamada pelo agrupador ROS quando necessitar saber 
    #a interpretacao dos motores da cabeça para alguma requisicao
    def getValues(self):
        """
        -> Output:
            - horLimitAccomplished: Informa se o limite do motor, para a requisicao atual, foi atingido horizontalmente
            - verLimitAccomplished: Informa se o limite do motor, para a requisicao atual, foi atingido verticalmente
            - verAngleAccomplished: Informa se a cabeca esta suficientemente rotacionada verticalmente para um bom chute
            - horAngleValue: Valor atual de medicao do motor horizontal da cabeca em relacao a referencia
        """

        return self.headPossibleMovements, self.verAngleAccomplished, self.horMotorOutOfCenter, self.horMotorPosition
    
    #Callback do tópico de infos dos motores da cabeça do ROS
    def callback_positions(self, msg):
        """
        -> Funcao:
        Repassar os valores dos motores da cabeça da robô para as variáveis de código 
        acessando os valores recebidos no tópico e verificar dinamicamente se o motor
        vertical atingiu o estabelecido como "bom chute"
        -> Input:
            - msg: Variavel associada a mensagem recebida no topico do ROS, contem as
            informacoes dos motores horizontal e vertical da cabeça   
        """

        #Captura das informações dos motores de forma mais customizável possível, no máximo será preciso mudar o nome do
        #campo da mensagem
        self.horMotorPosition = msg.positions[indexHorPosition]
        self.verMotorPosition = msg.positions[indexVerPosition]

        #Avaliação se a cabeça verticalmente está boa para chute
        if(self.verMotorPosition > ifBallCenteredKickable):
            self.verAngleAccomplished = True
        else:
            self.verAngleAccomplished = False
        
        if self.horMotorPosition < centerLeftHorLimit or self.horMotorPosition > centerRightHorLimit:
            self.horMotorOutOfCenter = True
        else:
            self.horMotorOutOfCenter = False
        
        self.headPossibleMovements = ['L','R','U','D'] #Left, Right, Up, Down

        if(self.horMotorPosition + deltaX > lookRightLimit):
            self.headPossibleMovements.remove('R')
        elif(self.horMotorPosition - deltaX < lookLeftLimit):
            self.headPossibleMovements.remove('L')
        
        if(self.verMotorPosition - deltaY < lookUpLimit):
            self.headPossibleMovements.remove('U')
        elif(self.verMotorPosition + deltaY > lookDownLimit):
            self.headPossibleMovements.remove('D')

