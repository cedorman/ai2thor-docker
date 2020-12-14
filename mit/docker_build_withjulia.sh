#!/usr/bin/env bash

set -x

cd ..

# Add --no-cache to make it start from scratch
# docker build --no-cache --progress plain -f mit/combined_withjulia.dockerfile -t combined_withjulia:latest .

time docker build -f mit/combined_withjulia.dockerfile -t combined_withjulia:latest .


# 795237661910.dkr.ecr.us-east-1.amazonaws.com/mcs-mit-eval3
# docker login --username=cedorman
# docker tag combined_withjulia:latest cedorman/combined_withjulia:latest
# docker push cedorman/combined_withjulia:latest
