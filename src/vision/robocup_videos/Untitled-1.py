#!/usr/bin/env python3
# coding=utf-8
import os
import cv2

####################################################################################
# Código para gravar vídeo a partir da câmera

# Parâmetros
videoInput = "/dev/video2"  # Verifique se este é o índice correto do dispositivo de vídeo
width = 480  # Largura da imagem
height = 480  # Altura da imagem
pasta = "videos"  # Pasta para salvar os vídeos
videoName = ""

####################################################################################

# Cria a pasta, se não existir
if not os.path.exists(pasta):
    os.makedirs(pasta)

# Seta o nome do vídeo para não sobrescrever
os.chdir(pasta)
lista_de_arquivo = os.listdir(os.getcwd())
for i in range(len(lista_de_arquivo) + 1):
    if f"film{i+1}.avi" not in lista_de_arquivo:
        videoName = f"film{i+1}.avi"
        break
os.chdir("..")

# Seta parâmetros do OpenCV
fourcc = cv2.VideoWriter_fourcc(*'XVID')
escritor = cv2.VideoWriter(os.path.join(os.getcwd(), pasta, videoName), fourcc, 5.0, (width, height))

# Inicializa a captura de vídeo
cap = cv2.VideoCapture(videoInput)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Verifique se a câmera foi aberta corretamente
if not cap.isOpened():
    print("Erro: não foi possível acessar a câmera.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro: não foi possível capturar o quadro.")
            break
        cv2.imshow("Camera", frame)
        escritor.write(frame)
        if cv2.waitKey(1) == ord("q"):
            break

    # Libere a câmera e feche as janelas
    cap.release()
    escritor.release()
    cv2.destroyAllWindows()
