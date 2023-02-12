---
id: spliting_video_in_frames
title: Dividir os vídeos em frames
sidebar_position: 3
---



Agora, os vídeos serão divididos em frames. Para isso, executamos o seguinte script:

```py
import cv2
import os

pastaVideos = "videos" # Pasta onde videos estão salvos
pastaFrames = "frames" # Pasta onde frames serão salvos
pularFrames = 3 # A cada quantos frames um jpg será salvo

os.chdir(pastaVideos)
lista_de_arquivo = os.listdir(os.getcwd())
lista_de_videos = []
os.chdir("..")

for arquivo in lista_de_arquivo:
    if os.path.splitext(arquivo)[1] == ".avi":
        lista_de_videos.append(arquivo)

numero_frame=1
current_frame = 1

for video in lista_de_videos:

    print ('From...' + video)
    nome_do_video = pastaVideos + "/" + video
    cap = cv2.VideoCapture(nome_do_video)

    while(True):
        ret, frame = cap.read()        
        if ret:
            if current_frame % pularFrames == 0:
                name = pastaFrames + '/frame' + str(numero_frame) + '.jpg'
                numero_frame +=1
                print ('Creating...' + name)
                cv2.imwrite(name, frame)
            current_frame += 1
        else: break
    cap.release()
```

A primeira parte é onde são definidos os parâmetros. Modifique eles de acordo com o nome da pasta em que os videos estão, o nome da pasta em que os frames devem ser salvos, e a cada quantos frames do vídeo o script salvará um frame (utilizado para evitar frames identicos, para salvar todos os frames utilizar pularFrames = 1).

```py
pastaVideos = "videos" # Pasta onde videos estão salvos
pastaFrames = "frames" # Pasta onde frames serão salvos
pularFrames = 3 # A cada quantos frames um jpg será salvo
```

Em seguida, acessa a pasta dos videos e lê o nome de todos os arquivos para iterar sobre eles. Então, salva os que possuem a extensão .avi em uma lista (para evitar erros com "lixo" na pasta).

```py
os.chdir(pastaVideos)
lista_de_arquivo = os.listdir(os.getcwd())
lista_de_videos = []
os.chdir("..")

for arquivo in lista_de_arquivo:
    if os.path.splitext(arquivo)[1] == ".avi":
        lista_de_videos.append(arquivo)
```

Por fim, itera sobre todos os vídeos, salvando os frames na pasta designada no formato "frame0.jpg", "frame1.jpg", ..., "frameN.jpg".

```py
numero_frame=1
current_frame = 1

for video in lista_de_videos:

    print ('From...' + video)
    nome_do_video = pastaVideos + "/" + video
    cap = cv2.VideoCapture(nome_do_video)

    while(True):
        ret, frame = cap.read()        
        if ret:
            if current_frame % pularFrames == 0:
                name = pastaFrames + '/frame' + str(numero_frame) + '.jpg'
                numero_frame +=1
                print ('Creating...' + name)
                cv2.imwrite(name, frame)
            current_frame += 1
        else: break
    cap.release()
```

O resultado será os frames dos vídeos em formato .jpg pasta designada (no código exemplo, o script está no mesmo diretório que a pasta "videos" e a "frames").