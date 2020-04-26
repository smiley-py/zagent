import os
import sys
import cmd
from src import CustomMenu, CustomScheduled

TOKEN = '288fdafc07bf9783b6690e64266bc5fb29f07dda'
AGENTNAME = 'test_agent_1'
DELAY = 10

menu = CustomMenu()
service1 = CustomScheduled(TOKEN, DELAY)


class MyShell(cmd.Cmd, object):
    intro = 'Welcome to the agent shell.   Type help or ? to list commands.\n'
    prompt = '[Shell Prompt] :'

    # ----- basic commands -----
    def do_help(self, line):
        for item in menu.get_help_text():
            print(item)

    def do_start(self, line):
        if (TOKEN is ''):
            print('Please enter token before service started')
        else:
            service1.start()
            print('Scheduler Service started')

    def do_restart(self, line):
        if (TOKEN is ''):
            print('Please enter token before service restarted')
        else:
            service1.restart()
            print('Schedular Service restarted')

    def do_stop(self, line):
        if (TOKEN is ''):
            print('Please login before service stopped')
        else:
            service1.stop()
            print('Schedular Service stopped')

    def do_reset_config(self, line):
        if (TOKEN is not ''):
            print('Please enter token before reset configuration')
        else:
            print('All System Config was reset')

    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ': '

    def do_clear(self, line):
        os.system('cls')  # on windows
        # os.system('clear')  # on linux / os x

    def do_exit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def cmdloop(self, intro=None):
        print(self.intro)
        while True:
            try:
                super(MyShell, self).cmdloop(intro="")
                break
            except KeyboardInterrupt:
                print("^C")


# ----- out of class -----

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(str, arg.split()))


if __name__ == '__main__':
    app = MyShell()
    app.cmdloop()
