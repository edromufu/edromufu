---
id: comandos_visao
title: Comandos utilizados pela visão
description: Aqui serão explicados quais são os comandos da visão e suas funções
slug: /cmd_visao
sidebar_position: 2
---

A visão utiliza basicamente dois comandos que habilitam o seu funcionamento, sendo eles:


```py
roslaunch object_finder vision.launch
```

Esse comando inicia todos os códigos da visão, além de poder receber alguns argumentos, sendo eles:

**camera** : Recebe qual a câmera será utilizada (default 0).

**img_output** : Recebe um booleano (true ou false) se terá um retorno visual (default = false).

**ajuste** : Recebe um booleano para entrar no modo de ajuste de brilho, onde será utilizado "=" para aumentar o brilho, "-" para diminuir e "w" para continuar detecção (default = false).

**brilho** : Recebe um valor entre -64 e 64 para o fator de brilho da câmera (default = 4).

```py
rosrun object_finder connecting_and_showing.py
```

É o comando que roda o código do connecting and showing, que executa as funções da visão no geral

:::tip Como passar o argumento

Utilizar o modelo "nome_argumento:=valor_desejado"

:::
