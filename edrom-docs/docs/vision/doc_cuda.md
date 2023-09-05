---
id: cuda_cudnn
title: Instalação CUDA e cuDNN
description: Nesta seção serão listados as etapas para instalação do CUDA e suas dependências
slug: /cuda-cudnn
sidebar_position: 2
---

Nesta seção você encontrará o passo a passo detalhado para a instalação do CUDA e suas dependências.

:::tip Para começar

Conferir se possui os drivers gráficos da nvidia instalados (versão 520+ recomendável)

:::


## Instalando CUDA Toolkit

Executando os comandos abaixo no terminal seguindo a ordem listada, permitirá a instalação do CUDA Toolkit através de um arquivo .deb (será necessária a criação de uma senha):  

```jsx
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/12.0.0/local_installers/cuda-repo-ubuntu2004-12-0-local_12.0.0-525.60.13-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2004-12-0-local_12.0.0-525.60.13-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2004-12-0-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update

sudo apt-get -y install cuda
export PATH=/usr/local/cuda-12.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-12.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```

Para o bloco abaixo, caso o output da primeira linha for igual a imagem, não é necessário executar a ultima linha.

```jsx
sudo nvidia-smi -pm 1
```

![im](/img/IM.jpeg)

Para checar a versão do driver NVIDIA, execute:
```jsx
cat /proc/driver/nvidia/version
```

## Instalando cuDNN
Para prosseguir com esta etapa, é necessário se cadastrar no [site da NVIDIA](https://developer.nvidia.com/cudnn) caso não tenha uma conta ao clicar em "Download cuDNN". Feito isso, baixar os 3 arquivos abaixo:

[cuDNN Runtime Library for Ubuntu20.04 x86_64 (Deb)](https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/libcudnn8_8.8.0.121-1+cuda12.0_amd64.deb)

[cuDNN Developer Library for Ubuntu20.04 x86_64 (Deb)](https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/libcudnn8-dev_8.8.0.121-1+cuda12.0_amd64.deb)


Com isso, você deve ter os seguintes arquivos .deb:

1. libcudnn8-dev_8.8.0.121-1+cuda12.0_amd64.deb

2. libcudnn8_8.8.0.121-1+cuda12.0_amd64.deb

Entrar na pasta em q os pacotes foram instalados (ex: cd Downloads) e instalar usando: 
```jsx
sudo dpkg -i  libcudnn8_8.8.0.121-1+cuda12.0_amd64.deb
sudo dpkg -i libcudnn8-dev_8.8.0.121-1+cuda12.0_amd64.deb
```

Agora, é preciso testar se está havendo a comunicação entre o cuDNN e os drivers da NVIDIA:
```jsx
nvidia-smi
```

Caso retorne um erro de falha na comunicação, uma possivel correção é executar a linha abaixo. Será necessário a criação de uma senha e reinicialização do sistema antes de tentar rodar o "nvidia-smi" novamente.
```jsx
sudo mokutil --disable-validation
```

Caso ainda não tenha dado certo, provavelmente os drivers de vídeo nao foram devidamente instalados:

 abrir "Programas e atualizações" -> drivers adicionais -> NVIDIA Corporation e selecionar o driver mais recente **QUE NAO SEJA OPEN KERNEL**

Por fim, caso tenha dado certo, o terminal retornará algo do tipo:

![Output NVIDIA SMI](/img/output_nvidia-smi.jpeg)


## Instalando dependências do OpenCV e DNN GPU

```jsx
cd
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential cmake unzip pkg-config
sudo apt-get install libopenblas-dev libatlas-base-dev liblapack-dev gfortran
sudo apt-get install gcc-7 g++-7 -y
sudo ln -s /usr/bin/gcc-7 /usr/bin/gcc
sudo ln -s /usr/bin/g++-7 /usr/bin/g++
sudo ln -s /usr/bin/gcc-7 /usr/bin/cc
sudo ln -s /usr/bin/g++-7 /usr/bin/c++
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install libv4l-dev libxvidcore-dev libx264-dev
sudo apt-get install libgtk-3-dev
sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install python3-dev
```

## Baixando OpenCV configurando para rodar com NVIDIA GPU
```jsx
cd ~
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.6.0.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.6.0.zip
unzip opencv.zip
unzip opencv_contrib.zip
mv opencv-4.6.0 opencv
mv opencv_contrib-4.6.0 opencv_contrib
```

## Determinando a versão da arquitetura do CUDA
Usar o comando "nvidia-smi" se nao souber qual a arquiterura da sua placa de video

Entrar no [site](https://developer.nvidia.com/cuda-gpus) para encontrar sua placa e ver qual versão (Compute Capability) está relacionada a ela. Salvar esse número pois será usado posteriormente.

![Arquitetura do CUDA](/img/cuda_arch.jpeg)

## Configurando OpenCV com suporte para GPU NVIDIA
Entrar no ambiente virtual se não estiver mais (workon opencv_cuda)

```jsx
cd ~/opencv
mkdir build    
cd build
```

:::danger CUIDADO

Ao dar o comando do bloco abaixo, em "-D CUDA_ARCH_BIN=7.0 \" substituir 7.0 pela versão compatível com a sua placa descoberta nos passos anteriores

:::

```jsx
cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D INSTALL_C_EXAMPLES=OFF \
	-D OPENCV_ENABLE_NONFREE=ON \
	-D WITH_CUDA=ON \
	-D WITH_CUDNN=ON \
	-D OPENCV_DNN_CUDA=ON \
	-D ENABLE_FAST_MATH=1 \
	-D CUDA_FAST_MATH=1 \
	-D CUDA_ARCH_BIN=7.0 \
	-D WITH_CUBLAS=1 \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	-D HAVE_opencv_python3=ON \
	-D PYTHON_EXECUTABLE=~/.virtualenvs/opencv_cuda/bin/python \
	-D BUILD_EXAMPLES=ON ..
```

Caso o NVIDIA CUDA e cuDNN tiverem com "NO" na frente (nos lugares onde está com YES) executar o próximo bloco de comando:

![CUDA E CNN NO](/img/cuda_cudnn_NO.jpeg)

```jsx
sudo apt install nvidia-cuda-toolkit
```

Para compilar o OpenCV com suporte para DNN GPU:

```jsx
make -j8 
```

OBS: substituir o 8 pela quantidade de núcleos que tiver seu computador.

Se der erro nos 3% por conta do gcc, executar os seguintes comandos:

```jsx
sudo apt remove gcc
sudo apt-get install gcc-7 g++-7 -y
sudo ln -s /usr/bin/gcc-7 /usr/bin/gcc
sudo ln -s /usr/bin/g++-7 /usr/bin/g++
sudo ln -s /usr/bin/gcc-7 /usr/bin/cc
sudo ln -s /usr/bin/g++-7 /usr/bin/c++
```
E teste com:
```jsx
gcc --version
```
Para ter certeza que está usando a versão 7

## Instalando OpenCV com suporte para DNN GPU

```jsx
sudo make install
sudo ldconfig
ls -l /usr/local/lib/python3.8/site-packages/cv2/python-3.8
cd ~/.virtualenvs/opencv_cuda/lib/python3.8/site-packages/
ln -s /usr/local/lib/python3.8/site-packages/cv2/python-3.8/cv2.cpython-38-x86_64-linux-gnu.so cv2.so
```

OBS: conferir os paths e se versão do python do código é a mesma utilizada no projeto.
