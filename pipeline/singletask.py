#
# Runs a single job on a single machine.  Must be extended by derived classes
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
        raise NotImplementedError
