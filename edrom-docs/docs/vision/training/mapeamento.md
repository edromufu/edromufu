---
id: mapeamento
title: Árvore de Arquivos
description: Nesta seção conseguimos vemos a estrutura dos pacotes da visão
slug: /mapeamento-visao
sidebar_position: 4
---

A pasta da [Visão](https://github.com/edromufu/edromufu/tree/master/src/vision) fica dentro da src do repositório, e dentro dela fica todo o escopo do projeto que compete à visão. Os arquivos da área são separados em quatro pastas:

1. [Vision_msgs](https://github.com/edromufu/edromufu/tree/master/src/vision/vision_msgs)
2. [Robocup_cnn_files](https://github.com/edromufu/edromufu/tree/vision/YOLOv8/src/vision/robocup_cnn_files)
3. [Robocup_videos](https://github.com/edromufu/edromufu/tree/master/src/vision/robocup_videos)
4. [Object_finder](https://github.com/edromufu/edromufu/tree/vision/YOLOv8/src/vision/object_finder)

## Vision_msgs

Como o projeto utiliza [ROS2](https://www.ros.org/) para comunicação, faz-se necessário definir as mensagens que serão enviadas e recebidas pelos códigos. Nessa pasta, ficam as mensagens utilizadas na Visão.

## Robocup_cnn_files

O resultado do treinamento da rede neural é um arquivo: **yolov8n-vision.pt**. Esse arquivo possui os parâmetros que serão utilizados na inferência das imagens, e dentro dessa pasta ele é salvo, juntamente com backups de treinamentos antigos que funcionaram bem.

## Robocup_videos

Para prepara o dataset para o treinamento, é necessário realizar uma série de processos, melhores detalhados [aqui](./training/introducao.md). Para facilitar a criação desse dataset, foram desenvolvidos scripts auxiliares. Esses scripts são armazenados nessa pasta. Os scripts são os seguintes:

1. **recording_from_camera.py**: Utilizado para gravar vídeos com a câmera (ou webcam)
2. **spliting_video_in_frames.py**: Utilizado para dividir os vídeos gravados em frames
3. **organizing_dataset.py**: Utilizado para dividir os frames de acordo com seu propósito (treinamento, validação e avaliação)


Para evitar que o repositório fique carregado com arquivos desnecessários, recomenda-se que os scripts sejam copiados para outro local, e executados lá, de forma que os arquivos gerados (vídeos, frames ou txts) fiquem neste outro local, para depois serem enviados ao drive para treinamento.

## Object_finder

Por fim, a object_finder onde efetivamente acontece a Visão do projeto. Desde capturar as imagens, até enviar os resultados da inferência ao restante do projeto.

Dentro da src desse diretório, temos dois arquivos principais. Estes são [connecting_and_showing.py](https://github.com/edromufu/edromufu/blob/master/src/vision/object_finder/object_finder/connecting_and_showing.py) e [running_inference.py](https://github.com/edromufu/edromufu/blob/master/src/vision/object_finder/object_finder/running_inference.py).

O primeiro conecta à câmera utilizada, obtém as imagens, realiza a chamada da inferência, que é realizada no **running_inference.py**, sobre as imagens e mostra (opcionalmente) o resultado em tempo real da interpretação da rede neural, além de enviar o resultado por **ROS** ao restante do projeto.

O segundo é onde acontece a interpretação das imagens, seguindo os arquivos gerados no treinamento da rede neural. Nele também está a função que mostra (opcionalmente) o resultado da inferência desenhando um retângulo no frame antes de retorná-lo ao código anterior.
