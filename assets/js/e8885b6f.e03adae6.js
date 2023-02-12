"use strict";(self.webpackChunkedrom=self.webpackChunkedrom||[]).push([[3679],{3905:(a,e,n)=>{n.d(e,{Zo:()=>d,kt:()=>_});var o=n(7294);function t(a,e,n){return e in a?Object.defineProperty(a,e,{value:n,enumerable:!0,configurable:!0,writable:!0}):a[e]=n,a}function r(a,e){var n=Object.keys(a);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(a);e&&(o=o.filter((function(e){return Object.getOwnPropertyDescriptor(a,e).enumerable}))),n.push.apply(n,o)}return n}function i(a){for(var e=1;e<arguments.length;e++){var n=null!=arguments[e]?arguments[e]:{};e%2?r(Object(n),!0).forEach((function(e){t(a,e,n[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(a,Object.getOwnPropertyDescriptors(n)):r(Object(n)).forEach((function(e){Object.defineProperty(a,e,Object.getOwnPropertyDescriptor(n,e))}))}return a}function s(a,e){if(null==a)return{};var n,o,t=function(a,e){if(null==a)return{};var n,o,t={},r=Object.keys(a);for(o=0;o<r.length;o++)n=r[o],e.indexOf(n)>=0||(t[n]=a[n]);return t}(a,e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(a);for(o=0;o<r.length;o++)n=r[o],e.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(a,n)&&(t[n]=a[n])}return t}var l=o.createContext({}),p=function(a){var e=o.useContext(l),n=e;return a&&(n="function"==typeof a?a(e):i(i({},e),a)),n},d=function(a){var e=p(a.components);return o.createElement(l.Provider,{value:e},a.children)},c="mdxType",u={inlineCode:"code",wrapper:function(a){var e=a.children;return o.createElement(o.Fragment,{},e)}},m=o.forwardRef((function(a,e){var n=a.components,t=a.mdxType,r=a.originalType,l=a.parentName,d=s(a,["components","mdxType","originalType","parentName"]),c=p(n),m=t,_=c["".concat(l,".").concat(m)]||c[m]||u[m]||r;return n?o.createElement(_,i(i({ref:e},d),{},{components:n})):o.createElement(_,i({ref:e},d))}));function _(a,e){var n=arguments,t=e&&e.mdxType;if("string"==typeof a||t){var r=n.length,i=new Array(r);i[0]=m;var s={};for(var l in e)hasOwnProperty.call(e,l)&&(s[l]=e[l]);s.originalType=a,s[c]="string"==typeof a?a:t,i[1]=s;for(var p=2;p<r;p++)i[p]=n[p];return o.createElement.apply(null,i)}return o.createElement.apply(null,n)}m.displayName="MDXCreateElement"},3458:(a,e,n)=>{n.r(e),n.d(e,{assets:()=>l,contentTitle:()=>i,default:()=>u,frontMatter:()=>r,metadata:()=>s,toc:()=>p});var o=n(7462),t=(n(7294),n(3905));const r={id:"organizing_dataset",title:"Separar os frames",sidebar_position:4,slug:"vision/treinamento/organizing_dataset"},i=void 0,s={unversionedId:"Vis\xe3o/Treinamento da rede neural/organizing_dataset",id:"Vis\xe3o/Treinamento da rede neural/organizing_dataset",title:"Separar os frames",description:"Para o treinamento com Tiny YOLOv4, \xe9 necess\xe1rio separar as imagens em 3 categorias2val",source:"@site/docs/Vis\xe3o/Treinamento da rede neural/organizing_dataset.md",sourceDirName:"Vis\xe3o/Treinamento da rede neural",slug:"/Vis\xe3o/Treinamento da rede neural/vision/treinamento/organizing_dataset",permalink:"/edromufu/docs/Vis\xe3o/Treinamento da rede neural/vision/treinamento/organizing_dataset",draft:!1,editUrl:"https://github.com/edromufu/edromufu/tree/master/edrom-docs/docs/Vis\xe3o/Treinamento da rede neural/organizing_dataset.md",tags:[],version:"current",sidebarPosition:4,frontMatter:{id:"organizing_dataset",title:"Separar os frames",sidebar_position:4,slug:"vision/treinamento/organizing_dataset"},sidebar:"tutorialSidebar",previous:{title:"Dividir os v\xeddeos em frames",permalink:"/edromufu/docs/Vis\xe3o/Treinamento da rede neural/vision/treinamento/spliting_video_in_frames"},next:{title:"Marcando labels",permalink:"/edromufu/docs/Vis\xe3o/Treinamento da rede neural/vision/treinamento/marcando_labels"}},l={},p=[],d={toc:p},c="wrapper";function u(a){let{components:e,...n}=a;return(0,t.kt)(c,(0,o.Z)({},d,n,{components:e,mdxType:"MDXLayout"}),(0,t.kt)("p",null,'Para o treinamento com Tiny YOLOv4, \xe9 necess\xe1rio separar as imagens em 3 categorias: treinamento (train), valida\xe7\xe3o (val) e avalia\xe7\xe3o (eval). Os frames de treinamento s\xe3o os utilizados para o treinamento em si da rede neural. Os de valida\xe7\xe3o tamb\xe9m s\xe3o utilizados no treinamento, por\xe9m servem como um "teste com gabarito" para o treinamento. Enquanto os de avalia\xe7\xe3o s\xe3o os separados para testes manuais feitos com a rede ap\xf3s o treinamento e por isso n\xe3o precisam ser marcados ou alimentados no treinamento. No c\xf3digo de exemplo, foi utilizada a propor\xe7\xe3o de 7:2:1 para train:val:eval. O seguinte script \xe9 utilizado para renomear os arquivos e realizar a separa\xe7\xe3o:'),(0,t.kt)("pre",null,(0,t.kt)("code",{parentName:"pre",className:"language-py"},"import os\n\npastaFrames = \"frames\" # Pasta onde frames est\xe3o salvos\nproporcaoTreino = 0.7\nproporcaoValidacao = 0.2\n\nos.chdir(pastaFrames)\nlista_de_arquivo = os.listdir(os.getcwd())\nlista_de_imagens = []\n\nfor arquivo in lista_de_arquivo:\n    if os.path.splitext(arquivo)[1] == \".jpg\":\n        lista_de_imagens.append(arquivo)\n\nquant_treino = int(len(lista_de_imagens)*proporcaoTreino)\nquant_validacao = int(len(lista_de_imagens)*proporcaoValidacao)\nquant_avaliacao = len(lista_de_imagens)-(quant_treino + quant_validacao)\n\nlista_de_treino = lista_de_imagens[:quant_treino]\nlista_de_validacao = lista_de_imagens[quant_treino:quant_treino + quant_validacao]\nlista_de_avaliacao = lista_de_imagens[quant_treino+ quant_validacao:]\n\ncount_treino = 1\ncount_validacao = 1\ncount_avaliacao = 1\n\nfor arquivo in lista_de_arquivo:\n    if arquivo in lista_de_treino:\n        nome = os.path.splitext(arquivo)[0]\n        os.rename(nome + '.jpg', f'train_{count_treino}.jpg')\n        try:\n            os.rename(nome + '.txt', f'train_{count_treino}.txt')\n        except Exception:\n            pass\n        count_treino += 1\n\n    elif arquivo in lista_de_validacao:\n        nome = os.path.splitext(arquivo)[0]\n        os.rename(nome + '.jpg', f'val_{count_validacao}.jpg')\n        try:\n            os.rename(nome + '.txt', f'val_{count_validacao}.txt')\n        except Exception:\n            pass\n        count_validacao += 1\n\n    elif arquivo in lista_de_avaliacao:\n        nome = os.path.splitext(arquivo)[0]\n        os.rename(nome + '.jpg', f'eval_{count_avaliacao}.jpg')\n        try:\n            os.rename(nome + '.txt', f'eval_{count_avaliacao}.txt')\n        except Exception:\n            pass\n        count_avaliacao += 1\n\n")),(0,t.kt)("p",null,"Os par\xe2metros para esse script s\xe3o a pasta em que os frames est\xe3o, a propor\xe7\xe3o de frames para treinamento e para valida\xe7\xe3o (a soma total das propor\xe7\xf5es de treinamento, valida\xe7\xe3o e avalia\xe7\xe3o \xe9 = 1)."),(0,t.kt)("pre",null,(0,t.kt)("code",{parentName:"pre",className:"language-py"},'pastaFrames = "frames" # Pasta onde frames est\xe3o salvos\nproporcaoTreino = 0.7\nproporcaoValidacao = 0.2\n')),(0,t.kt)("p",null,'Em seguida, acessa a pasta dos frames e l\xea o nome de todos os arquivos para iterar sobre eles. Ent\xe3o, salva os que possuem a extens\xe3o .jpg em uma lista (para evitar erros com "lixo" na pasta).'),(0,t.kt)("pre",null,(0,t.kt)("code",{parentName:"pre",className:"language-py"},'os.chdir(pastaFrames)\nlista_de_arquivo = os.listdir(os.getcwd())\nlista_de_imagens = []\n\nfor arquivo in lista_de_arquivo:\n    if os.path.splitext(arquivo)[1] == ".jpg":\n        lista_de_imagens.append(arquivo)\n')),(0,t.kt)("p",null,"Ap\xf3s isso, calcula a quantidade de frames em cada categoria, e salva eles em listas separadas."),(0,t.kt)("pre",null,(0,t.kt)("code",{parentName:"pre",className:"language-py"},"quant_treino = int(len(lista_de_imagens)*proporcaoTreino)\nquant_validacao = int(len(lista_de_imagens)*proporcaoValidacao)\nquant_avaliacao = len(lista_de_imagens)-(quant_treino + quant_validacao)\n\nlista_de_treino = lista_de_imagens[:quant_treino]\nlista_de_validacao = lista_de_imagens[quant_treino:quant_treino + quant_validacao]\nlista_de_avaliacao = lista_de_imagens[quant_treino+ quant_validacao:]\n")),(0,t.kt)("p",null,'Com os frames j\xe1 separados, os arquivos s\xe3o renomeados para indicar para o que ser\xe3o utilizados. O nome dos frames segue o padr\xe3o "train_0.jpg", "val_0.jpg" e "eval_0.jpg".'),(0,t.kt)("pre",null,(0,t.kt)("code",{parentName:"pre",className:"language-py"},"count_treino = 1\ncount_validacao = 1\ncount_avaliacao = 1\n\nfor arquivo in lista_de_arquivo:\n    if arquivo in lista_de_treino:\n        nome = os.path.splitext(arquivo)[0]\n        os.rename(nome + '.jpg', f'train_{count_treino}.jpg')\n        try:\n            os.rename(nome + '.txt', f'train_{count_treino}.txt')\n        except Exception:\n            pass\n        count_treino += 1\n\n    elif arquivo in lista_de_validacao:\n        nome = os.path.splitext(arquivo)[0]\n        os.rename(nome + '.jpg', f'val_{count_validacao}.jpg')\n        try:\n            os.rename(nome + '.txt', f'val_{count_validacao}.txt')\n        except Exception:\n            pass\n        count_validacao += 1\n\n    elif arquivo in lista_de_avaliacao:\n        nome = os.path.splitext(arquivo)[0]\n        os.rename(nome + '.jpg', f'eval_{count_avaliacao}.jpg')\n        try:\n            os.rename(nome + '.txt', f'eval_{count_avaliacao}.txt')\n        except Exception:\n            pass\n        count_avaliacao += 1\n")),(0,t.kt)("p",null,"O resultado ser\xe1 os frames separados e renomeados de acordo com sua fun\xe7\xe3o (treinamento, valida\xe7\xe3o ou avalia\xe7\xe3o) seguindo a propor\xe7\xe3o definida para cada categoria."))}u.isMDXComponent=!0}}]);