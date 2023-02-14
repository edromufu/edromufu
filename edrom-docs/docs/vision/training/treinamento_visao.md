---
id: treinamento_visao
title: Arquivos a serem alterados para treinar
description: Aqui será descrito o que deve ser alterado no arquivo 
slug: /train_visao
sidebar_position: 7
---

O arquivo a ser alterado para realizar o treinamento personalizado é o [yolov4-tiny-obj.cfg](https://github.com/edromufu/edromufu/blob/master/src/vision/robocup_cnn_files/yolov4-tiny-obj.cfg)

O primeiro passo a ser realizado é garantir que as seguintes variáveis possuam os valores:

```py
batch=64
subdivision=16
```
Então, é necessário alterar a linha **max_division** para o número de classes desejadas vezes 2000.

:::tip Número de classes

O número de classes é a quantidade de objetos que você quer treinar para a rede reconhecer, se for apenas para detecção da bola, o número de classes é igual a 1

:::

Ou seja, para uma classe você teria:

```py
max_batches=2000
```
O passo seguinte é alterar a linha **steps** para 80% e 90% do max_steps respectivamente. Ou seja, para um max_batches=2000 o correto é ter

```py
steps=1600,1800
```

Setar os valores de **width** e **height** para 416 ambos (Ou algum outro valor múltiplo de 32 dependendo da aplicação)

```py
width=416
height=416
```
Agora é alterar as linhas **classes** para o número desejado

```py
classes=1
```

:::danger CUIDADO

É necessário alterar a linha classes em mais de um lugar, no arquivo em questão são nas linhas 220 e 269

:::

E por fim alterar **filters** para um valor igual a fórmula (classes+5)x3, ou seja, no caso de uma classe teremmos:

```py
filters=18
```

:::danger MUITO CUIDADO!!!

A variável filters deve ser atualizada algumas vezes ao decorrer do código, que são nos [convolutional] antes de cada cammada [yolo], no código em questão estão nas linhas 212 e 266

:::


Isso é tudo que deve ser alterado no arquivo de configuração