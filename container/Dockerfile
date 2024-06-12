M nvidia/cuda:11.8.0-cudnn8-devel-ubuntu20.04

SHELL ["/bin/bash", "-c"]

USER root

ENV DEBIAN_FRONTEND=noninteractive

RUN /usr/bin/ls
RUN sed -i "s,# deb http://archive.canonical.com/ubuntu,deb http://archive.canonical.com/ubuntu,g" /etc/apt/sources.list

## Install some deps
#RUN ls /etc/apt/
RUN apt-get update -y
RUN apt-get update -y && apt-get upgrade -y

RUN apt-get install -y build-essential \
    && apt-get install -y wget  && apt-get clean

RUN apt-get install -y python3.8 python3-pip
RUN python3 --version
RUN python3 -m pip install --upgrade pip

# Install vim to make Kenneth happy
RUN apt-get install vim -y

# packages for pointcept
RUN python3 -m pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
RUN python3 -m pip install open3d

RUN python3 -m pip install yapf==0.40.1
RUN python3 -m pip install h5py pyyaml sharedarray tensorboard tensorboardx addict einops scipy plyfile termcolor timm
RUN python3 -m pip install spconv-cu118

# Packages for our model
RUN python3 -m pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
RUN python3 -m pip install torch_geometric
RUN python3 -m pip install torch-cluster torch-scatter torch-sparse  -f https://data.pyg.org/whl/torch-2.1.0+cu118.html
RUN python3 -m pip install open3d
RUN python3 -m pip install dgl -f https://data.dgl.ai/wheels/cu118/repo.html
RUN python3 -m pip install dglgo -f https://data.dgl.ai/wheels-test/repo.html
RUN python3 -m pip install wandb

RUN apt-get install -y git
RUN pwd
RUN mkdir -p /opt/pointcept
RUN cd /opt/pointcept && git clone https://github.com/Pointcept/Pointcept

RUN cd  /opt/pointcept/Pointcept/libs/pointops && TORCH_CUDA_ARCH_LIST="7.5 8.0" python3  setup.py install

RUN mkdir /opt/pepr
RUN cd /opt/pepr && git clone https://github.com/cms-pepr/pytorch_cmspepr.git
rUN cd /opt/pepr/pytorch_cmspepr && FORCE_CUDA=1 TORCH_CUDA_ARCH_LIST="7.5 8.0" python3 -m pip install -e .

