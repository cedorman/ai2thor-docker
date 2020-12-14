#!/usr/bin/env bash

set -x

cd ..

# Add --no-cache to make it start from scratch
# time docker build --no-cache -f mit/mit_with_xserver.dockerfile -t mit_with_xserver:latest .
time docker build -f mit/mit_with_xserver.dockerfile -t mit_with_xserver:latest .


# 795237661910.dkr.ecr.us-east-1.amazonaws.com/mcs-mit-eval3
# docker login --username=cedorman
# docker tag mit_with_xserver:latest cedorman/mcs-mit-eval3:latest
# docker push cedorman/mcs-mit-eval3:latest

