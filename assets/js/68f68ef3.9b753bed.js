"use strict";(self.webpackChunkedrom=self.webpackChunkedrom||[]).push([[1587],{3905:(e,o,r)=>{r.d(o,{Zo:()=>m,kt:()=>f});var t=r(7294);function n(e,o,r){return o in e?Object.defineProperty(e,o,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[o]=r,e}function s(e,o){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var t=Object.getOwnPropertySymbols(e);o&&(t=t.filter((function(o){return Object.getOwnPropertyDescriptor(e,o).enumerable}))),r.push.apply(r,t)}return r}function a(e){for(var o=1;o<arguments.length;o++){var r=null!=arguments[o]?arguments[o]:{};o%2?s(Object(r),!0).forEach((function(o){n(e,o,r[o])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):s(Object(r)).forEach((function(o){Object.defineProperty(e,o,Object.getOwnPropertyDescriptor(r,o))}))}return e}function u(e,o){if(null==e)return{};var r,t,n=function(e,o){if(null==e)return{};var r,t,n={},s=Object.keys(e);for(t=0;t<s.length;t++)r=s[t],o.indexOf(r)>=0||(n[r]=e[r]);return n}(e,o);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(e);for(t=0;t<s.length;t++)r=s[t],o.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(n[r]=e[r])}return n}var i=t.createContext({}),c=function(e){var o=t.useContext(i),r=o;return e&&(r="function"==typeof e?e(o):a(a({},o),e)),r},m=function(e){var o=c(e.components);return t.createElement(i.Provider,{value:o},e.children)},d="mdxType",l={inlineCode:"code",wrapper:function(e){var o=e.children;return t.createElement(t.Fragment,{},o)}},p=t.forwardRef((function(e,o){var r=e.components,n=e.mdxType,s=e.originalType,i=e.parentName,m=u(e,["components","mdxType","originalType","parentName"]),d=c(r),p=n,f=d["".concat(i,".").concat(p)]||d[p]||l[p]||s;return r?t.createElement(f,a(a({ref:o},m),{},{components:r})):t.createElement(f,a({ref:o},m))}));function f(e,o){var r=arguments,n=o&&o.mdxType;if("string"==typeof e||n){var s=r.length,a=new Array(s);a[0]=p;var u={};for(var i in o)hasOwnProperty.call(o,i)&&(u[i]=o[i]);u.originalType=e,u[d]="string"==typeof e?e:n,a[1]=u;for(var c=2;c<s;c++)a[c]=r[c];return t.createElement.apply(null,a)}return t.createElement.apply(null,r)}p.displayName="MDXCreateElement"},1225:(e,o,r)=>{r.r(o),r.d(o,{assets:()=>i,contentTitle:()=>a,default:()=>l,frontMatter:()=>s,metadata:()=>u,toc:()=>c});var t=r(7462),n=(r(7294),r(3905));const s={id:"motores_estrutura",title:"Conhecendo os motores",description:"Breve abordagem sobre os motores que s\xe3o usados nas rob\xf4s",slug:"/motores_estrutura",sidebar_position:2},a=void 0,u={unversionedId:"structure/Conhecendo os motores/motores_estrutura",id:"structure/Conhecendo os motores/motores_estrutura",title:"Conhecendo os motores",description:"Breve abordagem sobre os motores que s\xe3o usados nas rob\xf4s",source:"@site/docs/structure/Conhecendo os motores/motores_estrutura.md",sourceDirName:"structure/Conhecendo os motores",slug:"/motores_estrutura",permalink:"/edromufu/docs/motores_estrutura",draft:!1,editUrl:"https://github.com/edromufu/edromufu/tree/master/edrom-docs/docs/structure/Conhecendo os motores/motores_estrutura.md",tags:[],version:"current",sidebarPosition:2,frontMatter:{id:"motores_estrutura",title:"Conhecendo os motores",description:"Breve abordagem sobre os motores que s\xe3o usados nas rob\xf4s",slug:"/motores_estrutura",sidebar_position:2},sidebar:"tutorialSidebar",previous:{title:"Como montar uma rob\xf4 da EDROM",permalink:"/edromufu/docs/montagem-robo"},next:{title:"Outras \xc1reas - coming soon",permalink:"/edromufu/docs/category/outras-\xe1reas---coming-soon"}},i={},c=[{value:"Apresenta\xe7\xe3o dos motores",id:"apresenta\xe7\xe3o-dos-motores",level:3},{value:"AX-12A",id:"ax-12a",level:3},{value:"MX-64",id:"mx-64",level:3},{value:"MX-106",id:"mx-106",level:3}],m={toc:c},d="wrapper";function l(e){let{components:o,...s}=e;return(0,n.kt)(d,(0,t.Z)({},m,s,{components:o,mdxType:"MDXLayout"}),(0,n.kt)("h3",{id:"apresenta\xe7\xe3o-dos-motores"},"Apresenta\xe7\xe3o dos motores"),(0,n.kt)("p",null,"A EDROM utiliza nas suas rob\xf4s tr\xeas tipos de motores: AX-12A, MX-64 e MX-106. Todos\ns\xe3o da dynamixel entretanto h\xe1 diferen\xe7as entre eles, uma delas \xe9 o tamanho de cada um, sendo o AX-12A o menor, o MX-106 o maior e o MX-64 que \xe9 maior que o AX-12A e menor que o MX-106. Importante salientar que o peso de cada um est\xe1 diretamente associado ao seu tamanho, ou seja, quando maior mais pesado \xe9 o motor."),(0,n.kt)("div",{align:"center"},(0,n.kt)("p",null,(0,n.kt)("img",{alt:"img",src:r(8040).Z,width:"1475",height:"827"}),"  ")),(0,n.kt)("h3",{id:"ax-12a"},"AX-12A"),(0,n.kt)("h3",{id:"mx-64"},"MX-64"),(0,n.kt)("h3",{id:"mx-106"},"MX-106"))}l.isMDXComponent=!0},8040:(e,o,r)=>{r.d(o,{Z:()=>t});const t=r.p+"assets/images/motoresAXeMX-7713457c5ecbe0ccecaff7c0ffa8e9b0.jpeg"}}]);