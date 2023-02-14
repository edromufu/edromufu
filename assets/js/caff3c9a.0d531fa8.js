"use strict";(self.webpackChunkedrom=self.webpackChunkedrom||[]).push([[3999],{3905:(e,o,r)=>{r.d(o,{Zo:()=>u,kt:()=>f});var t=r(7294);function a(e,o,r){return o in e?Object.defineProperty(e,o,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[o]=r,e}function n(e,o){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var t=Object.getOwnPropertySymbols(e);o&&(t=t.filter((function(o){return Object.getOwnPropertyDescriptor(e,o).enumerable}))),r.push.apply(r,t)}return r}function s(e){for(var o=1;o<arguments.length;o++){var r=null!=arguments[o]?arguments[o]:{};o%2?n(Object(r),!0).forEach((function(o){a(e,o,r[o])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):n(Object(r)).forEach((function(o){Object.defineProperty(e,o,Object.getOwnPropertyDescriptor(r,o))}))}return e}function i(e,o){if(null==e)return{};var r,t,a=function(e,o){if(null==e)return{};var r,t,a={},n=Object.keys(e);for(t=0;t<n.length;t++)r=n[t],o.indexOf(r)>=0||(a[r]=e[r]);return a}(e,o);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);for(t=0;t<n.length;t++)r=n[t],o.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}var d=t.createContext({}),p=function(e){var o=t.useContext(d),r=o;return e&&(r="function"==typeof e?e(o):s(s({},o),e)),r},u=function(e){var o=p(e.components);return t.createElement(d.Provider,{value:o},e.children)},c="mdxType",m={inlineCode:"code",wrapper:function(e){var o=e.children;return t.createElement(t.Fragment,{},o)}},l=t.forwardRef((function(e,o){var r=e.components,a=e.mdxType,n=e.originalType,d=e.parentName,u=i(e,["components","mdxType","originalType","parentName"]),c=p(r),l=a,f=c["".concat(d,".").concat(l)]||c[l]||m[l]||n;return r?t.createElement(f,s(s({ref:o},u),{},{components:r})):t.createElement(f,s({ref:o},u))}));function f(e,o){var r=arguments,a=o&&o.mdxType;if("string"==typeof e||a){var n=r.length,s=new Array(n);s[0]=l;var i={};for(var d in o)hasOwnProperty.call(o,d)&&(i[d]=o[d]);i.originalType=e,i[c]="string"==typeof e?e:a,s[1]=i;for(var p=2;p<n;p++)s[p]=r[p];return t.createElement.apply(null,s)}return t.createElement.apply(null,r)}l.displayName="MDXCreateElement"},9096:(e,o,r)=>{r.r(o),r.d(o,{assets:()=>d,contentTitle:()=>s,default:()=>m,frontMatter:()=>n,metadata:()=>i,toc:()=>p});var t=r(7462),a=(r(7294),r(3905));const n={id:"mapeamento",title:"\xc1rvore de Arquivos",description:"Nesta se\xe7\xe3o conseguimos vemos a estrutura dos pacotes da vis\xe3o",slug:"/mapeamento-visao",sidebar_position:4},s=void 0,i={unversionedId:"vision/mapeamento",id:"vision/mapeamento",title:"\xc1rvore de Arquivos",description:"Nesta se\xe7\xe3o conseguimos vemos a estrutura dos pacotes da vis\xe3o",source:"@site/docs/vision/mapeamento.md",sourceDirName:"vision",slug:"/mapeamento-visao",permalink:"/edromufu/docs/mapeamento-visao",draft:!1,editUrl:"https://github.com/edromufu/edromufu/tree/master/edrom-docs/docs/vision/mapeamento.md",tags:[],version:"current",sidebarPosition:4,frontMatter:{id:"mapeamento",title:"\xc1rvore de Arquivos",description:"Nesta se\xe7\xe3o conseguimos vemos a estrutura dos pacotes da vis\xe3o",slug:"/mapeamento-visao",sidebar_position:4},sidebar:"tutorialSidebar",previous:{title:"Comandos utilizados pela vis\xe3o",permalink:"/edromufu/docs/cmd_visao"},next:{title:"C\xf3digos de detec\xe7\xe3o",permalink:"/edromufu/docs/category/c\xf3digos-de-detec\xe7\xe3o"}},d={},p=[{value:"Vision_msgs",id:"vision_msgs",level:2},{value:"Robocup_cnn_files",id:"robocup_cnn_files",level:2},{value:"Robocup_videos",id:"robocup_videos",level:2},{value:"Object_finder",id:"object_finder",level:2}],u={toc:p},c="wrapper";function m(e){let{components:o,...r}=e;return(0,a.kt)(c,(0,t.Z)({},u,r,{components:o,mdxType:"MDXLayout"}),(0,a.kt)("p",null,"A pasta da ",(0,a.kt)("a",{parentName:"p",href:"https://github.com/edromufu/edromufu/tree/master/src/vision"},"Vis\xe3o")," fica dentro da src do reposit\xf3rio, e dentro dela fica todo o escopo do projeto que compete \xe0 vis\xe3o. Os arquivos da \xe1rea s\xe3o separados em quatro pastas:"),(0,a.kt)("ol",null,(0,a.kt)("li",{parentName:"ol"},(0,a.kt)("a",{parentName:"li",href:"https://github.com/edromufu/edromufu/tree/master/src/vision/vision_msgs"},"Vision_msgs")),(0,a.kt)("li",{parentName:"ol"},(0,a.kt)("a",{parentName:"li",href:"https://github.com/edromufu/edromufu/tree/master/src/vision/robocup_cnn_files"},"Robocup_cnn_files")),(0,a.kt)("li",{parentName:"ol"},(0,a.kt)("a",{parentName:"li",href:"https://github.com/edromufu/edromufu/tree/master/src/vision/robocup_videos"},"Robocup_videos")),(0,a.kt)("li",{parentName:"ol"},(0,a.kt)("a",{parentName:"li",href:"https://github.com/edromufu/edromufu/tree/master/src/vision/object_finder"},"Object_finder"))),(0,a.kt)("h2",{id:"vision_msgs"},"Vision_msgs"),(0,a.kt)("p",null,"Como o projeto utiliza ",(0,a.kt)("a",{parentName:"p",href:"https://www.ros.org/"},"ROS")," para comunica\xe7\xe3o, faz-se necess\xe1rio definir as mensagens que ser\xe3o enviadas e recebidas pelos c\xf3digos. Nessa pasta, ficam as mensagens utilizadas na Vis\xe3o."),(0,a.kt)("h2",{id:"robocup_cnn_files"},"Robocup_cnn_files"),(0,a.kt)("p",null,"O resultado do treinamento da rede neural s\xe3o dois arquivos: ",(0,a.kt)("strong",{parentName:"p"},"yolov4-tiny-obj.cfg")," e ",(0,a.kt)("strong",{parentName:"p"},"yolov4-tiny-obj.weights"),". Esses arquivos possuem os par\xe2metros que ser\xe3o utilizados na infer\xeancia das imagens, e dentro dessa pasta eles s\xe3o salvos, juntamente com backups de treinamentos antigos que funcionaram bem."),(0,a.kt)("h2",{id:"robocup_videos"},"Robocup_videos"),(0,a.kt)("p",null,"Para prepara o dataset para o treinamento, \xe9 necess\xe1rio realizar uma s\xe9rie de processos, melhores detalhados ",(0,a.kt)("a",{parentName:"p",href:"/edromufu/docs/introducao"},"aqui"),". Para facilitar a cria\xe7\xe3o desse dataset, foram desenvolvidos scripts auxiliares. Esses scripts s\xe3o armazenados nessa pasta, bem como os arquivos ",(0,a.kt)("strong",{parentName:"p"},"train.txt")," e ",(0,a.kt)("strong",{parentName:"p"},"valid.txt"),", que s\xe3o utilizados no treinamento. Os scripts s\xe3o os seguintes:"),(0,a.kt)("ol",null,(0,a.kt)("li",{parentName:"ol"},(0,a.kt)("strong",{parentName:"li"},"recording_from_camera.py"),": Utilizado para gravar v\xeddeos com a c\xe2mera (ou webcam)"),(0,a.kt)("li",{parentName:"ol"},(0,a.kt)("strong",{parentName:"li"},"spliting_video_in_frames.py"),": Utilizado para dividir os v\xeddeos gravados em frames"),(0,a.kt)("li",{parentName:"ol"},(0,a.kt)("strong",{parentName:"li"},"organizing_datase.py"),": Utilizado para dividir os frames de acordo com seu prop\xf3sito (treinamento, valida\xe7\xe3o e avalia\xe7\xe3o)"),(0,a.kt)("li",{parentName:"ol"},(0,a.kt)("strong",{parentName:"li"},"criando_txts_dataset.py"),": Utilizado para gerar os arquivos ",(0,a.kt)("strong",{parentName:"li"},"train.txt")," e ",(0,a.kt)("strong",{parentName:"li"},"valid.txt")," pr\xe9viamente citados")),(0,a.kt)("p",null,"Para evitar que o reposit\xf3rio fique carregado com arquivos desnecess\xe1rios, recomenda-se que os scripts sejam copiados para outro local, e executados l\xe1, de forma que os arquivos gerados (v\xeddeos, frames ou txts) fiquem neste outro local, para depois serem enviados ao drive para treinamento."),(0,a.kt)("h2",{id:"object_finder"},"Object_finder"),(0,a.kt)("p",null,"Por fim, a object_finder onde efetivamente acontece a Vis\xe3o do projeto. Desde capturar as imagens, at\xe9 enviar os resultados da infer\xeancia ao restante do projeto."),(0,a.kt)("p",null,"Dentro da src desse diret\xf3rio, temos dois arquivos principais. Estes s\xe3o ",(0,a.kt)("a",{parentName:"p",href:"https://github.com/edromufu/edromufu/blob/master/src/vision/object_finder/src/connecting_and_showing_current_frame_robocup.py"},"connecting_and_showing_current_frame_robocup.py")," e ",(0,a.kt)("a",{parentName:"p",href:"https://github.com/edromufu/edromufu/blob/master/src/vision/object_finder/src/running_inference_robocup.py"},"running_inference_robocup.py"),"."),(0,a.kt)("p",null,"O primeiro conecta \xe0 c\xe2mera utilizada, obt\xe9m as imagens, realiza a chamada da infer\xeancia, que \xe9 realizada no ",(0,a.kt)("strong",{parentName:"p"},"running_inference_robocup.py"),", sobre as imagens e mostra (opcionalmente) o resultado em tempo real da interpreta\xe7\xe3o da rede neural, al\xe9m de enviar o resultado por ",(0,a.kt)("strong",{parentName:"p"},"ROS")," ao restante do projeto."),(0,a.kt)("p",null,"O segundo \xe9 onde acontece a interpreta\xe7\xe3o das imagens, seguindo os arquivos gerados no treinamento da rede neural. Nele tamb\xe9m est\xe1 a fun\xe7\xe3o que mostra (opcionalmente) o resultado da infer\xeancia desenhando um ret\xe2ngulo no frame antes de retorn\xe1-lo ao c\xf3digo anterior."))}m.isMDXComponent=!0}}]);