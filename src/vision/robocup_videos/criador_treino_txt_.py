import os

os.chdir("frames")
lista_de_arquivo = os.listdir(os.getcwd())
lista_de_imagens = []

os.chdir('..')
arquivo_train = open('train.txt', 'a')
arquivo_val = open('valid.txt', 'a')

line = 'data/obj/'

for arquivo in lista_de_arquivo:
    if arquivo.__contains__('train') and arquivo.__contains__('.jpg'):
        arquivo_train.write(line + arquivo + '\n')
    elif arquivo.__contains__('eval') and arquivo.__contains__('.jpg'):
        pass
    elif arquivo.__contains__('.jpg'):
        arquivo_val.write(line + arquivo + '\n')
    else:
        pass

arquivo_train.close()
arquivo_val.close()


