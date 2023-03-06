#!/bin/bash
source ./env/bin/activate
pkill -9 python

python3 ./rabbitmq/FileUService/main.py &
python3 ./grpc/FileUService/main.py &
python3 ./apigateway/app.py &
