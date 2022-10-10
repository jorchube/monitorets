from io import SEEK_SET
from threading import Thread
from time import sleep


class Sampler:
    def __init__(self, file, new_sample_callback):
        self._path = file
        self._sample_callback = new_sample_callback
        self._interval = 1.0
        self._task = None
        self._is_running = False

    def start(self):
        self._is_running = True
        self._task = Thread(target=self._sample_forever)
        self._task.start()

    def stop(self):
        self._is_running = False
        # if self._task:
        #     self._task.join()

    def _sample_forever(self):
        while self._is_running:
            self._sample()
            sleep(self._interval)

    def _sample(self):
        value = int(self._read())
        self._sample_callback(value)

    def _read(self):
        with open(self._path, "r") as opened_file:
            opened_file.seek(0, SEEK_SET)
            return opened_file.readline()
