#
# Run all the tasks (in directory taskfiles/) on all the machines that we have.
#
import threading
from os import listdir, path
from os.path import isfile, join

from pipeline import util
from pipeline.singletask import SingleTask

TASK_FILE_PATH = "./taskfiles/"

# Task files is a list of all the tasks that need to be done.  Note that it is global and shared by threads.
task_files = []


def runThreadOnMachine(machine_dns):
    """ Function that runs on its own thread, with thread-local variable of the machine to use.  While
    there are more task files to run, get one and run it, exiting the thread when there are no more tasks."""

    # Lock to be able to count tasks remaining and get one in a thread-safe way.  Otherwise, we could
    # count tasks remaining and before we pop it, some other thread might pop it
    lock = threading.RLock()
    while True:
        lock.acquire()
        if len(task_files) == 0:
            lock.release()
            return
        task_file = task_files.pop()
        lock.release()

        singleTask = SingleTask(machine_dns, task_file)
        singleTask.process()


class RunTasks:

    def __init__(self):
        self.available_machines = []

    def runTasks(self):
        global task_files

        # Determine the DNS for all the machine that we have
        self.available_machines = util.getAllMachines()

        # Get all the tasks files
        task_files = [path.abspath(join(TASK_FILE_PATH, f)) for f in listdir(TASK_FILE_PATH) if
                      isfile(join(TASK_FILE_PATH, f))]

        # Create a thread for each machine
        threads = []
        for machine in self.available_machines:
            processThread = threading.Thread(target=runThreadOnMachine, args=(machine,))
            processThread.start()
            threads.append(processThread)

        # Wait for them all to finish
        for thread in threads:
            thread.join()


if __name__ == '__main__':
    run_tasks = RunTasks()
    run_tasks.runTasks()
