#
# Runs a single job on a single machine
#
import os.path

from pipeline import util


class RunJob:

    def __init__(self, machine_dns, json_file_name):
        """  Passed a p2.xlarge machine name on AWS and a json file,
        this runs a job on AWS."""

        self.machine_dns = machine_dns
        self.json_file_name = json_file_name

    def process(self):
        # Make sure the file exists
        if not os.path.isfile(self.json_file_name):
            print(f"File does not exist {self.json_file_name}, trying to get to run on {self.machine_dns}")
            return

        # Copy the file to the machine
        success = util.copyFileToAWS(self.machine_dns, self.json_file_name)
        if not success:
            print(f"Attempted to copy file {self.json_file_name} to {self.machine_dns} but got {success}")
            return

        # Run the docker command
        success = util.dockerRunCommand(self.machine_dns, self.json_file_name)
        if not success:
            print(
                f"Attempted to run docker command on {self.json_file_name} on machine {self.machine_dns} but got {success}")
            return

        return
