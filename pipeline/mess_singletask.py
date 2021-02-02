#
# Runs a single job on a single machine
#
import os.path

from pipeline import util
from pipeline.singletask import SingleTask


class MessSingleTask(SingleTask):

    def process(self):
        head, tail = os.path.split(self.json_file_name_fullpath)
        self.log.info(f"---- Starting task with json file: {tail}")

        all_tasks_dir = "/home/ubuntu/tasks/passive/all"
        current_tasks_dir = "/home/ubuntu/mess_original_code/mess_final/tasks"

        # Clear out current tasks
        cmd = "rm -f " + current_tasks_dir + "* || true"
        return_code = util.shellRunCommand(self.machine_dns, cmd, self.log)
        if return_code != 0:
            self.log.warn("Failed on rm old tasks step")
            return return_code

        # Copy the file from task dir to current task dir
        cmd = "cp " + all_tasks_dir + tail + " " + current_tasks_dir
        return_code = util.shellRunCommand(self.machine_dns, cmd, self.log)
        if return_code != 0:
            self.log.warn("Failed on cp new tasks step")
            return return_code

        # Run the command
        cmd = "conda activate myenv && cd /home/ubuntu/mess_original_code/mess_final && ./runall.sh"
        return_code = util.shellRunCommand(self.machine_dns, cmd, self.log)
        if return_code != 0:
            self.log.warn("Failed on run step")
            return return_code

        self.log.info(f"---- Ended task with json file: {tail}  Return_code: {return_code}")
        return return_code
