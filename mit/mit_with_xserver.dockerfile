# FROM gen-pram-combined:latest
# FROM gen-pram-combined_3.5:latest
FROM gen-pram-combined_3.7_fixed:latest

# ------------------------------
# The base image from IBMMIT does not have all the pci and X11 stuff we need
# Add emacs becauses there is no editor
# ------------------------------
RUN apt update && apt install -y xauth xorg pciutils emacs 

# ------------------------------
# X and NVidia stuff  
# ------------------------------
# WORKDIR will create /mcs if it does not exist
WORKDIR /mcs

# Add nvidia driver and run it
ADD scripts/install_nvidia.sh /mcs
RUN NVIDIA_VERSION=450.80.02 /mcs/install_nvidia.sh

# Put our special X11 stuff in /mcs.  
ADD run_startx.py /mcs
COPY ai2thor_docker /mcs/ai2thor_docker

# Task for testing 
ADD retrieval_goal-0005.json /mcs

# ------------------------------
# Configuration
# Do not add these because they have secrets in them 
# ------------------------------
# ADD mit/mcs_config_oracle.yaml /
# ADD mit/mcs_config_level1.yaml /
# ADD mit/mcs_config_level2.yaml /
ENV MCS_CONFIG_FILE_PATH /mcs_config_level1.yaml

# ------------------------------
# Julia is using the wrong ssl libs, no idea why.  Getting error: 
# julia: symbol lookup error: /root/.julia/artifacts/e6e5f41352118bbeb44677765ebccab8c151c72a/lib/libssl.so: undefined symbol: EVP_idea_cbc, version OPENSSL_1_1_0
# So, copy from regular libs
# ------------------------------
RUN apt install -y libssl-dev && \ 
    cp /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1 /root/.julia/artifacts/e6e5f41352118bbeb44677765ebccab8c151c72a/lib/ && \ 
    cp /usr/lib/x86_64-linux-gnu/libssl.so.1.1  /root/.julia/artifacts/e6e5f41352118bbeb44677765ebccab8c151c72a/lib/

