#!/bin/bash

# Following environments variables are supported
IS_CLOUD="1"
SERVER_IP="0.0.0.0"
GRADIO_SERVER_PORT="7860"

repo="ghcr.io/amperecomputingai"
cont_name="sentiment-analysis-pt-aio-demo"
tag="hackathon-2022"
echo "Starting $cont_name container"

docker run \
  -it --init --rm -d \
  --privileged=true \
  --env "IS_CLOUD=$IS_CLOUD" \
  --env "GRADIO_SERVER_PORT=$GRADIO_SERVER_PORT" \
  --env "JUPYTER_PORT=$JUPYTER_PORT" \
  --env "SERVER_IP=$SERVER_IP" \
  --network host \
  --ipc host \
  --name $cont_name \
  --entrypoint /bin/bash \
  "$repo/$cont_name":$tag >& /dev/null

cont_id=`docker ps | grep $cont_name | awk '{print $1}'`
echo "Docker container ID:$cont_id"

# Starting the Webapp and Jupyter notebook
#docker exec $cont_id ./start-webapp.sh
#docker exec $cont_id ./start-notebook.sh
docker exec -it $cont_id bash
