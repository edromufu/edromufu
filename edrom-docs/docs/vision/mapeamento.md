---
id: mapeamento
title: Árvore de Arquivos
description: Nesta seção conseguimos vemos a estrutura dos pacotes da visão
slug: /mapeamento-visao
sidebar_position: 4
---

A pasta da [Visão](https://github.com/edromufu/edromufu/tree/master/src/vision) fica dentro da src do repositório, e dentro dela fica todo o escopo do projeto que compete à visão. Os arquivos da área são separados em quatro pastas:

1. [Vision_msgs](https://github.com/edromufu/edromufu/tree/master/src/vision/vision_msgs)
2. [Robocup_cnn_files](src/vision/robocup_cnn_files)
3. [Robocup_videos](https://github.com/edromufu/edromufu/tree/master/src/vision/robocup_videos)
4. [Object_finder](https://github.com/edromufu/edromufu/tree/master/src/vision/object_finder)

## Vision_msgs

Como o projeto utiliza [ROS2](https://www.ros.org/) para comunicação, faz-se necessário definir as mensagens que serão enviadas e recebidas pelos códigos. Nessa pasta, ficam as mensagens utilizadas na Visão.

## Robocup_cnn_files

O resultado do treinamento da rede neural são dois arquivos: **yolov8-tiny-obj.cfg** e **yolov8-tiny-obj.weights**. Esses arquivos possuem os parâmetros que serão utilizados na inferência das imagens, e dentro dessa pasta eles são salvos, juntamente com backups de treinamentos antigos que funcionaram bem.

## Robocup_videos

Para prepara o dataset para o treinamento, é necessário realizar uma série de processos, melhores detalhados [aqui](./training/introducao.md). A organização do dataset foi realizada utilizando o Google Drive, com a seguinte estrutura:

- **Pasta Principal "Teste"**: Contém todo o conjunto de dados.
  - **Subpasta "Ball"**: Armazena as divisões de treinamento e validação.
    - **Subpasta "train"**: Contém os dados de treinamento.
      - **Subpasta "images"**: Imagens de treinamento prefixadas com "train".
      - **Subpasta "labels"**: Arquivos de rótulos de treinamento prefixados com "train" e o arquivo "classes.txt".
    - **Subpasta "valid"**: Contém os dados de validação.
      - **Subpasta "images"**: Imagens de validação prefixadas com "val".
      - **Subpasta "labels"**: Arquivos de rótulos de validação prefixados com "val" e o arquivo "classes.txt".

## Object_finder

Por fim, a object_finder onde efetivamente acontece a Visão do projeto. Desde capturar as imagens, até enviar os resultados da inferência ao restante do projeto.

Dentro da src desse diretório, temos dois arquivos principais. Estes são [connecting_and_showing_current_frame_robocup.py](https://github.com/edromufu/edromufu/blob/master/src/vision/object_finder/src/connecting_and_showing_current_frame_robocup.py) e [running_inference_robocup.py](https://github.com/edromufu/edromufu/blob/master/src/vision/object_finder/src/running_inference_robocup.py).

O primeiro conecta à câmera utilizada, obtém as imagens, realiza a chamada da inferência, que é realizada no **running_inference_robocup.py**, sobre as imagens e mostra (opcionalmente) o resultado em tempo real da interpretação da rede neural, além de enviar o resultado por **ROS2** ao restante do projeto.

O segundo é onde acontece a interpretação das imagens, seguindo os arquivos gerados no treinamento da rede neural. Nele também está a função que mostra (opcionalmente) o resultado da inferência desenhando um retângulo no frame antes de retorná-lo ao código anterior.
