import os

os.chdir("film7")
lista_de_frames = os.listdir(os.getcwd())

cont = 591
for frame in lista_de_frames:
    os.rename(frame, str(cont) + '.jpg')
    cont += 1