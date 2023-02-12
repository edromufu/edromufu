---
id: introducao
title: Introdução
sidebar_position: 1
slug: vision/treinamento/introducao
---



Para realizar o treinamento da rede, utilizamos o tutorial do repositório [Darknet](https://github.com/AlexeyAB/darknet), que ensina o treinamento com o modelo YOLO. Na nossa aplicação, utilizamos o Tiny YOLOv4, que é uma versão do YOLOv4 menos precisa, porém mais leve, o que funciona muito bem em nosso projeto.

Para realizar o treinamento, primeiro é necessário preparar o dataset que será utilizado de base, seguindo as orientações do tutorial do Darknet. Dividimos isso em cinco etapas até o treinamento em si:

1. [Gravar as imagens com a câmera utilizada](./recording_from_camera.md)
2. [Dividir os vídeos em imagens (denominadas "frames")](./spliting_video_in_frames.md)
3. [Separar os frames em treinamento, validação e avaliação](./organizing_dataset.md)
4. [Marcar os frames para o treinamento](./marcando_labels.md)
5. [Criar os arquivos auxiliares para o treinamento](./criando_txts_dataset.md)

Com exceção do quarto passo, todos possuem scripts para auxiliar na preparação do dataset, porém acompanhar o tutorial do Darknet é fortemente aconselhado ao longo do de todas as etapas do processo.

Nas próximas seções, serão apresentados os scripts, bem como explicada a maneira correta de utilizá-los.
