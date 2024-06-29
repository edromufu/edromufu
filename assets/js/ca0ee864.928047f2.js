"use strict";(self.webpackChunkedrom=self.webpackChunkedrom||[]).push([[6487],{5680:(e,a,n)=>{n.d(a,{xA:()=>c,yg:()=>d});var o=n(6540);function r(e,a,n){return a in e?Object.defineProperty(e,a,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[a]=n,e}function s(e,a){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);a&&(o=o.filter((function(a){return Object.getOwnPropertyDescriptor(e,a).enumerable}))),n.push.apply(n,o)}return n}function t(e){for(var a=1;a<arguments.length;a++){var n=null!=arguments[a]?arguments[a]:{};a%2?s(Object(n),!0).forEach((function(a){r(e,a,n[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):s(Object(n)).forEach((function(a){Object.defineProperty(e,a,Object.getOwnPropertyDescriptor(n,a))}))}return e}function i(e,a){if(null==e)return{};var n,o,r=function(e,a){if(null==e)return{};var n,o,r={},s=Object.keys(e);for(o=0;o<s.length;o++)n=s[o],a.indexOf(n)>=0||(r[n]=e[n]);return r}(e,a);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(e);for(o=0;o<s.length;o++)n=s[o],a.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var l=o.createContext({}),p=function(e){var a=o.useContext(l),n=a;return e&&(n="function"==typeof e?e(a):t(t({},a),e)),n},c=function(e){var a=p(e.components);return o.createElement(l.Provider,{value:a},e.children)},m="mdxType",g={inlineCode:"code",wrapper:function(e){var a=e.children;return o.createElement(o.Fragment,{},a)}},u=o.forwardRef((function(e,a){var n=e.components,r=e.mdxType,s=e.originalType,l=e.parentName,c=i(e,["components","mdxType","originalType","parentName"]),m=p(n),u=r,d=m["".concat(l,".").concat(u)]||m[u]||g[u]||s;return n?o.createElement(d,t(t({ref:a},c),{},{components:n})):o.createElement(d,t({ref:a},c))}));function d(e,a){var n=arguments,r=a&&a.mdxType;if("string"==typeof e||r){var s=n.length,t=new Array(s);t[0]=u;var i={};for(var l in a)hasOwnProperty.call(a,l)&&(i[l]=a[l]);i.originalType=e,i[m]="string"==typeof e?e:r,t[1]=i;for(var p=2;p<s;p++)t[p]=n[p];return o.createElement.apply(null,t)}return o.createElement.apply(null,n)}u.displayName="MDXCreateElement"},2624:(e,a,n)=>{n.r(a),n.d(a,{assets:()=>l,contentTitle:()=>t,default:()=>g,frontMatter:()=>s,metadata:()=>i,toc:()=>p});var o=n(8168),r=(n(6540),n(5680));const s={id:"connecting_and_showing.py",title:"connecting_and_showing.py",desrcion:"Nesta se\xe7\xe3o teremos um explica\xe7\xe3o sobre o c\xf3digo connecting_and_showing.py",slug:"/connecting_and_showing",sidebar_position:2},t=void 0,i={unversionedId:"vision/codes/connecting_and_showing.py",id:"vision/codes/connecting_and_showing.py",title:"connecting_and_showing.py",description:"Nesta se\xe7\xe3o teremos um explica\xe7\xe3o detalhada sobre o c\xf3digo connectingandshowing.py",source:"@site/docs/vision/codes/connecting_and_showing.md",sourceDirName:"vision/codes",slug:"/connecting_and_showing",permalink:"/edromufu/docs/connecting_and_showing",draft:!1,editUrl:"https://github.com/edromufu/edromufu/tree/master/edrom-docs/docs/vision/codes/connecting_and_showing.md",tags:[],version:"current",sidebarPosition:2,frontMatter:{id:"connecting_and_showing.py",title:"connecting_and_showing.py",desrcion:"Nesta se\xe7\xe3o teremos um explica\xe7\xe3o sobre o c\xf3digo connecting_and_showing.py",slug:"/connecting_and_showing",sidebar_position:2},sidebar:"tutorialSidebar",previous:{title:"vision.launch",permalink:"/edromufu/docs/vision_launch"},next:{title:"running_inference.py",permalink:"/edromufu/docs/running_inference"}},l={},p=[{value:"init()",id:"init",level:2},{value:"Get_webcam()",id:"get_webcam",level:2},{value:"Show_result_frame()",id:"show_result_frame",level:2},{value:"Publish_result_frame()",id:"publish_result_frame",level:2},{value:"Connect_to_webots() e convert_ros_image_to_cv2()",id:"connect_to_webots-e-convert_ros_image_to_cv2",level:2},{value:"Ajuste_camera()",id:"ajuste_camera",level:2}],c={toc:p},m="wrapper";function g(e){let{components:a,...n}=e;return(0,r.yg)(m,(0,o.A)({},c,n,{components:a,mdxType:"MDXLayout"}),(0,r.yg)("p",null,"Nesta se\xe7\xe3o teremos um explica\xe7\xe3o detalhada sobre o c\xf3digo connecting_and_showing.py"),(0,r.yg)("pre",null,(0,r.yg)("code",{parentName:"pre",className:"language-py",metastring:'title="object_finder/src/connecting_and_showing.py"',title:'"object_finder/src/connecting_and_showing.py"'},"#!/usr/bin/env python3\n# coding=utf-8\n\nimport rospy\nfrom sensor_msgs.msg import Image as ROS_Image\n\nimport cv2\nfrom cv_bridge import CvBridge\nimport running_inference as ri\n\nfrom vision_msgs.msg import Ball\nfrom vision_msgs.msg import Webotsmsg\nimport sys\n\nsys.setrecursionlimit(100000)\nwidth = 416 # Largura da imagem (conferir no v\xeddeo)\nheight = 416 # Altura da imagem (Conferir no v\xeddeo)\n")),(0,r.yg)("p",null,"Nesse c\xf3digo temos algumas importa\xe7\xf5es:"),(0,r.yg)("ul",null,(0,r.yg)("li",{parentName:"ul"},(0,r.yg)("p",{parentName:"li"},(0,r.yg)("strong",{parentName:"p"},"\u201crospy\u201d")," = Biblioteca de Python para o ROS")),(0,r.yg)("li",{parentName:"ul"},(0,r.yg)("p",{parentName:"li"},(0,r.yg)("strong",{parentName:"p"},"\u201cROS_Image\u201d")," = Tipo de mensagem utilizada pelo webots, que neste caso utilizamos para receber as imagens quando o c\xf3digo \xe9 utilizado no webots")),(0,r.yg)("li",{parentName:"ul"},(0,r.yg)("p",{parentName:"li"},(0,r.yg)("strong",{parentName:"p"},"\u201ccv2\u201d")," = OpenCV, Biblioteca para trabalhar com imagens")),(0,r.yg)("li",{parentName:"ul"},(0,r.yg)("p",{parentName:"li"},(0,r.yg)("strong",{parentName:"p"},"\u201cCvBridge\u201d")," = Biblioteca que serve para converter as imagens, que neste caso utilizamos para converter as imagens recebidas pelo webots para um formato que o OpenCV trabalha")),(0,r.yg)("li",{parentName:"ul"},(0,r.yg)("p",{parentName:"li"},(0,r.yg)("strong",{parentName:"p"},"\u201crunning_inference\u201d")," = Outro c\xf3digo da vis\xe3o que ser\xe1 explicado logo em seguida")),(0,r.yg)("li",{parentName:"ul"},(0,r.yg)("p",{parentName:"li"},(0,r.yg)("strong",{parentName:"p"},"\u201cBall\u201d")," e ",(0,r.yg)("strong",{parentName:"p"},"\u201cWebotsmsg\u201d")," = Formatos de mensagem que publicamos para o Behaviour")),(0,r.yg)("li",{parentName:"ul"},(0,r.yg)("p",{parentName:"li"},(0,r.yg)("strong",{parentName:"p"},"\u201csys\u201d")," = Biblioteca sys que tem fun\xe7\xf5es de gerenciamento de arquivos"))),(0,r.yg)("p",null,"Ap\xf3s as importa\xe7\xf5es temos algumas defini\xe7\xf5es:"),(0,r.yg)("ul",null,(0,r.yg)("li",{parentName:"ul"},(0,r.yg)("p",{parentName:"li"},(0,r.yg)("strong",{parentName:"p"},"\u201csys.setrecursionLimit\u201d")," = Define a profundidade m\xe1xima da pilha do interpretador Python para o limite setado.")),(0,r.yg)("li",{parentName:"ul"},(0,r.yg)("p",{parentName:"li"},(0,r.yg)("strong",{parentName:"p"},"\u201cwidth \u201d")," e ",(0,r.yg)("strong",{parentName:"p"},"\u201cheight\u201d")," = Define a altura e a largura da imagem que ser\xe1 analisada"))),(0,r.yg)("pre",null,(0,r.yg)("code",{parentName:"pre",className:"language-py",metastring:'title="object_finder/src/connecting_and_showing.py"',title:'"object_finder/src/connecting_and_showing.py"'},"'''import cProfile, pstats, io\nfrom pstats import SortKey\npr = cProfile.Profile()\npr.enable()\n'''\n")),(0,r.yg)("pre",null,(0,r.yg)("code",{parentName:"pre",className:"language-py",metastring:'title="object_finder/src/connecting_and_showing.py"',title:'"object_finder/src/connecting_and_showing.py"'},"'''\npr.disable()\ns = io.StringIO()\nsortby = SortKey.CUMULATIVE\nps = pstats.Stats(pr, stream=s).sort_stats(sortby)\nps.print_stats()\nprint(s.getvalue())'''\n")),(0,r.yg)("p",null,"Temos tamb\xe9m em seguida, algumas fun\xe7\xf5es auxiliares que s\xe3o utilizadas para mostrar para n\xf3s, o tempo de execu\xe7\xe3o do programa e quanto tempo o programa gasta em cada fun\xe7\xe3o do c\xf3digo. Essa fun\xe7\xe3o \xe9 \xf3tima para ajudar na otimiza\xe7\xe3o do nosso c\xf3digo."),(0,r.yg)("h2",{id:"init"},"init()"),(0,r.yg)("pre",null,(0,r.yg)("code",{parentName:"pre",className:"language-py",metastring:'title="object_finder/src/connecting_and_showing.py"',title:'"object_finder/src/connecting_and_showing.py"'},"def __init__(self,nome_no):\n\n    #Iniciando o ROS\n    #Capturar parametros (qual camera e se queremos output de imagem) do launch\n    self.camera = rospy.get_param('vision/camera')\n    self.output_img = rospy.get_param('vision/img_output')\n    self.ajuste = rospy.get_param('vision/ajuste')\n    self.bright = rospy.get_param('vision/brilho')\n\n\n    #Iniciando o n\xf3 e obtendo os arquivos que definem a rede neural\n    rospy.init_node(nome_no, anonymous = True)\n    self.net = ri.get_cnn_files()\n    self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)\n    self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)   \n    self.model = ri.set_model_input(self.net)\n    self.searching = True\n    self.cap = cv2.VideoCapture(self.camera,cv2.CAP_ANY)\n    self.cap.set(cv2.CAP_PROP_BRIGHTNESS, (self.bright))\n    self.publisher = rospy.Publisher('/webots_natasha/vision_inference', Webotsmsg, queue_size=100)\n\n    \n    #SE FOR NO REAL\n    self.get_webcam()\n\n    #SE FOR NO WEBOTS\n    #self.connect_to_webots()\n")),(0,r.yg)("p",null,"A fun\xe7\xe3o construtora da nossa classe, onde setamos e buscamos algumas informa\xe7\xf5es."),(0,r.yg)("ul",null,(0,r.yg)("li",{parentName:"ul"},(0,r.yg)("p",{parentName:"li"},(0,r.yg)("strong",{parentName:"p"},"\u201cget_param\u201d")," = Primeira coisa que fazemos \xe9 buscar as informa\xe7\xf5es fornecidas pelo nosso launch e colocar nas variaveis ",(0,r.yg)("strong",{parentName:"p"},"\u201cself.camera\u201d"),", \u201d",(0,r.yg)("strong",{parentName:"p"},"self.ouput_img\u201d"),", ",(0,r.yg)("strong",{parentName:"p"},"\u201cself.ajuste\u201d"),", ",(0,r.yg)("strong",{parentName:"p"},"\u201cself.bright\u201d"))),(0,r.yg)("li",{parentName:"ul"},(0,r.yg)("p",{parentName:"li"},(0,r.yg)("strong",{parentName:"p"},"\u201cinit_node\u201d")," = Iniciamos aqui o nosso node ",(0,r.yg)("strong",{parentName:"p"},"\u201cvision\u201d")," onde rodar\xe1 os processos")),(0,r.yg)("li",{parentName:"ul"},(0,r.yg)("p",{parentName:"li"},(0,r.yg)("strong",{parentName:"p"},"\u201cget_cnn_files\u201d")," = fun\xe7\xe3o do ",(0,r.yg)("strong",{parentName:"p"},"\u201crunning_inference.py\u201d"))),(0,r.yg)("li",{parentName:"ul"},(0,r.yg)("p",{parentName:"li"},(0,r.yg)("strong",{parentName:"p"},"\u201csetPreferableBackend\u201d")," e ",(0,r.yg)("strong",{parentName:"p"},"\u201csetPreferableTarget\u201d")," = fun\xe7\xf5es para rodarmos nosso c\xf3digo com o CUDA ativado")),(0,r.yg)("li",{parentName:"ul"},(0,r.yg)("p",{parentName:"li"},(0,r.yg)("strong",{parentName:"p"},"\u201cset_model_input\u201d")," = fun\xe7\xe3o do ",(0,r.yg)("strong",{parentName:"p"},"\u201crunning_inference.py\u201d"))),(0,r.yg)("li",{parentName:"ul"},(0,r.yg)("p",{parentName:"li"},(0,r.yg)("strong",{parentName:"p"},"\u201cself.searching\u201d")," = iniciando a nossa vari\xe1vel de procura para True, para que quando formos publicar temos a confirma\xe7\xe3o que est\xe1 rodando certo a detec\xe7\xe3o")),(0,r.yg)("li",{parentName:"ul"},(0,r.yg)("p",{parentName:"li"},(0,r.yg)("strong",{parentName:"p"},"\u201ccv2.VideoCapture\u201d")," = setamos aqui vari\xe1vel que ser\xe1 nossa c\xe2mera")),(0,r.yg)("li",{parentName:"ul"},(0,r.yg)("p",{parentName:"li"},(0,r.yg)("strong",{parentName:"p"},"\u201ccap.set\u201d")," = ajustamos o brilho da nossa camera com o valor recebido pelo launch")),(0,r.yg)("li",{parentName:"ul"},(0,r.yg)("p",{parentName:"li"},(0,r.yg)("strong",{parentName:"p"},"\u201crospy.Publisher\u201d")," = Iniciamos nosso publisher que ir\xe1 publicar os resultados da nossa detec\xe7\xe3o.")),(0,r.yg)("li",{parentName:"ul"},(0,r.yg)("p",{parentName:"li"},(0,r.yg)("strong",{parentName:"p"},"\u201cget_webcam\u201d")," e ",(0,r.yg)("strong",{parentName:"p"},"\u201cconnect_to_webots\u201d")," = come\xe7amos a rodar nossa primeira fun\xe7\xe3o dentro desse c\xf3digo. Se queremos que o c\xf3digo rode na robo real utilizamos ",(0,r.yg)("strong",{parentName:"p"},'"get_webcam()"')," e se quisermos que ele rode dentro do webots utilizamos ",(0,r.yg)("strong",{parentName:"p"},'"connect_to_webots()"'),"."))),(0,r.yg)("h2",{id:"get_webcam"},"Get_webcam()"),(0,r.yg)("pre",null,(0,r.yg)("code",{parentName:"pre",className:"language-py",metastring:'title="object_finder/src/connecting_and_showing.py"',title:'"object_finder/src/connecting_and_showing.py"'},'def get_webcam(self):\n\n    print("\\n----Vis\xe3o Operante----\\n")\n    if self.ajuste == True:\n        print("Ajuste de Brilho \'=\' para aumentar e \'-\' para diminuir.\\n")\n        print("Para continuar a detec\xe7\xe3o. Aperte W.\\n")\n\n    while True:\n        ret , self.current_frame = self.cap.read()\n        self.classes, self.scores, self.boxes, self.fps = ri.detect_model(self.model,self.current_frame)\n\n        if not ret:\n            print("Error capturing frame")\n            break\n\n        if self.output_img == True:\n            self.show_result_frame()\n\n        if self.ajuste == True:\n            self.ajuste_camera()\n\n\n        self.publish_results()\n\n        if cv2.waitKey(1) == ord("q") :\n            self.cap.release()\n            cv2.destroyAllWindows()\n')),(0,r.yg)("p",null,"A fun\xe7\xe3o ",(0,r.yg)("em",{parentName:"p"},"get_webcam")," \xe9 usada para capturar frames da webcam e usar o modelo de detec\xe7\xe3o de objetos para detectar objetos em cada frame. A fun\xe7\xe3o come\xe7a com a impress\xe3o de uma mensagem no console informando sobre a detec\xe7\xe3o de objetos na vis\xe3o operante."),(0,r.yg)("p",null,"O loop \xe9 iniciado e, dentro dele, a fun\xe7\xe3o ",(0,r.yg)("em",{parentName:"p"},"cap.read()")," \xe9 usada para capturar um frame da webcam e retornar o valor ",(0,r.yg)("em",{parentName:"p"},"ret")," que indica se a captura foi bem-sucedida ou n\xe3o. O frame capturado \xe9 armazenado na vari\xe1vel ",(0,r.yg)("em",{parentName:"p"},"self.current_frame"),"."),(0,r.yg)("p",null,"A seguir, a fun\xe7\xe3o ",(0,r.yg)("em",{parentName:"p"},"ri.detect_model")," \xe9 chamada para detectar objetos no frame capturado. O modelo \xe9 passado como primeiro argumento e o frame capturado \xe9 passado como segundo argumento. A fun\xe7\xe3o retorna quatro valores: ",(0,r.yg)("em",{parentName:"p"},"classes"),", ",(0,r.yg)("em",{parentName:"p"},"scores"),", ",(0,r.yg)("em",{parentName:"p"},"boxes")," e ",(0,r.yg)("em",{parentName:"p"},"fps"),". Esses valores s\xe3o armazenados nas respectivas vari\xe1veis de inst\xe2ncia do objeto."),(0,r.yg)("p",null,"Se a vari\xe1vel ",(0,r.yg)("em",{parentName:"p"},"self.output_img")," for ",(0,r.yg)("em",{parentName:"p"},"True"),", a fun\xe7\xe3o ",(0,r.yg)("em",{parentName:"p"},"self.show_result_frame")," \xe9 chamada para mostrar o resultado da detec\xe7\xe3o de objetos na tela. Se a vari\xe1vel ",(0,r.yg)("em",{parentName:"p"},"self.ajuste")," for ",(0,r.yg)("em",{parentName:"p"},"True"),", a fun\xe7\xe3o ",(0,r.yg)("em",{parentName:"p"},"self.ajuste_camera")," \xe9 chamada para ajustar o brilho da webcam."),(0,r.yg)("p",null,"Por fim, a fun\xe7\xe3o ",(0,r.yg)("em",{parentName:"p"},"self.publish_results")," \xe9 chamada para publicar os resultados da detec\xe7\xe3o de objetos. O loop \xe9 repetido at\xe9 que a tecla ",(0,r.yg)("strong",{parentName:"p"},'"q"')," seja pressionada, momento em que o recurso da webcam \xe9 liberado e todas as janelas do OpenCV s\xe3o destru\xeddas."),(0,r.yg)("h2",{id:"show_result_frame"},"Show_result_frame()"),(0,r.yg)("pre",null,(0,r.yg)("code",{parentName:"pre",className:"language-py",metastring:'title="object_finder/src/connecting_and_showing.py"',title:'"object_finder/src/connecting_and_showing.py"'},"def show_result_frame(self):\n    '''Mostra o resultado do frame obtido pela rede neural em um janela do OpenCV.'''\n    ri.draw_results(self.current_frame, self.classes, self.scores, self.boxes)\n    cv2.imshow(\"Current Frame\", self.current_frame)\n")),(0,r.yg)("p",null,"Fun\xe7\xe3o que manda o frame, as ",(0,r.yg)("em",{parentName:"p"},"classes"),", os ",(0,r.yg)("em",{parentName:"p"},"scores")," e as ",(0,r.yg)("em",{parentName:"p"},"boxes")," para a fun\xe7\xe3o ",(0,r.yg)("em",{parentName:"p"},"draw_results")," do c\xf3digo ",(0,r.yg)("em",{parentName:"p"},"running_inference")," e mostra o resultado na tela"),(0,r.yg)("h2",{id:"publish_result_frame"},"Publish_result_frame()"),(0,r.yg)("pre",null,(0,r.yg)("code",{parentName:"pre",className:"language-py",metastring:'title="object_finder/src/connecting_and_showing.py"',title:'"object_finder/src/connecting_and_showing.py"'},"def publish_results(self):\n\n    objects_msg = Webotsmsg()\n    objects_msg.searching = self.searching\n    objects_msg.fps = self.fps\n\n    self.list_of_classes_in_current_frame = []\n    self.dict_of_xs = dict()\n\n    for i in range(len(self.boxes)):\n        [x_top, y_top, roi_width, roi_height] = self.boxes[i]\n\n        x = int(x_top + roi_width/2)\n        y = int(y_top + roi_height/2)\n        \n        results = [True, x, y, roi_width, roi_height]\n\n        \n\n        self.dict_of_xs[i] = {\"classe\": self.classes[i], \"x\": x}\n        print(self.dict_of_xs)\n\n        if self.classes[i] not in self.list_of_classes_in_current_frame:\n            self.list_of_classes_in_current_frame.append(self.classes[i])\n\n            if self.classes[i]== 1:\n                ball = Ball()\n                [ball.found, ball.x, ball.y, ball.roi_width, ball.roi_height] = results\n                objects_msg.ball = ball\n        \n        else:\n            self.maior_x = -1\n            self.menor_x = 500\n            for key in self.dict_of_xs.keys():\n                if self.dict_of_xs[key]['classe'] != 0:\n                    if self.dict_of_xs[key]['x'] >= self.maior_x:\n                        self.maior_x = self.dict_of_xs[key]['x']\n                        self.pos_maior_x = key\n\n                    if self.dict_of_xs[key]['x'] < self.menor_x:\n                        self.menor_x = self.dict_of_xs[key]['x']\n                        self.pos_menor_x = key\n\n            if self.dict_of_xs[self.pos_maior_x]['classe'] == 2:\n                self.dict_of_xs[self.pos_menor_x]['classe'] = 1\n\n            elif self.dict_of_xs[self.pos_maior_x]['classe'] == 1:\n                self.dict_of_xs[self.pos_maior_x]['classe'] = 2\n\n\n            print(\"Detectei duas iguais!\")\n            print(self.dict_of_xs)\n            \n    self.publisher.publish(objects_msg)\n")),(0,r.yg)("p",null,'Esta fun\xe7\xe3o itera sobre a lista de caixas de objetos detectados, armazenados em "self.boxes", e calcula a posi\xe7\xe3o x e y de cada objeto como o ponto central da caixa de ROI (regi\xe3o de interesse). Al\xe9m disso, a fun\xe7\xe3o armazena a classe de cada objeto detectado em "self.classes" em um dicion\xe1rio "self.dict_of_xs" com a classe como a chave e as posi\xe7\xf5es x e y como valores.'),(0,r.yg)("p",null,"Se a classe de um objeto n\xe3o estiver presente na lista de classes ",(0,r.yg)("strong",{parentName:"p"},'"self.list_of_classes_in_current_frame"'),", ela \xe9 adicionada a esta lista e, se a classe for ",(0,r.yg)("em",{parentName:"p"},'"1"'),", os resultados s\xe3o usados para preencher um objeto da classe ",(0,r.yg)("strong",{parentName:"p"},'"Ball"'),"."),(0,r.yg)("p",null,"Se houver duas classes iguais na lista de classes ",(0,r.yg)("strong",{parentName:"p"},'"self.list_of_classes_in_current_frame"'),", a fun\xe7\xe3o determina as posi\xe7\xf5es x mais alta e mais baixa e, em seguida, altera as classes dos objetos nessas posi\xe7\xf5es."),(0,r.yg)("p",null,"Finalmente, o objeto ",(0,r.yg)("strong",{parentName:"p"},'"objects_msg"')," \xe9 publicado usando um objeto publisher ",(0,r.yg)("strong",{parentName:"p"},'"self.publisher"'),"."),(0,r.yg)("h2",{id:"connect_to_webots-e-convert_ros_image_to_cv2"},"Connect_to_webots() e convert_ros_image_to_cv2()"),(0,r.yg)("pre",null,(0,r.yg)("code",{parentName:"pre",className:"language-py",metastring:'title="object_finder/src/connecting_and_showing.py"',title:'"object_finder/src/connecting_and_showing.py"'},"def connect_to_webots(self):\n\n    '''Pega o topico da vis\xe3o que est\xe1 sendo enviado da vis\xe3o e se inscreve nele.'''\n    self.topic_found = False\n    while self.topic_found == False:\n        try:\n            for sublist in rospy.get_published_topics(namespace = \"/\"):\n                for item in sublist:\n                    if \"vision_controller\" in item:\n                        self.vision_topic = item\n\n            rospy.Subscriber(self.vision_topic, ROS_Image, callback = self.convert_ros_image_to_cv2)\n            self.topic_found = True\n            rospy.spin()\n        except Exception:\n            pass\ndef convert_ros_image_to_cv2(self, message):\n\n    '''Converte de sensor_msgs/Image para um Numpy Array.'''\n    self.opencv_bridge = CvBridge()\n    \n    try:\n        self.current_frame = self.opencv_bridge.imgmsg_to_cv2(message, desired_encoding=\"bgr8\")\n    \n    except Exception as e:\n        print(f\"{e}\")\n\n    self.send_current_frame_to_inference()\n")),(0,r.yg)("p",null,"A primeira fun\xe7\xe3o, ",(0,r.yg)("strong",{parentName:"p"},'"connect_to_webots()"'),", \xe9 usada para se conectar ao t\xf3pico ",(0,r.yg)("em",{parentName:"p"},'"vision_controller"')," publicado pelo behaviour que pega do Webots (um simulador para rob\xf4s) e se inscreve nele. A fun\xe7\xe3o faz um loop enquanto a vari\xe1vel de inst\xe2ncia ",(0,r.yg)("em",{parentName:"p"},'"topic_found"')," for falsa. Dentro do loop, a fun\xe7\xe3o usa o m\xe9todo ",(0,r.yg)("em",{parentName:"p"},"rospy.get_published_topics()"),' para obter uma lista de t\xf3picos publicados no namespace "/". Em seguida, percorre a lista procurando por "vision_controller" e armazena o nome do t\xf3pico encontrado na vari\xe1vel de inst\xe2ncia "vision_topic". Em seguida, se inscreve no t\xf3pico usando o ',(0,r.yg)("em",{parentName:"p"},"rospy.Subscriber()"),' e passando o nome do t\xf3pico e a fun\xe7\xe3o "callback" para ser chamada quando novos dados s\xe3o publicados no t\xf3pico. '),(0,r.yg)("p",null,"A segunda fun\xe7\xe3o, ",(0,r.yg)("strong",{parentName:"p"},'"convert_ros_image_to_cv2()"'),', \xe9 usada para converter a imagem publicada no t\xf3pico "vision_controller" para um formato que o OpenCV possa ler. Ela \xe9 passada como "callback" para o ',(0,r.yg)("em",{parentName:"p"},"rospy.Subscriber()")," na primeira fun\xe7\xe3o. A fun\xe7\xe3o usa a classe ",(0,r.yg)("em",{parentName:"p"},"CvBridge()")," da biblioteca roscpp_opencv para fazer a convers\xe3o e armazena"),(0,r.yg)("h2",{id:"ajuste_camera"},"Ajuste_camera()"),(0,r.yg)("pre",null,(0,r.yg)("code",{parentName:"pre",className:"language-py",metastring:'title="object_finder/src/connecting_and_showing.py"',title:'"object_finder/src/connecting_and_showing.py"'},'def ajuste_camera(self):\n    \n    while cv2.waitKey(1) != ord("w"):\n        \n        if cv2.waitKey(1) == ord(\'=\'):\n            self.bright = self.bright + 10\n            if self.cap.get(cv2.CAP_PROP_BRIGHTNESS) < 64:\n                self.cap.set(cv2.CAP_PROP_BRIGHTNESS, (self.bright))\n            else:\n                self.bright = 64                \n            print("Brightness property current value:", self.cap.get(cv2.CAP_PROP_BRIGHTNESS))\n\n        if cv2.waitKey(1) == ord(\'-\'):\n            self.bright = self.bright - 10\n            if self.cap.get(cv2.CAP_PROP_BRIGHTNESS) > -64:\n                self.cap.set(cv2.CAP_PROP_BRIGHTNESS, (self.bright))\n            else:\n                self.bright = -64     \n            print("Brightness property current value:", self.cap.get(cv2.CAP_PROP_BRIGHTNESS))\n\n        #Atualizar Frame\n        _ , self.current_frame = self.cap.read()\n        cv2.imshow("Current Frame", self.current_frame)\n    self.ajuste = False\n')),(0,r.yg)("p",null,"Esta fun\xe7\xe3o ajusta as configura\xe7\xf5es de brilho de uma c\xe2mera usando o OpenCV. Enquanto o usu\xe1rio n\xe3o pressionar a tecla ",(0,r.yg)("strong",{parentName:"p"},'"w"'),", o loop ir\xe1 continuar verificando se o usu\xe1rio pressionou as teclas ",(0,r.yg)("strong",{parentName:"p"},'"+"')," ou ",(0,r.yg)("strong",{parentName:"p"},'"-"'),". Se o usu\xe1rio pressionar ",(0,r.yg)("strong",{parentName:"p"},'"+"'),", o brilho da c\xe2mera ser\xe1 aumentado em 10 e, se o valor de brilho for menor que 64, o brilho ser\xe1 ajustado. Caso contr\xe1rio, o valor de brilho ser\xe1 mantido em 64. O mesmo processo \xe9 seguido quando o usu\xe1rio pressiona ",(0,r.yg)("strong",{parentName:"p"},'"-"'),", mas neste caso o brilho \xe9 diminu\xeddo em 10. A cada itera\xe7\xe3o do loop, a fun\xe7\xe3o tamb\xe9m atualiza o frame da c\xe2mera e mostra a imagem atual. Quando o usu\xe1rio pressiona ",(0,r.yg)("strong",{parentName:"p"},'"w"'),", a fun\xe7\xe3o sai do loop e define a vari\xe1vel de inst\xe2ncia ",(0,r.yg)("em",{parentName:"p"},'"ajuste"')," como falso."))}g.isMDXComponent=!0}}]);