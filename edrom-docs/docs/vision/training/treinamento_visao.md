---
id: treinamento_visao
title: Trechos de código a serem alterados para treinar
description: Aqui será descrito o que deve ser alterado no arquivo 
slug: /train_visao
sidebar_position: 7
---

O arquivo a ser alterado para realizar o treinamento personalizado é o [TrainYolov8CustomDataset.ipynb](https://colab.research.google.com/drive/1Lv6hiIDyZOJj6Hee8C2NmSgl4f0gProb#scrollTo=oyZJX6PVfE7J)


Antes de iniciar o treinamento, é importante garantir que os nomes das pastas estejam configurados corretamente no arquivo TrainYolov8 do Google Colab. Caso os nomes das pastas tenham sido alterados, os seguintes trechos devem ser ajustados:

```py
# Conecta o Google Drive ao Google Colab
from google.colab import drive
drive.mount('/content/gdrive')

# Ajusta o diretório raiz para o caminho correto
cd /content/gdrive/My\ Drive/EDROM/

ROOT_DIR = '/content/gdrive/My Drive/EDROM/Ball'

```
:::danger CUIDADO
Certifique-se de também modificar o caminho no arquivo YAML para corresponder ao ROOT_DIR.
:::


Este bloco de código configura o diretório onde os resultados serão salvos durante o treinamento. O argumento 'runs_dir' é atualizado para especificar o local como sendo o diretório atual onde o terminal está acessando.
```py
settings.update({'runs_dir': './runs'})
```


Configuração do Modelo para o Treinamento

No bloco de código onde ocorre o treinamento, é importante manter a variável model de acordo com a ação pretendida.

Para aprimorar o treinamento, utilize:
```py
# Carrega um modelo pré-treinado
model = YOLO("/content/gdrive/MyDrive/Teste/best.pt")
```
Em que "best.pt" é o arquivo na pasta "Teste". Certifique-se de ajustar o caminho conforme necessário, dependendo de onde best.pt está salvo.

Para treinar do zero, utilize:
```py
# Configura um modelo novo para treinamento do zero
model = YOLO("yolov8n.yaml")
```


A função model.train do framework Ultralytics YOLOv8 é utilizada para treinar um modelo de detecção de objetos. Em que o argumento 'data' define o caminho para o arquivo de configuração YAML que especifica onde estão os dados de treinamento e validação. O argumento 'epochs' indica a quantidade de vezes que o modelo verá o conjunto completo de dados durante o treinamento. Por fim, o argumento 'name' insere um nome para diferenciar cada treinamento. Esse nome será utilizado para criar a pasta onde os resultados serão salvos.

```py
# Instala a biblioteca ultralytics
!pip install ultralytics
# Configura o local para salvar os resultados do treinamento
results = model.train(data=os.path.join(ROOT_DIR, "google_colab_config.yaml"), epochs=150, name='yolov8n-test')
```
