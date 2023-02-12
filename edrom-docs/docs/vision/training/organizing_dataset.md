---
id: organizing_dataset
title: Separar os frames
sidebar_position: 4
slug: /organizing_dataset
---



Para o treinamento com Tiny YOLOv4, é necessário separar as imagens em 3 categorias: treinamento (train), validação (val) e avaliação (eval). Os frames de treinamento são os utilizados para o treinamento em si da rede neural. Os de validação também são utilizados no treinamento, porém servem como um "teste com gabarito" para o treinamento. Enquanto os de avaliação são os separados para testes manuais feitos com a rede após o treinamento e por isso não precisam ser marcados ou alimentados no treinamento. No código de exemplo, foi utilizada a proporção de 7:2:1 para train:val:eval. O seguinte script é utilizado para renomear os arquivos e realizar a separação:

```py
import os

pastaFrames = "frames" # Pasta onde frames estão salvos
proporcaoTreino = 0.7
proporcaoValidacao = 0.2

os.chdir(pastaFrames)
lista_de_arquivo = os.listdir(os.getcwd())
lista_de_imagens = []

for arquivo in lista_de_arquivo:
    if os.path.splitext(arquivo)[1] == ".jpg":
        lista_de_imagens.append(arquivo)

quant_treino = int(len(lista_de_imagens)*proporcaoTreino)
quant_validacao = int(len(lista_de_imagens)*proporcaoValidacao)
quant_avaliacao = len(lista_de_imagens)-(quant_treino + quant_validacao)

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
            pass
        count_treino += 1

    elif arquivo in lista_de_validacao:
        nome = os.path.splitext(arquivo)[0]
        os.rename(nome + '.jpg', f'val_{count_validacao}.jpg')
        try:
            os.rename(nome + '.txt', f'val_{count_validacao}.txt')
        except Exception:
            pass
        count_validacao += 1

    elif arquivo in lista_de_avaliacao:
        nome = os.path.splitext(arquivo)[0]
        os.rename(nome + '.jpg', f'eval_{count_avaliacao}.jpg')
        try:
            os.rename(nome + '.txt', f'eval_{count_avaliacao}.txt')
        except Exception:
            pass
        count_avaliacao += 1

```

Os parâmetros para esse script são a pasta em que os frames estão, a proporção de frames para treinamento e para validação (a soma total das proporções de treinamento, validação e avaliação é = 1).

```py
pastaFrames = "frames" # Pasta onde frames estão salvos
proporcaoTreino = 0.7
proporcaoValidacao = 0.2
```

Em seguida, acessa a pasta dos frames e lê o nome de todos os arquivos para iterar sobre eles. Então, salva os que possuem a extensão .jpg em uma lista (para evitar erros com "lixo" na pasta).

```py
os.chdir(pastaFrames)
lista_de_arquivo = os.listdir(os.getcwd())
lista_de_imagens = []

for arquivo in lista_de_arquivo:
    if os.path.splitext(arquivo)[1] == ".jpg":
        lista_de_imagens.append(arquivo)
```

Após isso, calcula a quantidade de frames em cada categoria, e salva eles em listas separadas.

```py
quant_treino = int(len(lista_de_imagens)*proporcaoTreino)
quant_validacao = int(len(lista_de_imagens)*proporcaoValidacao)
quant_avaliacao = len(lista_de_imagens)-(quant_treino + quant_validacao)

lista_de_treino = lista_de_imagens[:quant_treino]
lista_de_validacao = lista_de_imagens[quant_treino:quant_treino + quant_validacao]
lista_de_avaliacao = lista_de_imagens[quant_treino+ quant_validacao:]
```

Com os frames já separados, os arquivos são renomeados para indicar para o que serão utilizados. O nome dos frames segue o padrão "train_0.jpg", "val_0.jpg" e "eval_0.jpg".

```py
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
            pass
        count_treino += 1

    elif arquivo in lista_de_validacao:
        nome = os.path.splitext(arquivo)[0]
        os.rename(nome + '.jpg', f'val_{count_validacao}.jpg')
        try:
            os.rename(nome + '.txt', f'val_{count_validacao}.txt')
        except Exception:
            pass
        count_validacao += 1

    elif arquivo in lista_de_avaliacao:
        nome = os.path.splitext(arquivo)[0]
        os.rename(nome + '.jpg', f'eval_{count_avaliacao}.jpg')
        try:
            os.rename(nome + '.txt', f'eval_{count_avaliacao}.txt')
        except Exception:
            pass
        count_avaliacao += 1
```

O resultado será os frames separados e renomeados de acordo com sua função (treinamento, validação ou avaliação) seguindo a proporção definida para cada categoria.