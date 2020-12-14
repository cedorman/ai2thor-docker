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

# See if there was a file passed in
arg_len = len(sys.argv)
file_name = None
if arg_len > 1:
    file_name = sys.argv[1]
    print(f"argument 1 is {file_name}")

#  -----------------------------------------
# Moved to an entirely different program
# ------------------------------------------
# # This uses code from AI2THOR Docker that creates a xorg.conf based on the
# # current GPU and then starts a headless Xorg in a new thread.
# startx()
#
# print(" Now going to sleep for 10 seconds ", flush=True)
# time.sleep(10)



directory = "/home/ced/work/mcs/eval3/mit/dev/"
# directory = "/home/ced/work/mcs/eval3/opics/mcs_eval3/unity_app/"
# directory = "/mcs/"
unity_app_file_path = directory + "MCS-AI2-THOR-Unity-App-v0.3.6.x86_64"
# config_json_file_path = "/home/ced/work/mcs/docker/ai2thor-docker-cedorman/retrieval_goal-0005.json"
config_json_file_path = "/home/ced/work/mcs/docker/ai2thor-docker-cedorman/interactive_obstacle_1_2.json"

controller = mcs.create_controller(unity_app_file_path) # , depth_masks=True, object_masks=True)

if controller is None:
    print("Controller is NONE. Problem initializaing AI2-THOR !!!")
    exit(1)

config_data, status = mcs.load_config_json_file(config_json_file_path)
output = controller.start_scene(config_data)

action = 'MoveAhead'

for x in range(0, 10):
    step_output = controller.step(action)
    # image_list = step_output.image_list
    # if len(image_list) == 1:
    #     image = image_list[0]
    #     filename = directory + "output_image_" + str(x) + ".jpg"
    #     image.save(filename)
    #     print(f"Image saved to {filename}")
    # else:
    #     print(f"Size of image list {len(image_list)}")

controller.end_scene(None)

# Produce something to send back
if file_name:
    output_filename = file_name + ".result"
    with open(output_filename, "w") as output_file:
        output_file.write("output\n")
    print(f"OUTPUT_FILE: {output_filename}")




