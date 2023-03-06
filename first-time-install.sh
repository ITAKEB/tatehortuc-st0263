#!/bin/bash
sudo apt update
sudo apt install -y python3-pip

sudo apt-get install rabbitmq-server
sudo systemctl start rabbitmq-server
sudo systemctl enable rabbitmq-server

apt install python3.10-venv
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
deactivate