#
# Runs a single job on a single machine
#
import os.path

from pipeline import util


class BaselineStartup:

    def __init__(self, machine_dns, log):
        self.machine_dns = machine_dns
        self.log = log

    def process(self):

        self.log.info(f"Startup on machine {self.machine_dns}")

        # Clear out current tasks
        cmd = "\"cd ~/ai2thor-docker/ && sudo python3 run_startx.py > /dev/null 2>&1 &\""
        return_code = util.shellRunBackground(self.machine_dns, cmd, self.log)
        if return_code != 0:
            self.log.warn("Failed on starup step")
            return return_code

        return return_code
