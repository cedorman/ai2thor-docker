#!/bin/bash

set -x 

#  This is called within the docker container 
source /opt/ros/noetic/setup.bash

cd /root/.julia/dev/GenGridSLAM
julia -e 'import Pkg; Pkg.update(); Pkg.instantiate()'

cd ../GenAgent/
julia -e 'import Pkg; Pkg.update(); Pkg.instantiate(); Pkg.add(["PyCall", "Revise", "RobotOS"]); Pkg.develop("GenGridSLAM"); Pkg.develop("GenAgent"); Pkg.build(); Pkg.API.precompile()'
