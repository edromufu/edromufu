#!/usr/bin/env python3

import cv2 #lê a biblioteca do OpenCV
import numpy as np #lê a biblioteca matricial do Numpy
import rospy
from vision_msgs.msg import Ball

def nothing(x): #faz uma função burra de retorno
    pass

captura = cv2.VideoCapture(0)

cv2.namedWindow("Filtrar cor") #cria uma janela de escaneamento
cv2.createTrackbar("Menor Hue", "Filtrar cor", 0, 255, nothing) #faz uma barra de nome Menor Hue, na janela Escaneamento, com valor inicial (ao rodar o programa de zero), 255 divisões e com função de retorno nothing
cv2.createTrackbar("Menor Saturation", "Filtrar cor", 0, 255, nothing)
cv2.createTrackbar("Menor Value", "Filtrar cor", 0, 255, nothing)
cv2.createTrackbar("Maior Hue", "Filtrar cor", 255, 255, nothing)
cv2.createTrackbar("Maior Saturation", "Filtrar cor", 255, 255, nothing)
cv2.createTrackbar("Maior Value", "Filtrar cor", 255, 255, nothing)

print("Lights, camera, action!") #apenas de enfeite

coordenadas_canto_esquerdo = []
coordenadas_canto_direito = []

x_centro_da_imagem = 640/2
y_centro_da_imagem = 480/2

# Iniciando o nó e fazendo o publicador do ROS
rospy.init_node('no_da_visao_do_PID', anonymous=True)
pub = rospy.Publisher('topico_da_visao_do_PID', Ball)

while not rospy.is_shutdown():    

    retorno, quadro = captura.read() #recebe a foto que vai passar pelo processo

    hsv = cv2.cvtColor(quadro, cv2.COLOR_BGR2HSV) #faz uma matriz de nome hsv, que será a transformação da foto pra hsv

    menor_hue = cv2.getTrackbarPos("Menor Hue", "Filtrar cor") #pega a posição em que está o cursor na barra Menor Hue, da janela escaneamento
    menor_saturation = cv2.getTrackbarPos("Menor Saturation", "Filtrar cor")
    menor_value = cv2.getTrackbarPos("Menor Value", "Filtrar cor")
    maior_hue = cv2.getTrackbarPos("Maior Hue", "Filtrar cor")
    maior_saturation = cv2.getTrackbarPos("Maior Saturation", "Filtrar cor")
    maior_value = cv2.getTrackbarPos("Maior Value", "Filtrar cor")

    menor_cor = np.array([menor_hue, menor_saturation, menor_value]) #faz um vetor com os valores mínimos definidos pelo usuário ao deslocar o cursor
    maior_cor = np.array([maior_hue, maior_saturation, maior_value])

    mask = cv2.inRange(hsv, menor_cor, maior_cor) #cria uma máscara da matriz hsv abrangendo o intervalo compreendido entre o vetor menor_cor e o vetor maior_cor

    contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    resultado = cv2.bitwise_and(quadro, quadro, mask=mask) #o resultado é a imagem original com a máscara aplicada sobre ela

    if len(contours) > 0:
        blue_area = max(contours, key=cv2.contourArea)
        (xg,yg,wg,hg) = cv2.boundingRect(blue_area)
        cv2.rectangle(resultado, (xg,yg), (xg+wg, yg+hg), (0,255,0), 2)

    # Encontrando o centróide
    xc = int(((xg)+(xg+wg))/(2))
    yc = int(((yg)+(yg+hg))/(2))
    cv2.circle(resultado, (xc, yc), 4, (0, 255, 0), -1)

    # Encontrando as coordenadas em relação ao centro
    x_em_relacao_ao_centro = int(xc - x_centro_da_imagem)
    y_em_relacao_ao_centro = int(yc - y_centro_da_imagem)
    print(x_em_relacao_ao_centro, y_em_relacao_ao_centro)

    # Publicando as coordenadas via ROS
    msg = Ball()
    msg.x = x_em_relacao_ao_centro
    msg.y = y_em_relacao_ao_centro
    pub.publish(msg)

    cv2.imshow('Original', quadro)
    cv2.imshow('Mascara', mask)
    cv2.imshow('Resultado', resultado)

    key = cv2.waitKey(1) #espera uma tecla ser pressionada para fechar
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cv2.destroyAllWindows()
