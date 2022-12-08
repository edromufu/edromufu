# **Instalando dependências da visão no ROS**
Para que o programa seja capaz de encontrar os objetos necessários para disputar uma partida de futebol, é necessária a instalação das seguintes dependências:

* **Repositório de modelos do tensorflow**

> Dê clone no repositório do tensorflow/models:
```
cd ~/edrom/src/vision/object_finder
git clone https://github.com/tensorflow/models.git
```
> Instalação do pip:
```
sudo apt-get install python-pip python-dev
```

> Depois, instale as dependencias do repositório:
```
sudo apt-get install protobuf-compiler python-pil python-lxml python-tk
sudo pip install Cython
sudo pip install jupyter
sudo pip install matplotlib
sudo pip install tensorflow
sudo pip install opencv-python
```

> Instale protobuf 3+:
```
sudo apt-get install autoconf autogen
cd 
git clone https://github.com/google/protobuf.git
cd protobuf
git submodule update --init --recursive
./autogen.sh
./configure
make
make check
sudo make install
sudo ldconfig
```

> Compile com protobuf:
```
cd ~/edrom/src/vision/object_finder/models/research
protoc object_detection/protos/*.proto --python_out=.
```

> Adicione o caminho para seu PYTHONPATH no arquivo .bashrc:
```
cd <CAMINHO PARA SUA PASTA models/research> && export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim && cd
```

> De source no seu .bashrc:
```
source ~/.bashrc
```

* **Bibliotecas listadas no arquivos de requirements**

> Rode o script de instalação no diretório humanoid_vision/object_finder:
```
sudo python install.py install
```
> Se você planeja treinar a rede neural, é aconselhavel instalar o [tensorflow-gpu](https://www.tensorflow.org/install/install_linux).

>Note que esses comandos instalam no ambiente do python 2.7, caso haja uma atualização do ros para versões mais recentes do python, isso será mudado.
