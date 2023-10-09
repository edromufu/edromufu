#!/usr/bin/env python3
#coding=utf-8

import rospy, os, sys
from vision_msgs.msg import Webotsmsg

edrom_dir = '/home/'+os.getlogin()+'/edromufu/src/'

sys.path.append(edrom_dir+'behaviour/transitions_and_states/src')
from behaviour_parameters import BehaviourParameters

class BallInterpreter():

    def __init__(self):
        """
        Construtor:
        - Define as variaveis do ROS
        - Define e inicializa variaveis do código
        """    

        self.parameters = BehaviourParameters()

        #Variaveis do ROS
        rospy.Subscriber(self.parameters.vision2BhvTopic, Webotsmsg, self.callback_vision)

        #Variaveis de código
        self.ballRelativePosition = 'none'
        self.ballClose = False
        self.ballFound = False
        self.countDistance = 0
        self.countFound = 0

    #Funcao chamada pelo agrupador ROS quando necessitar saber 
    #as interpretacoes da bola para alguma requisicao
    def getValues(self):
        """
        -> Output:
            - ballRelativePosition: Ultima posicao relativa da bola interpretada
            - ballClose: Interpretacao da proximidade da bola
            - ballFound: Se False, bola perdida ha muito tempo
        """
        return self.ballRelativePosition, self.ballClose, self.ballFound   

    #Callback do tópico de infos da bola do ROS
    def callback_vision(self, general):    
        """
        -> Funcao:
        Avaliar a bola atraves de:
            - Recebe os dados da bola da visao no campo ball do argumento general
            - Interpreta o x e y retornando a posicao relativa da bola
            - Interpreta o width e height retornando a proximidade da bola
            - Realiza resets das variaveis booelanas baseado em contador
            * Os dados so sao interpretados, ou seja, a posicao relativa so e atualizada
            * se a bola estiver sendo encontrada (para ter uma especie de 'visto por ultimo')  
        -> Input:
            - general: Variavel associada a mensagem recebida no topico do ROS, contem as
            informacoes de todos os objetos, e separada somente para a bola nesse caso.   
        """

        #Captura das informacoes da bola de dentro da mensagem completa
        msg = general.ball

        #Contador para informar que a bola foi perdida apos um numero de vezes sem encontra-la
        self.countFound += 1
        if (self.countFound > self.parameters.timerCountLimit):
            self.ballFound = False
            self.ballClose = False
            self.ballRelativePosition = 'nenhuma'

        if(msg.found):
            #Reseta o contador de informar que a bola foi perdida, pois encontrou :)
            self.ballFound = True
            self.countFound = 0

            #Módulo de verificacao da proximidade da bola, serve para resetar
            #a interpretacao apenas apos um numero definido de medidas desfavoraveis
            if (msg.roi_width*msg.roi_height < self.parameters.closeSize):
                self.countDistance += 1
                if (self.countDistance > self.parameters.timerCountLimit):
                    self.ballClose = False
            else:
                self.countDistance = 0
                self.ballClose = True

            #Módulo de verificacao da posicao relativa da bola
            #Interpretacao horizontal
            if(msg.x < self.parameters.xCenterLeftLimit):
                analysisX = self.parameters.left
            elif(msg.x > self.parameters.xCenterRightLimit):
                analysisX = self.parameters.right
            else:
                analysisX = self.parameters.center
            
            #Interpretacao vertical
            if(msg.y > self.parameters.yCenterBottomLimit): #Deve ser maior por conta da referência ([0,0] no canto superior esquerdo)
                analysisY = self.parameters.bottom
            elif(msg.y < self.parameters.yCenterTopLimit):
                analysisY = self.parameters.top
            else:
                analysisY = self.parameters.center

            #Junção das interpretações em cada eixo
            if(analysisX == self.parameters.center and analysisY == self.parameters.center):
                analysis = self.parameters.center
            else:
                analysis = f'{analysisX} {analysisY}'

            self.ballRelativePosition = analysis

    