---
id: T de Bateria®
title: T de Bateria®
description: Esta seção explica o funcionamento do T de Bateria no circuito de alimentação da Robô
slug: /t-de-bateria
sidebar_position: 2
---

## Finalidade <h2>

O _T de Bateria®_ é um componente que permite que a técnica de __Hot Swap__ seja utilizada pela equipe para manter em funcionamento, para testes ou partidas, as robôs sem que elas precisem serem reiniciadas durante esse período, perdendo assim, tempo operação e as informações que estão sendo coletadas durante o funcionamento. Isso permite um maior tempo de operação, que reflete um menor tempo fora de campo.

## Componentes <h2>

O _T de Bateria®_ é composto por:

- 2 Resistores de 65k
- 2 Resistores de 100k
- 4 Transistores PNP TIP42C
- 2 MOSFET IRF4905
- 3 Conectores XT60 tipo FÊMEA

## Operação <h2>

O _T de Bateria®_ funciona refazendo a rota da corrente no circuito de baterias de modo que, quando ligadas em paralelo, não haja retorno de corrente na bateria de menor tensão, podendo diminuir a vida útil da mesma.

<img src="/img/TdeBateria.gif" width="640" height="360" />