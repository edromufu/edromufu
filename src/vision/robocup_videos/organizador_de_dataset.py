import os

os.chdir("frames")
lista_de_arquivo = os.listdir(os.getcwd())
lista_de_imagens = []

for arquivo in lista_de_arquivo:
    if os.path.splitext(arquivo)[1] == ".jpg":
        lista_de_imagens.append(arquivo)

quant_treino = int(len(lista_de_imagens)*0.7)
quant_validacao = int(len(lista_de_imagens)*0.2)
quant_avaliacao = len(lista_de_imagens)-(quant_treino + quant_validacao)

#print(lista_de_imagens)
#print(quant_treino, "\n", quant_validacao, "\n", quant_avaliacao, "\n")
#print(len(lista_de_imagens))

lista_de_treino = lista_de_imagens[:quant_treino]
lista_de_validacao = lista_de_imagens[quant_treino:quant_treino + quant_validacao]
lista_de_avaliacao = lista_de_imagens[quant_treino+ quant_validacao:]

count_treino = 1
count_validacao = 1
count_avaliacao = 1

for arquivo in lista_de_arquivo:
    if arquivo in lista_de_treino:
        nome = os.path.splitext(arquivo)[0]
        os.rename(nome + '.jpg', f'train_{count_treino}.jpg')
        try:
            os.rename(nome + '.txt', f'train_{count_treino}.txt')
        except Exception:
            print(f'frame train_{count_treino} não possui txt \n')
        count_treino += 1

    elif arquivo in lista_de_validacao:
        nome = os.path.splitext(arquivo)[0]
        os.rename(nome + '.jpg', f'val_{count_validacao}.jpg')
        try:
            os.rename(nome + '.txt', f'val_{count_validacao}.txt')
        except Exception:
            print(f'frame val_{count_validacao} não possui txt \n')
        count_validacao += 1

    elif arquivo in lista_de_avaliacao:
        nome = os.path.splitext(arquivo)[0]
        os.rename(nome + '.jpg', f'eval_{count_avaliacao}.jpg')
        try:
            os.rename(nome + '.txt', f'eval_{count_avaliacao}.txt')
        except Exception:
            print(f'frame eval_{count_avaliacao} não possui txt \n')
        count_avaliacao += 1