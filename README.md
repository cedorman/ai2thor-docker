<p align="center">
  <img width = "50%" src='/doc/static/thor-logo-main_1.0_thick.png' />
  </p>

--------------------------------------------------------------------------------

# MCS Version of AI2-THOR Docker

The Machine Common Sense project is using code developed by the AI2-THOR project
(see https://github.com/NextCenturyCorporation/MCS and
https://github.com/NextCenturyCorporation/ai2thor).  We would like to be able to
run evaluations on many different parameters in simulations.  We are targeting
AWS Batch, which uses the Elastic Compute Service.  We need to have a docker
container that is able to run our code, extending AI2-THOR code, entirely
self-contained.

We thank the AI2-THOR project for their hard work and their generous
contribution of code.

## Building ##

On AWS, make an instance:  Deep Learning AMI (Ubuntu 18.04) Version 35.0 - ami-01aad86525617098d  with p2.xlarge

Then, create the docker container with the following commands: 

   ```
% git clone https://github.com/cedorman/ai2thor-docker.git
% cd ai2thor-docker
% ./scripts/build.sh
% ./scripts/build_mcs.sh
   ```

This will create a docker image that looks like the following: 

   ```
REPOSITORY                                                        TAG                      IMAGE ID            CREATED             SIZE
mcs-ai2thor-docker                                                latest                   876e6b8ffbc5        8 hours ago         8.52GB
   ```
   
To run it: 

   ```
ubuntu@ip-172-31-49-125:~/mcs/ai2thor-docker$ ./scripts/run.sh 
/usr/lib/python3/dist-packages/requests/__init__.py:80: RequestsDependencyWarning: urllib3 (1.25.11) or chardet (3.0.4) doesn't match a supported version!
  RequestsDependencyWarning)
Command staring x: ['Xorg', '-noreset', '+extension', 'GLX', '+extension', 'RANDR', '+extension', 'RENDER', '-config', '/tmp/tmpdsvjnhkn', ':0']

X.Org X Server 1.19.6
Release Date: 2017-12-20
X Protocol Version 11, Revision 0
Build Operating System: Linux 4.15.0-117-generic x86_64 Ubuntu
Current Operating System: Linux e03d11432ff4 5.4.0-1029-aws #30~18.04.1-Ubuntu SMP Tue Oct 20 11:09:25 UTC 2020 x86_64
Kernel command line: BOOT_IMAGE=/boot/vmlinuz-5.4.0-1029-aws root=UUID=6156ec80-9446-4eb1-95e0-9ae6b7a46187 ro console=tty1 console=ttyS0 nvme_core.io_timeout=4294967295
Build Date: 15 September 2020  07:40:51AM
xorg-server 2:1.19.6-1ubuntu4.7 (For technical support please see http://www.ubuntu.com/support)
Current version of pixman: 0.34.0
        Before reporting problems, check http://wiki.x.org
        to make sure that you have the latest version.
Markers: (--) probed, (**) from config file, (==) default setting,
        (++) from command line, (!!) notice, (II) informational,
        (WW) warning, (EE) error, (NI) not implemented, (??) unknown.
(==) Log file: "/var/log/Xorg.0.log", Time: Sat Oct 31 02:06:45 2020
(++) Using config file: "/tmp/tmpdsvjnhkn"
(==) Using system config directory "/usr/share/X11/xorg.conf.d"
Found path: /mcs/MCS-AI2-THOR-Unity-App-v0.3.1.x86_64
Mono path[0] = '/mcs/MCS-AI2-THOR-Unity-App-v0.3.1_Data/Managed'
Mono config path = '/mcs/MCS-AI2-THOR-Unity-App-v0.3.1_Data/Mono/etc'
Unable to preload the following plugins:
        ScreenSelector.so
Display 0 '0': 1024x768 (primary device).
PlayerPrefs - Creating folder: /root/.config/unity3d/CACI with the Allen Institute for Artificial Intelligence
PlayerPrefs - Creating folder: /root/.config/unity3d/CACI with the Allen Institute for Artificial Intelligence/MCS-AI2-THOR
Logging to /root/.config/unity3d/CACI with the Allen Institute for Artificial Intelligence/MCS-AI2-THOR/Player.log
Image saved to /mcs/output_image_0.jpg
Image saved to /mcs/output_image_1.jpg
Image saved to /mcs/output_image_2.jpg
Image saved to /mcs/output_image_3.jpg
Image saved to /mcs/output_image_4.jpg
Image saved to /mcs/output_image_5.jpg
Image saved to /mcs/output_image_6.jpg
Image saved to /mcs/output_image_7.jpg
Image saved to /mcs/output_image_8.jpg
Image saved to /mcs/output_image_9.jpg
```

If you look in the script file, it is simply creating the docker container and telling it to run a program called mcs_test.py

Note:  In the mcs_test.py, there is a line:   startx()  that calls the AI2-Thor code that actually starts an X server.

The following is from the original README.md




# AI2-THOR Docker

AI2-THOR Docker is a mini-framework that simplifies the task of running [AI2-THOR](https://ai2thor.allenai.org) within Docker. The primary feature this adds is configuring and running a X server to be used by Unity3d to render scenes. 

## Getting Started

To use AI2-THOR Docker you must have Docker installed on your host and a Nvidia GPU (required for 3D rendering).


1. Clone or fork this repository.

   ```bash
   git clone https://github.com/allenai/ai2thor-docker
   ```

2. Build the Docker container.

   ```
   cd ai2thor-docker
   ./scripts/build.sh
   ```

3. Run the example agent using Docker.

   ```
   ./scripts/run.sh
   ```

At this point you should see output that resembles the following: 
```
X.Org X Server 1.19.6
Release Date: 2017-12-20
X Protocol Version 11, Revision 0
Build Operating System: Linux 4.4.0-168-generic x86_64 Ubuntu
Current Operating System: Linux 6b162ce5c20d 4.15.0-62-generic #69-Ubuntu SMP Wed Sep 4 20:55:53 UTC 2019 x86_64
Kernel command line: BOOT_IMAGE=/boot/vmlinuz-4.15.0-62-generic root=UUID=0957189b-8526-4d31-b273-91e88970be46 ro quiet splash vt.handoff=1
Build Date: 14 November 2019  06:20:00PM
xorg-server 2:1.19.6-1ubuntu4.4 (For technical support please see http://www.ubuntu.com/support) 
Current version of pixman: 0.34.0
	Before reporting problems, check http://wiki.x.org
	to make sure that you have the latest version.
Markers: (--) probed, (**) from config file, (==) default setting,
	(++) from command line, (!!) notice, (II) informational,
	(WW) warning, (EE) error, (NI) not implemented, (??) unknown.
(==) Log file: "/var/log/Xorg.0.log", Time: Mon Jun 22 20:04:29 2020
(++) Using config file: "/tmp/tmpzrlxrl5r"
(==) Using system config directory "/usr/share/X11/xorg.conf.d"
Found path: /root/.ai2thor/releases/thor-Linux64-202006081330/thor-Linux64-202006081330
Mono path[0] = '/root/.ai2thor/releases/thor-Linux64-202006081330/thor-Linux64-202006081330_Data/Managed'
Mono config path = '/root/.ai2thor/releases/thor-Linux64-202006081330/thor-Linux64-202006081330_Data/MonoBleedingEdge/etc'
Unable to preload the following plugins:
	ScreenSelector.so
Display 0 '0': 1024x768 (primary device).
Display 1 '1': 1024x768 (secondary device).
Display 2 '2': 1024x768 (secondary device).
PlayerPrefs - Creating folder: /root/.config/unity3d/Allen Institute for Artificial Intelligence
PlayerPrefs - Creating folder: /root/.config/unity3d/Allen Institute for Artificial Intelligence/AI2-Thor
Logging to /root/.config/unity3d/Allen Institute for Artificial Intelligence/AI2-Thor/Player.log
Initialize return: {'cameraNearPlane': 0.1, 'cameraFarPlane': 20.0}
{'cameraHorizon': 0.0,
 'inHighFrictionArea': False,
 'isStanding': True,
 'name': 'agent',
 'position': {'x': -1.5, 'y': 0.9009982347488403, 'z': -1.5},
 'rotation': {'x': 0.0, 'y': 270.0, 'z': 0.0}}
```

## Docker

The Docker container is built with the highest version of CUDA that the host version's Nvidia driver will support.  In order to train/execute a model the code must either be explicitly copied into the container by adding an entry into the Dockerfile or by sharing a volume with your code to the container (see ./scripts/run.sh). 

## Example

The following is code for the example agent that executes a single command ```RotateRight```.  The only requirement for the Controller to run is ```startx()``` must be called in order to configure and run the Xorg server prior to constructing the Controller.

```python
from pprint import pprint
from ai2thor_docker.x_server import startx
import ai2thor.controller


if __name__ == '__main__':
    startx()
    controller = ai2thor.controller.Controller(scene='FloorPlan28')
    event = controller.step(action='RotateRight')
    pprint(event.metadata['agent'])

```

