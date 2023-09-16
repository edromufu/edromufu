#!/usr/bin/env python3
#coding=utf-8

class BehaviourParameters():

    def __init__(self):
        self.visionwiseParameters()
        self.behaviourwiseParameters()
        self.movementwiseParameters()

    def movementwiseParameters(self):
        #Tópico do ROS da cabeça
        self.headPositionsTopic = '/u2d2_comm/data2head'

        #Parâmetros dos motores da cabeça 
        self.lookingLeftRad = 0.35
        self.lookingRightRad = -0.35
        self.minVerRad2Kick = -1.22

    def behaviourwiseParameters(self):
        #Relacionado à número de vezes que uma variável deve extrapolar certo valor para resetar
        self.timerCountLimit = 3

        #Tópico do ROS IMU
        self.imuAccelTopic = '/behaviour/imu_accel'

        #Parametros de avaliação de queda nos três eixos
        self.zGravitySecurity = -6  #Valor abaixo do qual a medida de z deve estar para queda
        self.xSensorFront     = 4 #Valor abaixo do qual a medida de x deve estar para queda de frente                           
        self.xSensorBack      = -4  #Valor acima do qual a medida de x deve estar para queda de costas                               
        self.ySensorLeft      = 4 #Valor abaixo do qual a medida de y deve estar para queda sobre o lado esquerdo         
        self.ySensorRight     = -4  #Valor acima do qual a medida de y deve estar para queda sobre o lado direito                         

        #Retornos possíveis da interpretação de posição relativa da bola
        self.left = 'Left'
        self.right = 'Right'
        self.center = 'Center'
        self.top = 'Top'
        self.bottom = 'Bottom'

        #Retornos possíveis da interpretação de queda 
        #(faltam certos parametros como left e right pois serão os mesmos da bola)
        self.front = 'Front'
        self.up = 'Up'
        self.back = 'Back'

        #Tópico de conversa entre ros_packer e state_machine_receiver
        self.stateMachineTopic = '/sensor_observer/state_machine_vars'

        #Tópico de publicação do IMU (Gyro)
        self.imuGyroTopic = '/behaviour/imu_gyro'

    def visionwiseParameters(self):
        #Tópico do ROS
        self.vision2BhvTopic = '/webots_natasha/vision_inference'

        #Parâmetros da câmera
        self.cameraWidth =  640
        self.cameraHeight = 480

        #Parâmetros de interpretação da câmera
        self.xCenterLeftLimit = self.cameraWidth/4
        self.xCenterRightLimit = 3*self.cameraWidth/4
        self.yCenterBottomLimit = 2*self.cameraHeight/3
        self.yCenterTopLimit = self.cameraHeight/3

        self.closeSize = 80*80

