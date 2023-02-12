"use strict";(self.webpackChunkedrom=self.webpackChunkedrom||[]).push([[1269],{3905:(e,r,a)=>{a.d(r,{Zo:()=>p,kt:()=>f});var o=a(7294);function n(e,r,a){return r in e?Object.defineProperty(e,r,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[r]=a,e}function t(e,r){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);r&&(o=o.filter((function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable}))),a.push.apply(a,o)}return a}function s(e){for(var r=1;r<arguments.length;r++){var a=null!=arguments[r]?arguments[r]:{};r%2?t(Object(a),!0).forEach((function(r){n(e,r,a[r])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):t(Object(a)).forEach((function(r){Object.defineProperty(e,r,Object.getOwnPropertyDescriptor(a,r))}))}return e}function i(e,r){if(null==e)return{};var a,o,n=function(e,r){if(null==e)return{};var a,o,n={},t=Object.keys(e);for(o=0;o<t.length;o++)a=t[o],r.indexOf(a)>=0||(n[a]=e[a]);return n}(e,r);if(Object.getOwnPropertySymbols){var t=Object.getOwnPropertySymbols(e);for(o=0;o<t.length;o++)a=t[o],r.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(n[a]=e[a])}return n}var d=o.createContext({}),m=function(e){var r=o.useContext(d),a=r;return e&&(a="function"==typeof e?e(r):s(s({},r),e)),a},p=function(e){var r=m(e.components);return o.createElement(d.Provider,{value:r},e.children)},l="mdxType",u={inlineCode:"code",wrapper:function(e){var r=e.children;return o.createElement(o.Fragment,{},r)}},c=o.forwardRef((function(e,r){var a=e.components,n=e.mdxType,t=e.originalType,d=e.parentName,p=i(e,["components","mdxType","originalType","parentName"]),l=m(a),c=n,f=l["".concat(d,".").concat(c)]||l[c]||u[c]||t;return a?o.createElement(f,s(s({ref:r},p),{},{components:a})):o.createElement(f,s({ref:r},p))}));function f(e,r){var a=arguments,n=r&&r.mdxType;if("string"==typeof e||n){var t=a.length,s=new Array(t);s[0]=c;var i={};for(var d in r)hasOwnProperty.call(r,d)&&(i[d]=r[d]);i.originalType=e,i[l]="string"==typeof e?e:n,s[1]=i;for(var m=2;m<t;m++)s[m]=a[m];return o.createElement.apply(null,s)}return o.createElement.apply(null,a)}c.displayName="MDXCreateElement"},752:(e,r,a)=>{a.r(r),a.d(r,{assets:()=>d,contentTitle:()=>s,default:()=>u,frontMatter:()=>t,metadata:()=>i,toc:()=>m});var o=a(7462),n=(a(7294),a(3905));const t={id:"spliting_video_in_frames",title:"Dividir os v\xeddeos em frames",sidebar_position:3},s=void 0,i={unversionedId:"Vis\xe3o/Treinamento da rede neural/spliting_video_in_frames",id:"Vis\xe3o/Treinamento da rede neural/spliting_video_in_frames",title:"Dividir os v\xeddeos em frames",description:"Agora, os v\xeddeos ser\xe3o divididos em frames. Para isso, executamos o seguinte script:",source:"@site/docs/Vis\xe3o/Treinamento da rede neural/spliting_video_in_frames.md",sourceDirName:"Vis\xe3o/Treinamento da rede neural",slug:"/Vis\xe3o/Treinamento da rede neural/spliting_video_in_frames",permalink:"/edromufu/docs/Vis\xe3o/Treinamento da rede neural/spliting_video_in_frames",draft:!1,editUrl:"https://github.com/edromufu/edromufu/tree/master/edrom-docs/docs/Vis\xe3o/Treinamento da rede neural/spliting_video_in_frames.md",tags:[],version:"current",sidebarPosition:3,frontMatter:{id:"spliting_video_in_frames",title:"Dividir os v\xeddeos em frames",sidebar_position:3},sidebar:"tutorialSidebar",previous:{title:"Gravando as imagens",permalink:"/edromufu/docs/Vis\xe3o/Treinamento da rede neural/recording_from_camera"},next:{title:"Separar os frames",permalink:"/edromufu/docs/Vis\xe3o/Treinamento da rede neural/organizing_dataset"}},d={},m=[],p={toc:m},l="wrapper";function u(e){let{components:r,...a}=e;return(0,n.kt)(l,(0,o.Z)({},p,a,{components:r,mdxType:"MDXLayout"}),(0,n.kt)("p",null,"Agora, os v\xeddeos ser\xe3o divididos em frames. Para isso, executamos o seguinte script:"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-py"},'import cv2\nimport os\n\npastaVideos = "videos" # Pasta onde videos est\xe3o salvos\npastaFrames = "frames" # Pasta onde frames ser\xe3o salvos\npularFrames = 3 # A cada quantos frames um jpg ser\xe1 salvo\n\nos.chdir(pastaVideos)\nlista_de_arquivo = os.listdir(os.getcwd())\nlista_de_videos = []\nos.chdir("..")\n\nfor arquivo in lista_de_arquivo:\n    if os.path.splitext(arquivo)[1] == ".avi":\n        lista_de_videos.append(arquivo)\n\nnumero_frame=1\ncurrent_frame = 1\n\nfor video in lista_de_videos:\n\n    print (\'From...\' + video)\n    nome_do_video = pastaVideos + "/" + video\n    cap = cv2.VideoCapture(nome_do_video)\n\n    while(True):\n        ret, frame = cap.read()        \n        if ret:\n            if current_frame % pularFrames == 0:\n                name = pastaFrames + \'/frame\' + str(numero_frame) + \'.jpg\'\n                numero_frame +=1\n                print (\'Creating...\' + name)\n                cv2.imwrite(name, frame)\n            current_frame += 1\n        else: break\n    cap.release()\n')),(0,n.kt)("p",null,"A primeira parte \xe9 onde s\xe3o definidos os par\xe2metros. Modifique eles de acordo com o nome da pasta em que os videos est\xe3o, o nome da pasta em que os frames devem ser salvos, e a cada quantos frames do v\xeddeo o script salvar\xe1 um frame (utilizado para evitar frames identicos, para salvar todos os frames utilizar pularFrames = 1)."),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-py"},'pastaVideos = "videos" # Pasta onde videos est\xe3o salvos\npastaFrames = "frames" # Pasta onde frames ser\xe3o salvos\npularFrames = 3 # A cada quantos frames um jpg ser\xe1 salvo\n')),(0,n.kt)("p",null,'Em seguida, acessa a pasta dos videos e l\xea o nome de todos os arquivos para iterar sobre eles. Ent\xe3o, salva os que possuem a extens\xe3o .avi em uma lista (para evitar erros com "lixo" na pasta).'),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-py"},'os.chdir(pastaVideos)\nlista_de_arquivo = os.listdir(os.getcwd())\nlista_de_videos = []\nos.chdir("..")\n\nfor arquivo in lista_de_arquivo:\n    if os.path.splitext(arquivo)[1] == ".avi":\n        lista_de_videos.append(arquivo)\n')),(0,n.kt)("p",null,'Por fim, itera sobre todos os v\xeddeos, salvando os frames na pasta designada no formato "frame0.jpg", "frame1.jpg", ..., "frameN.jpg".'),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-py"},"numero_frame=1\ncurrent_frame = 1\n\nfor video in lista_de_videos:\n\n    print ('From...' + video)\n    nome_do_video = pastaVideos + \"/\" + video\n    cap = cv2.VideoCapture(nome_do_video)\n\n    while(True):\n        ret, frame = cap.read()        \n        if ret:\n            if current_frame % pularFrames == 0:\n                name = pastaFrames + '/frame' + str(numero_frame) + '.jpg'\n                numero_frame +=1\n                print ('Creating...' + name)\n                cv2.imwrite(name, frame)\n            current_frame += 1\n        else: break\n    cap.release()\n")),(0,n.kt)("p",null,'O resultado ser\xe1 os frames dos v\xeddeos em formato .jpg pasta designada (no c\xf3digo exemplo, o script est\xe1 no mesmo diret\xf3rio que a pasta "videos" e a "frames").'))}u.isMDXComponent=!0}}]);