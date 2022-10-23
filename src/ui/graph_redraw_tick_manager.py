from threading import Timer
from resource import *


class GraphRedrawTickManager:
    _TICK_FREQUENCY_SECONDS = 0.1

    def __init__(self, redraw_callback, tick_frequency_seconds=_TICK_FREQUENCY_SECONDS):
        self._tick_frequency_seconds = tick_frequency_seconds
        self._redraw_callback = redraw_callback
        self._timer = None
        self._stop = False

    def start(self):
        self._arm_timer()

    def stop(self):
        self._stop = True

    def _tick(self):
        self._redraw_callback()

    def _arm_timer(self):
        if self._stop:
            return
        self._timer = Timer(self._tick_frequency_seconds, self._redraw_and_rearm)
        self._timer.start()

    def _redraw_and_rearm(self):
        self._tick()
        self._arm_timer()
