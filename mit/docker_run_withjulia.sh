#!/usr/bin/env bash

set +x
DIR=`pwd`
export GEN_INPUT_PATH_INTERACTION=${DIR}/input
export GEN_AGENT_DEBUG_OUTPUT_PATH=${DIR}/debug
export PRAM_PROJECT_DIR=${DIR}

# Could map project over container to develop:           -v "${PRAM_PROJECT_DIR}":/root/.julia/dev \
# Could alternatively use . /opt/ros/noetic/setup.bash && source ~/.bashrc &&
docker run -it -e PYTHONIOENCODING=utf8 -e XAUTHORITY=/tmp/.docker.xauth -e DISPLAY=:1 \
           -v "${GEN_INPUT_PATH_INTERACTION}":/input \
           -v "${GEN_AGENT_DEBUG_OUTPUT_PATH}":/debug \
           -v /tmp/.X11-unix:/tmp/.X11-unix \
           -v /tmp/.docker.xauth:/tmp/.docker.xauth \
           --net host --gpus all --rm combined_postinstall2:latest bash -c \
            "source /opt/ros/noetic/setup.bash && \
            cd /root/.julia/dev/GenPRAM.jl/agent_experiments/ && \
            julia container_execution.jl"
