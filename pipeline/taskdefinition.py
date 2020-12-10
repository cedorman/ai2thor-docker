class TaskDefinition:
    """ The information necessary to run a task.  Subclass with different
    values for different performers and / parameters

    The command will look something like:

    ssh -i ~/.ssh/pemfile.pem ubuntu@ec2.24342.compute.amazon.com "ENV=XYZ performerscript.sh

    where performerscript.sh runs the code and ENV=XYZ sets some environmental variable that
    performer script understands

    """
    process_command = []


class MITTaskDefinition(TaskDefinition):
    process_command = ["MCS_CONFIG_FILE=/mcs_config_level1.yaml", "mitscript.sh"]
