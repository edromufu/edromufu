#!/usr/bin/env python3
# coding=utf-8
import os
import subprocess
import rospy

from sensor_msgs.msg import Image as TipoMensagemImagem
from cv_bridge import CvBridge
import cv2

class Listener():
    def __init__(self):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.escritor = cv2.VideoWriter(os.path.join(os.path.expanduser('~'), 'edrom/src/vision/robocup_videos/') + 'film.avi', fourcc, 5.0, (640, 480))

        # rospy.init_node('recebeImagemWebots', anonymous = True)
        # rospy.Subscriber("/webots_natasha/vision_controller", TipoMensagemImagem, self.callback)  
        
        # rospy.spin()


        self.cap = cv2.VideoCapture("/dev/video2")

        while True:
            self.record()
            if cv2.waitKey(1) == ord("q"):
                self.excluir()


    # Função de callback
    def record(self):
        #bridge = CvBridge()
        
        _ , self.frame = self.cap.read()
        cv2.imshow("Camera", self.frame)
        self.escritor.write(self.frame)

        
    def excluir(self):
        self.escritor.release()
        cv2.destroyAllWindows()
        #rospy.signal_shutdown("Tudo desligado!")

"""# Obtendo todos os serviços em funcionamento no momento
servicos = subprocess.check_output("rosservice list", shell = True)
servicos = servicos.decode('ascii')
servicos = servicos.split("\n")
print(servicos)
print()

# Obtendo o serviço da câmera e dando enable
ind = 0
index_servico_camera = 0
for servico in servicos:
    if "camera/enable" in servico:
        index_servico_camera = ind
    ind += 1
print("Fornecendo True para o serviço camera/enable:")
print(servicos[index_servico_camera])
os.system('rosservice call {} "value: 1"'.format(servicos[index_servico_camera]))

# Obtendo todos os tópicos em funcionamento no momento
topicos = subprocess.check_output("rostopic list", shell = True)
topicos = topicos.decode('ascii')
topicos = topicos.split("\n")
print()
print(topicos)
print()

# Obtendo o tópico da câmera para se subscrever
ind = 0
index_topico_camera = 0
for topico in topicos:
    if "camera/image" in topico:
        index_topico_camera = ind
    ind += 1
print("Subscrevendo no tópico da câmera:")
print(topicos[index_topico_camera])"""

if __name__ == '__main__':
    escutador = Listener()