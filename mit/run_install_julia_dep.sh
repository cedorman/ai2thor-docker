#!/bin/bash

# This used to be needed because of the way thaty the docker container was set
# up by MIT, in that it chagned the SHELL command, so things didn't work right.
# this is no longer needed.

set -x 

#  This is called within the docker container 
source /opt/ros/noetic/setup.bash

cd /root/.julia/dev/GenGridSLAM
julia -e 'import Pkg; Pkg.update(); Pkg.instantiate()'

cd ../GenAgent/
julia -e 'import Pkg; Pkg.update(); Pkg.instantiate(); Pkg.add(["PyCall", "Revise", "RobotOS"]); Pkg.develop("GenGridSLAM"); Pkg.develop("GenAgent"); Pkg.build(); Pkg.API.precompile()'
