---
id: recording_from_camera
title: Gravando as imagens
sidebar_position: 2
slug: /recording_from_camera
---



Para obter as imagens para o treinamento, primeiro gravamos vídeos utilizando a câmera que futuramente será usada no projeto. Para isso, conectamos a câmera em um USB e executamos o seguinte script:

```py
import os
import cv2

videoInput = "/dev/video2" # É de onde vai pegar as imagens, "/dev/video2" é pegando por um dos usbs (o numero muda) e 0 é a webcam
width = 640 # Largura da imagem (conferir no vídeo)
height = 480 # Altura da imagem (Conferir no vídeo)
pasta = "videos" # Pasta para salvar os videos

os.chdir(pasta)
lista_de_arquivo = os.listdir(os.getcwd())
for i in range(len(lista_de_arquivo)):
    if not lista_de_arquivo.__contains__("film"+str(i+1)+".avi"):
        videoName = "film"+str(i+1)+".avi"
        break
os.chdir("..")

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
```

A primeira parte é onde são definidos os parâmetros. Modifique eles de acordo com a USB que estiver conectada a câmera (ou 0 para a webcam), o tamanho dos frames desejados e a pasta destino dos vídeos.

```py
videoInput = "/dev/video2" # É de onde vai pegar as imagens, "/dev/video2" é pegando por um dos usbs (o numero muda) e 0 é a webcam
width = 640 # Largura da imagem (conferir no vídeo)
height = 480 # Altura da imagem (conferir no vídeo)
pasta = "videos" # Pasta para salvar os videos
```

Em seguida, é definido o nome do arquivo do vídeo para não sobrescrever vídeos antigos (permitindo a gravação de multiplos vídeos em sequência) seguindo o padrão "film0.avi", "film1.avi", ..., "filmN.avi".

```py
os.chdir(pasta)
lista_de_arquivo = os.listdir(os.getcwd())
for i in range(len(lista_de_arquivo)):
    if not lista_de_arquivo.__contains__("film"+str(i+1)+".avi"):
        videoName = "film"+str(i+1)+".avi"
        break
os.chdir("..")
```

Por fim, configura o escritor do OpenCV e realiza a captura das imagens, frame por frame, salvando o vídeo na pasta configurada, com o nome determinado.

```py
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
```

Para iniciar a gravação, basta executar o script. Apertar a tecla "q" irá finaliza-la. O resultado será um vídeo em formato avi na pasta designada (no código exemplo, o script está no mesmo diretório que a pasta "videos").