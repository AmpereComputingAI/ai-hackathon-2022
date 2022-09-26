#!/bin/bash

if [[ $IS_CLOUD = "1" ]]
then
	export GRADIO_SERVER_NAME="0.0.0.0"
	server_ip=`curl -s https://ipinfo.io/ip`
else
	export GRADIO_SERVER_NAME=$SERVER_IP
	server_ip=$SERVER_IP
fi
#echo "Server IP: $server_ip"

pattern='local[[:space:]]URL'
log="out_webapp.log"

cd $DEMO_DIR/

python -u app.py >& $log &

echo -en "\nGetting Webapp URL ."
until grep $pattern $log > /dev/null; do sleep 1; echo -n "."; done
sleep 1
echo -en "\nWebapp URL: "

#grep $pattern $log | sed -e 's/Running on local URL:  //' -e "s/localhost/$server_ip/"
url=`grep $pattern $log`
url=`grep $pattern $log | sed -e 's/Running on local URL:  //'`
if [[ $IS_CLOUD = "1" ]]
then
	url=`echo $url | sed "s/localhost/$server_ip/"`
fi
echo $url
echo

cd - &> /dev/null
