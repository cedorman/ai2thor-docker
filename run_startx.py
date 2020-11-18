#
#
# A minimalist test for MCS.  It starts a controller, reads in a scene
# (randomly picked) and goes forward for 10 steps.   On each step,
# it saves an image 
#
#
import machine_common_sense as mcs
from ai2thor_docker.x_server import startx
import time
import sys


# This uses code from AI2THOR Docker that creates a xorg.conf based on the
# current GPU and then starts a headless Xorg in a new thread.
startx()

print(" Now going to sleep for 10 seconds ", flush=True)
time.sleep(10)

print(" Back from sleep ", flush=True)


while True:
    time.sleep(1)
