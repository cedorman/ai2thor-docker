FROM gen-pram-combined:latest

# The base image for mit does not have all the pci and X11 stuff we need
RUN apt update && apt install -y xauth xorg pciutils vim

# WORKDIR will create /mcs if it does not exist
WORKDIR /mcs

# Add nvidia driver and run it
ADD scripts/install_nvidia.sh /mcs
RUN NVIDIA_VERSION=450.80.02 /mcs/install_nvidia.sh

# Put our special X11 stuff in /mcs.  
ADD run_startx.py /mcs

# This has x_server.py in it
COPY ai2thor_docker /mcs/ai2thor_docker

# Test data and program
# ADD mcs_test.py /mcs
ADD retrieval_goal-0005.json /mcs

# This will install the julia dependencies
# ADD mit/run_install_julia_dep.sh /

# RUN chmod +x /run_install_julia_dep.sh

