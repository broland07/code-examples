FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt upgrade -y && apt install -y nano \
                                                htop \
                                                iftop \
                                                nload \
                                                python3 \
                                                nfs-common \
                                                git \
                                                rsync


RUN mkdir actions-runner && cd actions-runner

RUN curl -o actions-runner-linux-x64-2.299.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.299.1/actions-runner-linux-x64-2.299.1.tar.gz

RUN tar xzf ./actions-runner-linux-x64-2.299.1.tar.gz

RUN ./config.sh --url https://github.com/broland07/code-examples --token $TOKEN