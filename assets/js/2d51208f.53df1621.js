"use strict";(self.webpackChunkedrom=self.webpackChunkedrom||[]).push([[2374],{3905:(e,a,t)=>{t.d(a,{Zo:()=>m,kt:()=>v});var r=t(7294);function n(e,a,t){return a in e?Object.defineProperty(e,a,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[a]=t,e}function o(e,a){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);a&&(r=r.filter((function(a){return Object.getOwnPropertyDescriptor(e,a).enumerable}))),t.push.apply(t,r)}return t}function i(e){for(var a=1;a<arguments.length;a++){var t=null!=arguments[a]?arguments[a]:{};a%2?o(Object(t),!0).forEach((function(a){n(e,a,t[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):o(Object(t)).forEach((function(a){Object.defineProperty(e,a,Object.getOwnPropertyDescriptor(t,a))}))}return e}function s(e,a){if(null==e)return{};var t,r,n=function(e,a){if(null==e)return{};var t,r,n={},o=Object.keys(e);for(r=0;r<o.length;r++)t=o[r],a.indexOf(t)>=0||(n[t]=e[t]);return n}(e,a);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)t=o[r],a.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(n[t]=e[t])}return n}var l=r.createContext({}),d=function(e){var a=r.useContext(l),t=a;return e&&(t="function"==typeof e?e(a):i(i({},a),e)),t},m=function(e){var a=d(e.components);return r.createElement(l.Provider,{value:a},e.children)},p="mdxType",u={inlineCode:"code",wrapper:function(e){var a=e.children;return r.createElement(r.Fragment,{},a)}},c=r.forwardRef((function(e,a){var t=e.components,n=e.mdxType,o=e.originalType,l=e.parentName,m=s(e,["components","mdxType","originalType","parentName"]),p=d(t),c=n,v=p["".concat(l,".").concat(c)]||p[c]||u[c]||o;return t?r.createElement(v,i(i({ref:a},m),{},{components:t})):r.createElement(v,i({ref:a},m))}));function v(e,a){var t=arguments,n=a&&a.mdxType;if("string"==typeof e||n){var o=t.length,i=new Array(o);i[0]=c;var s={};for(var l in a)hasOwnProperty.call(a,l)&&(s[l]=a[l]);s.originalType=e,s[p]="string"==typeof e?e:n,i[1]=s;for(var d=2;d<o;d++)i[d]=t[d];return r.createElement.apply(null,i)}return r.createElement.apply(null,t)}c.displayName="MDXCreateElement"},3469:(e,a,t)=>{t.r(a),t.d(a,{assets:()=>l,contentTitle:()=>i,default:()=>u,frontMatter:()=>o,metadata:()=>s,toc:()=>d});var r=t(7462),n=(t(7294),t(3905));const o={id:"criando_txts_dataset",title:"Criando arquivos auxiliares",sidebar_position:6},i=void 0,s={unversionedId:"Vis\xe3o/Treinamento da rede neural/criando_txts_dataset",id:"Vis\xe3o/Treinamento da rede neural/criando_txts_dataset",title:"Criando arquivos auxiliares",description:"Por fim, para realizar o treinamento, \xe9 necess\xe1rio informar quais os frames ser\xe3o utilizados para treinamento e valida\xe7\xe3o, bem como seu endere\xe7o no drive. Para isso, \xe9 utilizado o seguinte script:",source:"@site/docs/Vis\xe3o/Treinamento da rede neural/criando_txts_dataset.md",sourceDirName:"Vis\xe3o/Treinamento da rede neural",slug:"/Vis\xe3o/Treinamento da rede neural/criando_txts_dataset",permalink:"/edromufu/docs/Vis\xe3o/Treinamento da rede neural/criando_txts_dataset",draft:!1,editUrl:"https://github.com/edromufu/edromufu/tree/master/edrom-docs/docs/Vis\xe3o/Treinamento da rede neural/criando_txts_dataset.md",tags:[],version:"current",sidebarPosition:6,frontMatter:{id:"criando_txts_dataset",title:"Criando arquivos auxiliares",sidebar_position:6},sidebar:"tutorialSidebar",previous:{title:"Marcando labels",permalink:"/edromufu/docs/Vis\xe3o/Treinamento da rede neural/marcando_labels"},next:{title:"Tutorial - Extras",permalink:"/edromufu/docs/category/tutorial---extras"}},l={},d=[],m={toc:d},p="wrapper";function u(e){let{components:a,...t}=e;return(0,n.kt)(p,(0,r.Z)({},m,t,{components:a,mdxType:"MDXLayout"}),(0,n.kt)("p",null,"Por fim, para realizar o treinamento, \xe9 necess\xe1rio informar quais os frames ser\xe3o utilizados para treinamento e valida\xe7\xe3o, bem como seu endere\xe7o no drive. Para isso, \xe9 utilizado o seguinte script:"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-py"},"import os\n\npastaFrames = \"frames\" # Pasta onde frames est\xe3o salvos\n\nos.chdir(pastaFrames)\nlista_de_arquivo = os.listdir(os.getcwd())\nlista_de_imagens = []\nos.chdir('..')\n\nfor arquivo in lista_de_arquivo:\n    if os.path.splitext(arquivo)[1] == \".jpg\":\n        lista_de_imagens.append(arquivo)\n\nif os.path.exists('train.txt'):\n    os.remove('train.txt')\n    \nif os.path.exists('valid.txt'):\n    os.remove('valid.txt')\n\narquivo_train = open('train.txt', 'a')\narquivo_val = open('valid.txt', 'a')\n\nline = 'data/obj/'\n\nfor imagem in lista_de_imagens:\n    if imagem.__contains__('train'):\n        if lista_de_arquivo.__contains__(os.path.splitext(imagem)[0]+'.txt'):\n            arquivo_train.write(line + imagem + '\\n')\n        else: os.remove(pastaFrames + '/' + imagem)\n\n    elif imagem.__contains__('eval'): pass\n\n    elif imagem.__contains__('val'):\n        if lista_de_arquivo.__contains__(os.path.splitext(imagem)[0]+'.txt'):\n            arquivo_val.write(line + imagem + '\\n')\n        else: os.remove(pastaFrames + '/' + imagem)\n\narquivo_train.close()\narquivo_val.close()\n")),(0,n.kt)("p",null,"O \xfanico par\xe2metro desse c\xf3digo \xe9 a pasta em que os frames est\xe3o."),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-py"},'pastaFrames = "frames" # Pasta onde frames est\xe3o salvos\n')),(0,n.kt)("p",null,'Em seguida, acessa a pasta dos frames e l\xea o nome de todos os arquivos para iterar sobre eles. Ent\xe3o, salva os que possuem a extens\xe3o .jpg em uma lista (para evitar erros com "lixo" na pasta).'),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-py"},"os.chdir(pastaFrames)\nlista_de_arquivo = os.listdir(os.getcwd())\nlista_de_imagens = []\nos.chdir('..')\n\nfor arquivo in lista_de_arquivo:\n    if os.path.splitext(arquivo)[1] == \".jpg\":\n        lista_de_imagens.append(arquivo)\n")),(0,n.kt)("p",null,'Ap\xf3s isso, deleta os arquivos "train.txt" e "valid.txt", caso existam, e em seguida cria os novos.'),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-py"},"if os.path.exists('train.txt'):\n    os.remove('train.txt')\n    \nif os.path.exists('valid.txt'):\n    os.remove('valid.txt')\n\narquivo_train = open('train.txt', 'a')\narquivo_val = open('valid.txt', 'a')\n")),(0,n.kt)("p",null,'Por fim, itera sobre todos os frames, registrando os marcados como train na "train.txt" e os marcados com val na "valid.txt". Os frames s\xe3o registrados precedidos de \'data/obj/\', pois \xe9 o endere\xe7o da pasta que estar\xe3o quando enviados para o drive para realizar o treinamento (seguindo o tutorial do Darknet).'),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-py"},"line = 'data/obj/'\n\nfor imagem in lista_de_imagens:\n    if imagem.__contains__('train'):\n        if lista_de_arquivo.__contains__(os.path.splitext(imagem)[0]+'.txt'):\n            arquivo_train.write(line + imagem + '\\n')\n        else: os.remove(pastaFrames + '/' + imagem)\n\n    elif imagem.__contains__('eval'): pass\n\n    elif imagem.__contains__('val'):\n        if lista_de_arquivo.__contains__(os.path.splitext(imagem)[0]+'.txt'):\n            arquivo_val.write(line + imagem + '\\n')\n        else: os.remove(pastaFrames + '/' + imagem)\n\narquivo_train.close()\narquivo_val.close()\n")),(0,n.kt)("p",null,'O resultado do script s\xe3o os dois arquivos, "train.txt" e "valid.txt", com os nomes e endere\xe7os dos frames de treinamento de valida\xe7\xe3o.'),(0,n.kt)("p",null,"Com isso, a etapa de prepara\xe7\xe3o do dataset para treinamento foi conclu\xedda. Os pr\xf3ximos passos agora, seguindo o tutorial do ",(0,n.kt)("a",{parentName:"p",href:"https://github.com/AlexeyAB/darknet"},"Darknet"),", \xe9 upar os arquivos para seus respectivos destinos no drive, e seguir o passo a passo do treinamento no Colab."))}u.isMDXComponent=!0}}]);