from subprocess import Popen, PIPE


class CustomBatch():
    def __init__(self, path, script_content, script_inputs):
        self.path = path
        self.script_content = script_content
        self.script_inputs = script_inputs

        myBat = open(self.path, 'w+')
        myBat.write(self.script_content)
        myBat.close()

        self.output = ""
        self.err = ""
        self.result = ""

    def launch(self):
        # subprocess.Popen(self.path, creationflags=subprocess.CREATE_NEW_CONSOLE)
        inputs = self.script_inputs.split(';')

        proc = Popen(self.path, stdout=PIPE, stdin=PIPE,
                     stderr=PIPE, universal_newlines=True)
        out = None
        err = None

        for input in inputs:
            proc.stdin.write("{}\n".format(input))
            out, err = proc.communicate(input="{}\n".format(input))

        self.output = out
        self.err = err
        self.result = proc.returncode
        # print(out)
