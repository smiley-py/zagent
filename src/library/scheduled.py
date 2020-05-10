# -*- coding: utf-8 -*-
import threading
import datetime
import time
from .batch import CustomBatch


class CustomScheduled():
    def __init__(self, API):
        self.API = API
        self.thread_a = CustomThread(1, "Thread-1", API)
        self.msg = ''

    def start(self):
        try:
            self.thread_a.start()
        except Exception as e:
            self.msg = "" + str(e)

        self.msg = "Scheduler Service is started"

    def stop(self):
        try:
            self.thread_a.stop()
            self.thread_a = CustomThread(1, "Thread-1", self.API)
        except Exception as e:
            self.msg = "" + str(e)

        self.msg = "Scheduler Service is stopped"

    def restart(self):
        try:
            self.thread_a.restart()
        except Exception as e:
            self.msg = "" + str(e)

        self.msg = "Scheduler Service is restarted"


class CustomThread (threading.Thread):
    def __init__(self, threadID, name, API):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = 10
        self.api = API

        self.stoprequest = threading.Event()

    def run_batch_file(self):
        self.api.login()
        self.api.get_agent()

        self.delay = int(self.api.agent["delay"])

        if self.api.agent["is_scheduled"] == "1":
            dt = datetime.datetime.strptime(self.api.agent["start_time"].split('+')[0],
                                            "%Y-%m-%dT%H:%M:%S")

            if datetime.datetime.now() >= dt:
                batch = CustomBatch(
                    self.api.agent["path"], self.api.agent["script_content"], self.api.agent["script_inputs"])
                batch.launch()

                self.api.agent["output"] = batch.output
                self.api.agent["result"] = batch.result
                self.api.agent["is_scheduled"] = 2

                self.api.set_agent()
                print(dt, ' executor.bat was triggered.', '\n')

    def start(self):
        threading.Thread.start(self)

    def stop(self):
        self.stoprequest.set()

    def restart(self):
        threading.Thread.__init__(self)
        threading.Thread.start(self)

    def run(self):
        while not self.stoprequest.isSet():
            self.run_batch_file()
            time.sleep(self.delay)
