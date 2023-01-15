from threading import Thread
from time import sleep


class Sampler:
    def __init__(self, sampling_frequency_hz=1):
        self._sample_callback = None
        self._sampling_frequency_seconds = 1/sampling_frequency_hz
        self._task = None
        self._is_running = False

    def install_new_sample_callback(self, callback):
        self._sample_callback = callback

    def start(self):
        self._is_running = True
        self._task = Thread(target=self._sample_forever)
        self._task.daemon = True
        self._task.start()

    def stop(self):
        self._is_running = False

    def _sample_forever(self):
        while self._is_running:
            self._sample()
            sleep(self._sampling_frequency_seconds)

    def _sample(self):
        value = self._get_sample()
        self._sample_callback(value)

    def _get_sample(self):
        raise NotImplementedError
