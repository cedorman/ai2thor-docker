#!/usr/bin/env bash

# Script to be run by hand on a local machine.  Note that you need to run xauth first

set +x
DIR=`pwd`
export GEN_INPUT_PATH_INTERACTION=${DIR}/input
export GEN_AGENT_DEBUG_OUTPUT_PATH=${DIR}/debug
export PRAM_PROJECT_DIR=${DIR}

time docker run --rm -e PYTHONIOENCODING=utf8 -e XAUTHORITY=/tmp/.docker.xauth -e DISPLAY=:1 \
           -v "${GEN_INPUT_PATH_INTERACTION}":/input \
           -v "${GEN_AGENT_DEBUG_OUTPUT_PATH}":/debug \
           -v /tmp/.X11-unix:/tmp/.X11-unix \
           -v /tmp/.docker.xauth:/tmp/.docker.xauth \
           --net host --gpus all --rm combined_withjulia:latest bash -c \
            "cd /root/.julia/dev/GenPRAM.jl/agent_experiments/ && \
            julia container_execution.jl"


# time docker run -it -e PYTHONIOENCODING=utf8 -e XAUTHORITY=/tmp/.docker.xauth -e DISPLAY=:1 -v /home/ced/work/mcs/docker/ai2thor-docker-cedorman/mit/input:/input -v /home/ced/work/mcs/docker/ai2thor-docker-cedorman/mit/debug:/debug -v /tmp/.X11-unix:/tmp/.X11-unix -v /tmp/.docker.xauth:/tmp/.docker.xauth --net host --gpus all --rm combined_withjulia:latest /bin/bash

#             cd /root/.julia/dev/GenPRAM.jl/agent_experiments/
#            julia container_execution.jl"
