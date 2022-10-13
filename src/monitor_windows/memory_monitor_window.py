from ..monitor_windows.monitor_window import MonitorWindow
from ..samplers.memory_sampler import MemorySampler
from .. import colors


class MemoryMonitorWindow(MonitorWindow):
    def __init__(self, *args, **kwargs):
        title = "Memory"
        sampler = MemorySampler()

        super().__init__(title, sampler, color=colors.ORANGE, *args, **kwargs)
