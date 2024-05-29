"use strict";(self.webpackChunkedrom=self.webpackChunkedrom||[]).push([[5539],{5680:(e,a,r)=>{r.d(a,{xA:()=>u,yg:()=>g});var t=r(6540);function n(e,a,r){return a in e?Object.defineProperty(e,a,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[a]=r,e}function o(e,a){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var t=Object.getOwnPropertySymbols(e);a&&(t=t.filter((function(a){return Object.getOwnPropertyDescriptor(e,a).enumerable}))),r.push.apply(r,t)}return r}function s(e){for(var a=1;a<arguments.length;a++){var r=null!=arguments[a]?arguments[a]:{};a%2?o(Object(r),!0).forEach((function(a){n(e,a,r[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(a){Object.defineProperty(e,a,Object.getOwnPropertyDescriptor(r,a))}))}return e}function i(e,a){if(null==e)return{};var r,t,n=function(e,a){if(null==e)return{};var r,t,n={},o=Object.keys(e);for(t=0;t<o.length;t++)r=o[t],a.indexOf(r)>=0||(n[r]=e[r]);return n}(e,a);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(t=0;t<o.length;t++)r=o[t],a.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(n[r]=e[r])}return n}var l=t.createContext({}),p=function(e){var a=t.useContext(l),r=a;return e&&(r="function"==typeof e?e(a):s(s({},a),e)),r},u=function(e){var a=p(e.components);return t.createElement(l.Provider,{value:a},e.children)},c="mdxType",d={inlineCode:"code",wrapper:function(e){var a=e.children;return t.createElement(t.Fragment,{},a)}},m=t.forwardRef((function(e,a){var r=e.components,n=e.mdxType,o=e.originalType,l=e.parentName,u=i(e,["components","mdxType","originalType","parentName"]),c=p(r),m=n,g=c["".concat(l,".").concat(m)]||c[m]||d[m]||o;return r?t.createElement(g,s(s({ref:a},u),{},{components:r})):t.createElement(g,s({ref:a},u))}));function g(e,a){var r=arguments,n=a&&a.mdxType;if("string"==typeof e||n){var o=r.length,s=new Array(o);s[0]=m;var i={};for(var l in a)hasOwnProperty.call(a,l)&&(i[l]=a[l]);i.originalType=e,i[c]="string"==typeof e?e:n,s[1]=i;for(var p=2;p<o;p++)s[p]=r[p];return t.createElement.apply(null,s)}return t.createElement.apply(null,r)}m.displayName="MDXCreateElement"},1197:(e,a,r)=>{r.r(a),r.d(a,{assets:()=>l,contentTitle:()=>s,default:()=>d,frontMatter:()=>o,metadata:()=>i,toc:()=>p});var t=r(8168),n=(r(6540),r(5680));const o={id:"treinamento_visao",title:"Arquivos a serem alterados para treinar",description:"Aqui ser\xe1 descrito o que deve ser alterado no arquivo",slug:"/train_visao",sidebar_position:7},s=void 0,i={unversionedId:"vision/training/treinamento_visao",id:"vision/training/treinamento_visao",title:"Arquivos a serem alterados para treinar",description:"Aqui ser\xe1 descrito o que deve ser alterado no arquivo",source:"@site/docs/vision/training/treinamento_visao.md",sourceDirName:"vision/training",slug:"/train_visao",permalink:"/edromufu/docs/train_visao",draft:!1,editUrl:"https://github.com/edromufu/edromufu/tree/master/edrom-docs/docs/vision/training/treinamento_visao.md",tags:[],version:"current",sidebarPosition:7,frontMatter:{id:"treinamento_visao",title:"Arquivos a serem alterados para treinar",description:"Aqui ser\xe1 descrito o que deve ser alterado no arquivo",slug:"/train_visao",sidebar_position:7},sidebar:"tutorialSidebar",previous:{title:"Criando arquivos auxiliares",permalink:"/edromufu/docs/criando_txts_dataset"},next:{title:"Outras \xc1reas - coming soon",permalink:"/edromufu/docs/category/outras-\xe1reas---coming-soon"}},l={},p=[],u={toc:p},c="wrapper";function d(e){let{components:a,...r}=e;return(0,n.yg)(c,(0,t.A)({},u,r,{components:a,mdxType:"MDXLayout"}),(0,n.yg)("p",null,"O arquivo a ser alterado para realizar o treinamento personalizado \xe9 o ",(0,n.yg)("a",{parentName:"p",href:"https://github.com/edromufu/edromufu/blob/master/src/vision/robocup_cnn_files/yolov4-tiny-obj.cfg"},"yolov4-tiny-obj.cfg")),(0,n.yg)("p",null,"O primeiro passo a ser realizado \xe9 garantir que as seguintes vari\xe1veis possuam os valores:"),(0,n.yg)("pre",null,(0,n.yg)("code",{parentName:"pre",className:"language-py"},"batch=64\nsubdivision=16\n")),(0,n.yg)("p",null,"Ent\xe3o, \xe9 necess\xe1rio alterar a linha ",(0,n.yg)("strong",{parentName:"p"},"max_division")," para o n\xfamero de classes desejadas vezes 2000."),(0,n.yg)("admonition",{title:"N\xfamero de classes",type:"tip"},(0,n.yg)("p",{parentName:"admonition"},"O n\xfamero de classes \xe9 a quantidade de objetos que voc\xea quer treinar para a rede reconhecer, se for apenas para detec\xe7\xe3o da bola, o n\xfamero de classes \xe9 igual a 1")),(0,n.yg)("p",null,"Ou seja, para uma classe voc\xea teria:"),(0,n.yg)("pre",null,(0,n.yg)("code",{parentName:"pre",className:"language-py"},"max_batches=2000\n")),(0,n.yg)("p",null,"O passo seguinte \xe9 alterar a linha ",(0,n.yg)("strong",{parentName:"p"},"steps")," para 80% e 90% do max_steps respectivamente. Ou seja, para um max_batches=2000 o correto \xe9 ter"),(0,n.yg)("pre",null,(0,n.yg)("code",{parentName:"pre",className:"language-py"},"steps=1600,1800\n")),(0,n.yg)("p",null,"Setar os valores de ",(0,n.yg)("strong",{parentName:"p"},"width")," e ",(0,n.yg)("strong",{parentName:"p"},"height")," para 416 ambos (Ou algum outro valor m\xfaltiplo de 32 dependendo da aplica\xe7\xe3o)"),(0,n.yg)("pre",null,(0,n.yg)("code",{parentName:"pre",className:"language-py"},"width=416\nheight=416\n")),(0,n.yg)("p",null,"Agora \xe9 alterar as linhas ",(0,n.yg)("strong",{parentName:"p"},"classes")," para o n\xfamero desejado"),(0,n.yg)("pre",null,(0,n.yg)("code",{parentName:"pre",className:"language-py"},"classes=1\n")),(0,n.yg)("admonition",{title:"CUIDADO",type:"danger"},(0,n.yg)("p",{parentName:"admonition"},"\xc9 necess\xe1rio alterar a linha classes em mais de um lugar, no arquivo em quest\xe3o s\xe3o nas linhas 220 e 269")),(0,n.yg)("p",null,"E por fim alterar ",(0,n.yg)("strong",{parentName:"p"},"filters")," para um valor igual a f\xf3rmula (classes+5)x3, ou seja, no caso de uma classe teremmos:"),(0,n.yg)("pre",null,(0,n.yg)("code",{parentName:"pre",className:"language-py"},"filters=18\n")),(0,n.yg)("admonition",{title:"MUITO CUIDADO!!!",type:"danger"},(0,n.yg)("p",{parentName:"admonition"},"A vari\xe1vel filters deve ser atualizada algumas vezes ao decorrer do c\xf3digo, que s\xe3o nos ","[convolutional]"," antes de cada cammada ","[yolo]",", no c\xf3digo em quest\xe3o est\xe3o nas linhas 212 e 266")),(0,n.yg)("p",null,"Isso \xe9 tudo que deve ser alterado no arquivo de configura\xe7\xe3o"))}d.isMDXComponent=!0}}]);