#!/bin/bash

# Command to be run in the container on the EC2 machine.  Does not change. 

cd /mcs

python3 run_startx.py &

sleep 10

cd /root/.julia/dev/GenPRAM.jl/agent_experiments/

julia container_execution.jl


