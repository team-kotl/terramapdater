# Terramapdater

This repository contains the source code for the Tarramapdater application.

### Create your conda environment

```shell
conda create --prefix ./tmpdtr
conda activate ./tmpdtr
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu126 # CUDA-enabled torch
conda install --file requirements.txt -c conda-forge
```
