---
id: treinamento_visao
title: Trechos de código a serem alterados para treinar
description: Aqui será descrito o que deve ser alterado no arquivo 
slug: /train_visao
sidebar_position: 7
---

O arquivo a ser alterado para realizar o treinamento personalizado é o [yolov4-tiny-obj.cfg](https://github.com/edromufu/edromufu/blob/master/src/vision/robocup_cnn_files/yolov4-tiny-obj.cfg)

Antes de iniciar o treinamento, é importante garantir que os nomes das pastas estejam configurados corretamente no arquivo TrainYolov8 do Google Colab. Caso os nomes das pastas tenham sido alterados, os seguintes trechos devem ser ajustados:

```py
cd /content/gdrive/My\ Drive/EDROM/

ROOT_DIR = '/content/gdrive/My Drive/EDROM/Ball'
```

:::danger CUIDADO
Certifique-se de também modificar o caminho no arquivo YAML para corresponder ao ROOT_DIR.
:::

Configuração do Modelo para o Treinamento

No bloco de código onde ocorre o treinamento, é importante manter a variável model de acordo com a ação pretendida.

Para aprimorar o treinamento, utilize:
```py
model = YOLO("/content/gdrive/MyDrive/Teste/best.pt")
```
Em que "best.pt" é o arquivo na pasta "Teste". Certifique-se de ajustar o caminho conforme necessário, dependendo de onde best.pt está salvo.

Para treinar do zero, utilize:
```py
model = YOLO("yolov8n.yaml").
```
No argumento name='', insira um nome para diferenciar cada treinamento. Esse será o nome da pasta onde os resultados serão salvos.
```py
results = model.train(data=os.path.join(ROOT_DIR, "google_colab_config.yaml"), epochs=150, name='yolov8n-test')
```
