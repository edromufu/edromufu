#!/usr/bin/env python3
# coding=utf-8
import os
import cv2

####################################################################################
# Código para gravar vídeo a partir da câmera

# Parâmetros
videoInput = "/dev/video2" # É de onde vai pegar as imagens, "/dev/video2" é pegando por um dos usbs (o numero muda) e 0 é a webcam
width = 640 # Largura da imagem (conferir no vídeo)
height = 480 # Altura da imagem (Conferir no vídeo)
pasta = "videos" # Pasta para salvar os videos

####################################################################################


# Seta o nome do video para não sobrescrever
os.chdir(pasta)
lista_de_arquivo = os.listdir(os.getcwd())
for i in range(len(lista_de_arquivo)):
    if not lista_de_arquivo.__contains__("film"+str(i+1)+".avi"):
        videoName = "film"+str(i+1)+".avi"
        break
os.chdir("..")

# Seta parametros do OpenCV
fourcc = cv2.VideoWriter_fourcc(*'XVID')
escritor = cv2.VideoWriter(os.path.join(os.getcwd(), pasta) + videoName, fourcc, 5.0, (width, height))

cap = cv2.VideoCapture(videoInput)

while True:
    _ , frame = cap.read()
    cv2.imshow("Camera", frame)
    escritor.write(frame)
    if cv2.waitKey(1) == ord("q"):
        cap.release()
        cv2.destroyAllWindows()