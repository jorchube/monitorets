from ..window import UIMonitorWindow


class MonitorWindow:
    def __init__(self, title, sampler, color=None, *args, **kwargs):
        self._window = UIMonitorWindow(title, sampler, color, *args, **kwargs)

    def close(self):
        self._window.close()

    def present(self):
        self._window.present()
