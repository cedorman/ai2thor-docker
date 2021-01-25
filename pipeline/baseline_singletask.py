#
# Runs a single job on a single machine
#
import os.path

from pipeline import util


class BaselineSingleTask:

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

        all_tasks_dir = "/home/ubuntu/tasks/unzipped/"
        current_tasks_dir = "/home/ubuntu/baseline/tasks/"

        # Clear out current tasks
        cmd = "rm -f " + current_tasks_dir + "* || true"
        return_code = util.shellRunCommand(self.machine_dns, cmd, self.log)
        if return_code != 0:
            self.log.warn("Failed on rm old tasks step")
            return return_code

        # Copy the file from /home/ubuntu/tasks/unzipped to /home/ubuntu/baseline/tasks
        cmd = "cp " + all_tasks_dir + tail + " " + current_tasks_dir
        return_code = util.shellRunCommand(self.machine_dns, cmd, self.log)
        if return_code != 0:
            self.log.warn("Failed on cp new tasks step")
            return return_code

        # Run the command
        cmd = "source activate pytorch_latest_p37 && cd /home/ubuntu/baseline && ./runall.sh"
        return_code = util.shellRunCommand(self.machine_dns, cmd, self.log)
        if return_code != 0:
            self.log.warn("Failed on run step")
            return return_code

        self.log.info(f"---- Ended task with json file: {tail}  Return_code: {return_code}")
        return return_code
