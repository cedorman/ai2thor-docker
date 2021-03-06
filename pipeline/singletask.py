#
# Runs a single job on a single machine
#
import os.path

from pipeline import util


class SingleTask:

    def __init__(self, machine_dns, json_file_name_fullpath, log, definition):
        """  Passed a p2.xlarge machine name on AWS and a json file,
        this runs a job on AWS."""

        self.machine_dns = machine_dns
        self.json_file_name_fullpath = json_file_name_fullpath
        self.log = log
        self.taskdefinition = definition

    def process(self):
        head, tail = os.path.split(self.json_file_name_fullpath)
        self.log.info(f"---- Starting task with json file: {tail}")

        # Make sure the file exists locally
        if not os.path.isfile(self.json_file_name_fullpath):
            self.log.warn(
                f"File does not exist {self.json_file_name_fullpath}, trying to get to run on {self.machine_dns}")
            return 2

        # Copy the file to the machine; this puts it in the home directory
        return_code = util.copyFileToAWS(self.machine_dns, self.json_file_name_fullpath,
                                         self.log, self.taskdefinition.where_to_put_json)
        if return_code > 0:
            self.log.warn(
                f"Attempted to copy file {self.json_file_name_fullpath} to {self.machine_dns} but got {return_code}")
            return return_code

        # Run the docker command
        return_code, output_file = util.dockerRunCommand(self.machine_dns, self.json_file_name_fullpath,
                                                         self.taskdefinition.process_command, self.log)
        if return_code > 0:
            self.log.warn(f"Attempted to run docker command on {self.json_file_name_fullpath} " +
                          f"on machine {self.machine_dns} but got {return_code}")
            return return_code

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

        self.log.info(f"---- Ended task with json file: {tail}  Return_code: {return_code}")

        return return_code
