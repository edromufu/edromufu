---
id: marcando_labels
title: Marcando labels
sidebar_position: 5
slug: vision/treinamento/marcando_labels
---



Agora, os frames estão separados de acordo com sua função e devem ser marcados para o treinamento. Para isso, será utilizado o [LabelImg](https://github.com/heartexlabs/labelImg). 

Após abrir o programa, configure a label gerada para YOLO na barra lateral.

![Menu Lateral LabelImg](./img/barra_lateral_labelimg.png)

Em seguida, abra o diretório em que os frames estão, e selecione o mesmo diretório para salvar as labels.

![Menu Lateral LabelImg](./img/barra_lateral_2_labelimg.png)

No menu de exibição, habilite o "Auto Save mode" e o "Single Class Mode".

![Configurações de Visualização LabelImg](./img/configuracoes_labelimg.png)

Para marcar uma imagem, pressione a tecla "w" e selecione a região a ser marcada. Após isso, configure o nome da label no menu à direita.

![Selecionar Label LabelImg](./img/selecionar_label_labelimg.png)

Para facilitar a marcação, sugerimos selecionar a label desejada como padrão, para acelerar o processo, e navegar pelas imagens utilizando as teclas "a" e "d", para voltar ou avançar entre as imagens, respectivamente.

Cada label ficará salva em um arquivo .txt na pasta designada, com o mesmo nome do frame que a gerou. Por exemplo, após marcar a label do arquivo "val_291.jpg", ela ficará salva no arquivo "val_291.txt".

:::tip ATENÇÃO

Os frames para avaliação (denominados eval) não precisam ser marcados, pois são utilizados para testar o resultado do treinamento

:::
