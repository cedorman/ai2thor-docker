#!/bin/bash

# This is called within the docker container 

set -x

echo "Starting the x server" 
python3 run_startx.py &

echo "Starting sleep" 
sleep 15

echo "Starting program" 
python3 mcs_test.py

cat /var/log/Xorg.0.log
