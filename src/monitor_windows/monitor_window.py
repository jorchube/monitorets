from ..ui.window import UIMonitorWindow


class MonitorWindow:
    def __init__(self, title, sampler, type=None, color=None, *args, **kwargs):
        self._window = UIMonitorWindow(title, sampler, type, color, *args, **kwargs)

    def close(self):
        self._window.close()

    def present(self):
        self._window.present()

    @property
    def monitor_type(self):
        return self._window.monitor_type
