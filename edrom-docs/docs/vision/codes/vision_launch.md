---
id: vision.launch
title: vision.launch
description: Nesta seção teremos um explicação sobre o código vision.launch
slug: /vision_launch
sidebar_position: 1
---

Nesta seção teremos um explicação detalhada sobre o código vision.launch
  

```jsx title="object_finder/launch/vision.launch"
from launch import LaunchDescription
from launch_ros.actions import Node	
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    #Declaração dos argumentos que poderão ser passados na execução de ros2 launch
    camera = DeclareLaunchArgument('camera',default_value='0')
    output_img = DeclareLaunchArgument('img_output',default_value='False')
    ajuste = DeclareLaunchArgument('ajuste',default_value='False')
    bright = DeclareLaunchArgument('brilho',default_value='4')

    #Estrutura do launch
    return LaunchDescription([
       camera,
       output_img,
       ajuste,
       bright,
       
       #Visão
       Node(
           package='object_finder',
           namespace='EDROM',
           executable='finder',
           name='vision',
           output='screen',
           parameters=[
               {'vision/camera': LaunchConfiguration('camera')},
               {'vision/img_output': LaunchConfiguration('img_output')},
               {'vision/ajuste' : LaunchConfiguration('ajuste')},
               {'vision/brilho': LaunchConfiguration('brilho')},
            ],
            emulate_tty=True,   #Utililizado para os prints acontecerem em tempo real
        )
   ])
```


No launch da visão temos 4 tipos de argumentos que são passados:


1. __camera__ que irá receber qual é a câmera que será utilizada, normalmente temos 0 para computadores que só tem uma câmera, por exemplo a da robô, ou utilizamos 2 quando estamos fazendo testes em um notebook que possui a webcam integrada dele. Tendo como DEFAULT 0.

2. __output_img__ que irá receber um booleano (true ou false), se for true teremos um retorno visual com uma tela mostrando o que a robô está vendo e false não teremos essa tela. Tendo como DEFAULT *false*.

3. __ajuste__ que irá receber um booleano (true ou false), se for true entrará no modo de ajuste de brilho da câmera. Seguirá o seguinte padrão: “ = ” para aumentar, “ - ” para diminuir e “ W ” para continuar para a detecção. Tendo como DEFAULT *false*.

4.  __bright__ que irá receber um número de –64 até 64, esse número será utilizado como fator de brilho da câmera, sendo 64 o maior brilho possível e por consequência –64 o menor. Tendo como DEFAULT 4.


No contexto do ROS 2, o script connect_and_showing.py é referenciado pelo nome do executável finder. Este nome é definido no arquivo de configuração do pacote, geralmente no setup.py ou em arquivos de configuração específicos do ROS 2. Isso significa que, ao referenciar finder, o ROS 2 sabe que deve executar connect_and_showing.py.

Esse código usa algumas substituições: 

* __DeclareLaunchArgument__ serve para declarar argumentos de lançamento (launch arguments) que podem ser passados para os arquivos de lançamento (launch files). Esses argumentos permitem a personalização e configuração de diferentes parâmetros no momento do lançamento. É usado dentro de um arquivo de lançamento para especificar argumentos opcionais ou obrigatórios, incluindo seus valores padrão e descrições.
  
* __LaunchConfiguration__ é necessário para acessar os valores dos argumentos de lançamento que foram declarados com DeclareLaunchArgument. Esses valores podem ser usados para configurar outros elementos no arquivo de lançamento. É utilizado para referenciar o valor de um argumento de lançamento em outros lugares do arquivo de lançamento, como ao configurar nós ou outros componentes.
  
* __LaunchDescription__ é a estrutura principal que define o conjunto de ações a serem executadas quando o arquivo de lançamento é invocado. Ele agrupa declarações de argumentos, configurações de nós, e outras ações que devem ser realizadas no início do sistema. Basicamente, é um contêiner que contém todos os elementos que compõem um lançamento ROS 2


:::tip Argumentos

Para um melhor entendimento de como utilizar os argumentos, visite a pagina de comandos da visão. 

:::
