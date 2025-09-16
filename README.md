# Terramapdater

This repository contains the source code for the Tarramapdater application.

## PLEASE USE PYTHON 3.11

### Environment and Dependency Setup

```shell
conda create --prefix ./tmpdtr python=3.11
conda activate ./tmpdtr
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu126 # CUDA-enabled torch
pip install segmentation-models-pytorch albumentations pyqt6
conda install -c conda-forge --file requirements.txt
conda install -c bioconda patchify
```
