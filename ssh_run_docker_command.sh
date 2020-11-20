#!/bin/bash

# This is the command that is run within the pipeline to run the docker container on the
# AWS instance

set -x

# ssh -i ~/.ssh/CED_Consulting_AWS_Key_Pair.pem ubuntu@ec2-52-91-116-180.compute-1.amazonaws.com docker run --privileged -v `pwd`:/data 924969863225.dkr.ecr.us-east-1.amazonaws.com/mcs-ai2thor-docker python3 mcs_test.py /data/retrieval_goal-0005.json


# Without mapping and data file (which are not really needed)
ssh -i ~/.ssh/CED_Consulting_AWS_Key_Pair.pem ec2-user@ec2-54-174-13-122.compute-1.amazonaws.com \
  docker run --privileged 924969863225.dkr.ecr.us-east-1.amazonaws.com/mcs-ai2thor-docker \
  ./run.sh
#   python3 mcs_test.py
