#!/bin/bash

# This is called within the docker container 

set -x

python3 run_startx.py

sleep 15

python3 mcs_test.py

cat /var/log/Xorg.0.log
