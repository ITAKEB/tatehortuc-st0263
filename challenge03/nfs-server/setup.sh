#!/bin/bash

sudo apt update

sudo apt install nfs-kernel-server

sudo mkdir /var/nfs/general

sudo chown nobody:nogroup /var/nfs/general
