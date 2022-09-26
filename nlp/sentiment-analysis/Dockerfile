FROM aio-pytorch-1.11.0:1.3.0

ARG PACKAGE_DIR=/workspace
ARG DEMO_NAME=sentimental_analysis
ENV DEMO_DIR=$PACKAGE_DIR/$DEMO_NAME
ENV IS_CLOUD="1"
ENV SERVER_IP="0.0.0.0"
ENV GRADIO_SERVER_PORT="7861"

RUN apt update -y && apt install -y vim cargo ffmpeg curl 
RUN pip install -U pip setuptools scipy transformers "gradio==3.2" emoji

COPY app.py start-webapp.sh $DEMO_DIR/

WORKDIR $DEMO_DIR
