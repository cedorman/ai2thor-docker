#!/usr/bin/env bash

set -x

cd ..

time docker build -f mit/mit_with_xserver.dockerfile -t mit_with_xserver_3.7_fixed:latest .

# Instructions to push to EC2: 
# 795237661910.dkr.ecr.us-east-1.amazonaws.com/mcs-mit-eval3
# docker login --username=cedorman
# docker tag mit_with_xserver:latest cedorman/mcs-mit-eval3:latest
# docker push cedorman/mcs-mit-eval3:latest

# Instructions to push to dockerhub:
# docker login --username=cedorman
# docker tag mit_with_xserver_3.7_fixed:latest cedorman/combined_withjulia
# docker push cedorman/combined_withjulia

