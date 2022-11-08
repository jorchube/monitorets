from .monitor_widget import MonitorWidget
from ..samplers.memory_sampler import MemorySampler
from . import colors


class MemoryMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        title = "Memory"
        sampler = MemorySampler()
        color = colors.ORANGE

        super().__init__(title, sampler, color, *args, **kwargs)
