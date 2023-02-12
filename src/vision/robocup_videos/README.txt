ATENÇÃO: Não colocar os frames/vídeos nessa pasta, copie os scripts para outra ou mude os parametros do endereço para evitar deixar o repositório carregado de frames/vídeos.

Bem tranquilo, só ir rodando os .py em ordem, marcar as labels entre o 3° e 5°, mas sempre lembrando de conferir o tutorial da Darknet (https://github.com/AlexeyAB/darknet)

Todos os arquivos estão com um pouco de documentação e com os parâmetros na parte de cima pra serem editados.

Resumo:

1 - Grava um video pela camera setada e salva na pasta setada (videos). Ele já seleciona o nome automático pro vídeo vendo quais já tem na pasta (não precisa ficar renomeando manualmente)

2 - Divide os vídeos em frames e salva na pasta setada (frames). Já pega todos os vídeos da pasta setada (videos) sozinho.

3 - Divide os frames em train, val e eval.

4 - Só um lembrete de quando marcar as labels.

5 - Cria a train.txt e a valid.txt com os frames e labels. Exclui automaticamente todos os train e val que não possuem labels.

ATENÇÃO: Não colocar os frames/vídeos nessa pasta, copie os scripts para outra ou mude os parametros do endereço para evitar deixar o repositório carregado de frames/vídeos.