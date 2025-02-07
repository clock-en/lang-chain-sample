FROM python:3.13.2-slim-bullseye
WORKDIR /workspace
COPY requirements.txt .
RUN apt update && apt install -y vim git \
    && echo "source /usr/share/bash-completion/completions/git" >> ~/.bashrc \
    && pip install --no-cache-dir -r requirements.txt
COPY . /workspace
