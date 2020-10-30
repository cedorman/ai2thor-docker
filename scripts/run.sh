#!/bin/bash
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $DIR/../

export ROBOTHOR_BASE_DIR=`pwd`

# Inference on train split
X11_PARAMS=""
if [[ -e /tmp/.X11-unix && ! -z ${DISPLAY+x} ]]; then
  echo "Using local X11 server"
  X11_PARAMS="-e DISPLAY=$DISPLAY  -v /tmp/.X11-unix:/tmp/.X11-unix:rw"
  xhost +local:root
fi;

# docker run --privileged $X11_PARAMS -it ai2thor-docker:latest python3 example_agent.py
docker run --privileged $X11_PARAMS -it mcs-ai2thor-docker:latest python3 mcs_test.py

if [[ -e /tmp/.X11-unix && ! -z ${DISPLAY+x} ]]; then
    xhost -local:root
fi;

