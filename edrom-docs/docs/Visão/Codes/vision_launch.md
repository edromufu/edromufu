---
id: vision.launch
title: vision.launch
description: Nesta seção teremos um explicação sobre o código vision.launch
slug: vision/codes/vision_launch
sidebar_position: 1
---

Nesta seção teremos um explicação detalhada sobre o código vision.launch
  

```jsx title="object_finder/launch/vision.launch"
<launch>

    <arg name="camera" default="0"/>
    <arg name="img_output" default="false"/>
    <arg name="ajuste" default="false"/>
    <arg name="brilho" default="4"/>
    
    <!-- Visão -->
    <node name="vision" pkg="object_finder" type="connecting_and_showing.py" output="log" > 
        <param name="camera" value="$(eval arg('camera'))" />
        <param name="img_output" value="$(eval arg('img_output'))" />
        <param name="ajuste" value="$(eval arg('ajuste'))" />
        <param name="brilho" value="$(eval arg('brilho'))" />
    </node>

</launch>
```


No launch da visão temos 4 tipos de argumentos que são passados:


1. __camera__ que irá receber qual é a câmera que será utilizada, normalmente temos 0 para computadores que só tem uma câmera, por exemplo a da robô, ou utilizamos 2 quando estamos fazendo testes em um notebook que possui a webcam integrada dele. Tendo como DEFAULT 0.

2. __img_output__ que irá receber um booleano (true ou false), se for true teremos um retorno visual com uma tela mostrando o que a robô está vendo e false não teremos essa tela. Tendo como DEFAULT *false*.

3. __ajuste__ que irá receber um booleano (true ou false), se for true entrará no modo de ajuste de brilho da câmera. Seguirá o seguinte padrão: “ = ” para aumentar, “ - ” para diminuir e “ W ” para continuar para a detecção. Tendo como DEFAULT *false*.

4.  __brilho__ que irá receber um número de –64 até 64, esse número será utilizado como fator de brilho da câmera, sendo 64 o maior brilho possível e por consequência –64 o menor. Tendo como DEFAULT 4.


E nesse Node o arquivo que será executado é o __“connecting_and_showing.py”__ que utilizará todos esses parâmetros para realizar a detecção.

:::tip Argumentos

Para um melhor entendimento de como utilizar os argumentos, visite a pagina de comandos da visão. 

:::