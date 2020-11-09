import random

from pipeline import util
from pipeline.secrets import Secrets
from pipeline.util import copyFileToAWS

MACHINE_DNS = Secrets['MACHINE_DNS']

def test_copyFileToAWS():
    tmpname = "/tmp/file_" + str(random.randint(0, 999999))
    with open(tmpname, 'w') as f:
        f.write("blah\n")
    print(f"Filename: {tmpname} ")
    success = copyFileToAWS(MACHINE_DNS, tmpname)
    print(f"Success: {success}")
    return tmpname


def test_printCommand():
    print("\n---test_printCommand---")
    tmpname = test_copyFileToAWS()
    success = util.dockerRunCommand(MACHINE_DNS, tmpname)
    print(f"Success: {success}")


test_copyFileToAWS()
test_printCommand()
