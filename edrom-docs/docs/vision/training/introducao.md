---
id: introducao
title: Introdução
sidebar_position: 1
slug: /introducao
---


Na visão, é utilizada a YOLOv8, uma arquitetura de rede neural convolucional para detecção de objetos em tempo real. Para entender mais da bilbioteca é recomendado o vídeo a seguir: [![YOLOv8](https://img.youtube.com/vi/wuZtUMEiKWY/0.jpg)](https://www.youtube.com/watch?v=wuZtUMEiKWY)

O tutorial detalhado de [como realizar o treinamento de um dataset customizado](https://docs.ultralytics.com/) pode ser encontrado na docuemntação da Ultralytics, empresa responsável pelo desenvolvimento da YOLOv8.


Entretanto, as outras secções da documentação da edrom explicam o passo a passo utilizado na equipe para a deteção dos objetos desejados, de forma a manter um padrão e evitar conflitos (Mas vale ressaltar que tudo se baseia na documentação oferecida pela Ultralytics).

O passo a passo do treinamento é:

1. [Gravar as imagens com a câmera utilizada](./recording_from_camera.md)
2. [Dividir os vídeos em imagens (denominadas "frames")](./spliting_video_in_frames.md)
3. [Separar os frames em treinamento, validação e avaliação](./organizing_dataset.md)
4. [Marcar os frames para o treinamento](./marcando_labels.md)
5. [Organização do dataset](./criando_txts_dataset.md)
6. [Treinamento em si](./treinamento_visao.md)