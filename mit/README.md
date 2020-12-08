
# README for MIT

## Build Modified MIT

Build the MIT code as described in the MIT_Beta/GenPRAM.jl/container_hierarchy/README
with the following modifications:

- Remove the SHELL ["/bin/bash", "-c", "source ~/.bashrc"]
   command


- Replace it with

    # ----------------------------------------------------------------------
    # Environment variables as set by the ROS setup.bash
    # ----------------------------------------------------------------------
    ENV CMAKE_PREFIX_PATH=/opt/ros/noetic
    ENV LD_LIBRARY_PATH=/opt/ros/noetic/lib:/usr/lib/x86_64-linux-gnu:/usr/lib/i386-linux-gnu:/usr/local/nvidia/lib:/usr/local/nvidia/lib64
    # ENV NVIDIA_DRIVER_CAPABILITIES=graphics,compat32,utility
    # ENV NVIDIA_VISIBLE_DEVICES=all
    ENV PATH=/opt/ros/noetic/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    ENV PKG_CONFIG_PATH=/opt/ros/noetic/lib/pkgconfig
    ENV PYTHONPATH=/opt/ros/noetic/lib/python3/dist-packages
    ENV ROSLISP_PACKAGE_DIRECTORIES=
    ENV ROS_DISTRO=noetic
    ENV ROS_ETC_DIR=/opt/ros/noetic/etc/ros
    ENV ROS_MASTER_URI=http://localhost:11311
    ENV ROS_PACKAGE_PATH=/opt/ros/noetic/share
    ENV ROS_PYTHON_VERSION=3
    ENV ROS_ROOT=/opt/ros/noetic/share/ros
    ENV ROS_VERSION=1
    
    RUN python3 -m pip install rosdep

Label it gen-pram-combined2:latest (i.e. change the -t in the build.sh file)

# Build MCS Version

- Run docker_build_withjulia.sh

# Run MCS Version locally

- Make an input directory and a debug directory in whatever directory
  you are going to run from.

- Put a task json file in the input directory

- Run the script that creates the correct xauth MIT_Beta/GenPRAM.jl/reset_x_authority.sh

- Run docker_run_withjulia.sh

# Run MCS Version on EC2 manually

This will run without DISPLAY, i.e. will run with no actual user interface or window.  
Runs using run_startx.py, which starts an Xorg xserver with appropriate xorg.conf with
fake display.

- Push to dockerhub

  - docker login --username=cedorman
  - docker tag combined_withjulia:latest cedorman/combined_withjulia:latest
  - docker push cedorman/combined_withjulia:latest
  
- Start ec2 machine and image and run it

  - Deep Learning AMI (Ubuntu 18.04) Version 37.0
  - p2.xlarge machine 
  - ssh -i ~/.ssh/clarkdorman-keypair.pem ubuntu@ec2-54-237-119-122.compute-1.amazonaws.com
  - docker pull cedorman/combined_withjulia:latest
  - docker run --rm --privileged -it b93d8fd63732 /bin/bash

- In the image, start the xserver

  

