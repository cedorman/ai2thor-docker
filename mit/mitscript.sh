#!/bin/bash

#
# Command to be run on the EC2 machine.  Can be run either manually or programmatically.  
#
# If you want to set an environment variable, suche as the config
# file to use, pass it in on the command line:
#     % MCS_CONFIG_FILE=/tmp/blah docker_run_ec2.

export MCS_CONFIG_FILE=${MCS_CONFIG_FILE:-"/mcs_config.yaml"}
echo "Config file " ${MCS_CONFIG_FILE}

set +x

docker run --rm --privileged \
       -e MCS_CONFIG_FILE_PATH=${MCS_CONFIG_FILE} \
       -v /home/ubuntu:/run \
       -v /home/ubuntu/input:/input \
       -v /home/ubuntu/debug:/debug \
       mit_with_xserver:latest \
       /run/mit_internal_script.sh


