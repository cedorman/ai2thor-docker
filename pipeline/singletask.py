#
# Runs a single job on a single machine
#
import os.path

from pipeline import util


class SingleTask:

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
        return_code = util.copyFileToAWS(self.machine_dns, self.json_file_name)
        if return_code > 0:
            print(f"Attempted to copy file {self.json_file_name} to {self.machine_dns} but got {return_code}")
            return

        # Run the docker command
        return_code, output_file = util.dockerRunCommand(self.machine_dns, self.json_file_name)
        if return_code > 0:
            print(f"Attempted to run docker command on {self.json_file_name} " +
                  f"on machine {self.machine_dns} but got {return_code}")
            return

        # Get the output file
        if output_file is not None and len(output_file) > 0:
            return_code = util.copyFileFromAWS(self.machine_dns, self.output_file)
            if not return_code:
                print(f"Attempted to copy file {self.json_file_name} from {self.machine_dns} but got {return_code}")
                return

        return
