"use strict";(self.webpackChunkedrom=self.webpackChunkedrom||[]).push([[9901],{3905:(e,o,t)=>{t.d(o,{Zo:()=>c,kt:()=>f});var n=t(7294);function a(e,o,t){return o in e?Object.defineProperty(e,o,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[o]=t,e}function r(e,o){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);o&&(n=n.filter((function(o){return Object.getOwnPropertyDescriptor(e,o).enumerable}))),t.push.apply(t,n)}return t}function i(e){for(var o=1;o<arguments.length;o++){var t=null!=arguments[o]?arguments[o]:{};o%2?r(Object(t),!0).forEach((function(o){a(e,o,t[o])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):r(Object(t)).forEach((function(o){Object.defineProperty(e,o,Object.getOwnPropertyDescriptor(t,o))}))}return e}function s(e,o){if(null==e)return{};var t,n,a=function(e,o){if(null==e)return{};var t,n,a={},r=Object.keys(e);for(n=0;n<r.length;n++)t=r[n],o.indexOf(t)>=0||(a[t]=e[t]);return a}(e,o);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);for(n=0;n<r.length;n++)t=r[n],o.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(a[t]=e[t])}return a}var u=n.createContext({}),l=function(e){var o=n.useContext(u),t=o;return e&&(t="function"==typeof e?e(o):i(i({},o),e)),t},c=function(e){var o=l(e.components);return n.createElement(u.Provider,{value:o},e.children)},m="mdxType",p={inlineCode:"code",wrapper:function(e){var o=e.children;return n.createElement(n.Fragment,{},o)}},d=n.forwardRef((function(e,o){var t=e.components,a=e.mdxType,r=e.originalType,u=e.parentName,c=s(e,["components","mdxType","originalType","parentName"]),m=l(t),d=a,f=m["".concat(u,".").concat(d)]||m[d]||p[d]||r;return t?n.createElement(f,i(i({ref:o},c),{},{components:t})):n.createElement(f,i({ref:o},c))}));function f(e,o){var t=arguments,a=o&&o.mdxType;if("string"==typeof e||a){var r=t.length,i=new Array(r);i[0]=d;var s={};for(var u in o)hasOwnProperty.call(o,u)&&(s[u]=o[u]);s.originalType=e,s[m]="string"==typeof e?e:a,i[1]=s;for(var l=2;l<r;l++)i[l]=t[l];return n.createElement.apply(null,i)}return n.createElement.apply(null,t)}d.displayName="MDXCreateElement"},1406:(e,o,t)=>{t.r(o),t.d(o,{assets:()=>u,contentTitle:()=>i,default:()=>p,frontMatter:()=>r,metadata:()=>s,toc:()=>l});var n=t(7462),a=(t(7294),t(3905));const r={id:"vision.launch",title:"vision.launch",description:"Nesta se\xe7\xe3o teremos um explica\xe7\xe3o sobre o c\xf3digo vision.launch",slug:"vision/codes/vision_launch",sidebar_position:1},i=void 0,s={unversionedId:"Vis\xe3o/Codes/vision.launch",id:"Vis\xe3o/Codes/vision.launch",title:"vision.launch",description:"Nesta se\xe7\xe3o teremos um explica\xe7\xe3o sobre o c\xf3digo vision.launch",source:"@site/docs/Vis\xe3o/Codes/vision_launch.md",sourceDirName:"Vis\xe3o/Codes",slug:"/Vis\xe3o/Codes/vision/codes/vision_launch",permalink:"/edromufu/docs/Vis\xe3o/Codes/vision/codes/vision_launch",draft:!1,editUrl:"https://github.com/edromufu/edromufu/tree/master/edrom-docs/docs/Vis\xe3o/Codes/vision_launch.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{id:"vision.launch",title:"vision.launch",description:"Nesta se\xe7\xe3o teremos um explica\xe7\xe3o sobre o c\xf3digo vision.launch",slug:"vision/codes/vision_launch",sidebar_position:1},sidebar:"tutorialSidebar",previous:{title:"C\xf3digos de detec\xe7\xe3o",permalink:"/edromufu/docs/category/c\xf3digos-de-detec\xe7\xe3o"},next:{title:"connecting_and_showing.py",permalink:"/edromufu/docs/Vis\xe3o/Codes/vision/codes/connecting_and_showing"}},u={},l=[],c={toc:l},m="wrapper";function p(e){let{components:o,...t}=e;return(0,a.kt)(m,(0,n.Z)({},c,t,{components:o,mdxType:"MDXLayout"}),(0,a.kt)("p",null,"Nesta se\xe7\xe3o teremos um explica\xe7\xe3o detalhada sobre o c\xf3digo vision.launch"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-jsx",metastring:'title="object_finder/launch/vision.launch"',title:'"object_finder/launch/vision.launch"'},'<launch>\n\n    <arg name="camera" default="0"/>\n    <arg name="img_output" default="false"/>\n    <arg name="ajuste" default="false"/>\n    <arg name="brilho" default="4"/>\n    \n    \x3c!-- Vis\xe3o --\x3e\n    <node name="vision" pkg="object_finder" type="connecting_and_showing.py" output="log" > \n        <param name="camera" value="$(eval arg(\'camera\'))" />\n        <param name="img_output" value="$(eval arg(\'img_output\'))" />\n        <param name="ajuste" value="$(eval arg(\'ajuste\'))" />\n        <param name="brilho" value="$(eval arg(\'brilho\'))" />\n    </node>\n\n</launch>\n')),(0,a.kt)("p",null,"No launch da vis\xe3o temos 4 tipos de argumentos que s\xe3o passados:"),(0,a.kt)("ol",null,(0,a.kt)("li",{parentName:"ol"},(0,a.kt)("p",{parentName:"li"},(0,a.kt)("strong",{parentName:"p"},"camera")," que ir\xe1 receber qual \xe9 a c\xe2mera que ser\xe1 utilizada, normalmente temos 0 para computadores que s\xf3 tem uma c\xe2mera, por exemplo a da rob\xf4, ou utilizamos 2 quando estamos fazendo testes em um notebook que possui a webcam integrada dele. Tendo como DEFAULT 0.")),(0,a.kt)("li",{parentName:"ol"},(0,a.kt)("p",{parentName:"li"},(0,a.kt)("strong",{parentName:"p"},"img_output")," que ir\xe1 receber um booleano (true ou false), se for true teremos um retorno visual com uma tela mostrando o que a rob\xf4 est\xe1 vendo e false n\xe3o teremos essa tela. Tendo como DEFAULT ",(0,a.kt)("em",{parentName:"p"},"false"),".")),(0,a.kt)("li",{parentName:"ol"},(0,a.kt)("p",{parentName:"li"},(0,a.kt)("strong",{parentName:"p"},"ajuste")," que ir\xe1 receber um booleano (true ou false), se for true entrar\xe1 no modo de ajuste de brilho da c\xe2mera. Seguir\xe1 o seguinte padr\xe3o: \u201c = \u201d para aumentar, \u201c - \u201d para diminuir e \u201c W \u201d para continuar para a detec\xe7\xe3o. Tendo como DEFAULT ",(0,a.kt)("em",{parentName:"p"},"false"),".")),(0,a.kt)("li",{parentName:"ol"},(0,a.kt)("p",{parentName:"li"},(0,a.kt)("strong",{parentName:"p"},"brilho")," que ir\xe1 receber um n\xfamero de \u201364 at\xe9 64, esse n\xfamero ser\xe1 utilizado como fator de brilho da c\xe2mera, sendo 64 o maior brilho poss\xedvel e por consequ\xeancia \u201364 o menor. Tendo como DEFAULT 4."))),(0,a.kt)("p",null,"E nesse Node o arquivo que ser\xe1 executado \xe9 o ",(0,a.kt)("strong",{parentName:"p"},"\u201cconnecting_and_showing.py\u201d")," que utilizar\xe1 todos esses par\xe2metros para realizar a detec\xe7\xe3o."),(0,a.kt)("admonition",{title:"Argumentos",type:"tip"},(0,a.kt)("p",{parentName:"admonition"},"Para um melhor entendimento de como utilizar os argumentos, visite a pagina de comandos da vis\xe3o. ")))}p.isMDXComponent=!0}}]);