"use strict";(self.webpackChunkedrom=self.webpackChunkedrom||[]).push([[5539],{5680:(e,o,r)=>{r.d(o,{xA:()=>c,yg:()=>g});var a=r(6540);function t(e,o,r){return o in e?Object.defineProperty(e,o,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[o]=r,e}function n(e,o){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);o&&(a=a.filter((function(o){return Object.getOwnPropertyDescriptor(e,o).enumerable}))),r.push.apply(r,a)}return r}function i(e){for(var o=1;o<arguments.length;o++){var r=null!=arguments[o]?arguments[o]:{};o%2?n(Object(r),!0).forEach((function(o){t(e,o,r[o])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):n(Object(r)).forEach((function(o){Object.defineProperty(e,o,Object.getOwnPropertyDescriptor(r,o))}))}return e}function s(e,o){if(null==e)return{};var r,a,t=function(e,o){if(null==e)return{};var r,a,t={},n=Object.keys(e);for(a=0;a<n.length;a++)r=n[a],o.indexOf(r)>=0||(t[r]=e[r]);return t}(e,o);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);for(a=0;a<n.length;a++)r=n[a],o.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(t[r]=e[r])}return t}var l=a.createContext({}),d=function(e){var o=a.useContext(l),r=o;return e&&(r="function"==typeof e?e(o):i(i({},o),e)),r},c=function(e){var o=d(e.components);return a.createElement(l.Provider,{value:o},e.children)},u="mdxType",p={inlineCode:"code",wrapper:function(e){var o=e.children;return a.createElement(a.Fragment,{},o)}},m=a.forwardRef((function(e,o){var r=e.components,t=e.mdxType,n=e.originalType,l=e.parentName,c=s(e,["components","mdxType","originalType","parentName"]),u=d(r),m=t,g=u["".concat(l,".").concat(m)]||u[m]||p[m]||n;return r?a.createElement(g,i(i({ref:o},c),{},{components:r})):a.createElement(g,i({ref:o},c))}));function g(e,o){var r=arguments,t=o&&o.mdxType;if("string"==typeof e||t){var n=r.length,i=new Array(n);i[0]=m;var s={};for(var l in o)hasOwnProperty.call(o,l)&&(s[l]=o[l]);s.originalType=e,s[u]="string"==typeof e?e:t,i[1]=s;for(var d=2;d<n;d++)i[d]=r[d];return a.createElement.apply(null,i)}return a.createElement.apply(null,r)}m.displayName="MDXCreateElement"},1197:(e,o,r)=>{r.r(o),r.d(o,{assets:()=>l,contentTitle:()=>i,default:()=>p,frontMatter:()=>n,metadata:()=>s,toc:()=>d});var a=r(8168),t=(r(6540),r(5680));const n={id:"treinamento_visao",title:"Trechos de c\xf3digo a serem alterados para treinar",description:"Aqui ser\xe1 descrito o que deve ser alterado no arquivo",slug:"/train_visao",sidebar_position:7},i=void 0,s={unversionedId:"vision/training/treinamento_visao",id:"vision/training/treinamento_visao",title:"Trechos de c\xf3digo a serem alterados para treinar",description:"Aqui ser\xe1 descrito o que deve ser alterado no arquivo",source:"@site/docs/vision/training/treinamento_visao.md",sourceDirName:"vision/training",slug:"/train_visao",permalink:"/edromufu/docs/train_visao",draft:!1,editUrl:"https://github.com/edromufu/edromufu/tree/master/edrom-docs/docs/vision/training/treinamento_visao.md",tags:[],version:"current",sidebarPosition:7,frontMatter:{id:"treinamento_visao",title:"Trechos de c\xf3digo a serem alterados para treinar",description:"Aqui ser\xe1 descrito o que deve ser alterado no arquivo",slug:"/train_visao",sidebar_position:7},sidebar:"tutorialSidebar",previous:{title:"Criando arquivos auxiliares",permalink:"/edromufu/docs/criando_txts_dataset"},next:{title:"El\xe9trica",permalink:"/edromufu/docs/category/el\xe9trica"}},l={},d=[],c={toc:d},u="wrapper";function p(e){let{components:o,...r}=e;return(0,t.yg)(u,(0,a.A)({},c,r,{components:o,mdxType:"MDXLayout"}),(0,t.yg)("p",null,"O arquivo a ser alterado para realizar o treinamento personalizado \xe9 o ",(0,t.yg)("a",{parentName:"p",href:"https://github.com/edromufu/edromufu/tree/master/src/vision/robocup_cnn_files"},"TrainYolov8CustomDataset.ipynb")),(0,t.yg)("p",null,"Antes de iniciar o treinamento, \xe9 importante garantir que os nomes das pastas estejam configurados corretamente no arquivo TrainYolov8 do Google Colab. Caso os nomes das pastas tenham sido alterados, os seguintes trechos devem ser ajustados:"),(0,t.yg)("pre",null,(0,t.yg)("code",{parentName:"pre",className:"language-py"},"# Conecta o Google Drive ao Google Colab\nfrom google.colab import drive\ndrive.mount('/content/gdrive')\n\n# Ajusta o diret\xf3rio raiz para o caminho correto\ncd /content/gdrive/My\\ Drive/EDROM/\n\nROOT_DIR = '/content/gdrive/My Drive/EDROM/Ball'\n\n")),(0,t.yg)("admonition",{title:"CUIDADO",type:"danger"},(0,t.yg)("p",{parentName:"admonition"},"Certifique-se de tamb\xe9m modificar o caminho no arquivo YAML para corresponder ao ROOT_DIR.")),(0,t.yg)("p",null,"Este bloco de c\xf3digo configura o diret\xf3rio onde os resultados ser\xe3o salvos durante o treinamento. O argumento 'runs_dir' \xe9 atualizado para especificar o local como sendo o diret\xf3rio atual onde o terminal est\xe1 acessando."),(0,t.yg)("pre",null,(0,t.yg)("code",{parentName:"pre",className:"language-py"},"settings.update({'runs_dir': './runs'})\n")),(0,t.yg)("p",null,"Configura\xe7\xe3o do Modelo para o Treinamento"),(0,t.yg)("p",null,"No bloco de c\xf3digo onde ocorre o treinamento, \xe9 importante manter a vari\xe1vel model de acordo com a a\xe7\xe3o pretendida."),(0,t.yg)("p",null,"Para aprimorar o treinamento, utilize:"),(0,t.yg)("pre",null,(0,t.yg)("code",{parentName:"pre",className:"language-py"},'# Carrega um modelo pr\xe9-treinado\nmodel = YOLO("/content/gdrive/MyDrive/EDROM/best.pt")\n')),(0,t.yg)("p",null,'Em que "best.pt" \xe9 o arquivo na pasta "EDROM". Certifique-se de ajustar o caminho conforme necess\xe1rio, dependendo de onde best.pt est\xe1 salvo.'),(0,t.yg)("p",null,"Para treinar do zero, utilize:"),(0,t.yg)("pre",null,(0,t.yg)("code",{parentName:"pre",className:"language-py"},'# Configura um modelo novo para treinamento do zero\nmodel = YOLO("yolov8n.yaml")\n')),(0,t.yg)("p",null,"A fun\xe7\xe3o model.train do framework Ultralytics YOLOv8 \xe9 utilizada para treinar um modelo de detec\xe7\xe3o de objetos. Em que o argumento 'data' define o caminho para o arquivo de configura\xe7\xe3o YAML que especifica onde est\xe3o os dados de treinamento e valida\xe7\xe3o. O argumento 'epochs' indica a quantidade de vezes que o modelo ver\xe1 o conjunto completo de dados durante o treinamento. Por fim, o argumento 'name' insere um nome para diferenciar cada treinamento. Esse nome ser\xe1 utilizado para criar a pasta onde os resultados ser\xe3o salvos."),(0,t.yg)("pre",null,(0,t.yg)("code",{parentName:"pre",className:"language-py"},"# Instala a biblioteca ultralytics\n!pip install ultralytics\n# Configura o local para salvar os resultados do treinamento\nresults = model.train(data=os.path.join(ROOT_DIR, \"google_colab_config.yaml\"), epochs=150, name='yolov8n-test')\n")))}p.isMDXComponent=!0}}]);