---
id: criando_txts_dataset
title: Criando arquivos auxiliares
slug: /criando_txts_dataset
sidebar_position: 6
---



Durante o processo de treinamento, optamos por utilizar o Google Colab como nossa plataforma principal, aproveitando sua potente infraestrutura em nuvem, e utilizamos o Google Drive para organizar e armazenar nosso conjunto de dados, simplificando o gerenciamento e promovendo a colaboração eficiente.

## Criação da estrutura de pastas no Google Drive:

1. No seu Google Drive, crie uma pasta (por exemplo, chamada "Teste").
2. Dentro da pasta "Teste", crie uma subpasta para o conjunto de dados (por exemplo, "Ball").
3. Dentro da subpasta "Ball", crie duas subpastas chamadas "train" e "valid".
   - Na pasta "train" serão colocadas as imagens de treinamento.
   - Na pasta "valid" serão colocadas as imagens de validação.
   - Lembrando que nomeamos as imagens com prefixo “train” e “val” para facilitar a organização dos respectivos arquivos.

4. Dentro de cada uma dessas subpastas ("train" e "valid"), crie duas subpastas adicionais chamadas "images" e "labels".

## Organização dos dados dentro das pastas:

- Na pasta "train":
  - Coloque as imagens de treinamento com o prefixo "train" na subpasta "images".
  - Coloque os arquivos de rótulos com o prefixo "train" na subpasta "labels", junto com o arquivo "classes.txt".

- Na pasta "valid":
  - Coloque as imagens de validação com o prefixo "val" na subpasta "images".
  - Coloque os arquivos de rótulos com o prefixo "val" na subpasta "labels", junto com o arquivo "classes.txt".
