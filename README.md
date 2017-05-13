0513: This is a clone from the following repo link

# Implementation-CVPR2015-CNN-for-ReID

Implementation for CVPR 2015 Paper: "An Improved Deep Learning Architecture for Person Re-Identification".

[`Paper link`](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Ahmed_An_Improved_Deep_2015_CVPR_paper.pdf)

This architechture is implemented based on `Keras` with `Tensorflow` backen using `Python` Programming Language.

## Train the model on which dataset?

1. [`Market-1501`](https://github.com/Deep-Learning-Person-Re-Identification/Implementaion-1/tree/master/market1501)

2. [`CUHK-03`](https://github.com/Deep-Learning-Person-Re-Identification/Implementaion-1/tree/master/CUHK03)

## The model structure

![](https://github.com/Deep-Learning-Person-Re-Identification/Implementaion-1/blob/master/model.png)


#0424
export PATH=/usr/local/cuda/bin:$PATH
export PATH=/usr/local/cudnn5.1/include:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/cudnn5.1/lib64:$LD_LIBRARY_PATH


%0512 this computer can only install 0.10:
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.10.0-cp27-none-linux_x86_64.whl
pip install --upgrade $TF_BINARY_URL

check keras version:  print(keras.__version__)


% want tensorflow (keras) to print less
$ TF_CPP_MIN_LOG_LEVEL=1 python



