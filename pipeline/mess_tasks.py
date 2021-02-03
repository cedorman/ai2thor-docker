#
# Run all the tasks (in directory taskfiles/) on all the machines that we have.
#
import threading
from os import listdir, path
from os.path import isfile, join

from pipeline import logger
from pipeline import util
from pipeline.mess_config_change import MessConfigChange
from pipeline.mess_singletask import MessSingleTask
from pipeline.xserver_check import XServerCheck
from pipeline.xserver_startup import XServerStartup

# Uncomment one of the following.  The first is for testing;  the second is for _all_ tasks (14600 of them)
TASK_FILE_PATH = "/home/clark/work/mcs/eval3/tasks/passive/all"
# TASK_FILE_PATH = "/home/clark/work/mcs/ai2thor-docker-cedorman/pipeline/taskfiles/"


class MessRunTasks:

    def __init__(self):
        self.available_machines = []
        self.task_files_full_path = []

        # Main Logger
        dateStr = util.getDateInFileFormat()
        self.log = logger.configureBaseLogging(dateStr + ".log")
        self.log.info("Starting runtasks")

    def runThreadOnEC2Machine(self, machine_dns):
        """ Function that runs on its own thread, with thread-local variable of the machine to use.  While
        there are more task files to run, get one and run it, exiting the thread when there are no more tasks."""

        dateStr = util.getDateInFileFormat()
        threadlog = logger.configureLogging(machine_dns, dateStr + "." + machine_dns)

        # Lock to be able to count tasks remaining and get one in a thread-safe way.  Otherwise, we could
        # count tasks remaining and before we pop it, some other thread might pop it
        lock = threading.RLock()
        while True:
            lock.acquire()
            if len(task_files_full_path) == 0:
                lock.release()
                return
            task_file = task_files_full_path.pop(0)
            lock.release()

            singleTask = MessSingleTask(machine_dns, task_file, threadlog, None)
            return_code = singleTask.process()

            if return_code > 0:
                lock.acquire()
                self.log.warning(f"Task for file {task_file} failed.  Adding back to the queue")
                task_files_full_path.append(task_file)
                lock.release()

    def getTasks(self):
        global task_files_full_path

        # Get all the tasks files
        task_files_full_path = [path.abspath(join(TASK_FILE_PATH, f)) for f in listdir(TASK_FILE_PATH) if
                                isfile(join(TASK_FILE_PATH, f))]
        task_files_full_path.sort()
        print(f"Tasks file {task_files_full_path}")
        self.log.info(f"Number of tasks: {len(task_files_full_path)}")

    def runTasks(self):
        self.getTasks()

        # Determine the DNS for all the machine that we have, default to us-east-1 and p2.xlarge
        self.available_machines = util.getAWSMachines()
        self.log.info(f"Machines available {self.available_machines}")

        # Create a thread for each machine
        threads = []
        for machine in self.available_machines:
            processThread = threading.Thread(target=self.runThreadOnEC2Machine, args=(machine,))
            processThread.start()
            threads.append(processThread)

        # Wait for them all to finish
        for thread in threads:
            thread.join()

        self.log.info("Ending runtasks")

    def getMachines(self):
        self.available_machines = util.getAWSMachines()
        self.log.info(f"Machines available {self.available_machines}")

    def runXStartup(self):
        ''' Start X Server on all the machines.  Note:  Not parallelized'''
        for machine in self.available_machines:
            bs = XServerStartup(machine, self.log)
            bs.process()

    def kill_and_restartX(self):
        for machine in self.available_machines:
            bs = XServerStartup(machine, self.log)
            bs.kill_and_restart()

    def change_mcs_config(self):
        for machine in self.available_machines:
            bs = MessConfigChange(machine, self.log)
            bs.process()

    def runCheckXorg(self):
        ''' Check X Server on all the machines.  Note:  Not parallelized'''
        self.available_machines = util.getAWSMachines()
        self.log.info(f"Machines available {self.available_machines}")

        for machine in self.available_machines:
            bs = XServerCheck(machine, self.log)
            bs.process()


if __name__ == '__main__':
    run_tasks = MessRunTasks()
    run_tasks.getMachines()
    # run_tasks.getTasks()
    # run_tasks.change_mcs_config()
    # run_tasks.runXStartup()
    # run_tasks.runCheckXorg()
    run_tasks.runTasks()
