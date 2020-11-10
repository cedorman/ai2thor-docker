#
# Runs a single job on a single machine
#
import os.path

from pipeline import util


class SingleTask:

    def __init__(self, machine_dns, json_file_name_fullpath, log):
        """  Passed a p2.xlarge machine name on AWS and a json file,
        this runs a job on AWS."""

        self.machine_dns = machine_dns
        self.json_file_name_fullpath = json_file_name_fullpath
        self.log = log

    def process(self):
        # Make sure the file exists
        if not os.path.isfile(self.json_file_name_fullpath):
            self.log.warn(f"File does not exist {self.json_file_name_fullpath}, trying to get to run on {self.machine_dns}")
            return

        # Copy the file to the machine
        return_code = util.copyFileToAWS(self.machine_dns, self.json_file_name_fullpath, self.log)
        if return_code > 0:
            self.log.warn(f"Attempted to copy file {self.json_file_name_fullpath} to {self.machine_dns} but got {return_code}")
            return

        # Run the docker command
        return_code, output_file = util.dockerRunCommand(self.machine_dns, self.json_file_name_fullpath, self.log)
        if return_code > 0:
            self.log.warn(f"Attempted to run docker command on {self.json_file_name_fullpath} " +
                          f"on machine {self.machine_dns} but got {return_code}")
            return

        # Get the output file
        # NOTE:  The current situation is that an output file is not being used.  Instead, the
        # container copies the file to S3.
        #
        # print(f"Outputfile : {output_file}")
        # if output_file is not None and len(output_file) > 0:
        #     return_code = util.copyFileFromAWS(self.machine_dns, self.output_file)
        #     if not return_code:
        #         print(f"Attempted to copy file {self.json_file_name} from {self.machine_dns} but got {return_code}")
        #         return

        return
