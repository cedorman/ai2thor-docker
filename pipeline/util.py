#
#  Utilities, in particular AWS things
#
# NOTE:   Please set your ssh config to allow ssh commands without having accept the fingerprint.
# To do that, add the following command to your ~/.ssh/config:     StrictHostKeyChecking accept-new
#
# See:  https://unix.stackexchange.com/questions/33271/how-to-avoid-ssh-asking-permission
#
import subprocess

from pipeline.secrets import Secrets

PEM_FILE = Secrets['PEM_FILE']
DOCKER_IMAGE = Secrets['DOCKER_IMAGE']
MACHINE_DNSes = Secrets['MACHINE_DNSes']

MACHINE_TYPE = "p2.xlarge"


def getAllMachines():
    """ Look on AWS and determine all the machines that we have running AWS that we can use.
    The assumption is that we are looking for machines of type MACHINE_TYPE """

    # TODO:  Make the AWS command line call to get the machines
    machines = MACHINE_DNSes
    return machines


def getRemoteUser(machine_dns):
    """ The name of the remote user depends on the type of machine that is running.  """
    return f"ubuntu@{machine_dns}"


def runCommandAndCaptureOutput(commandList):
    process = subprocess.Popen(commandList,
                               stdout=subprocess.PIPE,
                               universal_newlines=True)

    output_file = None

    while True:
        output = process.stdout.readline()
        stripped = output.strip()
        if len(stripped) > 0:
            print("Output: ", stripped)
        output_file_index = stripped.find("OUTPUT_FILE:")
        if output_file_index > 0:
            split_stripped = stripped.split(" ")
            if len(split_stripped) > 1:
                output_file = split_stripped[1]
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output
            for output in process.stdout.readlines():
                if len(output.strip()) > 0:
                    print("Output: ", output.strip())
            break
    return return_code, output_file


def dockerRunCommand(machine_dns, file_name):
    """ Running a command on a remote machine looks like :
            "ssh -i pem_file user@machine command"
        For ours, it looks like:
            "ssh -i pem_file user@machine docker run dockerimage python3 ta1_code json_file"
    """
    username = getRemoteUser(machine_dns)
    process_command = ["ssh", "-i", PEM_FILE, username, "docker", "run", "--privileged", DOCKER_IMAGE, "python3",
                       "mcs_test.py", file_name]
    process_text = " ".join(process_command)
    print(f"Text looks like: {process_text}")
    return_code, output_file = runCommandAndCaptureOutput(process_command)
    return return_code, output_file


def copyFileToAWS(machine_dns, file_name):
    ubuntu_machine_dns = getRemoteUser(machine_dns) + ":."
    print(f"Ubuntu command: {ubuntu_machine_dns}")
    process_command = ['scp', '-i', PEM_FILE, file_name, ubuntu_machine_dns]
    return_code, _ = runCommandAndCaptureOutput(process_command)
    return return_code


def copyFileFromAWS(machine_dns, file_name):
    ubuntu_machine_dns = getRemoteUser(machine_dns) + ":" + file_name
    print(f"Ubuntu command: {ubuntu_machine_dns}")
    process_command = ['scp', '-i', PEM_FILE, ubuntu_machine_dns, "."]
    return_code, _ = runCommandAndCaptureOutput(process_command)
    return return_code
