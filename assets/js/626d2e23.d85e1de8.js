"use strict";(self.webpackChunkedrom=self.webpackChunkedrom||[]).push([[2760],{3905:(e,a,t)=>{t.d(a,{Zo:()=>l,kt:()=>f});var o=t(7294);function r(e,a,t){return a in e?Object.defineProperty(e,a,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[a]=t,e}function i(e,a){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);a&&(o=o.filter((function(a){return Object.getOwnPropertyDescriptor(e,a).enumerable}))),t.push.apply(t,o)}return t}function s(e){for(var a=1;a<arguments.length;a++){var t=null!=arguments[a]?arguments[a]:{};a%2?i(Object(t),!0).forEach((function(a){r(e,a,t[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):i(Object(t)).forEach((function(a){Object.defineProperty(e,a,Object.getOwnPropertyDescriptor(t,a))}))}return e}function n(e,a){if(null==e)return{};var t,o,r=function(e,a){if(null==e)return{};var t,o,r={},i=Object.keys(e);for(o=0;o<i.length;o++)t=i[o],a.indexOf(t)>=0||(r[t]=e[t]);return r}(e,a);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(o=0;o<i.length;o++)t=i[o],a.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(r[t]=e[t])}return r}var d=o.createContext({}),c=function(e){var a=o.useContext(d),t=a;return e&&(t="function"==typeof e?e(a):s(s({},a),e)),t},l=function(e){var a=c(e.components);return o.createElement(d.Provider,{value:a},e.children)},p="mdxType",u={inlineCode:"code",wrapper:function(e){var a=e.children;return o.createElement(o.Fragment,{},a)}},m=o.forwardRef((function(e,a){var t=e.components,r=e.mdxType,i=e.originalType,d=e.parentName,l=n(e,["components","mdxType","originalType","parentName"]),p=c(t),m=r,f=p["".concat(d,".").concat(m)]||p[m]||u[m]||i;return t?o.createElement(f,s(s({ref:a},l),{},{components:t})):o.createElement(f,s({ref:a},l))}));function f(e,a){var t=arguments,r=a&&a.mdxType;if("string"==typeof e||r){var i=t.length,s=new Array(i);s[0]=m;var n={};for(var d in a)hasOwnProperty.call(a,d)&&(n[d]=a[d]);n.originalType=e,n[p]="string"==typeof e?e:r,s[1]=n;for(var c=2;c<i;c++)s[c]=t[c];return o.createElement.apply(null,s)}return o.createElement.apply(null,t)}m.displayName="MDXCreateElement"},5181:(e,a,t)=>{t.r(a),t.d(a,{assets:()=>d,contentTitle:()=>s,default:()=>u,frontMatter:()=>i,metadata:()=>n,toc:()=>c});var o=t(7462),r=(t(7294),t(3905));const i={id:"kicad",title:"KICAD",description:"Nesta se\xe7\xe3o ser\xe3o listados as utilidades do software kicad dentro do segmento da el\xe9trica",slug:"/kicad",sidebar_position:1},s=void 0,n={unversionedId:"eletrics/Placas de circuito impresso/kicad",id:"eletrics/Placas de circuito impresso/kicad",title:"KICAD",description:"Nesta se\xe7\xe3o ser\xe3o listados as utilidades do software kicad dentro do segmento da el\xe9trica",source:"@site/docs/eletrics/Placas de circuito impresso/KICAD.md",sourceDirName:"eletrics/Placas de circuito impresso",slug:"/kicad",permalink:"/edromufu/docs/kicad",draft:!1,editUrl:"https://github.com/edromufu/edromufu/tree/master/edrom-docs/docs/eletrics/Placas de circuito impresso/KICAD.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{id:"kicad",title:"KICAD",description:"Nesta se\xe7\xe3o ser\xe3o listados as utilidades do software kicad dentro do segmento da el\xe9trica",slug:"/kicad",sidebar_position:1},sidebar:"tutorialSidebar",previous:{title:"Cabos dos motores (TTL)",permalink:"/edromufu/docs/cabo_ttl"},next:{title:"Confec\xe7\xe3o de Placas de Circuito",permalink:"/edromufu/docs/confeccao"}},d={},c=[{value:"Instala\xe7\xe3o do KICAD",id:"instala\xe7\xe3o-do-kicad",level:2},{value:"Funcionalidades",id:"funcionalidades",level:2},{value:"Editor de Esquem\xe1tico",id:"editor-de-esquem\xe1tico",level:3},{value:"Editor de PCI",id:"editor-de-pci",level:3}],l={toc:c},p="wrapper";function u(e){let{components:a,...i}=e;return(0,r.kt)(p,(0,o.Z)({},l,i,{components:a,mdxType:"MDXLayout"}),(0,r.kt)("p",null,"O KICAD \xe9 um software que tem por objetivo facilitar a concep\xe7\xe3o de layouts e suas convers\xf5es para placas de circuito impresso."),(0,r.kt)("h2",{id:"instala\xe7\xe3o-do-kicad"},"Instala\xe7\xe3o do KICAD"),(0,r.kt)("p",null,"O software \xe9 de simples instala\xe7\xe3o atrav\xe9s do link: ",(0,r.kt)("a",{parentName:"p",href:"https://www.kicad.org/download/"},"https://www.kicad.org/download/")),(0,r.kt)("h2",{id:"funcionalidades"},"Funcionalidades"),(0,r.kt)("p",null,"O KICAD \xe9 basicamente dividido em duas interfaces principais: o ",(0,r.kt)("strong",{parentName:"p"},"editor de esquem\xe1tico"),", que oferece uma gama de ferramentas de f\xe1cil utiliza\xe7\xe3o para a confec\xe7\xe3o de esquemas eletr\xf4nicos; e o ",(0,r.kt)("strong",{parentName:"p"},"editor da PCI"),", que permite a cria\xe7\xe3o e visualiza\xe7\xe3o 3D de layouts de placas de circuito impresso."),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"im",src:t(6137).Z,width:"1920",height:"1020"})),(0,r.kt)("h3",{id:"editor-de-esquem\xe1tico"},"Editor de Esquem\xe1tico"),(0,r.kt)("p",null,"O editor de esquem\xe1tico \xe9 o local onde \xe9 feita toda a organiza\xe7\xe3o l\xf3gica do seu curcuito, \xe9 o ambiente onde \xe9 poss\xedvel criar, adicionar e nomear cada um dos componentes eletr\xf4nicos que se desejar adicionar. Ainda, \xe9 poss\xedvel realizar a atribui\xe7\xe3o de ",(0,r.kt)("em",{parentName:"p"},"footprints")," a fim de especificar cada componente para a pr\xf3xima etapa de organiza\xe7\xe3o da PCI."),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"im",src:t(4189).Z,width:"1363",height:"718"})),(0,r.kt)("h3",{id:"editor-de-pci"},"Editor de PCI"),(0,r.kt)("p",null,"No editor de PCI \xe9 feita a organiza\xe7\xe3o dos componentes adicionados no esquem\xe1tico dentro de um ambiente dividido em ",(0,r.kt)("em",{parentName:"p"},"layers"),". Essas ",(0,r.kt)("em",{parentName:"p"},"layers"),', ou camadas, s\xe3o as ferramentas que o software utiliza para especificar cada uma das opera\xe7\xf5es, por exemplo, existem as layers de "',(0,r.kt)("em",{parentName:"p"},"F. Cu"),'" e "',(0,r.kt)("em",{parentName:"p"},"B. Cu"),'" que remetem, respectivamente, as trilhas na parte da superior e inferior da placa; existe tambem a layer "',(0,r.kt)("em",{parentName:"p"},"Edge Cuts"),'", respons\xe1vel por definir os limites f\xedsicos da placa.'),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"im",src:t(7313).Z,width:"1365",height:"717"})),(0,r.kt)("p",null,'Ainda, \xe9 poss\xedvel visualizar um modelo 3D da sua placa ao utilizar o comando "Alt+3" nesse ambiente.'),(0,r.kt)("p",null,"Por fim, e para utiliza\xe7\xe3o do design modelado em uma placa real, o software permite a cria\xe7\xe3o de um arquivo Gerber, que por sua vez armazena as informa\xe7\xf5es das ",(0,r.kt)("em",{parentName:"p"},"layers")," e posi\xe7\xe3o de cada componente."),(0,r.kt)("admonition",{title:"Observa\xe7\xe3o",type:"tip"},(0,r.kt)("p",{parentName:"admonition"},"Para um tutorial em detalhes sobre o KICAD, recomendamos o ",(0,r.kt)("a",{parentName:"p",href:"https://www.youtube.com/watch?v=fcb3zco_BrQ"},"v\xeddeo")," introdut\xf3rio do professor Marcelo Barros (FEELT - UFU)")))}u.isMDXComponent=!0},6137:(e,a,t)=>{t.d(a,{Z:()=>o});const o=t.p+"assets/images/figura1-f84d987ad6abc7ff0396ed84fbf2d177.png"},4189:(e,a,t)=>{t.d(a,{Z:()=>o});const o=t.p+"assets/images/figura2-63a29cf1fb77588ef27c46d18658109f.png"},7313:(e,a,t)=>{t.d(a,{Z:()=>o});const o=t.p+"assets/images/figura3-db71a3e34fb1b3027951e7f956fbfd72.png"}}]);