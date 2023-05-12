---
id: kicad
title: KICAD
description: Nesta seção serão listados as utilidades do software kicad dentro do segmento da elétrica
slug: /kicad
sidebar_position: 1
---

O KICAD é um software que tem por objetivo facilitar a concepção de layouts e suas conversões para placas de circuito impresso.

## Instalação do KICAD

O software é de simples instalação através do link: https://www.kicad.org/download/

## Funcionalidades

O KICAD é basicamente dividido em duas interfaces principais: o **editor de esquemático**, que oferece uma gama de ferramentas de fácil utilização para a confecção de esquemas eletrônicos; e o **editor da PCI**, que permite a criação e visualização 3D de layouts de placas de circuito impresso.

![im](/img/figura1.png)

### Editor de Esquemático
O editor de esquemático é o local onde é feita toda a organização lógica do seu curcuito, é o ambiente onde é possível criar, adicionar e nomear cada um dos componentes eletrônicos que se desejar adicionar. Ainda, é possível realizar a atribuição de *footprints* a fim de especificar cada componente para a próxima etapa de organização da PCI.

![im](/img/figura2.png)

### Editor de PCI
No editor de PCI é feita a organização dos componentes adicionados no esquemático dentro de um ambiente dividido em *layers*. Essas *layers*, ou camadas, são as ferramentas que o software utiliza para especificar cada uma das operações, por exemplo, existem as layers de "*F. Cu*" e "*B. Cu*" que remetem, respectivamente, as trilhas na parte da superior e inferior da placa; existe tambem a layer "*Edge Cuts*", responsável por definir os limites físicos da placa.

![im](/img/figura3.png)

Ainda, é possível visualizar um modelo 3D da sua placa ao utilizar o comando "Alt+3" nesse ambiente.

[adicionar uma imagem aqui]: # "![im](/img/figura4.png)" 

Por fim, e para utilização do design modelado em uma placa real, o software permite a criação de um arquivo Gerber, que por sua vez armazena as informações das *layers* e posição de cada componente.

:::tip Observação

Para um tutorial em detalhes sobre o KICAD, recomendamos o [vídeo](https://www.youtube.com/watch?v=fcb3zco_BrQ) introdutório do professor Marcelo Barros (FEELT - UFU)

:::