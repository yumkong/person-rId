#0424 export PATH=/usr/local/cuda/bin:$PATH export PATH=/usr/local/cudnn5.1/include:$PATH export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH export LD_LIBRARY_PATH=/usr/local/cudnn5.1/lib64:$LD_LIBRARY_PATH

%0512 this computer can only install 0.10: export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.10.0-cp27-none-linux_x86_64.whl pip install --upgrade $TF_BINARY_URL

check keras version: print(keras.version)

% want tensorflow (keras) to print less $ TF_CPP_MIN_LOG_LEVEL=1 python
