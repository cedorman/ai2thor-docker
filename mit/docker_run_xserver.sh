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
           --net host --gpus all --rm mit_with_xserver_3.6:latest bash -c \
            "cd /root/.julia/dev/GenPRAM.jl/agent_experiments/ && \
            julia container_execution.jl"

#

# time docker run -it -e PYTHONIOENCODING=utf8 -e XAUTHORITY=/tmp/.docker.xauth -e DISPLAY=:1 -v /home/ced/work/mcs/docker/ai2thor-docker-cedorman/mit/input:/input -v /home/ced/work/mcs/docker/ai2thor-docker-cedorman/mit/debug:/debug -v /tmp/.X11-unix:/tmp/.X11-unix -v /tmp/.docker.xauth:/tmp/.docker.xauth --net host --gpus all --rm gen-pram-combined_3.5_patched:latest /bin/bash

# cd /root/.julia/dev/GenPRAM.jl/agent_experiments/
# julia container_execution.jl

# ----------------------------------------------------------------------

# Set correct tasks in input
#     cd input
#     cp ~/tasks/unzipped/* .
# Set correct location for output
#     edit data/mcs_config_level2.yaml  

# Run docker container: 
#   docker run -it --privileged -v /home/ubuntu/input:/input -v /home/ubuntu/debug:/debug -v /home/ubuntu/data:/data cedorman/combined_withjulia:latest /bin/bash

# Within docker container, set config to use
#    export MCS_CONFIG_FILE_PATH=/data/mcs_config_level1.yaml
#    export MCS_CONFIG_FILE_PATH=/data/mcs_config_level2.yaml
# Start X
#    cd /mcs
#    python3 run_startx.py &
# Run code:
#    cd /root/.julia/dev/GenPRAM.jl/agent_experiments/ && julia container_execution.jl


# How long to run ---------
#   2:53 utc 
#  22:17 local  23  24  1  2  3:17
#   24 minutes for 16  -->  1.5 min per task
#   for 1360 tasks -->  2010 minutes  or 33.5 hrs.   
