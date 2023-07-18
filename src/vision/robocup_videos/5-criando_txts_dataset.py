import os

####################################################################################
# Código para gerar train.txt e valid.txt a partir do dataset

# Parâmetros
pastaFrames = "frames" # Pasta onde frames estão salvos

####################################################################################

os.chdir(pastaFrames)
lista_de_arquivo = os.listdir(os.getcwd())
lista_de_imagens = []
os.chdir('..')

for arquivo in lista_de_arquivo:
    if os.path.splitext(arquivo)[1] == ".jpg":
        lista_de_imagens.append(arquivo)

if os.path.exists('train.txt'):
    os.remove('train.txt')
    
if os.path.exists('valid.txt'):
    os.remove('valid.txt')

arquivo_train = open('train.txt', 'a')
arquivo_val = open('valid.txt', 'a')

line = 'data/obj/'

for imagem in lista_de_imagens:
    if imagem.__contains__('train'):
        if lista_de_arquivo.__contains__(os.path.splitext(imagem)[0]+'.txt'):
            arquivo_train.write(line + imagem + '\n')
        else: os.remove(pastaFrames + '/' + imagem)

    elif imagem.__contains__('eval'): pass

    elif imagem.__contains__('val'):
        if lista_de_arquivo.__contains__(os.path.splitext(imagem)[0]+'.txt'):
            arquivo_val.write(line + imagem + '\n')
        else: os.remove(pastaFrames + '/' + imagem)


arquivo_train.close()
arquivo_val.close()


