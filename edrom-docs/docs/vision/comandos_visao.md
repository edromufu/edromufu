---
id: comandos_visao
title: Comandos utilizados pela visão
description: Aqui serão explicados quais são os comandos da visão e suas funções
slug: /cmd_visao
sidebar_position: 3
---

A visão utiliza basicamente dois comandos que habilitam o seu funcionamento, sendo eles:


```py
ros2 launch object_finder vision.launch.py
```
O _ros2 launch_ é um comando que __começa__ ou __para__ um _node (Processo que realizada computação) ROS_ que leva um ou mais arquivos tipo _.launch_ como argumentos. Para usar o launch é necessário o nome do arquivo tipo _launch_. Você pode especificar o caminho ou o arquivo _launch_ ou você pode especificar o nome do pacote e o arquivo _launch_ dentro desse pacote (como fazemos).

```py
ros2 launch <nome_do_pacote> <arquivo_.launch.py>
```

No nosso caso, executamos o vision.launch.py dentro do pacote _objectfinder_.

Esse comando inicia todos os códigos da visão, além de poder receber alguns argumentos, sendo eles:

**camera** : Recebe qual a câmera será utilizada (default 0).

**img_output** : Recebe um booleano (true ou false) se terá um retorno visual (default = false).

**ajuste** : Recebe um booleano para entrar no modo de ajuste de brilho, onde será utilizado "=" para aumentar o brilho, "-" para diminuir e "w" para continuar detecção (default = false).

**brilho** : Recebe um valor entre -64 e 64 para o fator de brilho da câmera (default = 4).

```py
ros2 run object_finder finder
```

O _ros2 run_ permite você executar um arquivo executável dentro de um pacote arbitrário de qualquer lugar sem ter que digitar seu caminho completo ou _cd/roscd_ primeiro.

```py
ros2 run <pacote> <executavel>
```
Neste caso, executamos o arquivo __Python__ *connect_and_showing.py* dentro do diretorio *object_finder*. O nome _finder_ é o nome do executável entendido pelo ROS 2, que se refere ao script _connect_and_showing.py_.

Esse comando roda o código do finder, que executa as funções principais da visão.

:::tip Como passar o argumento

Utilizar o modelo "nome_argumento:=valor_desejado"

:::
```py
ros2 launch vision.launch.py camera:=2 img_output:=True
```
O exemplo acima executa o comando alterando a camêra a ser utilizada e exibindo a imagem na tela.
