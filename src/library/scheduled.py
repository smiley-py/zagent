# -*- coding: utf-8 -*-
import threading
import datetime
import time
from .api import CustomApi
from .batch import CustomBatch


class CustomScheduled():
    def __init__(self, TOKEN, DELAY):
        self.thread_a = CustomThread(
            1, "Thread-1", TOKEN, DELAY)  # for each x seconds
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
    def __init__(self, threadID, name, token, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.token = token
        self.delay = delay
        self.stoprequest = threading.Event()

    def run_batch_file(self):
        batch = CustomBatch()
        batch.launch()

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
