import cv2
import os

####################################################################################
# Código para gerar frames a partir dos videos

# Parâmetros
pastaVideos = "videos" # Pasta onde videos estão salvos
pastaFrames = "frames" # Pasta onde frames serão salvos
pularFrames = 3 # A cada quantos frames um jpg será salvo

####################################################################################


# Pega todos os arquivos da pasta
os.chdir(pastaVideos)
lista_de_arquivo = os.listdir(os.getcwd())
lista_de_videos = []
os.chdir("..")

# Monta lista de videos
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