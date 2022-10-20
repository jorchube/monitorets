from .monitor_widget import MonitorWidget
from ..samplers.memory_sampler import MemorySampler
from ..monitor_type import MonitorType
from . import colors


class MemoryMonitorWidget(MonitorWidget):
    def __init__(self, *args, **kwargs):
        title = "title"
        sampler = MemorySampler()
        type = MonitorType.Memory
        color = colors.ORANGE

        super().__init__(title, sampler, type, color, *args, **kwargs)
