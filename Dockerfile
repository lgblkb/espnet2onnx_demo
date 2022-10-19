FROM python:3.9-slim as base

RUN apt-get update -yqq && apt-get install -y \
    git unzip libsndfile-dev

ARG USERNAME
ARG USER_ID
ARG GROUP_ID
ARG PROJECT_PATH

ENV HOME="/home/${USERNAME}"

RUN mkdir -p ${PROJECT_PATH} &&\
    groupadd -g ${GROUP_ID} ${USERNAME} &&\
    useradd --create-home --shell /bin/bash ${USERNAME}  \
    --gid ${GROUP_ID} --uid ${USER_ID} --home-dir ${HOME} &&\
    install --directory --mode=0755 --owner=${USERNAME} --group=${USERNAME} ${HOME} &&\
    chown --changes --silent --no-dereference --recursive \
    ${USER_ID}:${GROUP_ID} \
    ${HOME}

# RUN git clone https://github.com/mussakhojayeva/espnet2onnx_demo.git
#ARG STORAGE_PATH
#RUN ln -s ${STORAGE_PATH}/train_asr_ksc_v1 /espnet2onnx_demo/train_asr_ksc_v1

USER $USERNAME
COPY requirements.txt .
RUN pip install -U pip &&\
    pip install -r requirements.txt
RUN pip install uvicorn
ENV PATH="$HOME/.local/bin":$PATH
WORKDIR $PROJECT_PATH


