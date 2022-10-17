FROM python:3.9-slim as base

RUN apt-get update -yqq && apt-get install -y \
    git unzip libsndfile-dev

RUN git clone https://github.com/mussakhojayeva/espnet2onnx_demo.git

#ARG USERNAME
#ARG USER_ID
#ARG GROUP_ID
#ARG PROJECT_PATH
#
#RUN mkdir -p ${PROJECT_PATH} &&\
#    groupadd -g ${GROUP_ID} ${USERNAME} &&\
#    useradd --create-home --shell /bin/bash ${USERNAME}  \
#    --gid ${GROUP_ID} --uid ${USER_ID} --home-dir ${HOME} &&\
#    install --directory --mode=0755 --owner=${USERNAME} --group=${USERNAME} ${HOME} &&\
#    chown --changes --silent --no-dereference --recursive \
#    ${USER_ID}:${GROUP_ID} \
#    ${HOME}

#ARG STORAGE_PATH
#RUN ln -s ${STORAGE_PATH}/train_asr_ksc_v1 /espnet2onnx_demo/train_asr_ksc_v1

#USER $USERNAME

RUN cd /espnet2onnx_demo && \
    pip install -U pip &&\
    pip install -r requirements.txt

#ENV PATH="/root/.local/bin":$PATH

WORKDIR /espnet2onnx_demo

#### After cloning, go to espnet2onnx_demo folder. Copy the pretrained zip file in this folder, and unzip.
#### install dependencies:
#pip install -r requirements.txt
#After installing all dependencies, run: python3.9 run.py --file sample.wav