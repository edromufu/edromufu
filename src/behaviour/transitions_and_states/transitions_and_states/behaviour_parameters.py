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
        # mudar para a camera nova
        self.lookingLeftRad = 0.35
        self.lookingRightRad = -0.35
        self.minVerRad2Kick = -1.22

    def behaviourwiseParameters(self):
        #Relacionado à número de vezes que uma variável deve extrapolar certo valor para resetar
        #Tirar essas variáveis aqui para o imu NOVO
        self.timerCountLimit = 3
        self.timerPage = 60 #s
        self.timerFirstPose = 5 #s
        self.timerWalk = 15 #s

        #Tópico do ROS IMU
        #Muda esse tópico igual gyro
        self.imuAccelTopic = '/behaviour/imu_accel'

        #Só da para arrumar com robo pronta
        self.xGravitySecurity = 6 #Valor absoluto do qual a medida de x deve estar para queda
        self.xSensorFront     = 6 #Valor abaixo do qual a medida de x deve estar para queda de frente                           
        self.xSensorBack      = -6  #Valor acima do qual a medida de x deve estar para queda de costas                               
        self.ySensorLeft      = 6 #Valor abaixo do qual a medida de y deve estar para queda sobre o lado esquerdo         
        self.ySensorRight     = -6  #Valor acima do qual a medida de y deve estar para queda sobre o lado direito                         

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
        #Tópico novo que recebe 
        self.imuGyroTopic = '/behaviour/imu_gyro'

    def visionwiseParameters(self):
        #Tópico do ROS
        self.vision2BhvTopic = '/vision/vision_inference'
#######################################################Camera nova###############################3
        #Parâmetros da câmera
        #Conferir com o Leo a camera nova
        self.cameraWidth =  416
        self.cameraHeight = 416

        #Parâmetros de interpretação da câmera
        self.xCenterLeftLimit = 4*self.cameraWidth/10
        self.xCenterRightLimit = 6*self.cameraWidth/10
        self.yCenterBottomLimit = 6*self.cameraHeight/10
        self.yCenterTopLimit = 4*self.cameraHeight/10

        self.closeSize = 80*80

