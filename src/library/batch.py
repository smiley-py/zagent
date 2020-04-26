from subprocess import Popen, PIPE


class CustomBatch():
    def __init__(self):
        self.path = "D:/git5/zagent/test.bat"

    def launch(self):
        # subprocess.Popen(self.path, creationflags=subprocess.CREATE_NEW_CONSOLE)
        pwd = "Y"
        proc = Popen(self.path, stdout=PIPE, stdin=PIPE,
                     stderr=PIPE, universal_newlines=True)
        proc.stdin.write("{}\n".format(pwd))
        out, err = proc.communicate(input="{}\n".format("Y"))
        print(out)
        print(proc.returncode)
