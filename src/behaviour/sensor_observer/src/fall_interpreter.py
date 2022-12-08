#!/usr/bin/env python3
#coding=utf-8

import rospy
from geometry_msgs.msg import Vector3

simulation2BhvTopic = '/webots_natasha/behaviour_controller' #Endereço do tópico que está transmitindo as informações do acelerometro

timesSecurity = 7 #Numero de vezes para verificacoes de seguranca no codigo

#Parametros de avaliação de queda nos três eixos
yGravitySecurity = 4  #Valor abaixo do qual a medida de y deve estar para queda
zSensorFront     = -5 #Valor abaixo do qual a medida de z deve estar para queda de frente                           
zSensorBack      = 5  #Valor acima do qual a medida de z deve estar para queda de costas                               
xSensorLeft      = -5 #Valor abaixo do qual a medida de x deve estar para queda sobre o lado esquerdo         
xSensorRight     = 5  #Valor acima do qual a medida de x deve estar para queda sobre o lado direito                         

class FallInterpreter():

    def __init__(self):
        """
        Construtor:
        - Define as variaveis do ROS
        - Define e inicializa variaveis do código
        """
        
        #Variaveis do ROS
        rospy.Subscriber(simulation2BhvTopic, Vector3, self.callback_sensor)

        #Variaveis de código
        self.fallState = 'Up' #Estado da queda do robô, sendo up = em pé
        self.countFalled = 0 #Contador de quedas interpretadas para segurança
    
    #Funcao chamada pelo agrupador ROS quando necessitar saber 
    #a interpretacao da queda para alguma requisicao
    def getValues(self):
        """
        -> Output:
            - fallState: Estado de queda avaliado pelo código, Up = de pé
        """

        return self.fallState
    
    #Callback do tópico de infos do acelerometro do ROS
    def callback_sensor(self, msg):
        """
        -> Funcao:
        Avaliar se houve queda e para que lado atraves de:
            - Recebe os dados do acelerometro do simulador no msg
            - Interpreta a medição y retornando se houve queda
            - Interpreta as medições x e z retornando a orientação da queda
            - Confia mais no estar de pé do que na queda, evitando falsos positivos 
            * A orientação só é interpretada se a queda for detectada mais vezes do que o timesSecurity estipula 
            (lembrando que o timesSecurity é a variavel que estipula o numero de vezes para verificacoes de seguranca), poupando processamento
        -> Input:
            - msg: Variavel associada a mensagem recebida no topico do ROS, contem as
            informacoes do acelerometro    
        """

        #Contando quantas das ultimas medições detectou-se queda, 
        #reseta quando apenas uma não conta, ou seja, confia em estar de pé
        #desconfia de ter caido, pois durante a caminhada a acelaração efetuada
        #pelo robô pode fazer com que o sensor tenha uma medida de "queda"
        if (msg.y < yGravitySecurity):
            self.countFalled += 1
        else:
            self.fallState = 'Up'
            self.countFalled = 0

        #Situação na qual interpretou-se queda muitas vezes seguidas,
        #realizará as verificações para determinar o lado de queda
        if(self.countFalled > timesSecurity):
            #Verificação se caiu sobre algum lado é feita depois
            #da verificação se caiu de frente ou de costas, pois os
            #últimos são mais prováveis e eficientes (page costuma 
            #levantar mesmo se não estiver)
            if msg.z < zSensorFront:
                #Caiu de costa
                self.fallState = 'Back'

            elif msg.z > zSensorBack:
                #Caiu de frente     
                self.fallState = 'Front'

            elif msg.x < xSensorLeft:
                #Caiu sobre o lado direito    
                self.fallState = 'Right'

            elif msg.x > xSensorRight:
                #Caiu sobre o lado esquerdo    
                self.fallState = 'Left'  





    