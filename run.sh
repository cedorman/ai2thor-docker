#!/bin/bash

set -x

python3 mcs_test.py

cat /var/log/Xorg.0.log
