---
id: criando_txts_dataset
title: Criando arquivos auxiliares
slug: /criando_txts_dataset
sidebar_position: 6
---



Por fim, para realizar o treinamento, é necessário informar quais os frames serão utilizados para treinamento e validação, bem como seu endereço no drive. Para isso, é utilizado o seguinte script:

```py
import os

pastaFrames = "frames" # Pasta onde frames estão salvos

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
```

O único parâmetro desse código é a pasta em que os frames estão.

```py
pastaFrames = "frames" # Pasta onde frames estão salvos
```

Em seguida, acessa a pasta dos frames e lê o nome de todos os arquivos para iterar sobre eles. Então, salva os que possuem a extensão .jpg em uma lista (para evitar erros com "lixo" na pasta).

```py
os.chdir(pastaFrames)
lista_de_arquivo = os.listdir(os.getcwd())
lista_de_imagens = []
os.chdir('..')

for arquivo in lista_de_arquivo:
    if os.path.splitext(arquivo)[1] == ".jpg":
        lista_de_imagens.append(arquivo)
```

Após isso, deleta os arquivos "train.txt" e "valid.txt", caso existam, e em seguida cria os novos.

```py
if os.path.exists('train.txt'):
    os.remove('train.txt')
    
if os.path.exists('valid.txt'):
    os.remove('valid.txt')

arquivo_train = open('train.txt', 'a')
arquivo_val = open('valid.txt', 'a')
```

Por fim, itera sobre todos os frames, registrando os marcados como train na "train.txt" e os marcados com val na "valid.txt". Os frames são registrados precedidos de 'data/obj/', pois é o endereço da pasta que estarão quando enviados para o drive para realizar o treinamento (seguindo o tutorial do Darknet).

```py
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
```

O resultado do script são os dois arquivos, "train.txt" e "valid.txt", com os nomes e endereços dos frames de treinamento de validação.

Com isso, a etapa de preparação do dataset para treinamento foi concluída. Os próximos passos agora, seguindo o tutorial do [Darknet](https://github.com/AlexeyAB/darknet), é upar os arquivos para seus respectivos destinos no drive, e seguir o passo a passo do treinamento no Colab.